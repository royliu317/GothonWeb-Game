# Test for form_test3.py

from nose.tools import *
from form_test3 import app    

app.config['TESTING'] = True    # Flask的web app就是一个普通对象，可以直接调用其属性、方法等
web = app.test_client()         # 让Flask应用给我一个测试客户端，相当于一个假的浏览器（这使得Flask很易于进行测试）

def test_index():
    rv = web.get('/', follow_redirects=True)
    assert_equal(rv.status_code, 404)

    rv = web.get('/hello', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    assert_in(b"Fill Out This Form", rv.data)  # 读取rv的data属性，判断其是否包含"Fill..."字符串
    # 如上的b很重要，因为从rv.data返回的数据不是Unicode，而是UTF-8，所以要转换一下

    test_input = {'greet': 'Hola', 'name': 'Zed'}
    rv = web.post('/hello', follow_redirects=True, data=test_input)  # 使用post()方法进行发送POST请求的测试，并把form表单数据以字典形式传递进去
    assert_in(b"Hola", rv.data)
    assert_in(b"Zed", rv.data)



# assert_in(member, container, msg=None) : 判断merber是否in container
# nose.tools中assert的函数工具: https://blog.csdn.net/zcabcd123/article/details/54909255