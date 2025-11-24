# Stock0lyzer

A command-line tool for quick stock analysis and financial news updates.

## Features

* **ASCII Art Interface:** A retro-style interface for a modern CLI.
* **Stock Information:** View detailed stock data, including corporate officers, market metrics, and technical analysis (50-Day Moving Average) using the `/view <TICKER>` command.
* **Integrated News Scraping:** Automatically fetches corporate officer data from yfinance and scrapes the web for the latest news articles as a fallback.
* **Simulated Exchange Connection:** A `/boot` command that simulates connecting to a live stock exchange server.
* **Government Watch:** The `/gov` command scrapes search results for recent events or speeches by key financial figures, such as the Federal Reserve.
* **Color-Coded Output:** Important information is color-coded for readability (errors in red, warnings in yellow, success in green).

## Installation

Since `setup.py` defines an entry point (`stock0lyzer`) and lists required dependencies, the recommended way to install and use the tool globally is to use pip:

1.  **Install the application:**
    ```bash
    pip install .
    ```
    *Note: This command should be run in the directory containing `setup.py`.*

    Alternatively, if you prefer a direct run without global installation:
    ```bash
    # You must first ensure all dependencies are installed manually:
    pip install pandas yfinance requests beautifulsoup4 colorama setuptools
    ```

## Usage

Once installed globally, you can run the application directly using the entry point:

```bash
stock0lyzer <command> [options]
