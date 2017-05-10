import datetime
from unittest import TestCase

from freezegun import freeze_time
import numpy as np

from neurokit.bio.bio_ecg import _create_rri, _create_time_index


class BioEcg(TestCase):
    def test_create_rri_based_on_sampling_rate_1000(self):
        r_peaks = np.array([559, 1180, 1734, 2289, 2862])

        rri = _create_rri(r_peaks, sampling_rate=1000)

        expected = np.array([621, 554, 555, 573])

        np.testing.assert_array_equal(rri, expected)


class TimeIndex(TestCase):
    @freeze_time('2017-5-10 17:22:58,539465')
    def test_create_time_index(self):
        ts = np.array([1.17999607,  1.73399422,  2.28899237,  2.86199046])

        time_index = _create_time_index(ts)
        expected = [datetime.datetime(2017, 5, 10, 17, 22, 59, 719461),
                    datetime.datetime(2017, 5, 10, 17, 23, 1, 453455),
                    datetime.datetime(2017, 5, 10, 17, 23, 3, 742448),
                    datetime.datetime(2017, 5, 10, 17, 23, 6, 604438)
                    ]

        np.testing.assert_array_equal(time_index, expected)
