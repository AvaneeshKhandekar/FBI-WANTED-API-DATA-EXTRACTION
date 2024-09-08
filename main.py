import argparse
import sys

import requests
import json

URL = 'https://api.fbi.gov/wanted/v1/list'


def format_data(data):
    formatted_string = []
    items = data["items"]
    if not items:
        return "No items available"
    for item in items:
        title = item["title"]
        subjects = ','.join(item["subjects"]) if item["subjects"] else ''
        field_offices = ','.join(item["field_offices"]) if item["field_offices"] else ''
        formatted_string.append('\u00FE'.join([title, subjects, field_offices]))
    return formatted_string


def fetch_details_local(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        if data:
            return format_data(data)
    return ["No Data Found"]


def fetch_details_from_api(page_number):
    response = requests.get(URL, params={'page': page_number})
    data = json.loads(response.content)
    if data:
        return format_data(data)
    return ["No Data Found"]


def print_data(data):
    for item in data:
        print(item)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Fetch page from API or local based on user input.")
    parser.add_argument("--page", type=int, required=False, help="Path to local Json File.")
    parser.add_argument("--file", type=str, required=False, help="Path to local Json File.")
    args = parser.parse_args()

    if not args.page and not args.file:
        print("Must provide either --page or --file as an argument.")
        sys.exit(1)

    if args.page and args.file:
        print("Must provide either --page or --file as an argument not both.")
        sys.exit(1)

    if args.page:
        print_data(fetch_details_from_api(args.page))
    elif args.file:
        print_data(fetch_details_local(args.file))
