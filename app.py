
from pathlib import Path
import argparse

note_path = Path("notes")
note_path.mkdir(parents=True , exist_ok=True)


parser = argparse.ArgumentParser(description="Simple Note Taking App")
subparsers = parser.add_subparsers(dest='command')

note = subparsers.add_parser('note', help='Make markdown note')
note = subparsers.add_parser('list', help='See avalible note list')
args = parser.parse_args()

if args.command == 'note':
    print("working note...")

elif args.command == 'list':
    print("working list...")