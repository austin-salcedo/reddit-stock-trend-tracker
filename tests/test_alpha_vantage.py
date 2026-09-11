import csv
from io import StringIO
from alpha_vantage import build_query_string, get_url, extract_ticker_symbols

def test_build_query_string():
    params = {
        "function": "LISTING_STATUS",
        "apikey": "fake_key",
    }

    result = build_query_string(params)

    assert result == "function=LISTING_STATUS&apikey=fake_key"


def test_get_url():
    base_url = "https://example.com/query"
    query_string = "function=LISTING_STATUS&apikey=fake_key"

    result = get_url(base_url, query_string)

    assert result == (
        "https://example.com/query?"
        "function=LISTING_STATUS&apikey=fake_key"
    )

def test_extract_symbols():
    csv_text = (
        "symbol,name,exchange,status\n"
        "AAPL,Apple Inc,NASDAQ,Active\n"
        "MSFT,Microsoft Corp,NASDAQ,Active\n"
        "SPY,SPDR S&P 500 ETF,NYSE,Active\n"
    )

    reader = csv.DictReader(StringIO(csv_text))

    result = extract_ticker_symbols(reader)

    assert result == {"AAPL", "MSFT", "SPY"}
    