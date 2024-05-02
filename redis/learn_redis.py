import redis

r = redis.Redis(host="localhost", port=6379, password=None)

r.set("foo", "Привіт")
#r.set(ex="int-seconds") - time of live for key,value in seconds

value = r.get("foo")
print('<->'*20 +'\n' + str(value) + '\n' + '<->' *20)

value = r.get("foo").decode()
print('<->'*20 +'\n' + str(value) + '\n' + '<->' *20)   