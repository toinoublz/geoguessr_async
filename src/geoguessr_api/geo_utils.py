def flatten_dict(d, parent_key="", separator="", index_separator=""):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{separator}{k.capitalize()}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, separator, index_separator).items())
        elif isinstance(v, list):
            for i, item in enumerate(v):
                list_key = f"{new_key}{index_separator}{i}"
                if isinstance(item, dict):
                    items.extend(
                        flatten_dict(item, list_key, separator, index_separator).items()
                    )
                else:
                    items.append((list_key, item))
        else:
            items.append((new_key, v))
    return dict(items)
