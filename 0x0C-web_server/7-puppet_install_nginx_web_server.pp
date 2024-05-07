# 7-puppet_install_nginx_web_server.pp

# Install Nginx
package { 'nginx':
  ensure => installed,
}

# Configure Nginx to listen on port 80
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.conf.erb'),
  notify  => Service['nginx'],
}

# Create a template for the default Nginx configuration
file { '/etc/nginx/sites-available/default.conf':
  ensure => file,
  content => '
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        try_files $uri $uri/ =404;
        return 200 "Hello World!";
    }

    location /redirect_me {
        return 301 https://alx.com;
    }
}
',
  notify  => Service['nginx'],
}

# Restart Nginx after configuration changes
service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  hasstatus  => true,
  require    => Package['nginx'],
}
