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
