# CodeBench
[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/mekhushi/CodeBench)

CodeBench is a lightweight command-line utility for benchmarking the performance of code snippets. It measures execution time and memory usage, provides an estimated time complexity, and presents the results in a clear, comparative table.

## Features

-   **Performance Metrics:** Measures execution time and peak memory consumption.
-   **Comparative Analysis:** Run two code snippets side-by-side to determine the winner.
-   **Complexity Estimation:** Provides a basic Big O complexity estimation based on code structure.
-   **Multi-Language Support:** Natively supports Python, C++, and Go.
-   **Clean Output:** Uses `rich` to display results in a well-formatted table in your terminal.
-   **Export Results:** Save benchmark data to a JSON file for further analysis.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/mekhushi/CodeBench.git
    cd CodeBench
    ```

2.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Language Prerequisites:**
    Ensure you have the necessary compilers/interpreters installed for the languages you want to benchmark.
    -   **C++:** `g++` compiler
    -   **Go:** Go toolchain

## Usage

CodeBench is operated via the command line. You can benchmark a single file or compare two files.

### Benchmarking a Single Snippet

Use the `--run` flag followed by the file path and the language identifier (`python`, `cpp`, or `go`).

```bash
python codebench.py --run examples/code1.py python
```

### Comparing Two Snippets

Use the `--compare` flag followed by the path and language for the first file, and then the path and language for the second file.

```bash
python codebench.py --compare examples/code1.py python examples/code2.cpp cpp
```

### Saving Results

Add the `--save` flag with a desired filename to any `run` or `compare` command to save the output as a JSON file.

```bash
python codebench.py --compare examples/code1.py python examples/code2.cpp cpp --save benchmark_results.json
```

## Example Output

When running a comparison, CodeBench will display a table similar to this:

```
$ python codebench.py --compare examples/code1.py python examples/code2.cpp cpp

CodeBench Results
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃        Snippet        ┃  Time (s)  ┃  Memory (MB)  ┃ Est. Complexity   ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
│ Snippet 1 (python)    │   0.095 s  │     8.45 MB   │   Possibly O(1)   │
│   Snippet 2 (cpp)     │   0.015 s  │     1.23 MB   │   Possibly O(n)   │
└───────────────────────┴────────────┴───────────────┴───────────────────┘
Winner: Snippet 2 (cpp) (Fastest Execution)

```

## How It Works

-   **Runner (`runner.py`):** Uses Python's `subprocess` module to execute code files. For compiled languages like C++, it first compiles the code and then runs the resulting executable.
-   **Monitoring (`runner.py`):** While the subprocess is running, `psutil` monitors the process's Resident Set Size (RSS) to determine the peak memory usage.
-   **Complexity Analysis (`utils.py`):**
    -   For **Python**, it uses the `ast` module to parse the code into an Abstract Syntax Tree, then counts loops and checks for recursion.
    -   For **C++ and Go**, it uses regular expressions to find keywords like `for` and `while` and to detect simple recursive patterns. This is a heuristic and may not be perfectly accurate for complex code.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
