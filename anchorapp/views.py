from anchorapp import app, inpfiles
from flask_uploads import UploadNotAllowed
from flask import redirect, url_for, request, render_template, g
from utils import DivisibilityProblem, BadInstance, FileValidationError
import os

@app.route('/')
def start():
	return render_template('base.html', input_text='Input file text', output_text='Output file text')

@app.route('/upload', methods=['POST'])
def upload():
	if 'inpt' in request.files:
		try:
			g.filename = inpfiles.save(request.files['inpt'])
			path_to_file = os.path.join(os.path.dirname(__file__), 'inputs/' + g.filename)
			g.file = open(path_to_file,'r')
			return render_template('base.html', input_text=g.file.read(), output_text='Output file text, generate on Compute button.')
		except UploadNotAllowed as e: #TO-DO: FLASH ERROR MESSAGE INTO THE SAME TEMPLATE.
			return 'Sorry, this upload was not allowed, text files only.'
	return render_template('base.html', input_text='Input file text', output_text='Output file text')	

@app.route('/compute')
def compute(filename):
	solver = DivisibilityProblem()
	parser = FileParser(g.file)

	try:
		parser.parse()
	except FileValidationError as e:
		return e
	return ''