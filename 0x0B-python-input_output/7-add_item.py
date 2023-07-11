#!/usr/bin/python3
import os
import sys
"""this function creates saves and adds"""


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

args = sys.argv

if not os.path.exists("add_item.json"):
    with open("add_item.json", mode="w", encoding="utf-8") as file:
        file.write("[]")

objects = load_from_json_file("add_item.json")
for arg in args[1:]:
    objects.append(arg)
save_to_json_file(objects, "add_item.json")
