from datetime import datetime

def get_username():
    with open('db/log_account.txt', 'r') as file:
        username = file.readline().strip()
    return username

def store_post():
    delete_post()
    username = get_username()
    post = input('Masukkan post yang ingin di unggah: ')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        with open('db/data_post.txt', 'a') as file:
            file.write(f'{username},{post},{timestamp}\n')
        print('\nPostingan berhasil dikirim!\n')
    except FileNotFoundError:
        print('File tidak ditemukan.')
    
def delete_post():
    try:
        file = open('db/data_post.txt', 'r')
    except FileNotFoundError:
        print('File tidak ditemukan.')
        return
    lines = file.readlines()
    file.close()
    with open('db/data_post.txt', 'w') as file:
        for line in lines:
            username, post, timestamp = line.strip().split(',')
            post_date = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
            if (datetime.now() - post_date).days < 1:
                file.write(f'{username},{post},{timestamp}\n')
    
def timeline():
    delete_post()
    with open('db/data_post.txt', 'r') as file:
        posts = file.readlines()
    sorted_posts = []
    for post in posts:
        username, post_content, timestamp = post.strip().split(',')
        sorted_posts.append((username, post_content, timestamp))
    
    for i in range(len(sorted_posts)):
        for j in range(i + 1, len(sorted_posts)):
            if datetime.strptime(sorted_posts[i][2], '%Y-%m-%d %H:%M:%S') < datetime.strptime(sorted_posts[j][2], '%Y-%m-%d %H:%M:%S'):
                sorted_posts[i], sorted_posts[j] = sorted_posts[j], sorted_posts[i]
    
    if not sorted_posts:
        print('\nPostingan tidak ada\n')
    else:
        for post in sorted_posts:
            username, post_content, timestamp = post
            print()
            print("----------------------")
            print(f'Username: {username}\nPost: {post_content}\n{timestamp}')
            print("----------------------")

def search_post():
    delete_post()
    keyword = input('\nMasukkan kata kunci: ')
    found = False
    try:
        with open('db/data_post.txt', 'r') as file:
            for line in file:
                username, post_content, timestamp = line.strip().split(',')
                if keyword in post_content:
                    found = True
                    print()
                    print("----------------------")
                    print(f'Username: {username}\nPost: {post_content}\n{timestamp}')
                    print("----------------------\n")
    except FileNotFoundError:
        print('File tidak ditemukan.')
                
    if not found:
        print('\nPost tidak ditemukan\n')
