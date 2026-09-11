import os
import csv
from dotenv import load_dotenv
from urllib.parse import urlencode
from urllib.request import urlopen
from io import StringIO

AV_BASE_URL = "https://www.alphavantage.co/query"

def build_query_string(params: dict[str, str]) -> str:
    return urlencode(params)

def get_url(base_url: str, query_string: str) -> str:
    return f"{base_url}?{query_string}"

def request_to_dict_reader(url: str) -> csv.DictReader:
    with urlopen(url) as response:
        # Transform: raw bytes -> text -> csv file -> dict
        raw_data = response.read()
        text_data = raw_data.decode("utf-8")
        csv_file = StringIO(text_data)
        dict_data = csv.DictReader(csv_file)
    return dict_data

def extract_ticker_symbols(reader: csv.DictReader) -> set[str]:
    symbols: set[str] = set()
    for row in reader:
        symbols.add(row["symbol"])
    return symbols

def fetch_valid_tickers() -> set[str]:
    load_dotenv()
    api_key = os.environ["ALPHA_VANTAGE_API_KEY"]

    query_params = {
        "function": "LISTING_STATUS",
        "apikey": api_key,
    }
    query_string = build_query_string(query_params)
    url = get_url(AV_BASE_URL, query_string)
    reader = request_to_dict_reader(url)

    return extract_ticker_symbols(reader)
