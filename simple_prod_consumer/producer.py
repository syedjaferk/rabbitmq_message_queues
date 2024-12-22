
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='order_queue')

channel.basic_publish(exchange='',
                      routing_key='order_queue',
                      body='Order #12345')
print("[x] Sent 'Order #12345'")
connection.close()