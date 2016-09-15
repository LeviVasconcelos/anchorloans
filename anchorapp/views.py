from anchorapp import app, inpfiles, INPUT_FILE, OUTPUT_FILE, FILE_REL_FOLDER
from flask_uploads import UploadNotAllowed, UploadSet
from flask import redirect, url_for, request, render_template, flash, session
from utils import DivisibilityProblem, BadInstance, FileValidationError, FileParser
import os


@app.route('/')
def start():
	return redirect(url_for('upload'))

@app.route('/upload', methods=['POST', 'GET'])
def upload():
	if 'inpt' in request.files:
		filepath = os.path.join(app.config['UPLOADED_INPFILES_DEST'],	INPUT_FILE)
		if os.path.exists( filepath ):
			os.remove(filepath)
		if inpfiles.file_allowed(request.files['inpt'], request.files['inpt'].filename):
			inpfiles.save(request.files['inpt'], name=INPUT_FILE)
			session['submited'] = True
			return redirect('compute')
		else:
			flash('Sorry, this upload was not allowed, .txt files only.')
			return render_template('upload.html')
	session['submited'] = False
	return render_template('upload.html')	

@app.route('/compute')
def compute():
	if not session.get('submited'):
		flash('Input file required.')
		return redirect(url_for('upload'))

	solver = DivisibilityProblem()
	input_filepath = os.path.join(os.path.dirname(__file__), FILE_REL_FOLDER + INPUT_FILE)
	output_filepath = os.path.join(os.path.dirname(__file__), FILE_REL_FOLDER + OUTPUT_FILE)
	
	parser = FileParser(filename = input_filepath)
	try:
		parser.parse()
	except FileValidationError as e:
		flash(e.message)
		return redirect(url_for('upload'))

	try:
		with open(output_filepath,'w') as out_file:
			for instance in parser.instances:
				solver.setInstance(instance[0], instance[1], instance[2])
				out_file.write(' '.join(str(i) for i in solver.getSolution()) + '\n')
	#TO-DO: FLASH ERRORS
	except BadInstance as e:
		flash(e.message)
		return redirect(url_for('upload'))

	except IOError as e:
		flash(e.message)
		return redirect(url_for('upload'))
	else:
		out_text = None
		with open(output_filepath,'r') as out_file:
			output_text = out_file.read()
			out_sz = len(output_text.split('\n'))
		with open(input_filepath, 'r') as input_file:
			input_text = input_file.read()
			in_sz = len(input_text.split('\n'))

		sz = max(in_sz,out_sz) + 1
		return render_template('display.html', input_text=input_text, output_text=output_text, in_sz=sz, out_sz=sz )

