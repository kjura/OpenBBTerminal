""" Market Watch Model """
__docformat__ = "numpy"


import pandas as pd
import random
import requests
from bs4 import BeautifulSoup

def get_user_agent() -> str:
    """Get a not very random user agent."""
    user_agent_strings = [
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.10; rv:86.1) Gecko/20100101 Firefox/86.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:86.1) Gecko/20100101 Firefox/86.1",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:82.1) Gecko/20100101 Firefox/82.1",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:86.0) Gecko/20100101 Firefox/86.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:86.0) Gecko/20100101 Firefox/86.0",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.10; rv:83.0) Gecko/20100101 Firefox/83.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:84.0) Gecko/20100101 Firefox/84.0",
    ]

    return random.choice(user_agent_strings)  # nosec


def get_sec_filings(symbol: str) -> pd.DataFrame:
    """Get SEC filings for a given stock ticker. [Source: Market Watch]

    Parameters
    ----------
    symbol : str
        Stock ticker symbol

    Returns
    -------
    df_financials : pd.DataFrame
        SEC filings data
    """

    pd.set_option("display.max_colwidth", None)

    url_financials = (
        f"https://www.marketwatch.com/investing/stock/{symbol}/financials/secfilings"
    )

    text_soup_secField = BeautifulSoup(requests.get(url_financials,
                                                    headers={"User-Agent": get_user_agent()}).text,
                                                    "lxml",
    )

    soup_secField = text_soup_secField.find("a", {"class": "link js-subTab",
                                                      "instrument-target": "financials/secfilings"})

    if not soup_secField:
        return print('This command is for US-listed tickers only.')
    else:
        pass

    # if url_financials in allLinks:

    #     print('Sec filings columns exists!')

    # else:
    #     print('Sec filings section does not exist. Please try your query with a different ticker')

    # print(soup_financials)
    #print(text_soup_financials.prettify())
    #print(type(allLinks[0]))


#get_sec_filings('AAPL') # vwce
get_sec_filings('aapl')
#sec = get_sec_filings('AAPL')
# attribute for sec fillings (unique?) <a class="link js-subTab" instrument-target="financials/secfilings"
# https://www.marketwatch.com/investing/stock/aapl/financials/secfilings



# if df_financials.empty:
#     print("This command is for US-listed tickers only.")
#     return None

# # Check if sec fillings field exists in HTML
# soup_secField = text_soup_financials.find("a", {"class": "link js-subTab",
#                                                 "instrument-target": "financials/secfilings"})
# if not soup_secField:
#     return pd.DataFrame()