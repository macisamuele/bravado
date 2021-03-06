# -*- coding: utf-8 -*-
from bravado.requests_client import RequestsClient


def test_separate_params():
    request_params = {
        'url': 'http://foo.com',
        'connect_timeout': 1,
        'timeout': 2
    }
    sanitized, misc = RequestsClient().separate_params(request_params)
    assert sanitized == {'url': 'http://foo.com'}
    assert misc == {
        'connect_timeout': 1,
        'ssl_cert': None,
        'ssl_verify': True,
        'follow_redirects': False,
        'timeout': 2,
    }
