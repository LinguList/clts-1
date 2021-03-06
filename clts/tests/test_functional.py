from clldutils.path import Path
from clld.tests.util import TestWithApp

import clts


class Tests(TestWithApp):
    __cfg__ = Path(clts.__file__).parent.joinpath('..', 'development.ini').resolve()
    __setup_db__ = False

    def test_install(self):
        from bs4 import BeautifulSoup
        assert BeautifulSoup

    def test_home(self):
        res = self.app.get('/', status=200)
