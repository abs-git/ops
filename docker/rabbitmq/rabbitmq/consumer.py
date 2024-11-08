import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

def callback(ch, method, properties, body):
    print('body : ', body)

channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print('waiting...')

channel.start_consuming()
connection.close()
