# Grad Tech Test - Python

## Description

This project is separated into two files, one for functionality (medals.py) and one for unit tests (medals_tests.py).

In the file medals.py, the function createMedalTable returns a dictionary containing country names and the number of points accumulated based on their podium position in various sports.

The file medals_tests.py contains three unit tests. The first one is the original test function which I included in the class for cohesion. The second function tests for country duplicates on the podium. The third function tests for invalid podium positions.

## Thought process

For the createMedalTable function, I implemented an O(N^2) nested loop as each podium entry for each sport needs to be parsed. The first loop iterates through each element in the larger list of results and extracts the value to the "podium" key, after that, the validatePodium function is called in order to see if the entries in podium have the accepted numbers for position and no duplicates of country. If no error is raised, the second loop iterates each entry in the list attributed as value to the "podium" key and separates it into position and country. Next, the medalTable dictionary is populated by attributing each country the number of points it earned for the respective sport.The number of points gaineed for each position was stored in the constant POINTS_PER_POSITION. The function returns the medalTable where each country is attributed the total number of points gained.

## Setup

Install python3 and matching pip on your system, use pip to install pytest.
Run the tests using pytest medals_tests.py




