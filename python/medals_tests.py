import unittest
import medals

class MedalTableTestCases(unittest.TestCase):
    def test_function(self):
        medalResults = [
            {
                "sport": "cycling",
                "podium": ["1.China", "2.Germany", "3.ROC"]
            },
            {
                "sport": "fencing",
                "podium": ["1.ROC", "2.France", "3.Italy"]
            },
            {
                "sport": "high jump",
                "podium": ["1.Italy", "1.Qatar", "3.Belarus"]
            },
            {
                "sport": "swimming",
                "podium": ["1.USA", "2.France", "3.Brazil"]
            }
        ]
        #This it the test function, please don't change me
        medalTable = medals.createMedalTable(medalResults)
        expectedTable = {
            "Italy": 4,
            "France": 4,
            "ROC": 4,
            "USA": 3,
            "Qatar": 3,
            "China": 3,
            "Germany": 2,
            "Brazil": 1,
            "Belarus": 1,
        }
        assert medalTable == expectedTable
        
    def test_createMedalTable_shouldThrowErrorIfCountryAppearsMoreThanOnceOnPodium(self):
        medalResults = [
            {
                "sport": "cycling",
                "podium": ["1.China", "2.China", "3.ROC"]
            }
        ]
        with self.assertRaises(ValueError) as ex:
            medals.createMedalTable(medalResults)
        self.assertEqual(str(ex.exception), "Duplicate country on podium")
        
    def test_createMedalTable_shouldThrowErrorIfPositionNotOnPodium(self):
        medalResults = [
            {
                "sport": "cycling",
                "podium": ["1.China", "2.USA", "5.ROC"]
            }
        ]
        with self.assertRaises(ValueError) as ex:
            medals.createMedalTable(medalResults)
        self.assertEqual(str(ex.exception), "Invalid podium position")
