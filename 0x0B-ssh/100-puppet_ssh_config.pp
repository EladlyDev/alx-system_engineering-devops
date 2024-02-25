# not accepting passwords, only ssh
file_line { 'Turn off passwd auth':
  ensure => 'present',
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}

# change the file to school
file_line { 'Declare identity file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
}
