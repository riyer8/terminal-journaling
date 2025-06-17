# combining all actions in this file

from entries import create_entry
from utils import print_entries, view_entries, search_entries, delete_entry
import argparse

def main():
    parser = argparse.ArgumentParser(description="📘 Journal CLI")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("add")
    subparsers.add_parser("list")
    subparsers.add_parser("view")
    subparsers.add_parser("search")
    subparsers.add_parser("delete")

    args = parser.parse_args()

    if args.command == "add":
        create_entry()
    elif args.command == "list":
        print_entries()
    elif args.command == "view":
        view_entries()
    elif args.command == "search":
        search_entries()
    elif args.command == "delete":
        delete_entry()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()