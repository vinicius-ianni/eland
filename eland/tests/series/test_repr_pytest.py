# File called _pytest for PyCharm compatability
import eland as ed
from eland.tests import ELASTICSEARCH_HOST
from eland.tests import FLIGHTS_INDEX_NAME
from eland.tests.common import TestData


class TestSeriesRepr(TestData):

    def test_repr(self):
        pd_s = self.pd_flights()['Carrier']
        ed_s = ed.Series(ELASTICSEARCH_HOST, FLIGHTS_INDEX_NAME, 'Carrier')

        pd_repr = repr(pd_s)
        ed_repr = repr(ed_s)

        assert pd_repr == ed_repr