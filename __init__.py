from flask import Flask
from flask_uploads import UploadSet, configure_uploads
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = '/inputs'
ALLOWED_EXTENSIONS = set(['txt'])

app = Flask(__name__)
app.config['UPLOADED_INPFILES_DEST'] = os.path.join(os.path.dirname(__file__), 'inputs/')
inpfiles = UploadSet('inpfiles', ('txt',))
configure_uploads(app, (inpfiles,))

import views
_ = views

