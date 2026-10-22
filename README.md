
# CCC Agent

An experimental Python-based agent for the Cloudflight
Coding Contest (CCC).

The agent generates candidate solutions using OpenAI and
Anthropic models, extracts Python code, runs test cases,
and selects a candidate based on its test results.

## Features

- Multiple AI-generated solution candidates
- Automatic Python code extraction and syntax validation
- Automated test execution with timeouts
- Candidate selection based on test results
- Configurable prompt templates

## Requirements

- Python version compatible with the project
- OpenAI API key
- Anthropic API key
- API access and available credits for the models used

## Installation

Clone the repository and enter the project directory.

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Copy `.env.example` to `.env` and add your API keys.

## Usage

Run the complete pipeline:

```bash
python main.py
```

Generated responses and candidate solutions are stored
locally in the `solutions/` directory.

## Configuration

Edit the prompt templates in `prompts/` and the test cases
in `tester.py` to customize the workflow.

## Limitations

Passing the available tests does not prove correctness
for every possible input. The current candidate selector
uses test results rather than a formal correctness proof.

Generated code is executed locally and is not securely
sandboxed. Only run trusted code.

## License

No license has been selected yet.
