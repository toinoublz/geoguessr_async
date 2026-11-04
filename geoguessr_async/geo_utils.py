from datetime import datetime
from typing import Any, Optional


def int_or_none(value: Optional[Any]) -> Optional[int]:
    """
    Safely convert a value to int, returning None if conversion fails.

    Args:
        value (Any): The value to convert to int.

    Returns:
        Optional[int]: The converted int value, or None if conversion fails.
    """
    try:
        return int(value) if value is not None else None
    except (ValueError, TypeError):
        return None


def bool_or_none(value: Optional[Any]) -> Optional[bool]:
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


def str_or_none(value: Optional[Any]) -> Optional[str]:
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


def float_or_none(value: Optional[Any]) -> Optional[float]:
    """
    Safely convert a value to float, returning None if conversion fails.

    Args:
        value (Any): The value to convert to float.

    Returns:
        Optional[float]: The converted float value, or None if conversion fails.
    """
    try:
        return float(value) if value is not None else None
    except (ValueError, TypeError):
        return None


def datetime_or_none(value: Optional[Any]) -> Optional[datetime]:
    """
    Safely convert a value to datetime, returning None if conversion fails.

    Args:
        value (Any): The value to convert to datetime.

    Returns:
        Optional[datetime]: The converted datetime value, or None if conversion fails.
    """
    try:
        return datetime.strptime(value.split(".")[0], "%Y-%m-%dT%H:%M:%S") if value is not None else None
    except (ValueError, TypeError):
        return None

def to_datetime(value: str) -> datetime:
    """
    Converts a string value to a datetime object.

    Args:
        value (str): The string value to convert.

    Returns:
        datetime: The converted datetime object.
    """
    return datetime.strptime(value.split(".")[0], "%Y-%m-%dT%H:%M:%S")
