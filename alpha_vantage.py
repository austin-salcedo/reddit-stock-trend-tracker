import os
import csv
from dotenv import load_dotenv
from urllib.parse import urlencode
from urllib.request import urlopen
from io import StringIO
from pathlib import Path
from datetime import datetime, timedelta

AV_BASE_URL = "https://www.alphavantage.co/query"
AV_LISTINGS_CACHE = Path("data/av_listing_status.csv")
CACHE_TTL_HOURS = 24

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

def cache_csv(data: str, cache_path: Path):
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(data)
    
def cache_expired(cache_path: Path) -> bool:
    if not cache_path.exists():
        return True

    modified_timestamp = cache_path.stat().st_mtime
    modified_time = datetime.fromtimestamp(modified_timestamp)

    current_time = datetime.now()
    cache_age = current_time - modified_time

    return cache_age > timedelta(hours=CACHE_TTL_HOURS)

def fetch_valid_tickers() -> set[str]:

    if not cache_expired(AV_LISTINGS_CACHE):
        text = AV_LISTINGS_CACHE.read_text()
    else:
        load_dotenv()
        api_key = os.environ["ALPHA_VANTAGE_API_KEY"]

        query_params = {
            "function": "LISTING_STATUS",
            "apikey": api_key,
        }
        query_string = build_query_string(query_params)
        url = get_url(AV_BASE_URL, query_string)
        text = request_csv_text(url)

        cache_csv(text, AV_LISTINGS_CACHE)

    reader = text_to_dict_reader(text)

    return extract_ticker_symbols(reader)
