#! python3

import sys
import psycopg2

def connectDb():
    conn = psycopg2.connect(
    host="localhost",
    database="follow_prices",
    user="postgres",
    password="")

    return conn

def getAllTickets(conn):
    cur = conn.cursor()
    cur.execute('select tck_date, tck_id, shop_name, tck_info  from ticket, shop where ticket.tck_id_shop  = shop.shop_id  ;')

    result = cur.fetchall()
    print(result)

def getAllShop(conn):
    cur = conn.cursor()
    cur.execute('select shop_id, shop_name from shop s ;')

    result = cur.fetchall()

    for i in result:
        print(i)
        print(i[1])
    print(result)
    return result

def insertTicket():
    year = 2023
    month = 2
    day = 2
    hour = 14
    minutes = 5

    ticketDate = datetime.datetime(year, month, day, hour, minutes)
    id_shop = 42

def main(av):
    print("here we work")
    conn = connectDb()

    #getAllTickets(conn)
    getAllShop(conn)

if __name__ == '__main__':
    main(sys.argv)
