def flatten_dict(d: dict, parentKey: str = "", separator: str = ""):
    """
    Flattens a nested dictionary into a single-level dictionary.

    Args:
        d (dict): The input dictionary to be flattened.
        parent_key (str, optional): The parent key used for recursive calls. Defaults to ''.
        separator (str, optional): The separator to be used between keys. Defaults to ''.

    Returns:
        dict: The flattened dictionary.

    """
    items = []
    for k, v in d.items():
        newKey = f"{parentKey}{separator}{k.capitalize()}" if parentKey else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, newKey, separator).items())
        else:
            items.append((newKey, v))
    return dict(items)
