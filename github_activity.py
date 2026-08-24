import json
import sys
from urllib import request
from urllib.error import HTTPError, URLError

commit_cache = {}


def fetch_events(username):
    url = f"https://api.github.com/users/{username}/events"

    try:
        response = request.urlopen(url)
        data = response.read()
        text = data.decode("utf-8")
        events = json.loads(text)

        return events

    except HTTPError as error:
        if error.code == 404:
            print("Error: GitHub user not found.")
        else:
            print(f"Error: GitHub API returned status code {error.code}.")

        return None

    except URLError:
        print("Error: Unable to connect to GitHub.")
        return None

    except json.JSONDecodeError:
        print("Error: Unable to process GitHub response.")
        return None


def format_action(action):
    if action:
        return action.capitalize()

    return "Performed"


def get_commit_count(owner, repo_name, before, head):
    cache_key = (owner, repo_name, before, head)

    if cache_key in commit_cache:
        return commit_cache[cache_key]

    compare_url = (
        f"https://api.github.com/repos/"
        f"{owner}/{repo_name}/compare/{before}...{head}"
    )

    try:
        response = request.urlopen(compare_url)

        data = response.read()
        decoded_text = data.decode("utf-8")
        json_data = json.loads(decoded_text)

        commit_count = json_data["total_commits"]
        commit_cache[cache_key] = commit_count

        return commit_count

    except HTTPError as error:
        if error.code == 404:
            print("Error: Unable to compare commits.")
        else:
            print(f"Error: GitHub API returned status code {error.code}.")

        return None

    except URLError:
        print("Error: Unable to connect to GitHub.")
        return None

    except json.JSONDecodeError:
        print("Error: Unable to process GitHub response.")
        return None


def display_events(events):
    for event in events:
        event_type = event.get("type")
        repo = event.get("repo", {}).get("name")
        payload = event.get("payload", {})

        if event_type == "PushEvent":
            before = payload.get("before")
            head = payload.get("head")

            owner, repo_name = repo.split("/")

            commit_count = get_commit_count(
                owner,
                repo_name,
                before,
                head
            )

            if commit_count is None:
                print(f"Pushed to {repo}")
            else:
                commit_word = "commit" if commit_count == 1 else "commits"
                print(f"Pushed {commit_count} {commit_word} to {repo}")

        elif event_type == "CreateEvent":
            ref_type = payload.get("ref_type")
            ref = payload.get("ref")

            if ref:
                print(f"Created {ref_type} {ref} in {repo}")
            else:
                print(f"Created {ref_type} in {repo}")

        elif event_type == "WatchEvent":
            print(f"Starred {repo}")

        elif event_type == "IssuesEvent":
            action = payload.get("action")
            print(f"{format_action(action)} an issue in {repo}")

        elif event_type == "PullRequestEvent":
            action = payload.get("action")
            print(f"{format_action(action)} a pull request in {repo}")


def main():
    if len(sys.argv) < 2:
        print("Please provide username!")
        sys.exit()

    username = sys.argv[1]
    print(f"GitHub Username: {username}")

    events = fetch_events(username)

    if events is None:
        return

    if not events:
        print("No recent activity found.")
        return

    display_events(events)


if __name__ == "__main__":
    main()