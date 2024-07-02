# This Puppet manifest ensures the /var/www/html/wp-content/uploads directory exists and has correct permissions to fix Apache 500 error.

class apache_fix (
  $directory_path,
) {
  file { $directory_path:
    ensure  => 'directory',
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0755',
  }
}

class { 'apache_fix':
  directory_path => '/var/www/html/wp-content/uploads',
}

