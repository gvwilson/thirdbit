import requests
import sys
import json


LABELS = [
    ["discuss", "question or discussion", "d876e3"],
    ["good first issue", "good for newcomers", "7057ff"],
    ["in-code", "software", "102d0e"],
    ["in-docs", "documentation", "0075ca"],
    ["in-infra", "infrastructure", "7a16b4"],
    ["in-tests", "tests", "92b6c3"],
    ["issue-bug", "something is broken", "d73a4a"],
    ["issue-feature", "something wanted", "a2eeef"],
    ["pr-feature", "adds something", "a2eeef"],
    ["pr-fix", "fixes something", "d73a4a"],
    ["task", "one-off job", "000000"],
]


def create_labels(repo_owner, repo_name, token):
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {token}",
    }
    base_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/labels"

    for name, description, color in LABELS:
        try:
            # Check if label already exists
            response = requests.get(f"{base_url}/{name}", headers=headers)

            if response.status_code != 404:
                print(f"Label {name} already exists")
            else:
                response = requests.post(
                    base_url,
                    headers=headers,
                    data=json.dumps({
                        "name": name,
                        "description": description,
                        "color": color,
                    })
                )
                if response.status_code == 201:
                    print(f"Created {name}")
                else:
                    print(f"Failed to create {name}: {response.text}")

        except requests.exceptions.RequestException as e:
            print(f"Error for {name}: {str(e)}")


def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py owner repo_name github_token")
        sys.exit(1)
    repo_owner = sys.argv[1]
    repo_name = sys.argv[2]
    github_token = sys.argv[3]
    create_labels(repo_owner, repo_name, github_token)


if __name__ == "__main__":
    main()
