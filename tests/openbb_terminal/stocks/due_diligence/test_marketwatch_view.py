# IMPORTATION STANDARD

# IMPORTATION THIRDPARTY
import pytest

# IMPORTATION INTERNAL
from openbb_terminal.stocks.due_diligence import marketwatch_view


@pytest.mark.vcr
@pytest.mark.record_stdout
def test_analyst():
    marketwatch_view.sec_filings(symbol="TSLA", limit=5, export=None)


@pytest.mark.vcr
@pytest.mark.record_stdout
def test_sec_filings_is_empty():
    # marketwatch_view.sec_filings(symbol="TSLA", limit=5, export=None)
    # marketwatch_view.sec_filings(symbol="TSLA", limit=5, export=None)
    # marketwatch_view.sec_filings(symbol="TSLA", limit=5, export=None)
    # marketwatch_view.sec_filings(symbol="TSLA", limit=5, export=None)
    pass
