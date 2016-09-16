from .. import app
from ..configurations import TEST_INPUT_DIR, TEST_SUCCESS_EXP, TEST_FAIL_EXP
from StringIO import StringIO
import  flask
import os
import unittest
import glob



class AnchorappTestCase(unittest.TestCase):
	def setUp(self):
		app.config['TESTING'] = True
		app.config['SECRET_KEY'] = 'awueri'
		self.anchorapp = app.test_client()
		self.dirpath = os.path.dirname(__file__)
		self.failfiles = glob.glob(os.path.join(self.dirpath, TEST_INPUT_DIR + '*fail*.txt')) #This can be optmized by checking a file with this preprocessment


	def _uploadFile(self, filename):
		fname = filename.split('/')[-1]
		with open(filename,'r') as file:
			data=dict(inpt=(StringIO(file.read()), fname),)
		return data

	def test_getRoot(self):
		rv = self.anchorapp.get('/')
		assert 'Redirecting' in rv.data
		assert '/upload' in rv.data
	
	def test_getUploadSubmitted(self):
		with self.anchorapp as c:
			rv = c.get('/upload')
			with self.anchorapp.session_transaction() as session:
				assert session.get('submitted') == False

	def test_postUploadSuccess(self):
		data = self._uploadFile(os.path.join(self.dirpath, TEST_SUCCESS_EXP))
		with self.anchorapp.post('/upload', data=data, follow_redirects=True) as rq:
			with self.anchorapp.session_transaction() as session:
				self.assertTrue(session.get('submitted',False))

	def test_getComputeDirectly(self):
		rv = self.anchorapp.get('/compute')
		assert 'Redirecting' in rv.data
		assert '/upload' in rv.data

	'''
	This test is automated as following:
		it loads all .txt files from ./input_files/*.txt
		according to the current filename tags, the test looks for exceptions raise.
		This schema was thought in order to be easily expandable, with the third tag being used to specify the raised exception
	'''
	def test_shouldFlashMsgs(self):
		for f in self.failfiles:
			data = self._uploadFile(f)
			with self.anchorapp.post('/upload', data=data, follow_redirects=True) as rq:
				assert '<li>' in rq.data
