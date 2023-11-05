Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
py
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    py
NameError: name 'py' is not defined
py --
SyntaxError: incomplete input
cars =['toyota','honda','benz']
cars.append('byd')
print(cars)
['toyota', 'honda', 'benz', 'byd']
cars.remove
<built-in method remove of list object at 0x000002278303D100>
cars.remove('honda')
print(cars)
['toyota', 'benz', 'byd']
cars.insert(0, 'tesla')
print(cars)
['tesla', 'toyota', 'benz', 'byd']
print(cars[1])
toyota
for i in cars:
    print(i)

    
tesla
toyota
benz
byd
print(*cars)
tesla toyota benz byd
for i,c in enumerate(cars):
    print(i,c)

    
0 tesla
1 toyota
2 benz
3 byd
for i,c in enumerate(cars, start=0):
    print(f'ลำดับที่ {i} {c}')

    
ลำดับที่ 0 tesla
ลำดับที่ 1 toyota
ลำดับที่ 2 benz
ลำดับที่ 3 byd
for i,c in enumerate(cars, start=1):
    print(f'ลำดับที่ {i} {c}')

    
ลำดับที่ 1 tesla
ลำดับที่ 2 toyota
ลำดับที่ 3 benz
ลำดับที่ 4 byd
cars[1] = 'suzuki'
print(cars)
['tesla', 'suzuki', 'benz', 'byd']
len(cars)
4
ord('ก')
3585
ord('ฃ')
3587
for i in range(10);
SyntaxError: incomplete input
for i in range(10):
    print(chr(3585+i))

    
ก
ข
ฃ
ค
ฅ
ฆ
ง
จ
ฉ
ช
for i in range(48):
    print(chr(3585+i))

    
ก
ข
ฃ
ค
ฅ
ฆ
ง
จ
ฉ
ช
ซ
ฌ
ญ
ฎ
ฏ
ฐ
ฑ
ฒ
ณ
ด
ต
ถ
ท
ธ
น
บ
ป
ผ
ฝ
พ
ฟ
ภ
ม
ย
ร
ฤ
ล
ฦ
ว
ศ
ษ
ส
ห
ฬ
อ
ฮ
ฯ
ะ
>>> for i in range(46):
...     th[i] = chr(i+3585)
... 
...     
Traceback (most recent call last):
  File "<pyshell#34>", line 2, in <module>
    th[i] = chr(i+3585)
NameError: name 'th' is not defined
>>> list(th)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    list(th)
NameError: name 'th' is not defined
>>> for i in range(46):
...     th.append(chr(3585+i))
... 
...     
Traceback (most recent call last):
  File "<pyshell#37>", line 2, in <module>
    th.append(chr(3585+i))
NameError: name 'th' is not defined
>>> th
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    th
NameError: name 'th' is not defined
>>> th = []
>>> for i in range(46):
...     th.append(chr(3585+i))
... 
...     
>>> print(th)
['ก', 'ข', 'ฃ', 'ค', 'ฅ', 'ฆ', 'ง', 'จ', 'ฉ', 'ช', 'ซ', 'ฌ', 'ญ', 'ฎ', 'ฏ', 'ฐ', 'ฑ', 'ฒ', 'ณ', 'ด', 'ต', 'ถ', 'ท', 'ธ', 'น', 'บ', 'ป', 'ผ', 'ฝ', 'พ', 'ฟ', 'ภ', 'ม', 'ย', 'ร', 'ฤ', 'ล', 'ฦ', 'ว', 'ศ', 'ษ', 'ส', 'ห', 'ฬ', 'อ', 'ฮ']
>>> pop = list()
