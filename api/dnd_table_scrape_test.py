import unittest
from dnd_table_scrape import match_d20_header

class TestMatchD20Header(unittest.TestCase):

    def test_all_possible_ints(self):
        answer = ""
        for i in range(1, 20):
            if i <= 3:
                answer = "1-3/Extreme"
            if i <= 9:
                answer = "4-9/Moderate"
            if i <= 20:
                answer = "10-20/Nuisance"
            self.assertEqual(match_d20_header(i), answer)

if __name__ == "__main__":
    unittest.main()
