# increase the limit
exec {'change hard limit':
  command  => 'sed -i "/^holberton/s/ [0-9]$/ 10000/"  /etc/security/limits.conf',
  provider => shell,
}
