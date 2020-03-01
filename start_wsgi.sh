#!/bin/bash
gunicorn -b 0.0.0.0:7575 --workers=$1 wsgi_app:app