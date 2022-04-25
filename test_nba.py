"modules for unitary testing"
import unittest
"module that include function where return pairs players"
import nba

"unittest class for Test function get_pairs_players"
class TestNBA(unittest.TestCase):
    maxDiff = None
    def test_find_pairs_players(self):
        
        result = "- Brevin Knight  Nate Robinson\n- Mike Wilks  Nate Robinson\n"
        self.assertEqual(nba.get_pairs_players(139), result )
        result1 = "No matches found"
        self.assertEqual(nba.get_pairs_players(45), result1)
        result2 = "- Chucky Atkins  Nate Robinson\n- Brevin Knight  Mike Wilks\n"
        self.assertNotEqual(nba.get_pairs_players(140), result2)
        result3 = "- Tyson Chandler  Yao Ming\n- Kyrylo Fesenko  Yao Ming\n- Marc Gasol  Yao Ming\n- Jerome James  Yao Ming\n- Shaquille O'Neal  Yao Ming\n- Joel Przybilla  Yao Ming\n- Cheikh Samb  Yao Ming\n- Robert Swift  Yao Ming\n"
        self.assertEqual(nba.get_pairs_players(175), result3)

if __name__ == '__main__':
    unittest.main()