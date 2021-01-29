import re


def get_ip_address(request) -> str:
    """
    Get the visitor's IP address.
    Получить IP адрес посетителя.
    """
    # A regular expression pattern for an IP address.
    # Шаблон регулярного выражения для IP адреса.
    # flake8: noqa W605
    IP_RE = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')

    ip_address = request.META.get(
        'HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', '127.10.0.1'))
    if ip_address:
        # make sure that only one IP
        # убедиться что только один IP
        try:
            ip_address = IP_RE.match(ip_address)
            if ip_address:
                ip_address = ip_address.group(0)
            else:
                # нет IP, вероятно, от какого-то прокси или другого устройства
                # на каком-то поддельном IP
                # no IP, probably from some proxy or other device
                # in some bogus IP
                ip_address = '10.0.0.1'
        except IndexError:
            pass
    return ip_address


def get_user_agent(request) -> str:
    """
    Get information about the visitor's browser.
    Получить информацию о браузере посетителя.
    """
    user_agent = request.META.get('HTTP_USER_AGENT', '')[:255]
    return user_agent


def get_session_key(request) -> str:
    """
    Get a visitor session.
    Получить сессию посетителя.
    """
    if not request.session.session_key:
        request.session.create()
    session_key = request.session.session_key
    return session_key
