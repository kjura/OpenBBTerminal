# IMPORTATION STANDARD

# IMPORTATION THIRDPARTY
import pytest

# IMPORTATION INTERNAL
from openbb_terminal.stocks.due_diligence import marketwatch_model


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": [("User-Agent", None)],
        "filter_query_parameters": [("token", "MOCK_TOKEN")],
    }


@pytest.mark.vcr
def test_get_rating_over_time(recorder):
    result_df = marketwatch_model.get_sec_filings(symbol="TSLA")
    recorder.capture(result_df)


@pytest.mark.vcr
@pytest.mark.parametrize(
    "ticker",
    [("VWCE.DE")],
)
def test_sec_filings_exists(recorder):
    pass
