#!/bin/bash

APP_PORT=${PORT:-8080}
cd /app/
/opt/venv/bin/uvicorn app.main:app --host 0.0.0.0 --port ${APP_PORT}
