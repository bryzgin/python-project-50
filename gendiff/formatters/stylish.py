def stringify(value, depth):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if not isinstance(value, dict):
        return str(value)

    current_indent = "    " * depth
    closing_indent = "    " * depth
    
    lines = ["{"]
    for key, val in value.items():
        lines.append(f"{current_indent}    {key}: {stringify(val, depth + 1)}")
    lines.append(f"{closing_indent}}}")
    return "\n".join(lines)


def render_stylish(tree, depth=1):
    indent = "    " * depth
    sign_indent = indent[:-2]
    
    lines = ["{"]
    
    for node in tree:
        node_type = node["type"]
        key = node["key"]

        if node_type == "nested":
            lines.append(f"{sign_indent}  {key}: {render_stylish(node["children"], depth + 1)}")
        elif node_type == "added":
            lines.append(f"{sign_indent}+ {key}: {stringify(node["value"], depth)}")
        elif node_type == "deleted":
            lines.append(f"{sign_indent}- {key}: {stringify(node["value"], depth)}")
        elif node_type == "unchanged":
            lines.append(f"{sign_indent}  {key}: {stringify(node["value"], depth)}")
        elif node_type == "changed":
            lines.append(f"{sign_indent}- {key}: {stringify(node["old_value"], depth)}")
            lines.append(f"{sign_indent}+ {key}: {stringify(node["new_value"], depth)}")

    closing_indent = "    " * (depth - 1)
    lines.append(f"{closing_indent}}}")
    
    return "\n".join(lines)
