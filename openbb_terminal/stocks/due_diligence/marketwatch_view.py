""" Market Watch View """
__docformat__ = "numpy"

import logging
import os

from openbb_terminal.decorators import log_start_end
from openbb_terminal.helper_funcs import export_data, print_rich_table
from openbb_terminal.stocks.due_diligence import marketwatch_model

logger = logging.getLogger(__name__)


@log_start_end(log=logger)
def sec_filings(symbol: str, limit: int = 5, export: str = ""):
    """Display SEC filings for a given stock ticker. [Source: Market Watch]

    Parameters
    ----------
    symbol: str
        Stock ticker symbol
    limit: int
        Number of ratings to display
    export: str
        Export dataframe data to csv,json,xlsx file
    """
    df_financials = marketwatch_model.get_sec_filings(symbol)

    if df_financials.empty:
        print("This command is for US-listed tickers only.")
        return None

    print_rich_table(
        df_financials.head(limit),
        headers=list(df_financials.columns),
        show_index=True,
        title="SEC Filings",
    )

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "sec",
        df_financials,
    )
