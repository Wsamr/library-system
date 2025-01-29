import sqlite3


def create_table():
    connection = sqlite3.connect('library.db')
    c = connection.cursor()

    # USER
    # c.execute('DROP TABLE user')
    # c.execute('''CREATE TABLE user(
    #     ssn text PRIMARY KEY NOT NULL,
    #     email text,
    #     name text,
    #     number text
    # )
    # ''')

    # LOAN
    # c.execute('DROP TABLE loan')
    # c.execute('''CREATE TABLE loan(
    #     user_id TEXT,
    #     book_id TEXT,
    #     issue_date TEXT,
    #     due_date TEXT,
    #     FOREIGN KEY(user_id) REFERENCES user(ssn),
    #     FOREIGN KEY(book_id) REFERENCES book(isbn))
    # ''')
    
    # ADMIN
    # c.execute('DROP TABLE admin')
    # c.execute('''CREATE TABLE admin(
    #     email TEXT PRIMARY KEY NOT NULL,
    #     name TEXT,
    #     password TEXT)
    # ''')

    # REPORT
    # c.execute('DROP TABLE report')
    # c.execute('''CREATE TABLE report(
    #     report_type TEXT,
    #     generated_on TEXT,
    #     report_data TEXT)
    # ''')
    connection.commit()
    connection.close()

create_table()
# USER
def add_user(ssn, name, email, number):
    connection = sqlite3.connect('library.db')
    c = connection.cursor()
    c.execute('INSERT INTO user(ssn, name, email, number) VALUES(?,?,?,?)', (ssn, name, email, number))
    connection.commit()
    connection.close()

user_list = [
    ('30408141401126', 'Maryam Tarek', 'mariamtarek2233@gmail.com', '01203311425'),
    ('3040-8141-40-1126', 'Maryam Tarek', 'mariamtarek2233@gmail.com', '01203311425'),
    ('alyaa-ssn', 'Alyaa Gamal', 'alyaa@gmail.com', '01200000000'),
    ('menna-ssn', 'Menna Hassan', 'menna@gmail.com', '01028248285'),
    ('26.19.164.10', 'Fred Cobb', 'ivatoeze@ca.com', '01069202046'),
    ('215.172.88.195', 'Ethan Gibson', 'lujur@zob.com', '01008499642'),
    ('56.164.200.3', 'Janie Ellis', 'nawga@we.com', '01093598760'),
    ('97.107.101.95', 'Curtis Delgado', 'johize@feldefpu.com', '01086563460'),
    ('6.200.63.210', 'Derek Curtis', 'guk@he.com', '01256350828'),
    ('99.35.193.65', 'Francisco Pope', 'ib@jikoro.com', '01108283761'),
    ('130.228.214.34', 'John Burns', 'ja@cab.com', '01093756056'),
    ('151.26.140.236', 'Leon Cummings', 'wuduli@anaumdu.com', '01065127436'),
    ('141.63.134.83', 'Kyle Byrd', 'ru@gesoca.com', '01006025184'),
]

# for item in user_list:
#     add_user(item[0], item[1], item[2], item[3])

def delete_user(ssn):
    connection = sqlite3.connect('library.db')
    c = connection.cursor()
    c.execute('DELETE FROM user WHERE ssn LIKE ?', (ssn,))
    connection.commit()
    connection.close()

# delete_user('30408141401126')

def update_user(ssn, name, email, number):
    connection = sqlite3.connect('library.db')
    c = connection.cursor()
    c.execute('UPDATE user SET name = ?, number = ?, email = ? WHERE ssn = ?', (name, number, email, ssn))
    connection.commit()
    connection.close()

# update_user('alyaa-ssn', email='alyaa@gmail.com', name='Alyaa Gamal', number='01207325896')

def show_user(search):
    connection = sqlite3.connect('library.db')
    c = connection.cursor()
    c.execute("SELECT ssn, name, email, number FROM user WHERE name LIKE ? OR ssn LIKE ?", (f'%{search}%',f'%{search}%'))
    users = c.fetchall()
    connection.commit()
    connection.close()
    return users

def get_user(search):
    connection = sqlite3.connect('library.db')
    c = connection.cursor()
    c.execute("SELECT ssn, name, email, number FROM user WHERE ssn LIKE ?", (search,))
    users = c.fetchall()
    connection.commit()
    connection.close()
    return users

def user_exist(ssn):
    user = get_user(ssn)
    if user == []:
        return False
    else: return True

# print(show_user('ssn'))

# BOOK
def add_book(isbn, title, author, genre):
    connection = sqlite3.connect('library.db')
    c = connection.cursor()
    c.execute('INSERT INTO book(isbn, title, author, genre) VALUES(?,?,?,?)', (isbn, title, author, genre))
    connection.commit()
    connection.close()

def delete_book(isbn):
    connection = sqlite3.connect('library.db')
    c = connection.cursor()
    c.execute('DELETE FROM book WHERE isbn LIKE ?', (isbn,))
    connection.commit()
    connection.close()

def update_book(isbn, title, author, genre):
    connection = sqlite3.connect('library.db')
    c = connection.cursor()
    c.execute('UPDATE book SET title = ?, author = ?, genre = ? WHERE isbn LIKE ?', (title, author, genre, isbn))
    connection.commit()
    connection.close()

def show_book(search):
    connection = sqlite3.connect('library.db')
    c = connection.cursor()
    c.execute("SELECT isbn, title, author, genre FROM book WHERE title LIKE ? OR isbn LIKE ? OR author LIKE ? OR genre LIKE ?", (f'%{search}%', f'%{search}%', f'%{search}%',f'%{search}%'))
    books = c.fetchall()
    connection.commit()
    connection.close()
    return books

def get_book(search):
    connection = sqlite3.connect('library.db')
    c = connection.cursor()
    c.execute("SELECT isbn, title, author, genre FROM book WHERE isbn LIKE ?", (search,))
    books = c.fetchall()
    connection.commit()
    connection.close()
    return books

def book_exist(isbn):
    book = get_book(isbn)
    if book == []:
        return False
    else: return True

# ADMIN
def add_admin(name, email, password):
    connection = sqlite3.connect('library.db')
    c = connection.cursor()
    c.execute('INSERT INTO admin(name, email, password) VALUES(?, ?, ?)', (name, email, password))
    books = c.fetchall()
    connection.commit()
    connection.close()

admin_list = [
    ('Alyaa Gamal', 'galyaa@gmail.com', '7454'),
    ('Menna Hassan', 'menna@gmail.com', '1111'),
    ('Maryam Tarek', 'maryam@gmail.com', '1234'),
    ('Wessam Reda', 'wessam@gmail.com', '1234'),
]

# for item in admin_list:
#     add_admin(item[0], item[1], item[2])

def get_admin(search):
    connection = sqlite3.connect('library.db')
    c = connection.cursor()
    c.execute("SELECT email, name, password FROM admin WHERE email LIKE ?", (search,))
    books = c.fetchall()
    connection.commit()
    connection.close()
    return books

def admin_exist(email):
    admin = get_admin(email)
    if admin == []:
        return False
    else: return True

# LOAN
def add_loan(user_id, book_id, issue_date, due_date):
    connection = sqlite3.connect('library.db')
    c = connection.cursor()
    c.execute('INSERT INTO loan(user_id, book_id, issue_date, due_date) VALUES(?,?,?,?)', (user_id, book_id, issue_date, due_date))
    connection.commit()
    connection.close()

def delete_loan(book_id):
    connection = sqlite3.connect('library.db')
    c = connection.cursor()
    c.execute('DELETE FROM loan WHERE book_id LIKE ?', (book_id,))
    connection.commit()
    connection.close()

# def update_book(isbn, title, author, genre):
#     connection = sqlite3.connect('library.db')
#     c = connection.cursor()
#     c.execute('UPDATE book SET title = ?, author = ?, genre = ? WHERE isbn LIKE ?', (title, author, genre, isbn))
#     connection.commit()
#     connection.close()

def show_loan(search):
    connection = sqlite3.connect('library.db')
    c = connection.cursor()
    c.execute("SELECT book_id, user_id, issue_date, due_date FROM loan WHERE book_id LIKE ?", (f'%{search}%',))
    books = c.fetchall()
    connection.commit()
    connection.close()
    return books

def book_available(book_id):
    book = show_loan(book_id)
    if book == []:
        return True
    else: return False


# REPORT
def add_report(report_type, generated_on, report_data):
    connection = sqlite3.connect('library.db')
    c = connection.cursor()
    c.execute('INSERT INTO report(report_type, generated_on, report_data) VALUES(?, ?, ?)', (report_type, generated_on, report_data))
    connection.commit()
    connection.close()

def show_report(search):
    connection = sqlite3.connect('library.db')
    c = connection.cursor()
    c.execute("SELECT report_type, generated_on, report_data FROM report WHERE report_data LIKE ?", (f'%{search}%',))
    books = c.fetchall()
    connection.commit()
    connection.close()

def filter_report(report_type, start_date, end_date):
    connection = sqlite3.connect('library.db')
    c = connection.cursor()
    c.execute("SELECT report_type, generated_on, report_data FROM report WHERE report_type LIKE ? AND generated_on >= ? AND generated_on <= ?", (report_type, start_date, end_date))
    report = c.fetchall()
    connection.commit()
    connection.close()
    return report