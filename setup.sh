#!/usr/bin/env bash
apt-get update
apt-get install -y libpq-dev python-dev
pip install -r requirements.txt
