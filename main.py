import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Replace 'base_url' with the root URL of your organization's wiki page
base_url = 'http://127.0.0.1:8000/'
page_links_with_broken_links = {}

def get_page_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        return None
    except requests.exceptions.RequestException:
        return None

def find_links(content, base_url, current_page):
    soup = BeautifulSoup(content, 'html.parser')
    links = soup.find_all('a', href=True)
    return [(urljoin(base_url, link['href']), current_page) for link in links]

def check_links(links):
    broken_count = 0
    total_count = len(links)
    for link in links:
        try:
            response = requests.head(link[0])
            if response.status_code >= 400:
                broken_count += 1
        except requests.exceptions.RequestException:
            broken_count += 1
    return broken_count, total_count

def crawl(url):
    content = get_page_content(url)
    if content:
        links = find_links(content, base_url, url)  # Pass base_url instead of url here
        broken_count, total_count = check_links(links)
        if total_count > 0:
            broken_percentage = (broken_count / total_count) * 100
            page_links_with_broken_links[url] = f"{broken_percentage:.2f}% broken links"

        for link, _ in links:
            if link.startswith(urlparse(base_url).netloc):
                crawl(link)

if __name__ == "__main__":
    crawl(base_url)

    if page_links_with_broken_links:
        print("Report on broken links:")
        for page, report in page_links_with_broken_links.items():
            print(f"Page: {page}, {report}")
    else:
        print("No broken links found.")
      
