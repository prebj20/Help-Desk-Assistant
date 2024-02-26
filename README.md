
# Help Desk Assistant

## Introduction
The Help Desk Assistant is a Python-based command-line application designed to streamline the process of generating support ticket templates and troubleshooting guides for help desk personnel. The application leverages predefined templates for common support scenarios, such as password resets, account activations, and device additions, allowing for quick and efficient support ticket creation.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Documentation](#documentation)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)
- [License](#license)

## Installation
To install the Help Desk Assistant, ensure you have Python and pip installed on your system. Follow these steps:
1. Clone the repository or download the source files.
2. Navigate to the project directory.
3. Install the required dependencies using pip:
   \`\`\`sh
   pip install -r requirements.txt
   \`\`\`

## Usage
To use the application, run the `main.py` script from the command line:
\`\`\`sh
python main.py
\`\`\`
Enter commands as prompted to retrieve specific support templates. Use `help` for a list of commands and `exit` to terminate the application.

## Features
- Predefined templates for common support issues.
- Easy-to-use command-line interface.
- Colored console output for better readability.
- Extendable template system for adding new support scenarios.

## Dependencies
See `requirments.txt` for more extensive list.
- Python 3.x
- `requests` for HTTP requests.
- `pyperclip` for clipboard operations.
- `beautifulsoup4` for HTML parsing in development modules.

## Configuration
No additional configuration is required for basic usage. For development purposes, especially when working with `Stew.py` for BeautifulSoup implementations, ensure you have the necessary HTML content or URLs for parsing.

## Documentation
Further documentation on extending templates and adding new command functionalities can be found in the inline comments within the `main.py` and `Mod.py` files.

## Examples
- Retrieve a password reset template:
  \`\`\`sh >>>> pr\`\`\`
- Get the description for the account activation process:
  \`\`\`sh >>>> aa -d\`\`\`

## Troubleshooting
If you encounter any issues with command recognition or template retrieval, ensure you're entering the commands as specified in the `help` menu. For issues related to BeautifulSoup implementations in `Stew.py`, verify the HTML content or URLs are correctly formatted and accessible.

## Contributors
`Creator:` Joel Prebish
`:`

## License
N/A
