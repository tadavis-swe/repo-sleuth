# repo-sleuth

A lightweight CLI tool for inspecting GitHub repositories

## Features
- Fetches live repo data (stars, forks, issues, last update)
- Graceful error handling for missing tokens, bad repos, and rate limits
- Simple command-line interface built with `argparse` and `rich`

## Installation

```bash
git clone https://github.com/tadavis-swe/repo-sleuth.git
cd repo-sleuth
pip install -r requirements.txt
```

## Usage
python -m src.main inspect --repo owner/repo

## Example Output
Repo: microsoft/vscode
Stars: 186003
Forks: 40387
Open Issues: 18376
Last Updated: 2026-06-06T13:58:51Z
Command: inspect
Repo: microsoft/vscode