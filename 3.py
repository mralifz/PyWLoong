"""
tiles = 10
row = 3 # 3 ชิ้นต่อแถว
total_row = tiles // row
remain = tiles % row
print(total_row)
print(remain)
buy_more = row - remain
print(f'กระเบื้องทั้งหมด: {tiles} แผ่น')
print(f'1 แถวปูกระเบื่องได้: {row} แผ่น')
print(f'-----หลังคำนวน-----')
print(f'กระเบื้องที่ปูได้ทั้งหมดครบแถว: {total_row} แถว')
print(f'เหลือกระเบื่อง: {remain} แผ่น')
print(f'ลูกค้าต้องซื้อกระเบื้องเพิ่ม: {buy_more} แผ่น')
#ลูกค้าต้องซื้อกระเบื้องเพิ่มกี่แผ่น

#โจทย์สนามบินสุวรรณภูมิ
tiles = 1456
row = 53 # 53 ชิ้นต่อแถว
total_row = tiles // row
remain = tiles % row
print(total_row)
print(remain)
buy_more = row - remain
print(f'กระเบื้องทั้งหมด: {tiles} แผ่น')
print(f'1 แถวปูกระเบื่องได้: {row} แผ่น')
print(f'-----หลังคำนวน-----')
print(f'กระเบื้องที่ปูได้ทั้งหมดครบแถว: {total_row} แถว')
print(f'เหลือกระเบื่อง: {remain} แผ่น')
print(f'ลูกค้าต้องซื้อกระเบื้องเพิ่ม: {buy_more} แผ่น')
"""
tilecolr = {'red':50, 'gold':200, 'white':90}
print('เรียนกับลุง EP.3')
try:
    tiles = int(input('คุณมีกระเบื้องทั้งหมดกี่แผ่น: '))
    row = int(input('หนึ่งแถวปูกี่แผ่น: '))
    color = input('กระเบื้องสีอะไร? [red / gold / white]:')
except:
    print('กรุณากรอกข้อมูลเป็นตัวเลขเท่านั้น')
    tiles = int(input('คุณมีกระเบื้องทั้งหมดกี่แผ่น: '))
    row = int(input('หนึ่งแถวปูกี่แผ่น: '))
total_row = tiles // row
remain = tiles % row
print(total_row)
print(remain)
buy_more = row - remain
print(f'กระเบื้องทั้งหมด: {tiles} แผ่น')
print(f'1 แถวปูกระเบื่องได้: {row} แผ่น')
print(f'-----หลังคำนวน-----')
print(f'กระเบื้องที่ปูได้ทั้งหมดครบแถว: {total_row} แถว')
print(f'เหลือกระเบื่อง: {remain} แผ่น')
print(f'ลูกค้าต้องซื้อกระเบื้องเพิ่ม: {buy_more} แผ่น')
print('ราคากระเบื้องที่ต้องซื้อเพิ่ม: {} บาท'.format(buy_more * tilecolr[color]))
      

