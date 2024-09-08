import json
import os
import sys
from unittest.mock import Mock

import main

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import fetch_details_from_api, fetch_details_local, format_data, print_data

data = {
    "items": [
        {"title": "name1", "subjects": ["subject1", "subject2"], "field_offices": ["field_office1"]},
        {"title": "name2", "subjects": ["subject3"], "field_offices": ["field_office2"]}
    ]
}


def test_fetch_details_from_api():
    result = fetch_details_from_api(1)
    assert isinstance(result, list)
    assert len(result) > 0


def test_fetch_details_from_api_no_data(monkeypatch):
    mock_response = Mock()
    mock_response.content = json.dumps({})
    monkeypatch.setattr(main.requests, 'get', lambda url, params: mock_response)
    result = fetch_details_from_api(500)
    assert result == ["No Data Found"]


def test_fetch_details_from_valid_data(monkeypatch):
    mock_response = Mock()
    mock_response.content = json.dumps(data)
    monkeypatch.setattr(main.requests, 'get', lambda url, params: mock_response)
    result = fetch_details_from_api(10)
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0] == "name1\u00FEsubject1,subject2\u00FEfield_office1"
    assert result[1] == "name2\u00FEsubject3\u00FEfield_office2"


def test_fetch_details_local():
    with open("test.json", "w") as file:
        json.dump(data, file)
    result = fetch_details_local("test.json")
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0] == "name1\u00FEsubject1,subject2\u00FEfield_office1"
    assert result[1] == "name2\u00FEsubject3\u00FEfield_office2"
    os.remove("test.json")


def test_format_data():
    result = format_data(data)
    assert isinstance(result, list)
    assert result[0] == "name1\u00FEsubject1,subject2\u00FEfield_office1"
    assert result[1] == "name2\u00FEsubject3\u00FEfield_office2"


def test_format_data_empty_items():
    result = format_data({"items": []})
    assert result == "No items available"


def test_print_data(capsys):
    data_list = ["item1", "item2", "item3"]
    print_data(data)
    captured = capsys.readouterr()
    print(captured.out)
    assert captured.out == '\n'.join(data) + '\n'
