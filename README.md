# GitHub Activity CLI

A simple command-line interface (CLI) built with Python that fetches and displays the recent activity of a GitHub user using the GitHub REST API.

## Features

* Accepts a GitHub username from the command line
* Fetches recent GitHub activity
* Displays GitHub events in the terminal
* Shows the number of commits for push events
* Supports multiple GitHub event types
* Handles invalid usernames
* Handles API and network errors
* Handles users with no recent activity
* Handles GitHub API rate-limit errors
* Uses only Python's standard library
* Uses in-memory caching for repeated commit comparisons

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
Created branch main in VijayKumar-028/ExamAlert
Opened a pull request in VijayKumar-028/Task-Tracker-CLI
```

The exact output depends on the user's recent GitHub activity.

## Supported Events

The application currently handles the following GitHub events:

* `PushEvent` - Displays repository push activity and commit count
* `CreateEvent` - Displays created branches or other GitHub resources
* `WatchEvent` - Displays starred repositories
* `IssuesEvent` - Displays issue actions
* `PullRequestEvent` - Displays pull request actions

## Project Structure

```text
github-activity-cli/
│
├── github_activity.py
├── README.md
└── .gitignore
```

## How It Works

The application follows this flow:

```text
GitHub Username
       ↓
Command Line Argument
       ↓
GitHub Events API
       ↓
JSON Response
       ↓
Parse GitHub Events
       ↓
Display Activity
```

For `PushEvent`, the application additionally uses GitHub's Compare API to determine the number of commits:

```text
PushEvent
    ↓
Before Commit + Head Commit
    ↓
GitHub Compare API
    ↓
Total Commit Count
    ↓
Display Result
```

## Caching

The application uses a simple in-memory cache for commit comparisons.

A comparison is identified using:

```text
Owner + Repository + Before Commit + Head Commit
```

The first time a comparison is requested, the application calls the GitHub Compare API and stores the result in the cache.

If the same comparison is requested again during the same program execution, the cached result is returned instead of making another API request.

The cache is stored in memory and is cleared when the program exits.

## Error Handling

The application handles common errors including:

* Missing GitHub username
* Invalid GitHub username
* GitHub API errors
* GitHub API rate-limit errors
* Network connection errors
* Invalid JSON responses
* Users with no recent activity
* Failed commit comparison requests

## Known Limitations

* GitHub's unauthenticated API has a rate limit, so repeated requests may result in a `403` response when the limit is exceeded.
* Push events use GitHub's Compare API to determine the number of commits, which requires an additional API request for each unique commit comparison.
* The in-memory cache only prevents repeated requests for the same comparison during a single program execution.
* The cache is cleared when the program exits.
* The application does not currently use GitHub authentication.

## What I Learned

Through this project, I practiced:

* Command-line arguments using `sys.argv`
* Making HTTP requests using Python's standard library
* Working with REST APIs
* Working with API endpoints
* Parsing JSON data
* Working with dictionaries and lists
* Accessing nested JSON data
* Creating and using functions
* Exception handling
* Handling HTTP errors
* Handling API rate limits
* Building a simple in-memory cache
* Using tuples as dictionary keys
* Refactoring Python code
* Structuring a small Python project

## API

This project uses the GitHub REST API.

GitHub Events API:

```text
https://api.github.com/users/<username>/events
```

GitHub Compare API:

```text
https://api.github.com/repos/<owner>/<repo>/compare/<before>...<head>
```

## Future Improvements

* Support additional GitHub event types
* Add event-type filtering
* Improve terminal formatting
* Add pagination
* Add GitHub authentication for higher API rate limits
* Add persistent caching
