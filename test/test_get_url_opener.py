from unittest import TestCase

from lib import api


def patch_config():
    # fill in your username and password to run tests
    settings = {
        'token': '',
        'username': '',
        'password': '',
        'logged_in': False,
        'configured': True,
        'uid': None,
        'last_login': "1970-01-01 23:59:00.000000",
    }

    def get_config(key):
        return settings[key]

    def set_config(key, value):
        settings[key] = value

    from lib.api import config
    config.get_config = get_config
    config.set_config = set_config
    config.get_setting = get_config
    config.set_setting = set_config


class TestGet_url_opener(TestCase):
    def test_login_success(self):
        patch_config()
        try:
            api.login()
        except Exception as e:
            self.fail(e.message)

    def test_get_channels(self):
        patch_config()

        try:
            channels = api.get_channels()
            self.assertGreater(len(channels), 0)
        except Exception as e:
            self.fail(e.message)

    def test_get_stream_url(self):
        patch_config()

        try:
            api.login()
            # 101 - LTV 1
            stream_url = api.get_stream_url("101")
            self.assertIsNotNone(stream_url)
        except Exception as e:
            self.fail(e.message)
