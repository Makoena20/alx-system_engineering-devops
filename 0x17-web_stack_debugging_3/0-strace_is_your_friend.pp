# This Puppet manifest ensures the /var/www/html/wp-content/uploads directory exists,
# sets correct permissions, and restarts Apache to fix the 500 error.

exec { 'fix-wordpress':
  command => 'mkdir -p /var/www/html/wp-content/uploads && chown -R www-data:www-data /var/www/html && service apache2 restart',
  path    => ['/bin', '/usr/bin'],
}

