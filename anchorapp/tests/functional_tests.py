import os
from anchorapp import app
import  flask
from StringIO import StringIO
import unittest
import tempfile
import glob

class AnchorappTestCase(unittest.TestCase):
	def setUp(self):
		app.config['TESTING'] = True
		app.config['SECRET_KEY'] = 'sekrit!'
		self.anchorapp = app.test_client()
		self.dirpath = os.path.dirname(__file__)
		self.failfiles = glob.glob(os.path.join(self.dirpath, 'input_files/*fail*.txt')) #This can be optmized by checking a file with this preprocessment


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
		data = self._uploadFile(os.path.join(self.dirpath, 'input_files/input1_success_0.txt'))
		with self.anchorapp.post('/upload', data=data, follow_redirects=True) as rq:
			with self.anchorapp.session_transaction() as session:
				self.assertTrue(session.get('submitted',False))

	def test_getComputeDirectly(self):
		rv = self.anchorapp.get('/compute')
		assert 'Redirecting' in rv.data
		assert '/upload' in rv.data

	def test_shouldFlashMsgs(self):
		for f in self.failfiles:
			data = self._uploadFile(f)
			with self.anchorapp.post('/upload', data=data, follow_redirects=True) as rq:
				assert '<li>' in rq.data
