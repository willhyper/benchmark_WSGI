from flask import Flask
from func import fib

__all__ = ['application']

application = Flask(__name__)


@application.route('/req/<num>')
def req(num: int):
    i = int(num)
    return str(fib(i))


