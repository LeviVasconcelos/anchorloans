from wbsite import app, inpfiles
from flask_uploads import UploadNotAllowed
from flask import redirect, url_for, request, render_template
from utils import DivisibilityProblem

@app.route('/')
def start():
	return render_template('base.html')

@app.route('/upload', methods=['POST'])
def upload():
	if 'inpt' in request.files:
		try:
			filename = inpfiles.save(request.files['inpt'])
		except UploadNotAllowed as e:
			return 'Sorry, this upload was not allowed, text files only.'
	return render_template('base.html')	

@app.route('/loaded/<string:filename>')
def loadfile(filename):
	return ''