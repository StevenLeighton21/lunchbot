from flask import Flask
from lunchbot import who_is_going_to_lunch


def create_lunchbot():
    app = Flask(__name__)
    @app.route('/lunch')
    def lunch():
        return who_is_going_to_lunch()

    return app

lunchbot = create_lunchbot()

if __name__ == '__main__':
    app = create_lunchbot()
    app.run(port=5000)
