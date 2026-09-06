EXAMPLE_TICKERS_LIST = ["AAPL", " tsla ", "AAPL", "goog", "TSLA", "aapl"]


def count_tickers(tickers):
    """Normalize ticker symbols and count their occurrences."""

    ticker_counts = {}

    for tckr in tickers:
        tckr = tckr.strip().upper()
        ticker_counts[tckr] = ticker_counts.get(tckr, 0) + 1

    return ticker_counts


def main():

    ticker_counts = count_tickers(EXAMPLE_TICKERS_LIST)
    print(f"Given a list of tickers: {EXAMPLE_TICKERS_LIST}\n" +
          f"Here are the counts of each ticker: {ticker_counts}")

if __name__ == "__main__":
    main()