from datetime import datetime
from typing import Any, Optional


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


def int_or_none(value: Any) -> Optional[int]:
    """
    Safely convert a value to int, returning None if conversion fails.

    Args:
        value (Any): The value to convert to int.

    Returns:
        Optional[int]: The converted int value, or None if conversion fails.
    """
    try:
        return int(value)
    except (ValueError, TypeError):
        return None


def bool_or_none(value: Any) -> Optional[bool]:
    """
    Safely convert a value to bool, returning None if conversion fails.

    Args:
        value (Any): The value to convert to bool.

    Returns:
        Optional[bool]: The converted bool value, or None if conversion fails.
    """
    try:
        return bool(value)
    except (ValueError, TypeError):
        return None


def str_or_none(value: Any) -> Optional[str]:
    """
    Safely convert a value to str, returning None if conversion fails.

    Args:
        value (Any): The value to convert to str.

    Returns:
        Optional[str]: The converted str value, or None if conversion fails.
    """
    try:
        return str(value)
    except (ValueError, TypeError):
        return None


def float_or_none(value: Any) -> Optional[float]:
    """
    Safely convert a value to float, returning None if conversion fails.

    Args:
        value (Any): The value to convert to float.

    Returns:
        Optional[float]: The converted float value, or None if conversion fails.
    """
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


def datetime_or_none(value: Any) -> Optional[datetime]:
    """
    Safely convert a value to datetime, returning None if conversion fails.

    Args:
        value (Any): The value to convert to datetime.

    Returns:
        Optional[datetime]: The converted datetime value, or None if conversion fails.
    """
    try:
        return datetime.strptime(value.split(".")[0], "%Y-%m-%dT%H:%M:%S")
    except (ValueError, TypeError):
        return None
