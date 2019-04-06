#!/bin/bash
sudo apt-get install -y python3-pip libmysqlclient-dev nginx virtualenv
sudo virtualenv --python=python3 /opt/env
source /opt/env/bin/active
sudo pip install -r requirements.txt
cp ./dashboard.conf /etc/supervisor/conf.d/dashboard.conf
sudo supervisordctl update
sudo ln -s /opt/Dashboard/nginx.conf /etc/nginx/site-enable/dashboard.org
