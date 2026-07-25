from app.evaluator.data.eval_questions import EVAL_SET
from app.retrieval.hybrid_retriever import hybrid_retrieve


def evaluate_retrieval():

    correct = 0

    for item in EVAL_SET:

        results = hybrid_retrieve(
            item["question"],
            k=5,
            extension=".py",  # evaluate code retrieval only
        )

        retrieved_files = [
            result["metadata"]["file_path"]
            for result in results
        ]

        rank = None

        for index, path in enumerate(
            retrieved_files,
            start=1
        ):
            if path == item["expected_file"]:
                rank = index
                break

        success = rank is not None

        if success:
            correct += 1

        print("\n" + "=" * 80)
        print(f"Question: {item['question']}")
        print(f"Expected: {item['expected_file']}")
        print("Retrieved:")

        for file_path in retrieved_files:
            print(f"  - {file_path}")

        print(f"Success: {success}")
        print(f"Rank: {rank}")

    accuracy = correct / len(EVAL_SET)

    print("\n" + "=" * 80)
    print(f"Correct: {correct}/{len(EVAL_SET)}")
    print(f"Accuracy: {accuracy:.2%}")