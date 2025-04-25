import difflib

def apply_changes(original, modified):
    return modified

def get_diff(original, modified):
    original_lines = original.splitlines()
    modified_lines = modified.splitlines()
    diff = difflib.unified_diff(original_lines, modified_lines, lineterm='')
    return "\n".join(diff)
