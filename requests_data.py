import psycopg2
import requests

url = 'https://dummyjson.com/users/'
# connecting to url and getting data from it
r = requests.get(url)
data = r.json()

conn = psycopg2.connect(dbname="postgres", host="localhost", port=5432, password=2508, user="postgres")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users (
        id serial PRIMARY KEY NOT NULL,
        firstname VARCHAR(255) NOT NULL,
        lastName varchar(255) NOT NULL,
        maidenName VARCHAR(255) NOT NULL,
        age INT NOT NULL,
        gender VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        phone VARCHAR(255) NOT NULL,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        birthday VARCHAR(255) NOT NULL,
        image VARCHAR(255) NOT NULL,
        bloodGroup VARCHAR(255) NOT NULL,
        height INT NOT NULL,
        weight INT NOT NULL,
        eyecolor VARCHAR(255) NOT NULL,
        hair VARCHAR(266) NOT NULL,
        "domain" VARCHAR(255) NOT NULL,
        ip VARCHAR(255) NOT NULL,
        address TEXT NOT NULL,
        macaddress VARCHAR(255) NOT NULL,
        university VARCHAR(255) NOT NULL,
        bank TEXT NOT NULL,
        company TEXT NOT NULL,
        ein varchar(255) NOT NULL,
        ssn VARCHAR(255) NOT NULL,
        userAgent VARCHAR(300) NOT NULL,
        crypto TEXT NOT NULL )""")
cur.connection.commit()

insert_into_data = """INSERT INTO users 
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """


def insert_data():
    for user in data['users']:
        cur.execute(insert_into_data, (user['id'], user['firstName'], user['lastName'], user['maidenName'],
                                       user['age'], user['gender'], user['email'], user['phone'], user['username'],
                                       user['password'], user['birthDate'], user['image'], user['bloodGroup'],
                                       user['height'], user['weight'], user['eyeColor'], str(user['hair']),
                                       user['domain'], user['ip'], str(user['address']), user['macAddress'],
                                       user['university'], str(user['bank']), str(user['company']), user['ein'],
                                       user['ssn'], user['userAgent'], str(user['crypto'])))
        conn.commit()


def select_users():
    cur.execute("SELECT * FROM users")
    users_data = cur.fetchall()
    for user in users_data:
        print(user)


select_users()
cur.close()
