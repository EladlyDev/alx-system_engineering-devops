# updating apt-get
exec { 'apt_update':
  command     => '/usr/bin/apt-get -y update',
  refreshonly => true,
}

# installing nginx
package { 'nginx':
  ensure  => installed,
  require => Exec['apt_update'],
}

# configuring the landing page
file { '/var/www/html/index.nginx-debian.html':
  ensure  => file,
  content => "Hello World!\n",
  require => Package['nginx'],
}

# string to add to the default file
$config = 'server {
        listen 80 default_server;
        listen [::]:80 default_server;


        root /var/www/html;

        # Add index.php to the list if you are using PHP
        index index.html index.htm index.nginx-debian.html;

        server_name _;
        rewrite ^/redirect_me https://www.youtube.com/watch?v=QH3-TGUlwu4 permanent;
        }'


file { '/etc/nginx/sites-available/default':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  replace => true,
  content => $config,
}

# starting nginx
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => [Package['nginx'], File['/etc/nginx/sites-available/default']],
}
