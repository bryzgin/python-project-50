def stringify(value, depth):
    if is instance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if not isinstance(value, dict):
        return str(value)
    
    current_indent = "    " * depth
    closing_indent = "    " * (depth - 1)
    
    lines = ["{"]
    
    for key, val in value.items():
        lines.append(f"{current_indent}    {key}: {stringify(val, depth + 1)}")
    lines.append(f"{closing_indent}}")
    
    return "\n".join(lines)


