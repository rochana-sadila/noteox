
from pathlib import Path
import argparse

note_path = Path("notes")
note_path.mkdir(parents=True , exist_ok=True)

parser = argparse.ArgumentParser(description="A Simple Note Taking CLI")
parser.add_argument(
        '--note', 
        action='store_true',
        help='Make Simple Markdown Note'
    )
args = parser.parse_args()

if args.note:
	print("work")
else: 
	print("not work")