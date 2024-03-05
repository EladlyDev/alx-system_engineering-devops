# updating apt
exec { 'update':
  command  => 'sudo apt-get -y update',
  provider => shell,
}

# installing nginx
-> exec { 'install':
  command  => 'sudo apt-get -y install nginx',
  provider => shell,
}

# adds the header to the file
-> exec { 'X-Served-By':
    command => 'sudo sed -i "/listen 80 default_server;/a         add_header X-Served-By $(hostname);
  " /etc/nginx/sites-available/default',
  provider  => shell,
}

# restarting nginx
-> exec { 'service -y nginx':
  command => '/usr/sbin/service nginx restart',
}
