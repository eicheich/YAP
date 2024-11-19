import os
from auth.auth import login, logout, register
from post.post import search_post, store_post, timeline


menu_options = ["Login", "Register", "Exit"]
post_menu_options = ["Timeline", "Buat Postingan", "Cari Postingan", "Logout", "Exit"]

def menu_index():
    print("\nSelamat datang di aplikasi Yap! \nMenu:")
    print("+----------------------------+")
    print("|        Selamat datang      |")
    print("|       di aplikasi Yap!     |")
    print("|                            |")
    print("|           /\_/\            |")
    print("|          ( o.o )           |")
    print("|           >Yap!<           |")
    print("+----------------------------+")
    for i, option in enumerate(menu_options, 1):
        print(f" {i}. {option}")
    input_menu = input(f"Masukkan pilihan Anda (1/2/3): ")
    if input_menu == "1":
        auth = login()
        if auth == True:
            menu_post()
        elif auth == False:
            menu_index()
    elif input_menu == "2":
        register()
        menu_index()
    elif input_menu == "3":
        exit_post()

def menu_post():
    print("Selamat datang di Yap! \nMenu:")
    for i, option in enumerate(post_menu_options, 1):
        print(f" {i}. {option}")
    input_menu = input("Masukkan pilihan Anda (1/2/3/4/5): ")
    if input_menu == "1":
        timeline()
        menu_post()
    elif input_menu == "2":
        store_post()
        menu_post()
    elif input_menu == "3":
        search_post()
        menu_post()
    elif input_menu == "4":
        logout()
        menu_index()
    elif input_menu == "5":
        exit_post()
def exit_post():
    print("+----------------------------+")
    print("|     keluar aplikasi....    |")
    print("|        ______              |")
    print("|       /      \             |")
    print("|      |  -  -  |            |")
    print("|      |   ---  |            |")
    print("|       \/Bye!\/             |")
    print("+----------------------------+")
    exit()
    
if os.path.exists('db/log_account.txt') and os.path.getsize('db/log_account.txt') > 0:
    menu_post()
else:
    menu_index()