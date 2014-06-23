import redis

client = redis.Redis('localhost')

client.incr('counter1')

client.incr('counter2')
