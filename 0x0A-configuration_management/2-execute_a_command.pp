# Kills a process by its name
exec {'pkill killmenow':
  command => '/usr/bin/pkill killmenow'
}
