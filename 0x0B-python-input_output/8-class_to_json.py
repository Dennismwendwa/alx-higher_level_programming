#!/usr/bin/python3
"""function return dictionary description with simple data structure"""


def class_to_json(obj):
    """this function dictionary description"""
    if isinstance(obj, (tuple, list)):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}
    elif isinstance(obj, str):
        return obj
    elif isinstance(obj, bool):
        return obj
    elif isinstance(obj, (int, float)):
        return obj
    elif hasattr(obj, "__dict__"):
        return class_to_json(obj.__dict__)
    else:
        return None
