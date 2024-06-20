# 0-strace_is_your_friend.pp
# This Puppet manifest ensures the required config.php file exists and has correct permissions

file { '/var/www/html/config.php':
  ensure  => file,
  content => "<?php\n// Configuration file\n?>",
  mode    => '0644',
  owner   => 'www-data',
  group   => 'www-data',
}

service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => File['/var/www/html/config.php'], # Restart Apache if config.php changes
}

