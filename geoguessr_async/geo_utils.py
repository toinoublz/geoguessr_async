def flatten_dict(d: dict, parent_key: str='', separator: str=''):
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
        new_key = f"{parent_key}{separator}{k.capitalize()}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, separator).items())
        else:
            items.append((new_key, v))
    return dict(items)
