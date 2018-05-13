import requests
from func import fib
from utils import timeit


n = 20
req = 'http://localhost:9999/req/' + str(n)
repeats = 10


expect = fib(n)

reqs = [req] * repeats

timed_req_get = timeit(requests.get)
resps = map(timed_req_get, reqs)

resps_200 = [r for r in resps if r.status_code == 200]

resps_correct = [r for r in resps_200 if int(r.text) == expect]

print(repeats, len(resps_correct))