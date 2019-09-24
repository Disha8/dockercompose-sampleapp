#!/usr/bin/env python

from flask import Flask
from redis import Redis
import os,socket

app = Flask(_name_)
redis = Redis(host="redis" , port=6379)

@app.route(' / ')
def hello():
    redis.incr('totalhits')
    return 'Docker - Learn in 10 Days, Hello Learners, hope you are enjoying the tutorial. A warm hello from container no %s ! I have been seen %s times .' %(socket.gethostname(), redis.get ('totalhits'))
    
if _name_== "_main_":
   app.run(host="0.0.0.0",debug=True
