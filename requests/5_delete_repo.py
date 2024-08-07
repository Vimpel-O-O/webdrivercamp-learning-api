import requests


def delete_repo(url):
    headers = {
        "Authorization": "Token *****",
    }
    response = requests.delete(url, headers=headers)
    print(f"Response status code: {response.status_code}")


if __name__ == "__main__":
    url = "https://api.github.com/repos/Vimpel-O-O/repo-created-with-api"

    delete_repo(url)
