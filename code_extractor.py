import ast, re

def extract_python_code(response: str) -> str:
    code_blocks = re.findall(
        r"```([a-zA-Z0-9_+-]*)[ \t]*\n(.?*)```",
        response,
        flags=re.DOTALL
    )

    candidates = [
        code.strip()
        for language, code in code_blocks
        if language.lower() in ("python", "py", "")
        and code.strip()
    ]

    if not candidates:
        raise ValueError(
            "No Python code found in the response."
        )

    source = max(candidates, key=len)

    ast.parse(source)

    return source
