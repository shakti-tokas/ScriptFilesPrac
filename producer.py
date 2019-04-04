from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('sampletopic', b'Hello, World!')
print('message sent')