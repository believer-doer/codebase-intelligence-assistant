import argparse
from app.commands.ask import ask_question
from app.commands.index import index_repository


# CLI command parser
parser = argparse.ArgumentParser()

parser.add_argument(
    "command",
    choices=["index", "ask"],
)

parser.add_argument(
    "value"
)

args = parser.parse_args()

if args.command == "index":
    index_repository(args.value)

elif args.command == "ask":
    ask_question(args.value)