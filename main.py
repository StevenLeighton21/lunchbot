from flask import Flask
from lunchbot import who_is_going_to_lunch
from private.config import SLACK_LUNCHBOT_SECRET


def create_lunchbot():
    app = Flask(__name__)
    @app.route('/lunch')
    def lunch():
        if request.form.get('token') == SLACK_LUNCHBOT_SECRET:
        channel = request.form.get('channel_name')
        username = request.form.get('user_name')
        text = request.form.get('text')
        inbound_message = username + " in " + channel + " says: " + text
        print(inbound_message)

        return who_is_going_to_lunch()

    return app

lunchbot = create_lunchbot()

if __name__ == '__main__':
    app = create_lunchbot()
    app.run(port=5000)
