Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def sawatdee():
    """ฟังชั่นนี่ใช้สำหรับสวัสดี"""
    print('สวัสดีครับ')

    
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'sawatdee']
>>> help(sawatdee)
Help on function sawatdee in module __main__:

sawatdee()
    ฟังชั่นนี่ใช้สำหรับสวัสดี

>>> def hello(friend);
SyntaxError: incomplete input
>>> def hello(friend):
...     print('Hi, {}'.format(friend))
... 
...     
>>> hello('Tony')
Hi, Tony
>>> def wacal(wid,long):
...     wa = wid*long/
...     
SyntaxError: incomplete input
>>> def wacal(wid,long):
...     wa = wid*long/4
...     print(f'ที่ดินเท่ากับ {wa}')
... 
...     
>>> wacal(5,5)
ที่ดินเท่ากับ 6.25
>>> def wacal(wid,long):
...     wa = wid*long/4
...     print(f'ที่ดินเท่ากับ {wa}')
...     return wa
... 
>>> wa = wacal(5,5)
ที่ดินเท่ากับ 6.25
>>> print(wa+5)
11.25
