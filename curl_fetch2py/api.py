import argparse
import logging
import shlex
from collections import OrderedDict, namedtuple
from http.cookies import SimpleCookie
import json


class CurlFetch2Py:
    """
    Класс для парсинга команд curl и fetch.

    Методы:
        parse_curl_context(curl_command): Парсит curl команду.
        parse_fetch_context(fetch_command): Парсит fetch команду.
    """

    def __init__(self):
        # Настройка логирования
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

        # Определение именованного кортежа для хранения контекста
        self.ParsedContext = namedtuple('ParsedContext',
                                        [
                                            'method', 'url', 'data', 'headers', 'cookies', 'verify', 'auth',
                                            'mode', 'cache', 'redirect', 'referrer', 'referrerPolicy', 'integrity',
                                            'keepalive', 'signal', 'window'
                                        ])

        # Инициализация парсера аргументов
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('command')
        self.parser.add_argument('url')
        self.parser.add_argument('-d', '--data')
        self.parser.add_argument('-b', '--data-binary', '--data-raw', default=None)
        self.parser.add_argument('-X', default='')
        self.parser.add_argument('-H', '--header', action='append', default=[])
        self.parser.add_argument('--compressed', action='store_true')
        self.parser.add_argument('-k', '--insecure', action='store_true')
        self.parser.add_argument('--user', '-u', default=())
        self.parser.add_argument('-i', '--include', action='store_true')
        self.parser.add_argument('-s', '--silent', action='store_true')
        self.parser.add_argument('--method', default='GET')
        self.parser.add_argument('--headers', default=None)
        self.parser.add_argument('--body', default=None)
        self.parser.add_argument('--credentials', default=None)
        self.parser.add_argument('--mode', default=None)
        self.parser.add_argument('--cache', default=None)
        self.parser.add_argument('--redirect', default=None)
        self.parser.add_argument('--referrer', default=None)
        self.parser.add_argument('--referrerPolicy', default=None)
        self.parser.add_argument('--integrity', default=None)
        self.parser.add_argument('--keepalive', default=None)
        self.parser.add_argument('--signal', default=None)
        self.parser.add_argument('--window', default=None)

    @staticmethod
    def parse_curl_context(curl_command):
        """
        Парсит curl команду в структурированный контекст.

        :param curl_command: str, строка с curl командой
        :return: ParsedContext, именованный кортеж с информацией о парсинге
        """
        instance = CurlFetch2Py()
        instance.logger.debug(f"Parsing curl command: {curl_command}")
        method = "get"
        tokens = shlex.split(curl_command)
        parsed_args = instance.parser.parse_args(tokens)

        # Определение HTTP метода
        post_data = parsed_args.data or parsed_args.data_binary
        if post_data:
            method = 'post'
        if parsed_args.X:
            method = parsed_args.X.lower()

        # Инициализация заголовков и cookies
        cookie_dict = OrderedDict()
        headers = OrderedDict()

        for curl_header in parsed_args.header:
            # Корректное разделение заголовка на ключ-значение
            parts = curl_header.split(":", 1)
            if len(parts) == 2:
                header_key, header_value = parts
                header_value = header_value.strip()
                if header_key.lower().strip("$") == 'cookie':
                    cookie = SimpleCookie(header_value)
                    for key in cookie:
                        cookie_dict[key] = cookie[key].value
                else:
                    headers[header_key] = header_value

        if headers.get('Accept-Encoding'):
            headers['Accept-Encoding'] = None

        # Добавление информации об аутентификации
        auth = None
        if parsed_args.user:
            auth = tuple(parsed_args.user.split(':'))

        context = instance.ParsedContext(
            method=method,
            url=parsed_args.url,
            data=post_data,
            headers=headers,
            cookies=cookie_dict,
            verify=not parsed_args.insecure,
            auth=auth,
            mode=None,
            cache=None,
            redirect=None,
            referrer=None,
            referrerPolicy=None,
            integrity=None,
            keepalive=None,
            signal=None,
            window=None
        )
        instance.logger.debug(f"Parsed context: {context}")
        return context

    @staticmethod
    def parse_fetch_context(fetch_command):
        """
        Парсит fetch команду в структурированный контекст.

        :param fetch_command: str, строка с fetch командой
        :return: ParsedContext, именованный кортеж с информацией о парсинге
        """
        instance = CurlFetch2Py()
        instance.logger.debug(f"Parsing fetch command: {fetch_command}")

        # Преобразование команды fetch в JSON-формат для парсинга
        command = fetch_command.replace('await ', '').replace("fetch(", "[", 1).rsplit(")", 1)[0] + "]"
        command = command.replace("\"", "\"")  # Fix the escaping issues

        try:
            command_json = json.loads(command)
        except json.JSONDecodeError as e:
            instance.logger.error(f"Error parsing fetch command: {e}")
            raise

        url = command_json[0]
        options = command_json[1]

        method = options.get("method", "GET").lower()
        headers = OrderedDict(options.get("headers", {}))

        if headers.get('Accept-Encoding'):
            headers['Accept-Encoding'] = None

        body = options.get("body", None)
        mode = options.get("mode", None)
        cache = options.get("cache", None)
        redirect = options.get("redirect", None)
        referrer = options.get("referrer", None)
        referrer_policy = options.get("referrerPolicy", None)
        integrity = options.get("integrity", None)
        keepalive = options.get("keepalive", None)
        signal = options.get("signal", None)
        window = options.get("window", None)

        cookie_dict = OrderedDict()
        if 'cookie' in headers:
            cookie = SimpleCookie(headers.pop('cookie'))
            for key in cookie:
                cookie_dict[key] = cookie[key].value

        context = instance.ParsedContext(
            method=method,
            url=url,
            data=body,
            headers=headers,
            cookies=cookie_dict,
            verify=True,
            auth=None,
            mode=mode,
            cache=cache,
            redirect=redirect,
            referrer=referrer,
            referrerPolicy=referrer_policy,
            integrity=integrity,
            keepalive=keepalive,
            signal=signal,
            window=window
        )
        instance.logger.debug(f"Parsed context: {context}")
        return context