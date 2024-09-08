import json
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import fetch_details_from_api, fetch_details_local, format_data, print_data


def test_fetch_details_from_api():
    result = fetch_details_from_api(1)
    assert isinstance(result, list)
    assert len(result) > 0


def test_fetch_details_local():
    data = {
        "items": [
            {"title": "name1", "subjects": ["subject1", "subject2"], "field_offices": ["field_office1"]},
            {"title": "name2", "subjects": ["subject3"], "field_offices": ["field_office2"]}
        ]
    }
    with open("test.json", "w") as file:
        json.dump(data, file)
    result = fetch_details_local("test.json")
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0] == "name1\u00FEsubject1,subject2\u00FEfield_office1"
    assert result[1] == "name2\u00FEsubject3\u00FEfield_office2"
    os.remove("test.json")


def test_format_data():
    data = {
        "items": [
            {"title": "name1", "subjects": ["subject1", "subject2"], "field_offices": ["field_office1"]},
            {"title": "name2", "subjects": ["subject3"], "field_offices": ["field_office2"]}
        ]
    }
    result = format_data(data)
    assert isinstance(result, list)
    assert result[0] == "name1\u00FEsubject1,subject2\u00FEfield_office1"
    assert result[1] == "name2\u00FEsubject3\u00FEfield_office2"


def test_format_data_empty_items():
    data = {"items": []}
    result = format_data(data)
    assert result == "No items available"


def test_print_data(capsys):
    data = ["item1", "item2", "item3"]
    print_data(data)
    captured = capsys.readouterr()
    print(captured.out)
    assert captured.out == '\n'.join(data) + '\n'
