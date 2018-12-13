from werkzeug.urls import url_parse, url_join
from flask import request


def is_safe_url(target) -> bool:
    ref_url = url_parse(request.host_url)
    print("=========== URL HELPERS ==========")
    print(ref_url)
    print(target)
    test_url = url_parse(url_join(request.host_url, target))
    print(test_url)
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc
