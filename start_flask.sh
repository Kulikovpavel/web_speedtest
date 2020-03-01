#!/bin/bash
gunicorn -b 0.0.0.0:7575 --workers=$1 flask_server:app