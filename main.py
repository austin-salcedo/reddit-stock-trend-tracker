from ticker_counter import count_tickers, EXAMPLE_TICKERS_LIST

def main():

    ticker_counts = count_tickers(EXAMPLE_TICKERS_LIST)
    print(f"Given a list of tickers: {EXAMPLE_TICKERS_LIST}\n" +
          f"Here are the counts of each ticker: {ticker_counts}")

if __name__ == "__main__":
    main()