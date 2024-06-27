# This Puppet manifest changes the OS configuration to increase the file descriptor limit for the holberton user

exec { 'increase_file_descriptor_limit':
  command => 'echo "holberton soft nofile 4096" >> /etc/security/limits.conf && echo "holberton hard nofile 8192" >> /etc/security/limits.conf',
  unless  => 'grep -q "holberton soft nofile 4096" /etc/security/limits.conf && grep -q "holberton hard nofile 8192" /etc/security/limits.conf',
}

exec { 'apply_ulimit_changes':
  command => 'ulimit -n 8192',
  onlyif  => 'test $(ulimit -n) -lt 8192',
}

file_line { 'pam_limits':
  path  => '/etc/pam.d/common-session',
  line  => 'session required pam_limits.so',
  match => '^#?session required pam_limits.so',
}

