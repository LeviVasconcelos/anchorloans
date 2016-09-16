from anchorapp import app, inpfiles 
from flask_uploads import UploadNotAllowed, UploadSet
from flask import redirect, url_for, request, render_template, flash, session
from fileparser import FileParser
from divisibilitysolver import DivisibilitySolver
from exceptions import FileValidationError
from configurations import *
import os

"""
Redirects to '/upload'
	actions:
		- redirect to 'upload'
"""
@app.route('/')
def start():
	return redirect(url_for('upload'))


"""
Responsible for rendering the 'upload.html' template as well as handling the uploaded files.
	actions:
		- render upload.html
		- handle file uploads
		- redirect to '/compute'
"""
@app.route('/upload', methods=['POST', 'GET'])
def upload():
	#checks for input file in the request object
	if 'inpt' in request.files:

		#secure filename, removing the previous file. --- Since there is no need for storing the files, it removes the previous one.
		filepath = os.path.join(app.config['UPLOADED_INPFILES_DEST'],	INPUT_FILE)
		if os.path.exists( filepath ):
			os.remove(filepath)

		#checks for type consistency (only .txt allowed). If consistency, save it.
		if inpfiles.file_allowed(request.files['inpt'], request.files['inpt'].filename):
			inpfiles.save(request.files['inpt'], name=INPUT_FILE)
			session['submitted'] = True
			return redirect('compute')
		else:
			flash(ERROR_MESSAGES['file_not_allowed'])
			return render_template('upload.html')

	#The user didn't submitted yet, thus set submitted flag off.
	session['submitted'] = False
	return render_template('upload.html')	

"""
Parse and validate the uploaded file. If validation succeeds, compute divisibility.
	actions:
		- handle validation (if fails, redirect to '/upload')
		- compute divisibility
		- render display.html
"""
@app.route('/compute')
def compute():
	#Checks if a file was submitted
	if not session.get('submitted'):
		flash('Input file required.')
		return redirect(url_for('upload'))

	#Instantiates the solver and evaluates the input and output files path.
	solver = DivisibilitySolver()
	input_filepath = os.path.join(os.path.dirname(__file__), FILE_REL_FOLDER + INPUT_FILE)
	output_filepath = os.path.join(os.path.dirname(__file__), FILE_REL_FOLDER + OUTPUT_FILE)
	
	#Parse the input file and checks for consistency.
	parser = FileParser(filename = input_filepath)
	try:
		parser.parse()
	except FileValidationError as e:
		flash(e.message)
		return redirect(url_for('upload'))

	#If consistent, solve instances and save into output file.
	with open(output_filepath,'w') as out_file:
		for instance in parser.instances:
			solver.setInstance(instance[0], instance[1], instance[2])
			out_file.write(' '.join(str(i) for i in solver.getSolution()) + '\n')

	#If everything went okay, send the output and input file content to the template and return to client.
	#This part should be considered for streaming in case of highly loaded problems which may cause slow template rendering.
	out_text = None
	with open(input_filepath, 'r') as input_file:
		input_text = input_file.read()
		in_sz = len(input_text.split('\n'))
	with open(output_filepath, 'r') as output_file:
		output_text = output_file.read()

	return render_template('display.html', input_text=input_text, output_text=output_text, text_sz=in_sz)

