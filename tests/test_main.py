from main import count_tickers

###########################################
## Test cases for count_tickers function ##
###########################################

def test_lowercase_normalization():
    test_input = ["aapl", "AAPL", "aaPl"]
    expected_output = {"AAPL": 3}

    assert expected_output == count_tickers(test_input)

def test_whitespace_normalization():
    test_input = [" aapl ", "AAPL", "aapl\n"]
    expected_output = {"AAPL": 3}

    assert expected_output == count_tickers(test_input)

def test_empty_input():
    test_input = []
    expected_output = {}

    assert expected_output == count_tickers(test_input)

def test_mixed_input():
    test_input = ["aapl", " MSFT ", "msft", "tsla ", "TSLA"]
    expected_output = {"AAPL": 1, "MSFT": 2, "TSLA": 2}

    assert expected_output == count_tickers(test_input)