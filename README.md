This repository contains solution to convert string logs into dict.

The objective is to parse the above log string into a dictionary with keys corresponding to log attributes and values being their respective data, even when values contain spaces or special characters.

### File Structure

- **`log_parser.py`**: This file contains the main function `parse_antivirus_log` which performs the log parsing.
- **`tests/test_log_parser.py`**: This file contains unit tests for the log parser, ensuring that it handles various cases correctly.

## Installation

### Prerequisites

- Python 3.x
- `pytest` for running unit tests

### Steps

1. **Clone the Repository**:
    - git clone https://github.com/poornachandra22/string-to-dict.git
    - cd string-to-dict

2. **Create a Virtual Environment**:
    It is recommended to create a virtual environment to manage dependencies:
    python -m venv venv
    source venv/bin/activate  # On Windows use .\venv\Scripts\activate

3. **Install Dependencies**:
    If you plan to run tests, you might want to install `pytest`:
    pip install pytest

## Running the Program

### Parsing a Log String

You can use the `parse_antivirus_log` function to parse a log string. Here’s how you can do it:

1. **Run the Program**:
   - python log_parser.py

### Running Unit Tests

To ensure the parser works as expected, run the unit tests provided in `tests/test_log_parser.py`:

1. **Run the Tests**:
    - pytest tests/test_log_parser.py
    This will run all the tests and output the results, helping you verify that the program is working correctly.
