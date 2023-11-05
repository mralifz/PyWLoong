Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
t = turtle.Pen()
tap.shape('bird')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    tap.shape('bird')
NameError: name 'tap' is not defined. Did you mean: 'map'?
t.shape('bird')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    t.shape('bird')
  File "C:\Python312\Lib\turtle.py", line 2832, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named bird
t.shape('turtle')
tao = {'color':'green','dis':100}
t.color(tao['color'])
def rect();
SyntaxError: incomplete input
def rect(tao_object, tdict):
...     for i in range(4):
...         tao_object.forward(tdict['dist'])
...         tao_object.left(90)
... 
...         
>>> rect(t, tao)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    rect(t, tao)
  File "<pyshell#12>", line 3, in rect
    tao_object.forward(tdict['dist'])
KeyError: 'dist'
>>> def rect(tao_object, tdict):
...     for i in range(4):
...         tao_object.forward(tdict['dis'])
...         tao_object.left(90)
... 
...         
>>> rect(t, tao)
>>> tao2 = turtle.Pen()
>>> tao2dict = {'color':'red','dis':50}
>>> tao2.color(tao['color'])
>>> rect(tao2, tao2dict)
>>> tao2.color(tao2dict['color'])
>>> tao2.shape('turtle')
>>> rect(tao2, tao2dict)
