# This is a clue, you'll need to JSONify the data in order to send it as part of
# a web response
from flask import jsonify

# these are our employees for now
employees = [
    'Alice',
    'Bob',
    'Charlie'
]

# this will return who is going to lunch!
def who_is_going_to_lunch():
    return jsonify(employees)
