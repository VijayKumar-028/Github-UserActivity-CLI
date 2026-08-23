import json
import sys
from urllib import request
from urllib.error import HTTPError, URLError


#fetching the events through the URL
def fetch_events(username):
    url = f"https://api.github.com/users/{username}/events"

    try:
        response = request.urlopen(url)
        data = response.read()
        text = data.decode("utf-8")
        events = json.loads(text)

        return events
    except HTTPError as error:
        print(error.headers)
        if error.code==404:
            print("Error : Github user not found")
        else:
            print(f"Error: GitHub API returned status code {error.code}.")

        return None

    except URLError:
        print("Error : Unable to connect to Github")
        return None
    
    except json.JSONDecodeError:
        print("Error: Unable to process GitHub response.")
        return None
    
def format_action(action):
    if action:
        return action.capitalize()

    return "Performed"

def get_commit_count(owner, repo_name, before, head):
    compare_url = f"https://api.github.com/repos/{owner}/{repo_name}/compare/{before}...{head}"

    try:
        response = request.urlopen(compare_url)
        data = response.read()
        decoded_text = data.decode("utf-8")
        json_data = json.loads(decoded_text)

        return len(json_data["commits"])

    except HTTPError as error:
        print(error.headers)

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
            before=payload.get("before")
            head=payload.get("head")
            parts=repo.split("/")
            owner=parts[0]
            repo_name=parts[1]
           
            commit_count=get_commit_count(owner, repo_name, before, head)
            commit_word= "commit" if commit_count==1 else "commits"
            print(f"Pushed {commit_count} {commit_word} to {repo}")

        # elif event_type == "CreateEvent":
            
        #     ref_type = payload.get("ref_type")
        #     ref = payload.get("ref")

        #     print(f"Created {ref_type} {ref} in {repo}")

        # elif event_type=="WatchEvent":
        #     print(f"Starred {repo}")

        # elif event_type=="IssueEvent":
            
            
        #     action = payload.get("action")

        #     print(f"{action.capitalize()} an issue in {repo}")

        # elif event_type=="PullRequestEvent":
        #     action=event["payload"]["action"]

        #     print(f"{action.capitalize()} a pull request in {repo}")


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
        print("No recent activity found")

    display_events(events)


if __name__=="__main__":
    main()