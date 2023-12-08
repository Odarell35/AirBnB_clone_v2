#!/usr/bin/env bash
#script that sets up your web servers for the deployment

sudo apt-get update
sudo apt-get install -y nginx

#create folders
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

#create symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

#Give ownership of the folder to the user AND group
chown -R ubuntu /data/
chgrp -R ubuntu /data/

#config nginx
replace="server_name _;\n\tlocation \/hbnb_static {\n\talias \/data\/web_static\/current;\n\tindex index.html index.htm;\n\t}"
sudo sed -i "s/server_name _;/$replace/" /etc/nginx/sites-enabled/default

#restart nginx
sudo service nginx restart
