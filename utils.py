import json
import ast
import re
from rich.console import Console

console = Console()

def format_memory(mb: float) -> str:
    return f"{mb:.2f} MB"

def format_time(seconds: float) -> str:
    return f"{seconds:.3f} s"

def highlight_winner(results: list) -> int:
    return min(range(len(results)), key=lambda i: results[i]['time'])

def save_results(results: list, filename: str) -> None:
    try:
        with open(filename, "w") as f:
            json.dump(results, f, indent=4)
        console.print(f"[green]Results saved to {filename}[/green]")
    except Exception as e:
        console.print(f"[red]Failed to save results: {e}[/red]")

def detect_complexity(file_path: str, lang: str) -> str:
    try:
        code = open(file_path, "r").read().lower()

        if lang.lower() == "python":
            tree = ast.parse(code)
            loop_count = sum(isinstance(node, (ast.For, ast.While)) for node in ast.walk(tree))
            recursion = any(
                isinstance(node, ast.FunctionDef) and 
                any(node.name in ast.unparse(body) for body in node.body)
                for node in ast.walk(tree)
            )
        else:
            loop_count = len(re.findall(r"\bfor\b|\bwhile\b", code))
            recursion = bool(
                re.search(r"\b[A-Za-z_]+\([^)]*\)\s*{", code) and 
                re.search(r"\breturn\b.*\b[A-Za-z_]+\(", code)
            )

        if recursion:
            return "Possibly O(2^n)" if loop_count > 0 else "Possibly O(n)"
        if loop_count >= 2:
            return "Possibly O(n^2)"
        if loop_count == 1:
            return "Possibly O(n)"
        return "Possibly O(1)"
    except Exception:
        return "Unknown"
