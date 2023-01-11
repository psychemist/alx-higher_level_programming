#!/usr/bin/python3
"""
Module 7-add_item

Adds all arguments to a Python list, and saves them to a JSON file
"""
import sys
import json
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


my_list = []
with open("add_item.json", mode="r+", encoding="utf-8") as f:
    args = sys.argv[1:]
    my_list.append(args)
    json.dump(my_list, f)
