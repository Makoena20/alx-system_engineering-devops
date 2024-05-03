# Puppet manifest to install Flask version 2.1.0

# Install flask and werkzeug using pip3
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}

package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  require  => Package['python3-pip'],
}

# Ensure python3-pip is installed
package { 'python3-pip':
  ensure => installed,
}

