# 2-puppet_custom_http_response_header.pp
#
# Puppet manifest to install Nginx and configure it to add a custom HTTP header
# X-Served-By with the hostname of the server.

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define Nginx server configuration
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  mode    => '0644',
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        try_files \$uri \$uri/ =404;
        add_header X-Served-By \$hostname;
    }
}
",
  notify => Service['nginx'],
}

# Enable Nginx site configuration
file { '/etc/nginx/sites-enabled/default':
  ensure  => 'link',
  target  => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
  notify  => Service['nginx'],
}

# Restart Nginx service when configuration changes
service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  subscribe  => File['/etc/nginx/sites-available/default'],
}

