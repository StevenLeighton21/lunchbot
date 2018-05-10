from flask import jsonify
import random

employees = [
    'Alice',
    'Bob',
    'Charlie',
    'Lola',
    'Derek',
    'Bobby',
    'Chloe',
    'Dan',
    'Julie',
    'Karen',
    'Sharon',
    'Susie',
    'Steve',
    'Luke',
    'Bobby C',
    'Melissa',
    'Jules',
    'Pippa',
    'Nathan',
    'Sandra',
    'Phillip'
]

def who_is_going_to_lunch():
    lunchers = random.sample(employees, 8)
    # generate the random value / name
    # return 8 random values each time the method is run
    # ensure that there are no repeat value generations until
    # all values have been selected
    return jsonify(lunchers)
