import urllib.request
import urllib.error
import builtwith


def download(url, user_agent='jinsh', num_retries=2):
    """print(builtwith.parse(url))"""
    print('当前下载链接', url)
    headers = {'User-agent': user_agent}
    request = urllib.request.Request(url, headers=headers)
    try:
        html = urllib.request.urlopen(request).read().decode('utf-8')
    except urllib.error.URLError as e:
        print('下载错误', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 >= e.code < 600:
                return download(url, user_agent, num_retries-1)
    return html

