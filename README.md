# GitHub Activity CLI

A simple command-line interface (CLI) built with Python that fetches and displays the recent activity of a GitHub user using the GitHub REST API.

## Features

* Accepts a GitHub username from the command line
* Fetches recent GitHub activity
* Displays GitHub events in the terminal
* Shows the number of commits for push events
* Handles invalid usernames
* Handles API and network errors
* Handles users with no recent activity
* Uses only Python's standard library

## Technologies Used

* Python
* GitHub REST API
* `urllib`
* JSON

## Requirements

* Python 3.x
* Internet connection

No external Python packages are required.

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/github-activity-cli.git
```

Navigate to the project directory:

```bash
cd github-activity-cli
```

## Usage

Run the program by providing a GitHub username:

```bash
python github_activity.py <username>
```

Example:

```bash
python github_activity.py VijayKumar-028
```

## Example Output

```text
GitHub Username: VijayKumar-028

Pushed 2 commits to VijayKumar-028/Task-Tracker-CLI
Pushed 1 commit to VijayKumar-028/Pandas_Practice
Starred brightdata/cli
Opened an issue in VijayKumar-028/ExamAlert
```

## Project Structure

```text
github-activity-cli/
│
├── github_activity.py
├── README.md
└── .gitignore
```

## What I Learned

* Command-line arguments using `sys.argv`
* Making HTTP requests using Python's standard library
* Working with REST APIs
* Parsing JSON data
* Working with dictionaries and lists
* Creating and using functions
* Exception handling
* Handling API errors
* Handling API rate limits
* Refactoring code

## API

This project uses the GitHub REST API to fetch user activity.

## Future Improvements

* Support more GitHub event types
* Add event-type filtering
* Improve terminal formatting
* Add pagination
* Add GitHub authentication for higher API rate limits

---

## GitHub Repository Description

A Python CLI tool that fetches and displays recent GitHub user activity using the GitHub REST API.

---

## `.gitignore`

```gitignore

__pycache__/
*.pyc
```



