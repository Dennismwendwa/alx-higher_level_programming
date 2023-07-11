#!/urs/bin/python3
import json
"""
This function writes file in json form
json.dump(my_obj, file, ensure_ascii=False, indent=4)
"""


def save_to_json_file(my_obj, filename):
    """This function writes json to file
    aparamitors:
        my_obj: object
        filename: file
        """
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
