from anchorapp import app, inpfiles
from flask_uploads import UploadNotAllowed
from flask import redirect, url_for, request, render_template, session
from utils import DivisibilityProblem, BadInstance, FileValidationError, FileParser
import os

@app.route('/')
def start():
	return render_template('base.html', input_text='Input file text', output_text='Output file text')

@app.route('/upload', methods=['POST'])
def upload():
	if 'inpt' in request.files:
		try:
			session['filename'] = inpfiles.save(request.files['inpt'])
			session['path_to_file'] = os.path.join(os.path.dirname(__file__), 'inputs/' + session['filename'])
			input_text = None
			with open(session['path_to_file'],'r') as file:
				session['input_text'] = file.read()
			return render_template('base.html', input_text=session['input_text'], output_text='Output file text, generate on Compute button.')
		except UploadNotAllowed as e: #TO-DO: FLASH ERROR MESSAGE INTO THE SAME TEMPLATE.
			return 'Sorry, this upload was not allowed, text files only.'
	return render_template('base.html', input_text='Input file text', output_text='Output file text')	

@app.route('/compute')
def compute():
	solver = DivisibilityProblem()
	#filename = getattr(session, 'filename', None)
	parser = FileParser(filename = session['path_to_file'])
	try:
		parser.parse()
	except FileValidationError as e:
		return e
	try:
		with open('tmp.txt','w') as out_file:
			for instance in parser.instances:
				solver.setInstance(instance[0], instance[1], instance[2])
				out_file.write(' '.join(str(i) for i in solver.getSolution()) + '\n')
	#TO-DO: FLASH ERRORS
	except BadInstance as e:
		return e
	except IOError as e:
		return e

	else:
		out_text = None
		with open('tmp.txt','r') as out_file:
			out_text = out_file.read()

		return render_template('base.html', input_text=session['input_text'], output_text=out_text)

	return render_template('base.html')