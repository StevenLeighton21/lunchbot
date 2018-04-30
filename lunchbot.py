from flask import jsonify

employees = [
    'Alice',
    'Bob',
    'Charlie'
]

def who_is_going_to_lunch():
    return jsonify(employees)
