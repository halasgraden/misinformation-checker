import requests
import trafilatura


    #url="https://www.scrapethissite.com/pages/" #placeholder

    #content = requests.get(url).text

    #soup = BeautifulSoup(content, "lxml")

    #print(soup)


def scraper():
    url = "https://apnews.com/article/ice-david-brouillette-johan-guerrero-maine-shooting-dbc30d6d59e2a95fb470afc188e125c6"
    downloaded = trafilatura.fetch_url(url)
    data = trafilatura.extract(downloaded, output_format="json", with_metadata=True)

    return data
