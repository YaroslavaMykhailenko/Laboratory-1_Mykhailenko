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
    print("Database opened successfully")
    cur = con.cursor()

    print('1.  \n')

    cur.execute(query_1)
    diagram_bar = {}
    for row in cur:
        diagram_bar[row[0]] = row[1]
        print(row)

    plt.bar(list(map(lambda x: str(x), list(diagram_bar.keys()))),diagram_bar.values())
    plt.xticks(rotation=45)
    plt.title('Кількість зроблених заказів в певний день')
    plt.xlabel('Дні')
    plt.ylabel('Кількість замовлень')
    plt.show()

    print('2.  \n')

    cur.execute(query_2)
    diagram_pie = {}
    for row in cur:
        diagram_pie[row[0]] = row[1]
        print(row)

    fig, ax = plt.subplots()
    colors = ['#4F6272', '#B7C3F3', '#DD7596', '#8EB897']
    ax.pie(diagram_pie.values(), labels = diagram_pie.keys(), autopct='%1.1f%%', colors=colors)
    plt.title('Поділ ринку між різними національностями кухні')
    plt.show()

    print('3.  \n')

    cur.execute(query_3)

    price = []
    quantity = []
    for row in cur:
        price.append(row[1])
        quantity.append(row[0])

        print(row)

    fig, ax = plt.subplots()
    ax.plot(price, quantity, marker='o')
    plt.title("Зв'язок між кількістю замовлень того, чи іншого продукту та їх цінами")
    plt.xlabel('Ціни')
    plt.ylabel('Кількість')
    plt.show()
