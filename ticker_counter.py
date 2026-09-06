
def count_tickers(tickers: list[str]) -> dict[str, int]:
    """Normalize ticker symbols and count their occurrences."""

    ticker_counts = {}

    for tckr in tickers:
        tckr = tckr.strip().upper()
        ticker_counts[tckr] = ticker_counts.get(tckr, 0) + 1

    return ticker_counts