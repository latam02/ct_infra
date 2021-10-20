#!/bin/bash

apt-get update
apt-get install apache2 -y

if ! [ -L /var/ww ]; then
  rm -Rf /var/www
  ln -fs /vagrant /var/www
fi