# Terminates the process `killmenow`
exec { 'killmenow':
  command => '/usr/bin/pkill killmenow'
}
