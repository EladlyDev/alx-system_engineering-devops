# change the trafic limit from 15 to 4096

# increase the limit
exec {'fix ULIMIT':
  command  => 'sed -i "s/15/4096/" /etc/default/nginx',
  provider => shell,
}

# restart so the changes take effact
-> exec { 'service nginx stop':
  command  => 'service nginx restart',
  provider => shell,
}
