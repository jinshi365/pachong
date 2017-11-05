import re
from web_spider_go import download
import urllib.parse as urlparse


def link_crawler(seed_url, link_regex):
    """从给定的种子URL折叠中抓取链接"""
    crawl_queue = [seed_url]
    seen = set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        for link in get_links(html):
            if re.findall(link_regex, link):
                link = urlparse.urljoin(seed_url, link)
                if link not in seen:
                    seen.add(link)
                    crawl_queue.append(link)
    print(crawl_queue)


def get_links(html):
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    print(webpage_regex.findall(html))
    all_links = webpage_regex.findall(html)
    all_links.remove('http://www.51bbw.cn/liulanqi')
    return all_links

#print(get_links('http://example.webscraping.com'))
link_crawler('http://www.51bbw.cn', '51bbw')