#!/bin/bash
sudo apt-get install mysql-server apache2 python3 python3-pip python3-venv libapache2-mod-wsgi-py3
sudo mysql < database.sql
python3 -m pip install mysql-connector apscheduler virtualenv
cp clearCookies.py /home/server
sudo cp clearCookies.service /etc/systemd/system
sudo cp 10periodic /etc/apt/apt.conf.d
sudo cp 20auto-upgrades /etc/apt/apt.conf.d
sudo rm -rf /var/www/*
sudo cp -r src /var/www
sudo cp -r static /var/www
sudo chmod 777 /var/www /var/www/static
sudo cp apache-selfsigned.crt /etc/ssl/certs/
sudo cp apache-selfsigned.key /etc/ssl/private/
sudo a2enmod ssl
sudo python3 -m venv /var/www/venv
sudo /var/www/venv/bin/pip3/install django mysql-connector scapy
sudo cp 000-default.conf /etc/apache2/sites-available
sudo cp apache2.conf /etc/apache2/
sudo mkdir /var/www/logs
sudo chmod 755 /var/www/logs
sudo cp 50-cloud-init.yaml /etc/netplan
sudo systemctl enable apache2 mysql
sudo reboot now

