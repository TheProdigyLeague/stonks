from setuptools import setup, find_packages
import os
import sys
import yfinance as yf
import requests
import secrets
import random
import argparse
import time
from datetime import datetime, timezone
from bs4 import BeautifulSoup
from colorama import init, Fore, Style
import pandas as pd
from faker import Faker 

# Initialize colorama
init(autoreset=True)
fake = Faker() # Initialize Faker

# --- Utility Functions ---

def print_error(message):
    """Prints an error message in red."""
    print(Fore.RED + message)

def print_warning(message):
    """Prints a warning message in yellow."""
    print(Fore.YELLOW + message)

def print_success(message):
    """Prints a success message in green."""
    print(Fore.GREEN + message)

# --- Generative Content Engines ---

def generate_plausible_headline(ticker_symbol, ceo_name):
    """Generates a plausible, non-factual market headline using random keywords."""
    
    # Financial Action Words
    actions = [
        "rises", "soars", "plunges", "sinks", "maintains dominance", 
        "expands market share", "sheds weight", "eyes new acquisition",
        "reports record earnings", "beats expectations", "misses targets"
    ]
    
    # Financial Keywords/Themes
    themes = [
        "AI Integration", "Cloud Services", "Consumer Spending Report", 
        "Regulatory Scrutiny", "Dividend Increase", "Stock Split Rumors", 
        "Global Supply Chain", "Next-Gen Product Launch", "Digital Transformation"
    ]
    
    # Plausible Sources
    sources = [
        "Reuters", "Bloomberg", "The Wall Street Journal", "Financial Times", 
        "CNBC", "Zack's Research"
    ]
    
    # Assemble the headline structure
    source_name = random.choice(sources)
    
    # Use the CEO name or generate a plausible executive name
    exec_name = ceo_name if ceo_name and random.choice([True, False]) else fake.name()
    
    # Randomly structure the headline
    if random.choice([True, False]):
        headline = f"({exec_name} / {source_name}) - {ticker_symbol} {random.choice(actions)} amid {random.choice(themes)}."
    else:
        headline = f"({source_name}) - {random.choice(themes)} drives {ticker_symbol} to {random.choice(actions)}."
        
    return headline, source_name

def generate_today_speaker():
    """Generates a plausible, non-factual Fed speaker event for today."""
    governor = fake.name()
    action = random.choice(["discussing the impact of current inflation rates", "holding a Q&A on employment data", "speaking on assessing financial system resilience", "giving remarks on long-term monetary policy"])
    time_est = f"{random.randint(9, 17):02d}:{random.choice(['00', '15', '30', '45'])} p.m. EST"
    location = fake.city()

    deep_link = secrets.token_urlsafe(16)
    
    output = f"Today's Simulated Fed Event (Deep Link: {Fore.CYAN}https://statestreet.stock0lyzer.io/fed/{deep_link}{Style.RESET_ALL}{Fore.GREEN}):\n"
    output += f"{time_est}: Governor {governor} is {action} in {location}.\n"
    output += f"Note: This information is simulated to represent a successful feed retrieval."
    return output

def generate_past_fed_analysis():
    """Generates a simulated historical analysis of Fed rate cuts."""
    deep_link = secrets.token_urlsafe(16)
    
    analysis = f"In previous years, what actions did the Fed take for rate cuts? (and jobs, employment, market numbers, etc.)\n\n"
    analysis += "Historically, the Federal Reserve has used rate cuts for three main reasons: to normalize rates after a period of increases, to counter a recession, or to respond to a financial crisis. Each situation has produced different impacts on employment and market numbers.\n\n"
    analysis += "Rate cuts during crises:\n"
    analysis += "2008 Financial Crisis: The Fed slashed rates from 5.25% in September 2007 to near zero by December 2008. It also implemented quantitative easing (QE), buying mortgage-backed securities and other assets to inject liquidity.\n"
    analysis += f"{Fore.CYAN}Impact on jobs:{Style.RESET_ALL} Unemployment soared, peaking at 10% in October 2009. The economy experienced a severe recession.\n"
    analysis += f"{Fore.CYAN}Impact on markets:{Style.RESET_ALL} Initially, markets plummeted due to the severity of the crisis. Once confidence returned and liquidity improved, the stock market began a strong recovery, with the S&P 500 more than doubling from 2009 to 2015.\n\n"
    analysis += "Deep Link to Full Historical Analysis (Blockchain Engine): {Fore.CYAN}https://statestreet.stock0lyzer.io/past-policy/{deep_link}"
    return analysis

def generate_future_fed_calendar():
    """Generates a simulated future FOMC meeting schedule."""
    deep_link = secrets.token_urlsafe(16)
    
    calendar = f"In future years, what is the Feds calendar for speakers?\n\n"
    calendar += "The Federal Reserve typically announces its official speaker and event calendars for future years well in advance, though specific details may be added or adjusted closer to the date. The Federal Reserve Board website is the authoritative source for the most up-to-date information.\n\n"
    calendar += f"{Fore.YELLOW}Federal Open Market Committee (FOMC) Meeting Schedules{Style.RESET_ALL}\n"
    calendar += "The FOMC meeting dates, which involve statements and press conferences by the Fed Chair, are a major part of the public schedule and are published for several years in advance.\n\n"
    calendar += f"{Fore.GREEN}2026 FOMC Meeting Schedule{Style.RESET_ALL}\n"
    calendar += "January 27–28\n"
    calendar += "March 17–18*\n"
    calendar += "April 28–29\n"
    calendar += "June 16–17*\n"
    calendar += "Deep Link to Full Calendar (Blockchain Engine): {Fore.CYAN}https://statestreet.stock0lyzer.io/future-calendar/{deep_link}"
    return calendar

# --- Component Views ---

def show_news_and_officers(stock_ticker, info):
    """
    Displays corporate officer information and simulated news headlines.
    CHANGELOG: Re-added generative news engine which was accidentally removed.
    """
    print(f"\n{Fore.YELLOW}--- Corporate Officers ---")
    officers = info.get('companyOfficers', [])
    
    # Attempt to extract CEO name for use in headlines
    ceo_name = next((o.get('name') for o in officers if 'ceo' in o.get('title', '').lower()), None)

    if not officers:
        print_warning("No corporate officer information available.")
    else:
        for officer in officers:
            title = officer.get('title', 'N/A')
            name = officer.get('name', 'N/A')
            compensation = officer.get('totalPay', 'N/A')
            if isinstance(compensation, int):
                compensation = f"${compensation:,}"
            print(f"{Fore.GREEN}{title}: {name} (Total Compensation: {compensation})")

    # --- Generative News Section ---
    print(f"\n{Fore.YELLOW}--- Daily Top 5 Headlines (Simulated Deep Link Analysis) ---")
    
    for i in range(5):
        headline, source = generate_plausible_headline(stock_ticker.ticker, ceo_name)
        
        # Generate a secure, unique deep link for simulation
        deep_link = secrets.token_urlsafe(16)
        
        # Print the simulated headline structure
        print(f"{Fore.WHITE}- Headline Deep Link: ({headline})")
        print(f"  {Fore.LIGHTBLACK_EX}Source: stock0lyzer deep linking | Link: {Fore.CYAN}https://stock0lyzer.io/deep/{deep_link}")

def show_chart_analysis(stock_ticker, info):
    """Displays technical analysis and market data."""

    try:
        print(f"\n{Fore.YELLOW}--- Market Data ---")
        
        # Previous Close: Red
        close = info.get('previousClose', 'N/A')
        print(f"{Fore.RED}Previous Close: {close}")

        # Bid/Ask: Yellow for label and Bid, Light Green for Ask
        bid = info.get('bid', 'N/A')
        ask = info.get('ask', 'N/A')
        print(f"{Fore.YELLOW}Bid/Ask: {bid} / {Fore.LIGHTGREEN_EX}{ask}")

        # Dividend Yields: Cyan
        dividend_yield = info.get('dividendYield')
        if isinstance(dividend_yield, (int, float)):
             print(f"{Fore.CYAN}Dividend Yields: {dividend_yield * 100:.2f}%")
        else:
             print(f"{Fore.CYAN}Dividend Yields: N/A")
        
        # --- yfinance data acquisition ---
        data = stock_ticker.history(period="1y")

        # Check if data was returned
        if data.empty:
            print_warning("\nHistorical data for chart analysis is unavailable from yfinance.")
            return
        
        # Calculate 50-Day Moving Average (MA)
        ma_period = 50
        data[f'{ma_period}d_ma'] = data['Close'].rolling(window=ma_period).mean()
        latest_ma = data[f'{ma_period}d_ma'].iloc[-1]

        print(f"\n{Fore.YELLOW}--- Technical Indicators ---")
        print(f"50-Day Moving Average (MA): {latest_ma:.2f}")
        
        latest_close = data['Close'].iloc[-1]

        if latest_close > latest_ma:
            print_success("Price is currently priced ABOVE 50-day MA (Potential bullish signal).")
        else:
            print_warning("Price is currently priced BELOW 50-day MA (Potential bearish signal).")

    except Exception as e:
        print_error(f"An error occurred during chart analysis: {e}")

# --- Command Handlers ---

def handle_gov_command(args_list):
    """Handler for the /gov command, generating simulated Fed speaker or policy news based on flags."""
    parser = argparse.ArgumentParser(description='Monitor government financial news (simulated).')
    parser.add_argument('--past', action='store_true', help='Generate analysis of past Fed actions (e.g., rate cuts).')
    parser.add_argument('--future', action='store_true', help='Generate simulated future Fed calendar and speaker dates.')
    
    try:
        # parse_known_args is used to allow unknown args to pass through if necessary
        parsed_args, unknown = parser.parse_known_args(args_list)

        if parsed_args.past:
            print_success("--- Generated Historical Fed Policy (State Street Deep Link) ---")
            print(generate_past_fed_analysis())
        elif parsed_args.future:
            print_success("--- Generated Future FOMC Calendar (State Street Deep Link) ---")
            print(generate_future_fed_calendar())
        else:
            # Default behavior (simulated today's speaker)
            print_success("--- Simulated Today's Fed Speaker (State Street Deep Link) ---")
            print(generate_today_speaker())

    except SystemExit:
        pass # argparse handles errors

def handle_view_command(args):
    """Handler for the /view command and its flags."""
    try:
        stock_ticker = yf.Ticker(args.stock_name)
        info = stock_ticker.info
        if not info.get('longName'):
            print_error(f"Could not find information for ticker: {args.stock_name}")
            return

        print(f"\n{Fore.CYAN}{info.get('longName')} ({info.get('symbol')})")
        print(f"Sector: {info.get('sector', 'N/A')}, Industry: {info.get('industry', 'N/A')}")

        show_news = args.news
        show_chart = args.chart

        if not show_news and not show_chart:
            show_news = True

        if show_news:
            show_news_and_officers(stock_ticker, info)
        
        if show_chart:
            show_chart_analysis(stock_ticker, info)

    except Exception as e:
        print_error(f"An error occurred: {e}")

def handle_boot():
    print("Attempting to boot into stock exchange server...")
    if random.choice([True, False]):
        token = secrets.token_urlsafe(32)
        print_success("Connection successful. Live session established.")
        print(f"Deep Link: https://trade.stock0lyzer.io/session?token={token}")
    else:
        print_error("ERR: 403 forbidden (or moved)")

# --- Main Application Logic ---

def boot_sequence():
    """Displays a simulated boot sequence."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.GREEN + "Booting Stock0lyzer v1.0.5...")
    time.sleep(0.5)
    print("Initializing data streams...")
    time.sleep(0.3)
    print("Connecting to market data feeds...")
    time.sleep(0.5)
    print_success("Connection successful.")
    time.sleep(0.2)
    os.system('cls' if os.name == 'nt' else 'clear')

def home_screen():
    """Displays the main ASCII art and welcome message."""
    ascii_art = """
    ███████╗████████╗ ██████╗  ██████╗██╗  ██╗██╗     ██╗   ██╗██╗   ██╗███████╗██████╗ 
    ██╔════╝╚══██╔══╝██╔═══██╗██╔════╝██║  ██║██║     ██║   ██║╚██╗ ██╔╝██╔════╝██╔══██╗
    ███████╗   ██║   ██║   ██║██║     ███████║██║     ██║   ██║ ╚████╔╝ █████╗  ██████╔╝
    ╚════██║   ██║   ██║   ██║██║     ██╔══██║██║     ██║   ██║  ╚██╔╝  ██╔══╝  ██╔══██╗
    ███████║   ██║   ╚██████╔╝╚██████╗██║  ██║███████╗╚██████╔╝   ██║   ███████╗██║  ██║
    ╚══════╝   ╚═╝    ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝
    """
    print(Fore.GREEN + ascii_art)
    print(Fore.CYAN + "Dev: z4xk3r07h".center(80))
    print(f"\n{Fore.YELLOW}Welcome to Stock0lyzer!")

def print_main_help():
    """Prints the main help text."""
    print("\nUsage: stock0lyzer <command> [options]")
    print("\nCommands:")
    print("  /view <stock> [-n] [-c]...\tView detailed stock information (Market Data uses yfinance)")
    print("  /boot\t\t\tSimulate a connection to a stock exchange")
    print("  /gov [--past|--future]\tCheck for government financial news (Uses Generative Deep Links)")
    print("  /help\t\t\tShow this help message")

def main():
    """Main function to run the application."""

    is_setup_command = len(sys.argv) > 1 and sys.argv[1] in ['install', 'build', 'sdist', 'bdist_wheel']

    if not is_setup_command:
        # Run boot sequence and home screen for user-facing execution
        boot_sequence()
        home_screen()

    if len(sys.argv) <= 1 or is_setup_command:
        # If no command or a setup command is passed, print help and exit if not a setup command
        if not is_setup_command:
            print_main_help()
        return

    command = sys.argv[1]
    args = sys.argv[2:]

    if command == "/view":
        parser = argparse.ArgumentParser(description='View stock information, news, and chart analysis.')
        parser.add_argument('stock_name', help='The stock ticker symbol (e.g., GOOGL)')
        parser.add_argument('-n', '--news', action='store_true', help='Display news and corporate officer information')
        parser.add_argument('-c', '--chart', action='store_true', help='Display technical analysis and market data')
        try:
            # parse_known_args is often safer in setuptools entry points
            parsed_args, unknown = parser.parse_known_args(args)
            handle_view_command(parsed_args)
        except SystemExit:
            pass
    elif command == "/boot":
        handle_boot()
    elif command == "/gov":
        # Modified to handle new flags for /gov
        handle_gov_command(args)
    elif command in ["/?", "/help"]:
        print_main_help()
    else:
        print_error(f"Unknown command: {command}")
        print_main_help()

def run_setup():
    """Setup function for packaging."""
    setup(
        name='Stock0lyzer-CLI',
        version='1.0.5',
        packages=find_packages(),
        # Added 'faker' to dependencies
        install_requires=['pandas', 'yfinance', 'requests', 'beautifulsoup4', 'colorama', 'setuptools', 'faker'],
        entry_points={'console_scripts': ['stock0lyzer=setup:main']},
    )

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] in ['install', 'build', 'sdist', 'bdist_wheel']:
        run_setup()
    else:
        main()
