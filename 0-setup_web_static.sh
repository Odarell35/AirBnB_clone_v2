#!/usr/bin/env bash
#script that sets up your web servers for the deployment

sudo apt-get update
sudo apt-get install -y nginx

#create folders
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Holberton School" > /data/web_static/releases/test/index.html

#create symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

#Give ownership of the folder to the user AND group
chown -R ubuntu /data/
chgrp -R ubuntu /data/

#config nginx
replace="add_header X-Served-By $hostname;\n\tlocation \/hbnb_static {\n\talias \/data\/web_static\/current;\n\tindex index.html index.htm;\n\t}"
sudo sed -i "s/add_header X-Served-By $hostname;/$replace/" /etc/nginx/sites-enabled/default

#restart nginx
sudo service nginx restart
