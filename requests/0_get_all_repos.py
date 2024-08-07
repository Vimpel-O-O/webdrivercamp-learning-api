import requests


def get_repos(url):
    response = requests.get(url)
    json_response = response.json()
    sorted_by_names = sorted(json_response['items'], key=lambda x: x['full_name'])
    print(sorted_by_names)
    print(f"Response status code: {response.status_code}")
    print(f"Total count of found items: {len(json_response['items'])}")
    return sorted_by_names


if __name__ == "__main__":
    url = "https://api.github.com/search/repositories?q=webdrivercamp-learning-python"
    list_of_items = get_repos(url)
    print()

    for item in list_of_items:
        user = item['owner']['login']
        repo = item['name']
        print(f"{user:15}", repo)
