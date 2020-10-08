#Debugging_4
exec { 'Debugging':
  command => 'sed -i \'s/^holberton hard nofile.*/holberton hard nofile 64000/g\' /etc/security/limits.conf',
  path    => '/bin/'
}
