from unittest import TestCase

from neurokit.bio.bio_rsp import _get_initial_phase, _get_final_phase


class RspTest(TestCase):
    def test_get_initial_phase_expiration(self):
        phases = ['Inspiration', 'Expiration', 'Inspiration']

        initial_phase = _get_initial_phase(phases)
        expected = 'Expiration'

        self.assertEqual(initial_phase, expected)

    def test_get_initial_phase_inspiration(self):
        phases = ['Expiration', 'Inspiration', 'Expiration']

        initial_phase = _get_initial_phase(phases)
        expected = 'Inspiration'

        self.assertEqual(initial_phase, expected)

    def test_get_final_phase_inspiration(self):
        phases = ['Inspiration', 'Expiration', 'Inspiration']

        last_phase = _get_final_phase(phases)
        expected = 'Expiration'

        self.assertEqual(last_phase, expected)

    def test_get_final_phase_expiration(self):
        phases = ['Expiration', 'Inspiration', 'Expiration']

        last_phase = _get_final_phase(phases)
        expected = 'Inspiration'

        self.assertEqual(last_phase, expected)
