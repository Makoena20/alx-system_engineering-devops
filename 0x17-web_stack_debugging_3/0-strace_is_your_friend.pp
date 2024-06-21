# This Puppet script fixes the Apache web stack by ensuring the correct permissions for the WordPress directory.
# It does this by using the `file` resource to set the permissions for the directory.

# Ensure the WordPress directory has the correct permissions.
file { '/var/www/html/wp-content/themes/twentyseventeen/assets/images':
  ensure  => 'directory',
  mode    => '0755',
  owner   => 'www-data',
  group   => 'www-data',
  require => File['/var/www/html'],
}
