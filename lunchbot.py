# This is a clue, you'll need to JSONify the data in order to send it as part of
# a web response
# from the package flask, import the function 'jsonify'
from flask import jsonify

# these are our employees for now - our test expects us to return them
employees = [
    'Alice',
    'Bob',
    'Charlie'
]

# this will return who is going to lunch!
def who_is_going_to_lunch():
    return 'FIXME'
