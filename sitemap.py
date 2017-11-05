from web_spider_go import download
import re


# 根据robots.TXT中的sitemap 便利网站结构


def carawl_sitemap(url):
    sitemap = download(url)
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    print(links)
    for link in links:
        html = download(link)
        print('ttttt' + html)


print(carawl_sitemap('http://example.webscraping.com/sitemap.xml'))
