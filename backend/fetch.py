import requests
import trafilatura


    #url="https://www.scrapethissite.com/pages/" #placeholder

    #content = requests.get(url).text

    #soup = BeautifulSoup(content, "lxml")

    #print(soup)


def scraper(url):
    downloaded = trafilatura.fetch_url(url)
    data = trafilatura.extract(downloaded, output_format="json", with_metadata=True, favor_precision=True, prune_xpath="//h1 | //h2 | //h3")

    return data
