


## ABOUT THIS DOCUMENT 

This document reports about the anchorloans test assignment.  
Problem: "Problem One: Divisibility"  
author: Levi Osterno Vasconcelos  
date: 09/15/016  


## ASSUMPTIONS MADE

* The system was designed to be hosted on linux environment. 
* Also, I assume that no negative inputs are provided, given the problem description. 

## DESIGN CHOICES

For the development of the web app I used python 2.7 along with Flask web framework. For the html/css I used jinja2 and bootstrap for better flexibility and responsive layout. For testing, I used PyUnit for unit tests and Flask-Client for the functional tests.

The code is modularized as follows: the main web app is called "anchorapp", and is formatted as a python package. The
package has the following structure:

root/  
---anchorapp/  
------\_\_init\_\_.py  
------views.py  
------utils.py  
---tests/  
------utils_test.py  
------functional_tests.py  
------input_files/  
------ ...  
---templates/  
------base.html  
------upload.html  
------display.html  
---static/  
------bootstrap.min.css  
---files/  
------input.txt  
------output.txt  

This structure modularizes the web views and the backend processing, where all view-related is handled at views.py and the backend evaluations at utils.py. All test-related files are within anchorapp/tests. The implementation design was thought to keep the code design simple as well as maintainable. Several features were implemented in that regard, including at tests, where a new test can be easily added by just creating a .txt following a filename pattern: "\<input_name\>\_\<fail or succeed\>\_\<error_code\>.txt" in tests/input_files.

### App Flow

URL | GET | POST
--- | --- | -----
'/' | redirect('/upload') | Not defined.
'/upload' | render template | redirect('/compute' or '/upload')
'/compute' | render template | Not defined


The flow was chosen to be farily simple. It starts redirecting the user to the '/upload' view. Once a file is chosen and uploaded, the validation process takes place and redirects the user accordingly. If the validation succeeds, the user is redirected to the '/compute' view where the result is diplayed. Otherwise, the app redirects to '/upload' exhibiting the proper error messages.

## TESTS 

Regarding application testing, I have deployed unit tests and functional tests. To
run the tests, one can execute the following command from the root folder:

python -m unittest -v anchorapp.tests.utils_test anchorapp.tests.functional_tests

The tests were thought to be easily extendable and thus, automated whenever possible.

## INSTALLATION GUIDE 

Assuming you already have virtualenv and pip installed, follow:

virtualenv \<dir\>  
cd \<dir\>  
git clone https://github.com/LeviVasconcelos/anchorloans.git  
cd anchorloans  
pip install -r requirements.txt  
python run.py  

Now, open your browser and access: "http://localhost:5000/".






