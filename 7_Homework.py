user = 'admin'
pw = '123456'
while True:
    login = str(input('Enter username: '))
    if login == user:
        entpw = str(input('Enter password: '))
        if entpw == pw:
            print('Log in success')
            break
