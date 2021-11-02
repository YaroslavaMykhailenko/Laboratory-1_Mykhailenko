import psycopg2
import math
import matplotlib.pyplot as plt

username = 'postgres'
password = 'Slava270602'
database = 'mykhailenkoyaroslava'
host = 'localhost'
port = '5432'

query_1 = '''

select order_date, count(*) as quantity_orders from orders group by order_date
'''
query_2 = '''
select TRIM(kitchen_type), count(*) as count_cuisine from restaurants group by kitchen_type
'''
query_3 = '''
SELECT COUNT(prod_price) AS quantity_products, products.prod_price
FROM products JOIN orders USING(prod_id)  GROUP BY prod_price
ORDER BY prod_price

'''

con = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(con))

with con:

    cur = con.cursor()

    print('1.  \n')
    cur.execute(query_1)
    for row in cur:
        print(row)

    print('\n2.  \n')
    cur.execute(query_2)
    for row in cur:
        print(row)

    print('\n3.  \n')
    cur.execute(query_3)
    for row in cur:
        print(row)
