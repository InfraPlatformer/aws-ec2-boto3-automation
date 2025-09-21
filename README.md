# aws-ec2-boto3-automation

Infrastructure-as-Code (IaC) with Python - AWS

## Overview

This repository contains Python automation scripts for infrastructure management.

## Prerequisites

- Python 3.8+
- pip package manager
- Required Python packages (see requirements.txt)

## Installation

\\\ash
# Clone the repository
git clone https://github.com/InfraPlatformer/aws-ec2-boto3-automation.git
cd aws-ec2-boto3-automation

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
\\\

## Usage

\\\ash
# Run the main script
python main.py

# Or run specific modules
python -m module_name
\\\

## Configuration

1. Copy \config.example.json\ to \config.json\
2. Update configuration values as needed

## Project Structure

\\\
aws-ec2-boto3-automation/
├── src/                    # Source code
├── config/                 # Configuration files
├── tests/                  # Test files
├── docs/                   # Documentation
├── requirements.txt        # Python dependencies
├── README.md              # This file
└── .gitignore             # Git ignore rules
\\\

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Last Updated

2025-09-21

## Author

[Alam Ahmed](https://github.com/InfraPlatformer)
