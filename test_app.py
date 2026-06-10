import unittest
from app import calculate_emissions, suggest_actions, validate_input

class TestEcoTrackAI(unittest.TestCase):

    def test_calculate_emissions_valid(self):
        result = calculate_emissions(transport=20, electricity=15, food=10)
        expected = 20*0.3 + 15*0.5 + 10*0.2
        self.assertAlmostEqual(result, expected, places=2)

    def test_calculate_emissions_zero(self):
        result = calculate_emissions(transport=0, electricity=0, food=0)
        self.assertEqual(result, 0)

    def test_validate_input_valid(self):
        self.assertEqual(validate_input("12", "Transport"), 12.0)

    def test_validate_input_negative(self):
        with self.assertRaises(ValueError):
            validate_input("-5", "Electricity")

    def test_validate_input_non_numeric(self):
        with self.assertRaises(ValueError):
            validate_input("abc", "Food")

    def test_suggest_actions_high(self):
        self.assertEqual(suggest_actions(12), "Try reducing electricity usage or carpooling.")

    def test_suggest_actions_medium(self):
        self.assertEqual(suggest_actions(7), "Consider walking, cycling, or eating less meat.")

    def test_suggest_actions_low(self):
        self.assertEqual(suggest_actions(3), "Great job! Keep tracking your footprint.")

if __name__ == '__main__':
    unittest.main()
