# This Puppet script fixes the 500 Internal Server Error in Apache by ensuring the necessary permissions and configuration.

exec { 'fix-permissions':
  command => 'chown -R www-data:www-data /var/www/html && chmod -R 755 /var/www/html',
  onlyif  => 'find /var/www/html \! -user www-data -o \! -perm 755',
}

service { 'apache2':
  ensure => running,
  enable => true,
  require => Exec['fix-permissions'],
}

file { '/var/www/html/index.php':
  ensure  => file,
  content => '<?php echo "Holberton"; ?>',
  require => Exec['fix-permissions'],
}

