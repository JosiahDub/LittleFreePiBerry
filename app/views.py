from app import app
from flask import render_template, jsonify
import os
from instagram_auth import INSTAGRAM_PASSWORD, INSTAGRAM_USERNAME
from instagram import InstagramSession
# For testing outside of the Pi
if os.uname()[4][:3] == 'arm':
    from config import camera


def _upload_to_instagram():
    insta = InstagramSession()
    if insta.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD):
        print("good job")
    # Example
    # filepath = "/tmp/square.jpg"
    # print "Uploading " + filepath
    # insta = InstagramSession()
    # if insta.login(USERNAME, PASSWORD):
    #     media_id = insta.upload_photo("/tmp/small.jpg")
    #     print media_id
    #     if media_id is not None:
    #         insta.configure_photo(media_id, "")


@app.route('/_take_pic')
def take_pic():
    _upload_to_instagram()
    return jsonify(success=1)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Home')
