# Puppet manifest to fix Apache 500 error caused by missing directory or permissions

# Ensure the directory /var/www/html/wp-content/uploads exists
file { '/var/www/html/wp-content/uploads':
  ensure  => 'directory',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
}

# Optionally, ensure Apache service is running (if you need to restart it)
service { 'apache2':
  ensure     => 'running',
  enable     => true,
  subscribe  => File['/var/www/html/wp-content/uploads'],
}

