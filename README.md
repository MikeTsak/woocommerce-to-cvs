# Project Title: WooCommerce Order Export Script

## Description
This Python script is designed to fetch orders from a WooCommerce store and export them into a CSV file. It utilizes the WooCommerce API to access store data and exports important order details such as customer information, order date, and purchase details.

## Features
- Fetch orders from WooCommerce using API
- Export orders data to a CSV file
- Customize CSV output with relevant order details
- Handle customer data with confidentiality

## Prerequisites

Before running the script, ensure you have Python installed on your system. Then, install the required dependencies:

1. Go to the [official Python website](https://www.python.org/downloads/).
2. Download the appropriate installer for your operating system.
3. Run the installer and follow the on-screen instructions. Ensure that you check the option that says "Add Python to PATH" during installation.


## Installation

After installing Python, you need to set up the script environment:

1. Clone the repository or download the source code to your local machine.
2. Open a command prompt or terminal window.
3. Navigate to the directory where the script is located.
4. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Unix or MacOS
```

## Usage

To use this script, follow these steps:
1. Set up WooCommerce API credentials (Consumer Key and Consumer Secret).
2. Store these credentials in a .env file for security.
3. Run the script:

```bash
python woocommerce_to_csv.py
```

The script will generate a CSV file named orders-<date-time>.csv with the exported order data.

## Configuration

- `WOO_STORE_URL`: Your WooCommerce store URL
- `WOO_CONSUMER_KEY`: Your WooCommerce API consumer key
- `WOO_CONSUMER_SECRET`: Your WooCommerce API consumer secret

## License
Copyright (c) 2023 by MikeTsak

Licensed under [LICENSE](https://github.com/MikeTsak/woocommerce-to-cvs/LICENSE).

For more information, visit [miketsak.gr](https://miketsak.gr/).