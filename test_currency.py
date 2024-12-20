import currency as cur
import json
import pandas as pd
import pytest

def test_convert_currencies_okdata():
    mock_data = json.loads('{"rates": {"SEK": 10, "EUR": 1}}')
    df = cur.convert_currencies(mock_data)
    assert isinstance(df, pd.DataFrame)

def test_convert_currencies_badjson():
    with pytest.raises(Exception):
        mock_data = json.loads('"rates": {"SEK": 10, "EUR": 1}}')