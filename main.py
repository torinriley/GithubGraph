import requests

# GitHub API base URL
GITHUB_API_URL = "https://api.github.com"

# Function to get repositories for a user
def get_repositories(username, token=None):
    url = f"{GITHUB_API_URL}/users/{username}/repos"
    
    headers = {}
    if token:
        headers['Authorization'] = f"token {token}"
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        repos = response.json()
        print(f"Repositories for user {username}:")
        for repo in repos:
            print(f"- {repo['name']} (Stars: {repo['stargazers_count']}, Forks: {repo['forks_count']})")
    else:
        print(f"Failed to fetch repositories for {username}. HTTP Status Code: {response.status_code}")

# Input GitHub username and token (optional)
if __name__ == "__main__":
    username = input("Enter GitHub username: ")
    token = input("Enter your GitHub token (optional, hit Enter if you don't have one): ")
    
    get_repositories(username, token if token else None)