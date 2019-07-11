# Test for form_test3.py

from nose.tools import *
from form_test3 import app    

app.config['TESTING'] = True                                        # web app of flask is an object which can call its properties and methods.
web = app.test_client()                                             # Flask provides a test client (likes a fake web browser which is easy to test）.

def test_index():
    rv = web.get('/', follow_redirects=True)
    assert_equal(rv.status_code, 404)

    rv = web.get('/hello', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    assert_in(b"Fill Out This Form", rv.data)                       # Load data property of rv and check whether it inclues "Fill..." string.
    # b is important since the data returned is not Unicode but UTF-8，so it needs to transform

    test_input = {'greet': 'Hola', 'name': 'Zed'}
    rv = web.post('/hello', follow_redirects=True, data=test_input) # Use post() method to send POST test，and send the data in form via dictionary type
    assert_in(b"Hola", rv.data)
    assert_in(b"Zed", rv.data)

