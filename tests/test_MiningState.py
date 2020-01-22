from unittest import TestCase
from MiningState import MiningState


class TestMiningState(TestCase):
    def test_get_state(self):
        self.assertIsInstance(MiningState.get_state(), str)
        self.assertEqual(MiningState.get_state(), "off", "on")

    def test_set_state(self):
        test_string = "cheese"
        MiningState.set_state(test_string)
        self.assertEqual(MiningState.get_state(), test_string)
        test_string = "cheese2"
        MiningState.set_state(test_string)
        self.assertEqual(MiningState.get_state(), test_string)
        # reset the state for deploy
        MiningState.set_state("off")
        self.assertEqual(MiningState.get_state(), "off")
