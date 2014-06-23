import redis

client = redis.Redis('localhost')

counter_key = client.get('foreign_key1')

client.incr(counter_key)
