import ast
from langchain_core.documents import Document


def chunk_python_document(document):

    source = document.page_content

    tree = ast.parse(source)

    chunks = []

    # imports/constants/module code
    module_lines = source.splitlines()

    for node in tree.body:

        if isinstance(
            node,
            (
                ast.FunctionDef,
                ast.AsyncFunctionDef,
                ast.ClassDef,
            )
        ):

            start = node.lineno - 1
            end = node.end_lineno

            chunk_text = "\n".join(
                module_lines[start:end]
            )

            chunk = Document(
                        page_content=chunk_text,
                        metadata=document.metadata.copy()
                    )
            chunk.metadata["symbol_type"] = "function"
            chunk.metadata["symbol_name"] = node.name
            chunks.append(chunk)


    return chunks