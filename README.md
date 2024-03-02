# MiniPHP Compiler in Python

## Overview

This project represents an in-progress miniPHP compiler written in Python, aimed at compiling a simplified version of PHP code. As of now, the project has reached the parsing phase, including error handling for syntactic mistakes. It's designed as an educational tool to demonstrate the initial stages of compiler design, particularly focusing on how PHP code can be tokenized and parsed.

## Current Features

- **Lexical Analysis**: Tokenization of PHP source code into a series of meaningful symbols.
- **Syntax Analysis**: Parsing of tokens to validate against the defined miniPHP grammar.
- **Error Handling**: Provision of descriptive error messages for syntax errors encountered during the parsing phase.

## Prerequisites

- Python 3.6 or higher
- PLY (Python Lex-Yacc) 

## Setup

This project includes a virtual environment with all the necessary dependencies pre-installed, allowing for easy replication and setup.

### Activating the Virtual Environment

1. Clone the repository: `git clone https://github.com/MiguelALF12/miniPHP-compiler.git`
2. Navigate to the project directory: cd miniPHP-compiler
3. Activate the virtual environment:
- On Windows:
  ```
  .\venv\Scripts\activate
  ```
- On Unix or MacOS:
  ```
  source venv/bin/activate
  ```

### In Case of Problems

If you encounter any issues with the virtual environment or dependencies, you may need to install the required libraries manually:

1. Ensure Python 3.6 or higher is installed on your system.

2. Install PLY (Python Lex-Yacc): `pip install ply`. It can change depending on your OS.

### Run the compiler
Execute the `main.py` file located at the rrot of the project. There is inside of it some test callers (lexer and parser). You should call wichever you want to test.

### Files to parse

Replace any of the files inside `test/` with the desired code to test

## Project Status

This project is currently in the early stages of development and has not been completed. The compiler can currently perform lexical and syntactic analysis with error handling but does not proceed to semantic analysis or code generation.

## TODO

- [ ] Implement semantic analysis to check for semantic errors.
- [ ] Develop code generation phase to convert parsed code into an intermediate representation or machine code.
- [ ] Enhance error handling to cover semantic errors and warnings.
- [ ] Introduce optimization phases to improve the efficiency of the generated code.
- [ ] Expand the supported subset of PHP to include more complex constructs and features.


## Acknowledgments

- PLY (Python Lex-Yacc) for providing the lexing and parsing tools.
- The PHP Group for the PHP language specification.
