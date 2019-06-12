import time

import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


def get_hit_count():
	retries = 5
	while True:
		try:
			return cache.incr('hits')
		except redis.exceptions.ConnectionError as exc:
			if retries == 0:
				raise exc
			retries -= 1
			time.sleep(0.5)


@app.route('/')
def hello():
	count = get_hit_count()
	return 'Hello from Docker! I have been seen {} times.\n'.format(count)

@app.route('/isPrime/<number>')
def is_prime(number):
	# If given number is greater than 1 
	num = int(number)
	if num > 1: 
		if num<4 or (num%6)-1 == 0 or (num%6)+1==6:
			storedPrimes = str(cache.get('prime'))
			if "["+number+"]" not in storedPrimes:
				cache.append('prime', "["+number+"]")
			return number+" is prime" 
	return number+" is not prime"

@app.route('/primesStored')
def primes_stored():
	primeN=str(cache.get('prime'))
	primeN=primeN.replace("][", ", ")
	primeN=primeN.replace("b'[", "")
	primeN=primeN.replace("]'", "")
	return primeN
