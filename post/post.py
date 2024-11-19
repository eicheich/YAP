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
    with open('db/data_post.txt', 'a') as file:
        file.write(f'{username},{post},{timestamp}\n')
    print('Postingan berhasil dikirim!')
    
def delete_post():
    file = open('db/data_post.txt', 'r')
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
    for post in reversed(posts):
        username, post_content, timestamp = post.strip().split(',')
        print()
        print("----------------------")
        print(f'Username: {username}\nPost: {post_content}\n{timestamp}')
        print("----------------------")

def search_post():
    delete_post()
    keyword = input('\nMasukkan kata kunci: ')
    with open('db/data_post.txt', 'r') as file:
        posts = file.readlines()
    found = False
    for post in posts:
        username, post_content, timestamp = post.strip().split(',')
        if keyword in post_content:
            found = True
            print()
            print(f'Username: {username}\nPost: {post_content}\n{timestamp}\n')
    if not found:
        print('Post tidak ditemukan')