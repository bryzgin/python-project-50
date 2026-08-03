def build_diff_tree(data1, data2):
    all_keys = sorted(data1.keys() | data2.keys())
    tree = []
    
    for key in all_keys:
        val1 = data1.get(key)
        val2 = data2.get(key)
        
        if isinstance(val1, dict) and isinstance(val2, dict):
            tree.append({
                "key": key,
                "type": "nested",
                "children": build_diff_tree(val1, val2)
            })        
        elif key in data1 and key not in data2:
            tree.append({
                "key": key,
                "type": "deleted",
                "value": val1
            })        
        elif key not in data1 and key in data2:
            tree.append({
                "key": key,
                "type": "added",
                "value": val2
            })        
        elif val1 != val2:
            tree.append({
                "key": key,
                "type": "changed",
                "old_value": val1,
                "new_value": val2
            })        
        else:
            tree.append({
                "key": key,
                "type": "unchanged",
                "value": val1
            })
        
        return tree