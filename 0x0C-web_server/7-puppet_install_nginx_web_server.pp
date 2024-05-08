# Puppet manifest to install and configure Nginx server

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure => running,
  enable => true,
}

# Define Nginx server block
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
server {
    listen 80;
    server_name _;
    location / {
        return 200 'Hello World!\n';
    }
    location /redirect_me {
        return 301 /;
    }
}
",
  notify  => Service['nginx'],
}

# Enable default server block
file { '/etc/nginx/sites-enabled/default':
  ensure  => 'link',
  target  => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
  notify  => Service['nginx'],
}

