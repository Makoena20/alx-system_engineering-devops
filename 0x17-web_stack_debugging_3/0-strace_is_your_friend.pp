# This Puppet manifest ensures the correct permissions for the web directory to fix Apache 500 error

exec { 'fix-apache-permissions':
  command => '/bin/chown -R www-data:www-data /var/www/html',
  path    => ['/bin', '/usr/bin'],
}

service { 'apache2':
  ensure  => 'running',
  enable  => true,
  require => Exec['fix-apache-permissions'],
}

