import requests
import trafilatura


    #url="https://www.scrapethissite.com/pages/" #placeholder

    #content = requests.get(url).text

    #soup = BeautifulSoup(content, "lxml")

    #print(soup)


def scraper():
    url = "https://www.scrapethissite.com/pages/"
    downloaded = trafilatura.fetch_url(url)
    data = trafilatura.extract(downloaded, output_format="json", with_metadata=True)

    return data
