# gRPC with Python

This project was created for learning purposes. Feel free to do whatever you want with it ;-).

# What is RPC?

[This](https://en.wikipedia.org/wiki/Remote_procedure_call) is all you need to have a basic understanding of the concept.

But basically you have remote objects (like OOP objects) and you can call their methods from a client that is running in another machine (or another physical or logical boundary) as if they were instanciated locally.

## What is gRPC?

It is an implementation of RPC. If you want to know more, here's the [link](https://grpc.io/).

## Why would I use it?

Because it's cool (?). And maybe it can be useful for you if you need to integrate multiple systems.

And learning is cool too (!).

# How do I run it?

First, install the dependencies.

_Please consider using a [virtual environment](https://docs.python.org/3/library/venv.html) for that._

`$ python3 -m pip install -r requirements.txt`

## Server

`$ python3 app/server.py`

_And now it's up and running!_

## Client

`$ python3 app/client.py <operation> <a> <b>`

```
<operation> := sum
<a> := INT | FLOAT
<b> := INT | FLOAT
```
