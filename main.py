import argparse
from app.commands.ask import ask_question
from app.commands.index import index_repository
from app.commands.summarize import summarize_repository


# CLI command parser
parser = argparse.ArgumentParser()

parser.add_argument(
    "command",
    choices=["index", "ask", "summarize"],
)

parser.add_argument(
    "value"
)

parser.add_argument(
    "--show-context",
    action="store_true"
)

parser.add_argument(
    "--show-scores",
    action="store_true"
)

parser.add_argument(
    "--show-expanded-query",
    action="store_true"
)
args = parser.parse_args()

if args.command == "index":
    index_repository(args.value)

elif args.command == "ask":
    ask_question(args.value, show_context = args.show_context, show_scores = args.show_scores, show_expanded_query = args.show_expanded_query)

elif args.command == "summarize":
    summarize_repository(args.value)