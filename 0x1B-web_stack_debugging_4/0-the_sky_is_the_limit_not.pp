# This Puppet manifest optimizes Nginx configuration for handling high concurrency and large number of requests
exec { 'fix--for-nginx':
  command => '/bin/sed -i "s/worker_connections [0-9]*;/worker_connections 4096;/" /etc/nginx/nginx.conf && /bin/sed -i "s/keepalive_timeout [0-9]*;/keepalive_timeout 65;/" /etc/nginx/nginx.conf && /bin/sed -i "s/# multi_accept on;/multi_accept on;/" /etc/nginx/nginx.conf && /bin/sed -i "s/# server_tokens off;/server_tokens off;/" /etc/nginx/nginx.conf && service nginx restart',
  path    => '/usr/bin:/usr/sbin:/bin:/usr/local/bin',
}

