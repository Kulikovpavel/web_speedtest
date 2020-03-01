# hey install
https://github.com/rakyll/hey

```.shell script
brew install hey

```

# service start

```shell script
./start_fastapi.sh 5 > /dev/null
./start_fastapi_gunicorn.sh 5 > /dev/null
./start_flask.sh 5 > /dev/null
./start_wsgi.sh.sh 5 > /dev/null
```

# testing

Simple response and response with delay (0.3s), sync and async in fastapi

```shell script
hey -z 5s -c 100 http://127.0.0.1:7575/simple
hey -z 5s -c 100 http://127.0.0.1:7575/delay
```

# results

## wsgi:

```
Summary:
  Total:	5.0176 secs
  Slowest:	0.1566 secs
  Fastest:	0.0057 secs
  Average:	0.0363 secs
  Requests/sec:	2745.5389


Summary delay:
  Total:	10.9150 secs
  Slowest:	6.0630 secs
  Fastest:	0.3032 secs
  Average:	4.4625 secs
  Requests/sec:	16.4911
```
## flask (gunicorn)
```
Summary:
  Total:	5.0188 secs
  Slowest:	0.1470 secs
  Fastest:	0.0049 secs
  Average:	0.0381 secs
  Requests/sec:	2616.1647
  
Summary delay:
  Total:	10.9675 secs
  Slowest:	6.1017 secs
  Fastest:	0.3416 secs
  Average:	4.4857 secs
  Requests/sec:	16.4121
```
## fastapi (uvicorn)
```
Summary:
  Total:	5.0057 secs
  Slowest:	0.0277 secs
  Fastest:	0.0010 secs
  Average:	0.0064 secs
  Requests/sec:	15641.8832
  
Summary delay:
  Total:	5.2261 secs
  Slowest:	0.3112 secs
  Fastest:	0.3010 secs
  Average:	0.3063 secs
  Requests/sec:	325.2915
```
## fastapi (gunicorn)
```
Summary:
  Total:	5.0057 secs
  Slowest:	0.0232 secs
  Fastest:	0.0010 secs
  Average:	0.0046 secs
  Requests/sec:	21732.5816

Summary delay:
  Total:	5.1459 secs
  Slowest:	0.3105 secs
  Fastest:	0.2996 secs
  Average:	0.3021 secs
  Requests/sec:	330.3580
```

# short

Short, with 5 gunicorn workers, on mac:

21700r/sec for fastapi (gunicorn), 2600r/sec for flask (gunicorn)

Almost 10x difference on single call time (0.003s vs 0.03 s, appr.), good internal optimization

Much more Interesting with sleep(0.3) inside, sync and async versions, can be much faster for fastapi with additional call-producers (100 in my test):

330.36r/sec for fastapi, 16.41r/sec for flask

