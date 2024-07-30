# curl_fetch2py

```markdown
CurlFetch2Py — это библиотека на Python, предназначенная для парсинга команд curl и fetch, преобразуя их в
структурированные объекты Python. Это особенно полезно для преобразования сложных HTTP-запросов в формат,
который можно легко использовать с библиотекой requests и прочими подобными библиотеками на Python (например httpx).
```

## Установка

Установить библиотеку можно через pip

```bash
pip install --upgrade curl_fetch2py
```

## Пример использования

```python
import requests
from curl_fetch2py import CurlFetch2Py


# работа с CURL (bash/windows) строкой
curl_str = ('curl "https://www.python.org/" --compressed -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; '
            'rv:128.0) Gecko/20100101 Firefox/128.0" -H "Accept: text/html,application/xhtml+xml,'
            'application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8" -H "Accept-Language: '
            'en-US,en;q=0.5" -H "Accept-Encoding: gzip, deflate, br, zstd" -H "Referer: https://www.google.com/" -H '
            '"Connection: keep-alive" -H "Cookie: _ga_TF35YF9CVH=GS1.1.1722329638.1.0.1722329638.0.0.0; '
            '_ga=GA1.1.1890680152.1722329639; __utma=32101439.1890680152.1722329639.1722329639.1722329639.1; '
            '__utmb=32101439.1.10.1722329639; __utmc=32101439; __utmz=32101439.1722329639.1.1.utmcsr=google^|utmccn=('
            'organic)^|utmcmd=organic^|utmctr=(not^%^20provided); __utmt=1" -H "Upgrade-Insecure-Requests: 1" -H '
            '"Sec-Fetch-Dest: document" -H "Sec-Fetch-Mode: navigate" -H "Sec-Fetch-Site: cross-site" -H '
            '"Sec-Fetch-User: ?1" -H "Priority: u=0, i" -H "TE: trailers"')

context_curl = CurlFetch2Py.parse_curl_context(curl_str)
request_curl = requests.get(url=context_curl.url, headers=context_curl.headers, cookies=context_curl.cookies)

with open('result_curl.html', 'w', encoding='utf-8') as result:
    result.write(request_curl.text)

# работа с FETCH строкой
fetch_str = '''
await fetch("https://www.python.org/", {
    "credentials": "include",
    "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-User": "?1",
        "Priority": "u=0, i"
    },
    "referrer": "https://www.google.com/",
    "method": "GET",
    "mode": "cors"
});
'''
request_fetch = requests.get(url=context_curl.url, headers=context_curl.headers, cookies=context_curl.cookies)

with open('result_fetch.html', 'w', encoding='utf-8') as result:
    result.write(request_fetch.text)
```

## License

Этот проект лицензируется по лицензии [MIT](https://choosealicense.com/licenses/mit/).