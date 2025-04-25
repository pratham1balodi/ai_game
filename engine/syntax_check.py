import ast

def assess_code(code):
    try:
        ast.parse(code)
        return "✅ Code is syntactically valid."
    except SyntaxError as e:
        return f"❌ Syntax Error: {e.msg} at line {e.lineno}"
