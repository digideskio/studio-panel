import os
from flask import Flask, Blueprint, render_template, redirect, url_for
from flask.ext.thumbnails import Thumbnail

import config

app = Flask(__name__)
app.config.from_object(config.Deployment)
thumb = Thumbnail(app)

filemanager = Blueprint('filemanager', __name__, static_folder='static/files')

@app.route("/")
def hello():
    images = []
    gooseberry = app.config['GOOSEBERRY_FOLDER']
    for dirname, dirnames, filenames in os.walk(gooseberry):
        for filename in filenames:
            if filename.endswith('.jpg') or filename.endswith('.png'):
                #print filename
                #print os.path.join(dirname, filename)
                relpath = os.path.relpath(dirname, gooseberry)
                file_relative_path = os.path.join('gooseberry/' + relpath, filename)
                images.append(file_relative_path)
                #images.append(filename)
                #print file_relative_path
                #print file_relative_path
    return render_template(
        'slideshow/index.html',
        title='Weekly Time',
        images=images)    

