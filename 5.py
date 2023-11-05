"""
product ={'ดินสอกด':{'ราคา':50,'สี':'แดง'},
          'ยางลบ':{'ราคา':3,'สี':'เขียว'},
          'ดินสอสี':{'ราคา':100,'สี':'ชมพู'}}

while True:
    print('-----กรุณากรอกข้อมูลสินค้า-----')
    p = input('ชื่อสินค้า: ')
    n = int(input('จำนวน: '))
    print('-----')
    if p in product:
        print(f'สินค้า: {p} \n ราคา: {product[p]['ราคา']} บาท \n สี: {product[p]['สี']}')
        print(f'จำนวน: {n} ชิ้น \n รวมทั้งหมด: {product[p]['ราคา']*n} บาท')
    else:
        print('ไม่พบสินค้าในระบบ')
"""

student = {
    'name': 'Alisu',
    'age': 20,
    'major': 'Computer Science'
}

print(f"Student's Name: {student['name']}" )
print(f"Student's Age: {student['age']}")
print(f"Student's Major: {student['major']}")
