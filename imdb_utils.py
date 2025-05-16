# Basics
import pandas as pd
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# Scraping
import requests
from bs4 import BeautifulSoup



# Global session
session = requests.Session()
session.headers.update({
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
}) # we use the same headers each time (important to specify, else IMDb wouldn't load)



def get_soup(url):
    r"""Simple get soup function.

    :param url: URL/link.
    :return: Soup
    """
    
    response = session.get(url)
    return BeautifulSoup(response.content, "html.parser")

def get_titles(soup):
    r"""Retrieves the IMDb title IDs from IMDb's Advanced Title Search page (https://www.imdb.com/search/title/).

    :param soup: Soup
    :return: List of titles
    """

    return [
        {
            "name": tag.text.split(". ", 1)[1], # Name of show
            "id": tag["href"].split("/")[2]     # IMDb ID of show
        }
        for tag in soup.find_all("a", class_="ipc-title-link-wrapper")
        if ". " in tag.text and "/title/" in tag["href"]
    ]

def get_cast(title: str) -> list:
    r"""Retrieves the cast list for a title (e.g. tt1515457) on IMDb.

    :param title: IMDb title ID.
    :return: List of cast names
    """

    url = f"https://www.imdb.com/title/{title}/fullcredits/"
    soup = get_soup(url)

    return [
        {
            "name": tag.text.strip(),
            "id": tag["href"].split("/")[2],
            "title": title
        }
        for tag in soup.find_all("a", class_="ipc-link ipc-link--base name-credits--title-text name-credits--title-text-big")
        if "ttfc_cst_" in tag.get("href", "")
    ]