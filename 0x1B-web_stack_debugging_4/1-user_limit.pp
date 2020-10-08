#Debugging_4
exec { 'Debugging':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
#Debugging_4
exec { 'Debugging':
  command => 'sed -i \'s/^holberton soft nofile.*/holberton soft nofile 50000/g\' /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
