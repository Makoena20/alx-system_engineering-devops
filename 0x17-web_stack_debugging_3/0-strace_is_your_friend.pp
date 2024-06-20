# This Puppet manifest ensures the required PHP module is installed to fix the Apache 500 error

# Ensure the PHP module is installed
package { 'php5-mysql':
  ensure => installed,
}

# Restart Apache to apply changes
service { 'apache2':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  require    => Package['php5-mysql'],
}

