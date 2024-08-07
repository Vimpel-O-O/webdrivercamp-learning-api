import requests


def get_with_auth(url):
    headers = {
        "Authorization": "Token *****"
    }
    response = requests.get(url, headers=headers)
    print(response.status_code)
    json_resp = response.json()
    return len(json_resp), len(response.headers)


if __name__ == "__main__":
    url = "https://api.github.com/user/repos"
    num_of_repos, headers = get_with_auth(url)
    print(f"Total Repos: {num_of_repos}")
    print(f"Response headers: {headers}")