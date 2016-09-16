from flask import Flask
from flask_uploads import UploadSet, configure_uploads
from werkzeug.utils import secure_filename
from configurations import *
import os



#Flask APP and configurations
app = Flask(__name__)
app.config['UPLOADED_INPFILES_DEST'] = os.path.join(os.path.dirname(__file__), FILE_REL_FOLDER)
app.config['MAX_CONTENT_PATH'] = 1024
app.config['SECRET_KEY'] = '32840248302d8d2098s810s80k4'

#Upload object and configurations
inpfiles = UploadSet('inpfiles', ('txt',))
configure_uploads(app, (inpfiles,))

import views
_ = views

