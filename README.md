# AmazonMQ Pub-Sub POC

Install dependencies:

```
pip install pika
```

Create a `.env` file with the following parameters filled in:

```
MQ_BROKER
MQ_USER
MQ_PW
MQ_REGION
```

Open up a couple of ternimal windows as consumers:

```
### terminal 1
python
>>> from consumer import Consumer
>>> Consumer("one")

### terminal 2
python
>>> from consumer import Consumer
>>> Consumer("two")
```

Send a message that will show up in both consumers at the same time:

```
python ./producer.py
```