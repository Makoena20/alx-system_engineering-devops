# Puppet manifest to kill a process named killmenow using exec resource and pkill

# Define the exec resource to kill the process
exec { 'killmenow':
  command     => '/usr/bin/pkill -f killmenow',
  path        => ['/bin', '/usr/bin'],
  refreshonly => true,
}

# End of Puppet manifest

