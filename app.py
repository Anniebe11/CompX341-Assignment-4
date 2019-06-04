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

@app.route('/isPrimeNumber/<number>')
def is_prime_number(number):
   # If given number is greater than 1 
   if num > 1: 
   # Iterate from 2 to n / 2  
   for i in range(2, num//2): 
       # If num is divisible by any number between  
       # 2 and n / 2, it is not prime  
       if (num % i) == 0: 
           print(num, "is not prime") 
           break
   else: 
       cache.append('prime', number)
       print(num, "is prime") 
else: 
   print(num, "is not prime") 

@app.route('/primesSaved')
def primes_saved():
    primes=[]
    print()
    while(redisClient.llen('LanguageList')!=0):
	primeN=redisClient.lpop('LanguageList')
        if primeN in primes:
	else:
            primes.append()
    print("Stored Primes:")
    
