#!/bin/bash
gunicorn GhughuServer.wsgi --bind 0.0.0.0:8000 --workers 3
