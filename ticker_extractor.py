import string

PUNCTUATION_STRING = string.punctuation.replace("$", "")
MAX_TICKER_LENGTH = 5

def extract_tickers(line: str, valid_tickers: set[str]) -> list[str]:
    """
    VERSION 1.0: only extracts ticker symbols prefixed with `$` symbol.

    Extracts ticker symbols from a string, stripping whitespace and normalizing case.
    Returns a list of ticker symbols in uppercase.

    Example line: "I like $AAPL and $GOOG, but not TSLA."
    Expected output: ['AAPL', 'GOOG']
    """ 
    tickers = []
    words = line.split()

    for w in words:
        # remove any punctuation except for '$'
        w = w.strip().upper().translate(str.maketrans('', '', PUNCTUATION_STRING))
        
        if w.startswith("$"):
            candidate = w[1:]
            if (1 <= len(candidate) <= MAX_TICKER_LENGTH) and candidate in valid_tickers:
                tickers.append(candidate)
    return tickers
