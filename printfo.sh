#!/bin/bash

sh scripts/login_server.sh
python scripts/convert_to_html.py
python scripts/parseHTML.py
