# Azamat Xabibullayev 5- oy imtihoni


# 1
from decimal import Decimal

class ToDecimal:
    def __init__(self, number):
        self.decimal = Decimal(number)


a = ToDecimal(3.14)
print(type(a.decimal))






# 2
import psycopg2
from decimal import Decimal

conn = psycopg2.connect(
    dbname="topshiriq",
    user="postgres",
    password="2005",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE Product (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        price DECIMAL(10, 2),
        color VARCHAR(50)
    )
""")

product_data = (1, 'Samsung A72', Decimal('452.13'), 'black')
cur.execute("INSERT INTO Product (id, name, price, color) VALUES (%s, %s, %s, %s)", product_data)

conn.commit()
conn.close()








# 3
# Git buyruqlari:
# 1. git add .
# 2. git commit -M "First commit"
# 3. git branch -M main
# 4. git push -u origin main







# 4
from collections import namedtuple

Transport = namedtuple('Transport', ['model', 'color', 'year'])


class Cars(Transport):
    def __new__(cls, model, color, year, price):
        return super().__new__(cls, model, color, year)

    def __init__(self, model, color, year, price):
        self.price = price


c = Cars('BMW M5 F90', 'black', '2020', '$150.000')

print(c.price)
print(c.model)







# 5
def connect(user, dbname, password, host):
    def select():
        import psycopg2
        connection = psycopg2.connect(user=user, dbname=dbname, password=password, host=host)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Product;")
        data = cursor.fetchall()
        return data

    return {"select": select}


a = connect(user="postgres", dbname="topshiriq", password="2005", host="localhost", )
b = a["select"]()
print(b)






# 6
class Alphabet:
    def __init__(self):
        self.letters = 'abcde'
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 5:
            a = self.letters[self.index]
            self.index += 1
            return a
        else:
            raise StopIteration


a = Alphabet()

for i in a:
    print(i)







# 7
keys = ["name", "description", "title", "keywords", "content", "charset"]
values = ["document", "The best document", "My document", "doc, word,excel", "None"]


def generator(a, b):
    c = {}
    for i, j in zip(a, b):
        c[i] = j
    yield c


c = generator(keys, values)
print(next(c))







# 8
import threading


def connect(user, dbname, password, host):
    def select():
        import psycopg2
        connection = psycopg2.connect(user=user, dbname=dbname, password=password, host=host)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Product;")
        data = cursor.fetchall()
        return data

    return {"select": select}


def main():
    a = connect(user="postgres", dbname="topshiriq", password="2005", host="localhost", )
    b = threading.Thread(target= a)
    b.start()
    b.join()


if __name__ == "__main__":
    main()







# 10
import requests
import json

url = 'https://dummyjson.com/products'
response = requests.get(url)
data = response.json()
print(data)




