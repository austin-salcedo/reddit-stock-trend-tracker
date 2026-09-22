import csv
import os
import time
from datetime import datetime, timedelta
from pathlib import Path
from io import StringIO
from alpha_vantage import build_query_string, get_url, extract_ticker_symbols, cache_csv, cache_expired

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


#################
# Cache testing #
#################

def test_cache_csv_writes_data(tmp_path):
    cache_path = tmp_path / "av_listing_status.csv"
    data = "symbol,name\nAAPL,Apple Inc\n"

    cache_csv(data, cache_path)

    assert cache_path.read_text() == data

def test_cache_expired_when_file_does_not_exist(tmp_path):
    cache_path = tmp_path / "missing.csv"

    assert cache_expired(cache_path) is True

def test_cache_not_expired_when_recent(tmp_path):
    cache_path = tmp_path / "av_listing_status.csv"
    cache_path.write_text("test")

    assert cache_expired(cache_path) is False

def test_cache_expired_when_old(tmp_path):
    cache_path = tmp_path / "av_listing_status.csv"
    cache_path.write_text("test")

    old_time = time.time() - (25 * 60 * 60)

    os.utime(cache_path, (old_time, old_time))

    assert cache_expired(cache_path) is True
