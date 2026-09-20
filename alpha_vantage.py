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

def request_csv_text(url: str) -> str:
    with urlopen(url) as response:
        raw_data = response.read()
        return raw_data.decode("utf-8")

def text_to_dict_reader(text_data: str) -> csv.DictReader:
    csv_file = StringIO(text_data)
    return csv.DictReader(csv_file)

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
    text = request_csv_text(url)
    reader = text_to_dict_reader(text)

    return extract_ticker_symbols(reader)
