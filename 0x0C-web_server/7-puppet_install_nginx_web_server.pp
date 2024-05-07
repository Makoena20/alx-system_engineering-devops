# This Puppet manifest installs and configures Nginx server
class nginx {
    package { 'nginx':
        ensure => installed,
    }

    file { '/var/www/html/index.html':
        ensure  => file,
        content => "Hello World!\n",
    }

    file { '/etc/nginx/sites-available/default':
        ensure  => file,
        source  => 'puppet:///modules/nginx/default',
        require => Package['nginx'],
        notify  => Service['nginx'],
    }

    file { '/etc/nginx/sites-enabled/default':
        ensure  => 'link',
        target  => '/etc/nginx/sites-available/default',
        notify  => Service['nginx'],
    }

    service { 'nginx':
        ensure     => 'running',
        enable     => true,
        hasrestart => true,
    }
}

class nginx::redirect {
    file { '/etc/nginx/sites-available/redirect':
        ensure  => file,
        content => "
            server {
                listen 80;
                server_name _;
                return 301 http://$host$request_uri;
            }
        ",
        require => Package['nginx'],
        notify  => Service['nginx'],
    }

    file { '/etc/nginx/sites-enabled/redirect':
        ensure  => 'link',
        target  => '/etc/nginx/sites-available/redirect',
        notify  => Service['nginx'],
    }
}

include nginx
include nginx::redirect

