#!/usr/bin/python3
"""
i add arguments so that it can be  saved into a JSON file
"""


from sys import argv

save_to_json = __import__("5-save_to_json_file").save_to_json_file
load_from_json = __import__("6-load_from_json_file").load_from_json_file

if __name__ == "__main__":
    try:
        list = load_from_json("add_item.json")
    except Exception:
        pass
        list = []
    for av in argv[1:]:
        list.append(av)
    save_to_json(list, "add_item.json")
