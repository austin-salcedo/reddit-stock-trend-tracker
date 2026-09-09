import alpha_vantage
from ticker_counter import count_tickers
from file_handler import lines_from
from pathlib import Path

TEST_TICKERS_FILE = Path("tests/test_data/test_tickers.txt")

def main():

    valid_tickers = alpha_vantage.fetch_valid_tickers()
    print(valid_tickers)

if __name__ == "__main__":
    main()