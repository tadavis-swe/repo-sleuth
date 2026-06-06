import os
import requests
from dotenv import load_dotenv

load_dotenv()

class GitHubAPIError(Exception):
    pass

def get_repo_info(repo):
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise GitHubAPIError("Missing GITHUB_TOKEN environment variable")
    
    headers = {"Authorization": f"token {token}"} if token else {}
    url = f"https://api.github.com/repos/{repo}"
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
    except requests.exceptions.RequestException as e:
        raise GitHubAPIError(f"Network error: {e}")
    
    if response.status_code == 404:
        raise GitHubAPIError(f"Repository '{repo} not found")
    
    if response.status_code == 401:
        raise GitHubAPIError("Invalid or expired GitHub token")
    
    if response.status_code == 403 and "rate limit" in response.text.lower():
        raise GitHubAPIError("GitHub API rate limit exceeded")
    
    if not response.ok:
        raise GitHubAPIError(f"GitHub API error: {response.status_code}")
    
    try:
        return response.json()
    except ValueError:
        raise GitHubAPIError("invalid JSON response from GitHub")