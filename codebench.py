import argparse
from rich.console import Console
from rich.table import Table
from rich import box
from runner import run_code
from utils import format_time, format_memory, highlight_winner, save_results, detect_complexity

console = Console()

def compare(snippets, save_file=None):
    console.print("CodeBench Results", style="bold cyan")

    table = Table(box=box.DOUBLE_EDGE)
    table.add_column("Snippet", style="cyan", justify="center")
    table.add_column("Time (s)", style="green", justify="center")
    table.add_column("Memory (MB)", style="yellow", justify="center")
    table.add_column("Est. Complexity", style="magenta", justify="center")

    results = []
    for idx, (file, lang) in enumerate(snippets):
        t, m = run_code(file, lang)
        complexity = detect_complexity(file, lang)
        results.append({
            "snippet": f"Snippet {idx+1} ({lang})",
            "time": t,
            "memory": m,
            "complexity": complexity
        })
        table.add_row(f"Snippet {idx+1} ({lang})", format_time(t), format_memory(m), complexity)

    console.print(table)

    winner_idx = highlight_winner(results)
    console.print(f"Winner: {results[winner_idx]['snippet']} (Fastest Execution)", style="bold green")

    if save_file:
        save_results(results, save_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CodeBench CLI - Benchmark Code Snippets")
    parser.add_argument("--compare", nargs=4, metavar=("file1", "lang1", "file2", "lang2"))
    parser.add_argument("--run", nargs=2, metavar=("file", "lang"))
    parser.add_argument("--save", metavar="filename")
    args = parser.parse_args()

    if args.compare:
        compare([(args.compare[0], args.compare[1]), (args.compare[2], args.compare[3])], args.save)
    elif args.run:
        compare([(args.run[0], args.run[1])], args.save)
    else:
        console.print("No valid command provided. Use --run or --compare.", style="red")
