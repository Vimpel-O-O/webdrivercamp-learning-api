import requests


def get_created_repo(url):
    headers = {
        "Authorization": "Token *****"
    }
    response = requests.get(url, headers=headers)
    repo = response.json()

    assert repo['has_wiki'] is False
    assert repo['private'] is True
    assert repo['name'] == 'repo-created-with-api'
    assert repo['owner']['login'] == 'Vimpel-O-O'
    print(f"Response status code: {response.status_code}")


if __name__ == "__main__":
    url = "https://api.github.com/repos/Vimpel-O-O/repo-created-with-api"
    get_created_repo(url)