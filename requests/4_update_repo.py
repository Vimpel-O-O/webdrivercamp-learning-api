import requests


def update_repo(url):
    headers = {
        "Authorization": "Token *****"
    }
    data = {
        "description": "I know Python Requests!"
    }
    response = requests.patch(url, headers=headers, json=data)
    print(f"Response status code: {response.status_code}")

    return response.json()


if __name__ == '__main__':

    url = 'https://api.github.com/repos/Vimpel-O-O/repo-created-with-api'
    repo = update_repo(url)
    assert repo['description'] == 'I know Python Requests!'
