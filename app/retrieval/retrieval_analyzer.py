import re

def analyze_retrieval(
    question,
    results
):

    text = get_retrieved_text(results)

    identifier = extract_identifier(
        question
    )

    if identifier:

        if contains_definition(
            identifier,
            text
        ):
            return {
                "enough_context": True,
                "reason": (
                    "Definition found"
                ),
                "next_query": None,
            }

        return {
            "enough_context": False,
            "reason": (
                "Only references found"
            ),
            "next_query": (
                f"{identifier} definition"
            ),
        }

    return {
        "enough_context": True,
        "reason": "No identifier",
        "next_query": None,
    }

import re

def extract_identifier(question):

    candidates = re.findall(
        r"\b[A-Za-z_][A-Za-z0-9_]*\b",
        question
    )

    for token in candidates:

        if "_" in token:
            return token

    return None

def get_retrieved_text(results):

    sections = []

    for result in results:
        sections.append(
            result["document"]
        )

    return "\n".join(sections)





def contains_definition(
    identifier,
    text
):
    patterns = [
        rf"def\s+{identifier}\s*\(",
        rf"class\s+{identifier}\s*[:\(]",
    ]

    return any(
        re.search(pattern, text)
        for pattern in patterns
    )