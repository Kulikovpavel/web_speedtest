#!/bin/bash
uvicorn fastapi_server:fastapi_app --host 0.0.0.0 --port 7575 --workers $1