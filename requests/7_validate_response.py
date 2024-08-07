import json
import requests
from pprint import pprint


def find_mismatched_data(url, file_name):
    response = requests.get(url)
    json_response = response.json()

    json_results = {}

    with open(file_name, 'r') as file:
        json_file = json.load(file)
        for dict1, dict2 in zip(json_response["results"], json_file["results"]):
            if dict1.keys() == dict2.keys():
                for key in dict1:
                    if dict1[key] != dict2[key]:
                        EXPECTED_VAL = dict2[key]
                        ACTUAL_VAL = dict1[key]
                        if dict1["name"] not in json_results:
                            json_results[dict1["name"]] = []
                        json_results[dict1["name"]].append([{key: {'Expected': EXPECTED_VAL, 'Actual': ACTUAL_VAL}}])
    return json_results


if __name__ == "__main__":
    url = "https://swapi.dev/api/planets/"
    file_name = "planets.json"
    pprint(find_mismatched_data(url, file_name))
