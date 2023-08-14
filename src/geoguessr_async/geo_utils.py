def flatten_dict(d: dict, parent_key: str='', separator: str=''):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{separator}{k.capitalize()}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, separator).items())
        else:
            items.append((new_key, v))
    return dict(items)