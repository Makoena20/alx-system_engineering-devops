# File: 2-puppet_custom_http_response_header.pp

# Install nginx package
package { 'nginx':
  ensure => installed,
}

# Define custom HTTP header
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  replace => true,
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        try_files $uri $uri/ =404;
        add_header X-Served-By $hostname;
    }
}
",
  notify  => Service['nginx'],
}

# Enable site configuration
file { '/etc/nginx/sites-enabled/default':
  ensure  => link,
  target  => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
}

# Restart nginx service to apply changes
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}

