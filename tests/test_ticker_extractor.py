from ticker_extractor import extract_tickers

VALID_TICKERS = {
    "VOO",
    "AMZN",
    "WMT",
    "CASY",
    "ASTS",
    "SPCX",
    "RDDT",
    "NVDA",
    "GOOG",
    "SPY",
    "TSLA",
    "AAPL",
}

def test_extract_ticker_with_dollarsign_prefix():
    """Tests inputs with only `$`-prefixed ticker symbols"""
    input1 = "Just $VOO and chill."
    expected1 = ["VOO"]
    actual1 = extract_tickers(input1, VALID_TICKERS)

    input2 = "I think $AMZN, $WMT and $CASY are about to skyrocket"
    expected2 = ["AMZN", "WMT", "CASY"]
    actual2 = extract_tickers(input2, VALID_TICKERS)

    input3 = "$aapl looks good"
    expected3 = ["AAPL"]
    actual3 = extract_tickers(input3, VALID_TICKERS)

    input4 = "I like ($AAPL) here"
    expected4 = ["AAPL"]
    actual4 = extract_tickers(input4, VALID_TICKERS)

    assert expected1 == actual1
    assert expected2 == actual2
    assert expected3 == actual3
    assert expected4 == actual4


def test_extract_ticker_with_no_dollarsign_prefix():
    """Tests inputs with no `$` prefixes before ticker symbols"""
    expected = []

    input1 = "No tickers or dollarsigns here."
    actual1 = extract_tickers(input1, VALID_TICKERS)

    input2 = "I just bought more SPY calls."
    actual2 = extract_tickers(input2, VALID_TICKERS)

    input3 = "I just made so much $$$ today."
    actual3 = extract_tickers(input3, VALID_TICKERS)

    input4 = "I just bought $4500 worth of AMZN"
    actual4 = extract_tickers(input4, VALID_TICKERS)

    assert actual1 == expected
    assert actual2 == expected
    assert actual3 == expected
    assert actual4 == expected

def test_extract_with_mixed_prefix():
    """Tests inputs with a mixture of tickers with and without `$` prefixes"""

    input1 = "I think $AMZN, $WMT and CASY are about to skyrocket"
    expected1 = ["AMZN", "WMT"]
    actual1 = extract_tickers(input1, VALID_TICKERS)

    input2 = "We have SPCX to thank for $ASTS dropping today"
    expected2 = ["ASTS"]
    actual2 = extract_tickers(input2, VALID_TICKERS)

    assert actual1 == expected1
    assert actual2 == expected2

def test_extract_with_adjacent_punctuation():
    """Tests inputs with adjacent punctuation marks"""
    input1 = "I just bought $NVDA, $TSLA, and $GOOG."
    expected1 = ["NVDA", "TSLA", "GOOG"]
    actual1 = extract_tickers(input1, VALID_TICKERS)

    input2 = " yeah ,$RDDT is really beaten down"
    expected2 = ["RDDT"]
    actual2 = extract_tickers(input2, VALID_TICKERS)

    assert actual1 == expected1
    assert actual2 == expected2

def test_extract_duplicate_mentions():
    input1 = "$AAPL looks good, but $AAPL is expensive."
    expected1 = ["AAPL", "AAPL"]
    actual1 = extract_tickers(input1, VALID_TICKERS)

    assert actual1 == expected1
