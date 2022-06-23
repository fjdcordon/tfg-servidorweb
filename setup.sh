#!/bin/bash
mysql < database.sql
python3 -m pip install mysql-connector apscheduler virtualenv
cp clearCookies.py /home/server
cp clearCookies.service /etc/systemd/system
cp 10periodic /etc/apt/apt.conf.d
cp 20auto-upgrades /etc/apt/apt.conf.d
rm -rf /var/www/*
cp -r src /var/www
cp -r static /var/www
chmod 777 /var/www /var/www/static
cp apache-selfsigned.crt /etc/ssl/certs/
cp apache-selfsigned.key /etc/ssl/private/
a2enmod ssl
python3 -m venv /var/www/venv
/var/www/venv/bin/pip3 install django mysql-connector scapy
cp 000-default.conf /etc/apache2/sites-available
cp apache2.conf /etc/apache2/
mkdir /var/www/logs
chmod 755 /var/www/logs
cp 50-cloud-init.yaml /etc/netplan
echo secure-file-priv = "" >> /etc/mysql/mysql.conf.d/mysqld.cnf
systemctl enable apache2 mysql clearCookies
reboot now