#!/bin/bash
gunicorn -b 0.0.0.0:7575 --workers=$1 fastapi_server:fastapi_app -k uvicorn.workers.UvicornWorker