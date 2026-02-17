"""
🔧 Repository Template Setup Script

This script automates the process of replacing repository-specific information
throughout the template files to set up a new project.

Usage:
    python template-script.py                    # Interactive mode
    python template-script.py --url <repo-url>   # With arguments
    python template-script.py --dry-run          # Preview changes only
"""

import argparse
import os
import sys
from pathlib import Path

# Files to process (markdown and common config files)
SUPPORTED_EXTENSIONS = {".md", ".txt", ".py"}

# Directories to skip
SKIP_DIRS = {".git", "__pycache__", "node_modules", ".venv", "venv", "dist", "build"}


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Setup repository template with your project details",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python template-script.py
  python template-script.py --url https://github.com/username/my-repo
  python template-script.py --url https://github.com/user/repo --dry-run
        """,
    )

    parser.add_argument(
        "--url",
        help="GitHub repository URL (e.g., https://github.com/username/repo)",
        type=str,
    )

    parser.add_argument(
        "--dir",
        help="Directory path to process (default: current directory)",
        type=str,
        default=".",
    )

    parser.add_argument(
        "--dry-run", help="Preview changes without modifying files", action="store_true"
    )

    return parser.parse_args()


def extract_repo_name(repo_url):
    """Extract repository name from GitHub URL."""
    repo_url = repo_url.strip().rstrip("/")

    if not repo_url.startswith("https://github.com/"):
        raise ValueError("URL must start with 'https://github.com/'")

    try:
        repo_name = repo_url.split("https://github.com/")[1]
        if not repo_name or "/" not in repo_name:
            raise ValueError("Invalid repository format")
        return repo_name
    except (IndexError, ValueError):
        raise ValueError("Could not extract repository name from URL")


def should_process_file(file_path, skip_dirs):
    """Check if file should be processed."""
    # Skip if in excluded directory
    if any(skip_dir in file_path.parts for skip_dir in skip_dirs):
        return False

    # Only process supported file types
    return file_path.suffix in SUPPORTED_EXTENSIONS


def process_files(dir_path, old_repo, new_repo, dry_run=False):
    """Process files in directory and replace repository references."""
    dir_path = Path(dir_path).resolve()

    if not dir_path.exists():
        raise FileNotFoundError(f"Directory '{dir_path}' does not exist")

    files_updated = 0
    files_to_update = []
    old_name = old_repo.split("/")[1]  # Extract just "repo-template"
    new_name = new_repo.split("/")[1]  # Extract new repo name

    print(f"\n🔍 Scanning directory: {dir_path}")
    print(f"🔄 Will replace:")
    print(f"   • '{old_repo}' → '{new_repo}'")
    print(f"   • '{old_name}' → '{new_name}'\n")

    # Walk through directory
    for file_path in dir_path.rglob("*"):
        if not file_path.is_file() or not should_process_file(file_path, SKIP_DIRS):
            continue

        try:
            content = file_path.read_text(encoding="utf-8")

            # Check if replacement is needed
            if old_repo in content or old_name in content:
                new_content = content.replace(old_repo, new_repo)
                new_content = new_content.replace(old_name, new_name)

                relative_path = file_path.relative_to(dir_path)

                if dry_run:
                    print(f"   📄 Would update: {relative_path}")
                    files_to_update.append(relative_path)
                else:
                    file_path.write_text(new_content, encoding="utf-8")
                    print(f"   ✅ Updated: {relative_path}")
                    files_updated += 1

        except Exception as e:
            print(f"   ⚠️  Warning: Could not process {file_path.name}: {str(e)}")

    return files_updated if not dry_run else len(files_to_update)


def main():
    """Main function to orchestrate the template setup."""
    args = parse_arguments()

    print("🚀 Repository Template Setup")
    print("=" * 50)

    # Get repository URL
    if args.url:
        repo_url = args.url
    else:
        repo_url = input("\n📦 Enter the GitHub repository URL: ").strip()

    # Extract and validate repository name
    try:
        repo_name = extract_repo_name(repo_url)
    except ValueError as e:
        print(f"❌ Error: {e}")
        print("   Expected format: https://github.com/username/repo-name")
        sys.exit(1)

    # Get directory path
    dir_path = args.dir

    # Confirm action if not in dry-run mode
    if not args.dry_run:
        confirm = input(
            f"\n⚠️  This will modify files in '{dir_path}'. Continue? [y/N]: "
        ).lower()
        if confirm != "y":
            print("❌ Operation cancelled")
            sys.exit(0)

    try:
        count = process_files(
            dir_path,
            old_repo="svijayb/repo-template",
            new_repo=repo_name,
            dry_run=args.dry_run,
        )

        if args.dry_run:
            print(f"\n🔍 Dry run complete! Found {count} file(s) to update")
            print("   Run without --dry-run to apply changes")
        else:
            print(f"\n✨ Done! Updated {count} file(s)")
            print("🎉 Your repository template is ready to use!")

    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
