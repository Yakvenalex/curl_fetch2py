import json

import requests

cookies = {
    'qrator_ssid': '1722280594.442.a57yReOZncEIUf8m-uugs31fp0nhrnnke5lf7co7q15atb807',
    'qrator_jsid': '1722280593.119.FYDZG7fpQe9BYN51-2jvlra5veahsrm83otikuk2erdmbk7d6',
    'lang': 'ru',
    'city_path': 'moscow',
    '_ab_': '^%^7B^%^22catalog-filter-title-test^%^22^%^3A^%^22GROUP_3^%^22^%^2C^%^22save-sort^%^22^%^3A^%^22CLASSIC_CHOICE^%^22^%^7D',
    'PHPSESSID': '5807662576565fc223211753d3bd173b',
    'current_path': '9565a5103f36ecea17597b8bfe0de40efdc12ecd83502fc6a8abccb573ee963ba^%^3A2^%^3A^%^7Bi^%^3A0^%^3Bs^%^3A12^%^3A^%^22current_path^%^22^%^3Bi^%^3A1^%^3Bs^%^3A116^%^3A^%^22^%^7B^%^22city^%^22^%^3A^%^2230b7c1f3-03fb-11dc-95ee-00151716f9f5^%^22^%^2C^%^22cityName^%^22^%^3A^%^22^%^5Cu041c^%^5Cu043e^%^5Cu0441^%^5Cu043a^%^5Cu0432^%^5Cu0430^%^22^%^2C^%^22method^%^22^%^3A^%^22default^%^22^%^7D^%^22^%^3B^%^7D',
    '_csrf': 'fa677590f9216c627782f0286b916b4584b6b78e926b8edb28298f7d1b79faa7a^%^3A2^%^3A^%^7Bi^%^3A0^%^3Bs^%^3A5^%^3A^%^22_csrf^%^22^%^3Bi^%^3A1^%^3Bs^%^3A32^%^3A^%^22OS6yEU2dGmSoHIkPEiq1vm-IoxSTMDvy^%^22^%^3B^%^7D',
    'phonesIdentV2': '13ffac65-b886-429e-b472-91a0f1a4eaa7',
    'rrpvid': '114100055544675',
    'cartUserCookieIdent_v3': 'e5f38df2ab81eb056835fee29ba7db4a7b12a87056844a68b66a76917da0c56fa^%^3A2^%^3A^%^7Bi^%^3A0^%^3Bs^%^3A22^%^3A^%^22cartUserCookieIdent_v3^%^22^%^3Bi^%^3A1^%^3Bs^%^3A36^%^3A^%^226fa7b8b0-3101-38c0-aad3-0da3f27ff130^%^22^%^3B^%^7D',
    '_ga_FLS4JETDHW': 'GS1.1.1722280604.1.1.1722282196.60.0.477514790',
    '_ga': 'GA1.1.1958258823.1722280604',
    '_gcl_au': '1.1.607980808.1722280605',
    'tmr_lvid': '7e6792bdbb78c74d065e4fbabb2a86fc',
    'tmr_lvidTS': '1722280606828',
    'rcuid': '66a7ea9b1c7c78f080f778aa',
    '_ym_uid': '1722280609244768003',
    '_ym_d': '1722280609',
    'domain_sid': 'ZqeVL7i7KlZUxx_toNb5f^%^3A1722280610144',
    '_ym_isad': '2',
    '_ym_visorc': 'b',
    'tmr_detect': '0^%^7C1722280825964',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0',
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'https://www.dns-shop.ru/catalog/recipe/54f67c2eee9f1578/s-besprovodnoj-zaradkoj/no-referrer',
    'X-Requested-With': 'XMLHttpRequest',
    'X-CSRF-Token': 'iQZ5oYn9eml27alQVSBuJXPiOQNWMDalXCcOMeC73DnGVU_YzKhIDTGA-j8daQV1NotIMiBdG-wzX11lrf-qQA==',
    'Origin': 'https://www.dns-shop.ru',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Connection': 'keep-alive',
    # 'Cookie': 'qrator_ssid=1722280594.442.a57yReOZncEIUf8m-uugs31fp0nhrnnke5lf7co7q15atb807; qrator_jsid=1722280593.119.FYDZG7fpQe9BYN51-2jvlra5veahsrm83otikuk2erdmbk7d6; lang=ru; city_path=moscow; _ab_=^%^7B^%^22catalog-filter-title-test^%^22^%^3A^%^22GROUP_3^%^22^%^2C^%^22save-sort^%^22^%^3A^%^22CLASSIC_CHOICE^%^22^%^7D; PHPSESSID=5807662576565fc223211753d3bd173b; current_path=9565a5103f36ecea17597b8bfe0de40efdc12ecd83502fc6a8abccb573ee963ba^%^3A2^%^3A^%^7Bi^%^3A0^%^3Bs^%^3A12^%^3A^%^22current_path^%^22^%^3Bi^%^3A1^%^3Bs^%^3A116^%^3A^%^22^%^7B^%^22city^%^22^%^3A^%^2230b7c1f3-03fb-11dc-95ee-00151716f9f5^%^22^%^2C^%^22cityName^%^22^%^3A^%^22^%^5Cu041c^%^5Cu043e^%^5Cu0441^%^5Cu043a^%^5Cu0432^%^5Cu0430^%^22^%^2C^%^22method^%^22^%^3A^%^22default^%^22^%^7D^%^22^%^3B^%^7D; _csrf=fa677590f9216c627782f0286b916b4584b6b78e926b8edb28298f7d1b79faa7a^%^3A2^%^3A^%^7Bi^%^3A0^%^3Bs^%^3A5^%^3A^%^22_csrf^%^22^%^3Bi^%^3A1^%^3Bs^%^3A32^%^3A^%^22OS6yEU2dGmSoHIkPEiq1vm-IoxSTMDvy^%^22^%^3B^%^7D; phonesIdentV2=13ffac65-b886-429e-b472-91a0f1a4eaa7; rrpvid=114100055544675; cartUserCookieIdent_v3=e5f38df2ab81eb056835fee29ba7db4a7b12a87056844a68b66a76917da0c56fa^%^3A2^%^3A^%^7Bi^%^3A0^%^3Bs^%^3A22^%^3A^%^22cartUserCookieIdent_v3^%^22^%^3Bi^%^3A1^%^3Bs^%^3A36^%^3A^%^226fa7b8b0-3101-38c0-aad3-0da3f27ff130^%^22^%^3B^%^7D; _ga_FLS4JETDHW=GS1.1.1722280604.1.1.1722282196.60.0.477514790; _ga=GA1.1.1958258823.1722280604; _gcl_au=1.1.607980808.1722280605; tmr_lvid=7e6792bdbb78c74d065e4fbabb2a86fc; tmr_lvidTS=1722280606828; rcuid=66a7ea9b1c7c78f080f778aa; _ym_uid=1722280609244768003; _ym_d=1722280609; domain_sid=ZqeVL7i7KlZUxx_toNb5f^%^3A1722280610144; _ym_isad=2; _ym_visorc=b; tmr_detect=0^%^7C1722280825964',
    'Priority': 'u=4',
    'Cache-Control': 'max-age=0',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

data = {"type": "product-buy",
        "containers": [{"id": "as-frrjZk", "data": {"id": "1342199"}}, {"id": "as-VczotO", "data": {"id": "5450482"}},
                       {"id": "as-u5lrtX", "data": {"id": "5450483"}}, {"id": "as-O9xpCW", "data": {"id": "5077906"}},
                       {"id": "as-Kl0XnG", "data": {"id": "5414843"}}, {"id": "as-_EDzG1", "data": {"id": "5414844"}},
                       {"id": "as-BQHHB-", "data": {"id": "5450484"}}, {"id": "as-YxRb26", "data": {"id": "5450485"}},
                       {"id": "as-IGEGWt", "data": {"id": "5450486"}}, {"id": "as-3djld3", "data": {"id": "5450487"}},
                       {"id": "as-nDxMB-", "data": {"id": "5458533"}}, {"id": "as-mlmkRn", "data": {"id": "5458532"}},
                       {"id": "as-XCg5uk", "data": {"id": "5015382"}}, {"id": "as-1k8em8", "data": {"id": "5024747"}},
                       {"id": "as-7wzIpJ", "data": {"id": "5015416"}}, {"id": "as-NbAY4d", "data": {"id": "5015418"}},
                       {"id": "as-ie9fus", "data": {"id": "5095628"}}, {"id": "as-fCzOSN", "data": {"id": "5095626"}}]}
data = {"type": "product-buy",
        "containers": [{"id": "", "data": {"id": "1342199"}}]}
data_json = json.dumps(data)
body = f"data={data_json}"
response = requests.post('https://www.dns-shop.ru/ajax-state/product-buy/', headers=headers, data=body)
print(response.json())

with open('result.html', 'w', encoding='utf-8') as result:
    result.write(response.text)