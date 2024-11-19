import os

def register():
    data = {'username': [], 'password': []}
    if os.path.exists('db/data_acc.txt'):
        file = open('db/data_acc.txt', 'r')
        for line in file:
            username, password = line.strip().split(': ')
            data['username'].append(username)
            data['password'].append(password) 
    
    while True:
        print("\nSelamat Datang di Sistem Register \n")
        username = input('Masukkan Username: ')
        password = input('Masukkan Password: ')
        if username in data['username']:
            print('\nUsername telah digunakan, silakan input username yang lain\n')
        else:
            valid = True
            for char in username:
                if not (char.isalnum() or char == '_'):
                    valid = False
                    
            if valid == False:
                print('\nusername hanya boleh terdiri dari huruf, angka, dan underscore\n')
                continue
            else:
                data['username'].append(username)
                data['password'].append(password)
                mode = 'a' if os.path.getsize('db/data_acc.txt') > 0 else 'w'
                file = open('db/data_acc.txt', mode)
                if mode == 'a':
                    file.write(f"\n{username}: {password}")
                else:
                    file.write(f"{username}: {password}")
                print('\nAnda berhasil register, silakan login\n')
                break

def login():
    data = {'username': [], 'password': []}
    if os.path.exists('db/data_acc.txt'):
        file = open('db/data_acc.txt', 'r')
        for line in file:
            username, password = line.strip().split(': ')
            data['username'].append(username)
            data['password'].append(password)
    print("\nSelamat Datang di Sistem Login \n")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    while True:
        if username in data['username']:
            index = data['username'].index(username)
            if password == data['password'][index]:
                with open('db/log_account.txt', 'w') as file:
                    file.write(username)
                print("\nLogin berhasil! Selamat datang!\n")
                return True
            else:
                print("\nPassword salah. Silakan coba lagi.\n")
                return False
        else:
            print("\nUsername tidak ditemukan. Silakan coba lagi.\n")
            return False
        
def logout():
    if os.path.exists('db/log_account.txt'):
        with open('db/log_account.txt', 'w') as file:
            file.write('')
        print("+----------------------------+")
        print("|     logout berhasil ....   |")
        print("|        ______              |")
        print("|       /      \             |")
        print("|      |  -  -  |            |")
        print("|      |   ---  |            |")
        print("|       \/Bye!\/             |")
        print("+----------------------------+")
        
    else:
        print("Anda belum login.")