


## ABOUT THIS DOCUMENT 

This document reports about the anchorloans test assignment.

Problem: "Problem One: Divisibility"

author: Levi Osterno Vasconcelos

date: 09/15/016


## ASSUMPTIONS MADE

The system was designed to be hosted on linux environment. Also, I assume that no
negative inputs are provided, given the problem description. 

## DESIGN CHOICES

For the development of the web app I used python 2.7 along with Flask web fra-
mework. For the html/css I used jinja2 and bootstrap for better flexibility and 
responsive layout. 

The code is modularized as follows:
The main web app is called "anchorapp", and is formatted as a python package. The
package has the following structure:

-root/
-  anchorapp/
-    \_\_init\_\_.py
-    views.py
-    utils.py
-    tests/
-      utils_test.py
-      functional_tests.py
-      input_files/
-      ...
-    templates/
-      base.html
-      upload.html
-      display.html
-    static/
-      bootstrap.min.css
-    files/
-      input.txt
-      output.txt

This structure, modularizes the web views and the backend processing. Where all view-
related is handled at views.py where the backend evaluations at utils.py.


## TESTS 

Regarding application testing, I have deployed unit tests and functional tests. To
run the tests, one can execute the followind command from the root folder:

python -m unittest -v anchorapp.tests.utils_test anchorapp.tests.functional_tests

The tests were thought to be easily extendable and thus, automated whenever possible.

## INSTALLATION GUIDE 

Assuming you already have virtualenv and pip installed, follow:

virtualenv <dir>

cd <dir>

git clone https://github.com/LeviVasconcelos/anchorloans.git

cd anchorloans

pip install -r requirements.txt

python run.py

Now, open your browser ant access: http://localhost:5000/





