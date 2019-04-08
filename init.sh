#!/bin/bash
sudo apt-get install -y python3-pip libpq-dev nginx virtualenv
sudo virtualenv --python=python3 /opt/env
touch /etc/nginx/sites-enable/dashboard.org
mkdir /var/log/dashboard
touch /var/log/dashboard/access.log
touch /var/log/dashboard/erro.log
source /opt/env/bin/active
sudo pip install -r requirements.txt
cp ./dashboard.conf /etc/supervisor/conf.d/dashboard.conf
sudo supervisordctl update
sudo ln -s /opt/Dashboard/nginx.conf /etc/nginx/sites-enable/dashboard.org
