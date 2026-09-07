from ticker_counter import count_tickers
from file_handler import lines_from
from pathlib import Path

TEST_TICKERS_FILE = Path("tests/test_data/test_tickers.txt")

def main():

    try:
        ticker_list = lines_from(TEST_TICKERS_FILE)
    except FileNotFoundError as exc:
        print(f"Error loading ticker data:\n {exc}")
        return

    ticker_counts = count_tickers(ticker_list)
    print(f"Given a list of tickers: {ticker_list}\n" +
          f"Here are the counts of each ticker: {ticker_counts}")

if __name__ == "__main__":
    main()