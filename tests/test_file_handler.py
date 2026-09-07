from file_handler import lines_from
from pathlib import Path
import pytest

TEST_TICKERS_FILE = Path("tests/test_data/test_tickers.txt")
EXPECTED_TICKERS = ['   aapl\n', 'Aapl\n', 'goog\n', ' GOOG\n', 
                    'GooG\n', 'tsLA\n', 'MSFT\n', 'mSft\n', 'nvda\n', 
                    'NVDA   \n', '  NvDa\n', 'amzn\n', 'Amzn\n', 
                    'AMZN\n', ' meta\n', 'mEtA\n', 'gme\n', 'GME \n', 
                    'amc\n', 'AmC  \n', '  pltr\n', ' PLTR\n', 'Pltr']

def test_lines_from_reads_file():
    tickers = lines_from(TEST_TICKERS_FILE)
    assert tickers == EXPECTED_TICKERS

def test_lines_from_empty_file(tmp_path):
    empty_input = tmp_path / "empty_tickers.txt"
    empty_input.write_text("")
    empty_tickers = lines_from(empty_input)
    assert empty_tickers == []

def test_lines_from_missing_file():
    with pytest.raises(FileNotFoundError):
        lines_from("non-existent.txt")

def test_lines_from_receives_path():
    assert isinstance(TEST_TICKERS_FILE, Path)