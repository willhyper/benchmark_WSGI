# benchmark_WSGI

## setup
```
git clone https://github.com/willhyper/benchmark_WSGI.git
cd benchmark_WSGI
mkdir .venv # this makes the virtual environment locally under project folder 
pipenv install
pipenv shell
```

## pick one WSGI server to run
```
./run_flask.sh
./run_twisted.sh
./run_gunicorn.sh
./run_mod_wsgi.sh
...
./run_*.sh
```

## run the traffic
```python
python reqs.py
```

## play
1. edit reqs.py to config how stress the traffic of requests are
2. edit func.py to define the single request logic
3. edit run_*.sh to config WSGI server
