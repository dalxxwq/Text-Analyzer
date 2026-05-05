# Text Analyzer

A small Python command-line tool that analyzes text and prints useful statistics in the terminal.

The project is built around basic string operations: cleaning input, splitting text into words, counting characters, checking letter case, and formatting readable output.

## Features

- Counts all characters in the text
- Counts characters without spaces
- Counts words
- Counts sentences
- Finds the most common word
- Shows the top 5 longest unique words
- Counts uppercase and lowercase letters
- Calculates uppercase and lowercase letter percentages

## Files

- `text_analyzer.py` - main Python script
- `sample.txt` - sample text for testing
- `README.md` - project documentation

## Requirements

- Python 3
- No external libraries required

## How to Run

Open the project folder in the terminal and run:

```bash
python text_analyzer.py
```

Then type or paste any text and press Enter.

## Example Input

```text
Python is powerful. Python is simple!
```

## Example Output

The program prints a formatted report with:

- character count
- word count
- sentence count
- most common word
- longest words
- uppercase and lowercase statistics

## What This Project Practices

This project helps practice real usage of Python strings:

- `input()`
- `strip()`
- `replace()`
- `split()`
- `lower()`
- `isupper()`
- `islower()`
- f-strings
- `Counter` from the `collections` module

## Future Improvements

- Read text directly from `sample.txt`
- Ignore punctuation when counting repeated words
- Split the code into reusable functions
- Add better input validation
- Add tests for the analyzer logic
