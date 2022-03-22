# Minor project : OptimalDelivery

This software is a route planning system and the purpose of this product is to provide the user with the most optimal and cost efficient route to the trucks between the pick-up point which is predetermined and the consumer.
Team 4 decided to use a command line interface that can be used on Linux, Microsoft, and MacOS systems by using the front end language, python. 
To approach this prompt, the team used agile methodology and scrum calls to address and come up with a solution in four sprints that involved: Requirements engineering; System Modeling; Architectural Design; Design and Implementation; Software Testing; and Evaluation.
All of these components helped us come up with a program that satisfies all the requirements. 


# Rutgers Delivery Tool

Did the front-end.
Did the back end



## Basic Setup
1. [Install Poetry](https://python-poetry.org/docs/). Don't forget to add the poetry command to your PATH (Instructions to do this is given post-installation)
2. Navigate to the GitHub Project
3. Install Dependencies with `poetry install`
4. Run with `poetry run python3 rutgersdelivery/main.py`. You need Python 3.9 and above to run

**Password is rurahrah**

# How to run the program 
This is on how to input user values: 

1. Click on the rutgersdelivery folder and open up the main.py file.
2. Run this program.
3. It asks for user input:
   - Password: 'rurahrah' 
   - If password is verified, it asks for the number of trucks required. 
   - Enter the number of trucks available
   - Enter the number of routes required
   - If approved (# of trucks >= # of routes) , the gas price is displayed
   - The next input is points of the truck's route
   - The input would be added to the truck's current route list
   - If finished, select 'END ROUTE SELECTION' option
   - If not finished, more inputs can be added 

## How to run test cases

We ran the testcases using pytest. 
1. Click on the rutgersdelivery folder and open up the main.py file. 
2. Open up the helpers.py.

## Contributors 
1. Akanksha Arun - aa2013@scarletmail.rutgers.edu
2. Eshaan Mathur - em919@scarletmail.rutgers.edu
3. Eoin O’Hare - eso25@scarletmail.rutgers.edu
4. Sidhu Arakkal - ssa150@scarletmail.rutgers.edu
5. Mohammad Awais Zubair - maz106@scarletmail.rutgers.edu
