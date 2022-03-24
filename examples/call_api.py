"""
References:
    https://betterprogramming.pub/asynchronous-programming-in-python-for-making-more-api-calls-faster-419a1d2ee058

"""
# Import Libraries
import os
import sys
import pandas as pd
import asyncio
import aiohttp
from datetime import datetime

import concurrent.futures
import threading
import time
from aiohttp import ClientSession

from decouple import config as d_config
from sec_api import QueryApi


# Define Directories
DIR_ROOT = d_config("DIR_ROOT")
DIR_SRC = d_config("DIR_SRC")
DIR_DATA = d_config("DIR_DATA")
DIR_RESULTS = d_config("DIR_RESULTS")

# Other Globals
API_KEY = d_config("SEC_API_KEY")
all_company_names = [
    "Ford Motor Company", "General Motors", "IBM", "Google",
    "Apple", "AIG", "Chubb", "Logitech",
] * 100

# Functions

def get_ticker_sync(company_names: list):
    """
    """
    start = datetime.now()

    queryApi = QueryApi(api_key=API_KEY)

    for co_name in company_names:
        query = {
        "query": { "query_string": {
            "query": f"companyName:\"{co_name}\" AND formType:\"10-Q\""
            } },
        "from": "0",
        "size": "10",
        "sort": [{ "filedAt": { "order": "desc" } }]
        }

        response = queryApi.get_filings(query)

    duration = datetime.now() - start

    print(f"Duration => {duration}")


get_ticker_sync(all_company_names)

thread_local = threading.local()

global result_object
result_object = {}

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = QueryApi(api_key=API_KEY)
    return thread_local.session


def get_ticker(company_name):
    queryApi = get_session()
    query = {
        "query": { "query_string": {
            "query": f"companyName:\"{company_name}\" AND formType:\"10-Q\""
            } },
        "from": "0",
        "size": "1",
        "sort": [{ "filedAt": { "order": "desc" } }]
        }

    result_object[company_name] = queryApi.get_filings(query)['filings'][0]['ticker']


def get_all_tickers(list_companies):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(get_ticker, list_companies)


if __name__ == '__main__':
    """
    start_time = time.time()
    get_all_tickers(all_company_names)
    duration = time.time() - start_time
    print(f"Duration => {duration}")
    print(result_object)
    """




