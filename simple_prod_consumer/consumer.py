import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='order_queue')

def callback(ch, method, properties, body):
    print(f"[x] Processed {body}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue='order_queue', on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()