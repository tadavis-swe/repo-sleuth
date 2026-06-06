import argparse

def build_cli():
    parser = argparse.ArgumentParser(
        prog="repo-sleuth",
        description="A GitHub repository inspection tool."
    )

    subparsers = parser.add_subparsers(dest="command")

    # inspect command
    inspect = subparsers.add_parser("inspect", help="Inpsect a repository")
    inspect.add_argument("--repo", required=True, help="Owner/repo format")
    inspect.add_argument("--json", action="store_true", help="Output JSON")

    # issues command
    issues = subparsers.add_parser("issues", help="List open issues")
    issues.add_argument("--repo", required=True)
    issues.add_argument("--json", action="store_true")

    # more commands later...

    return parser