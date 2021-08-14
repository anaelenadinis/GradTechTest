import unittest

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

POINTS_PER_POSITION = {1: 3, 2: 2, 3: 1}

def validatePodium(podium):
     countries = []
     for entry in podium:
            position, country = entry.split(".")
            #check if podium position is valid
            if int(position) not in [1, 2, 3]:
                raise ValueError("Invalid podium position")
            #check for country duplicates on podium
            if country in countries:           
                raise ValueError("Duplicate country on podium")
            countries.append(country)
            

def createMedalTable(results):
    '''
    Creates a dictionary with countries and their total number of points based 
    on podium positions aquired in each sport.
    
    Parameters
    ----------
    results : a list of dictionaries, each dictionary describing a sport and its podium.

    Returns
    -------
    medalTable : a dictionary with countries as keys and total points as values.

    '''
    medalTable = {}
    for sport in results:
        podium = sport.get("podium")
        validatePodium(podium)
        for entry in podium:
            position, country = entry.split(".")
            medalTable[country] = medalTable.get(country, 0) + POINTS_PER_POSITION[int(position)]    
    return medalTable
            
def test_function():
    #This it the test function, please don't change me
    medalTable = createMedalTable(medalResults)
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

#I think it would be better to have the tests in a different file, but I wrote the class
#here so it can be tested with pytest medals.py.
class MedalTableTestCases(unittest.TestCase):
    def test_createMedalTable_shouldThrowErrorIfCountryAppearsMoreThanOnceOnPodium(self):
        medalResults = [
            {
                "sport": "cycling",
                "podium": ["1.China", "2.China", "3.ROC"]
            }
        ]
        with self.assertRaises(ValueError) as ex:
            createMedalTable(medalResults)
        self.assertEqual(str(ex.exception), "Duplicate country on podium")
        
    def test_createMedalTable_shouldThrowErrorIfPositionNotOnPodium(self):
        medalResults = [
            {
                "sport": "cycling",
                "podium": ["1.China", "2.USA", "5.ROC"]
            }
        ]
        with self.assertRaises(ValueError) as ex:
            createMedalTable(medalResults)
        self.assertEqual(str(ex.exception), "Invalid podium position")
    
