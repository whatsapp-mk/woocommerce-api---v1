from woocommerce import API
from json import dumps
import psycopg2
from time import sleep

# pprint(a[3])



def start():
  def connectDB():
    global db, cr
    db = psycopg2.connect(user = "beiiukavuitazk",
                                password = "0a71ebf8517ad78a7ca580715e23662be5fe3b2b581dce332ad58d0c8451b0cb",
                                host = "ec2-34-247-118-233.eu-west-1.compute.amazonaws.com",
                                port = "5432",
                                database = "des6gvbscr1bu9")
    db.autocommit = True
    cr = db.cursor()

  def disconnectDB():
    global db, cr
    if(db):
        cr.close()
        db.close()

  def API_orders():
    wcapi = API(
        url="https://welightbox.com/mk/",
        consumer_key="ck_d98227d81bff606cb8a516b7da1b2d717f4a7b55",
        consumer_secret="cs_4d680ed93da62b02bc7cf16eb62a134f4aa8f5d2",
        version="wc/v3"
    )
    orders_data = wcapi.get("orders")
    orders = orders_data.json()
    return orders

  # get payment api data 
  print('Getting data from woocommerce api')
  while True:
    sleep(1)
    orders = API_orders()
    payment_process_data = []

    connectDB()
    db_payment_ids = []
    cr.execute("SELECT payment_id FROM offers_payment_process")
    db_payment_ids_data = cr.fetchall()

    for id in db_payment_ids_data:
      db_payment_ids.append(id[0])
    disconnectDB()

    for order in orders:
      if str(order['id']) not in db_payment_ids:
        if order['status'] == 'completed' or order['status'] == 'processing':
          payment_process_data.append((order.get('id'),
                                      order.get('line_items')[0].get('product_id'),
                                      order.get('billing')['email']))


    # print(payment_process_data)
    if payment_process_data != []:
      print(f'{len(payment_process_data)} payment found')
      for data in payment_process_data:
        connectDB()
        cr.execute(f"INSERT INTO offers_payment_process(payment_id,  product_id, email, done) VALUES ('{data[0]}', '{data[1]}', '{data[2]}', 'false')")
        disconnectDB()

        print('Payments completed successfully')


    print('payment not found')


start()