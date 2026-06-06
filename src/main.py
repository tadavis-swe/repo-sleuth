from rich.console import Console
from src.cli import build_cli
from src.github_api import get_repo_info, GitHubAPIError

console = Console()

def main():
    parser = build_cli()
    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return

    if args.command == "inspect":
        try:
            data = get_repo_info(args.repo)
        except GitHubAPIError as e:
            console.print(f"[bold red]Error:[/bold red] {e}")
            return
        
        console.print(f"[bold cyan]Repo:[/bold cyan] {args.repo}")
        console.print(f"Stars: {data['stargazers_count']}")
        console.print(f"Forks: {data['forks_count']}")
        console.print(f"Open Issues: {data['open_issues_count']}")
        console.print(f"Last Updated: {data['updated_at']}")
    else:
        parser.print_help()
    
    console.print(f"[bold cyan]Command:[/bold cyan] {args.command}")
    console.print(f"[bold cyan]Repo:[/bold cyan] {getattr(args, 'repo', None)}")

if __name__ == "__main__":
    main()