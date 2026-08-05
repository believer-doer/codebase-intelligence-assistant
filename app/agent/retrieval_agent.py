from app.agent.planner import create_retrieval_plan
from app.retrieval.hybrid_retriever import hybrid_retrieve
from app.retrieval.retrieval_analyzer import analyze_retrieval
from app.retrieval.query_refiner import generate_followup_queries

MAX_STEPS = 3


def agent_retrieve(
    question: str,
    extension: str = ".py",
    show_plan: bool = True,
    show_reasoning: bool = True,
    show_expanded_query: bool = False,
):
    """
    Agent retrieval loop.

    Flow:

        Question
            ↓
        Planner
            ↓
        Search Queue
            ↓
        Retrieve
            ↓
        Analyze
            ↓
        Need More?
          ↓      ↓
        Yes      No
         ↓        ↓
    Generate      Answer
    Follow-ups
    """

    plan = create_retrieval_plan(question)

    if show_plan:
        print("\n" + "=" * 80)
        print("Retrieval Plan")
        print(f"Goal: {plan['goal']}\n")

        print("Searches:")
        for i, search in enumerate(plan["searches"], start=1):
            print(f"{i}. {search}")

    search_queue = list(plan["searches"])
    searched_queries = set()

    all_results = []

    step = 1

    while search_queue and step <= MAX_STEPS:

        current_query = search_queue.pop(0)

        if current_query in searched_queries:
            continue

        searched_queries.add(current_query)

        if show_reasoning:
            print("\n" + "=" * 80)
            print(f"Agent Step {step}")
            print(f"Searching: {current_query}")

        results = hybrid_retrieve(
            current_query,
            extension=extension,
            show_expanded_query=show_expanded_query,
        )

        all_results.extend(results)
        all_results = deduplicate_results(all_results)

        analysis = analyze_retrieval(
            question,
            all_results,
        )

        if show_reasoning:
            print("\nAnalysis")
            print(f"Enough Context : {analysis['enough_context']}")
            print(f"Reason         : {analysis['reason']}")

        if analysis["enough_context"]:

            if show_reasoning:
                print("\nDecision: Stop searching.")

            break

        followup_queries = generate_followup_queries(
            question,
            analysis,
        )

        followup_queries = [
            query
            for query in followup_queries
            if query not in searched_queries
            and query not in search_queue
        ]

        if followup_queries:

            if show_reasoning:
                print("\nGenerated Follow-up Queries:")

                for query in followup_queries:
                    print(f"  + {query}")

            search_queue.extend(followup_queries)

        else:

            if show_reasoning:
                print("\nNo additional useful queries generated.")

        step += 1

    return all_results


def deduplicate_results(results):
    """
    Remove duplicate chunks while preserving order.
    """

    seen = set()
    unique = []

    for result in results:

        key = (
            result["metadata"]["file_path"],
            result["metadata"]["chunk_index"],
        )

        if key in seen:
            continue

        seen.add(key)
        unique.append(result)

    return unique