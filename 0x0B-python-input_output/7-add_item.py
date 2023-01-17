#!/usr/bin/python3
"""
Module 7-add_item adds all main arguments
to a list and saves them to a JSON file
"""
import sys
import json
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


args = sys.argv[1:]
filename = "add_item.json"

try:
    all_args = load(filename)
except FileNotFoundError:
    all_args = []

all_args.extend(args)
save(all_args, filename)
