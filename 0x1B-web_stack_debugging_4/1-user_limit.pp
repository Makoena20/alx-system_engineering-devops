# This Puppet script adjusts the OS configuration to increase the open file limit for the holberton user.

exec { 'set_file_limits':
  command => 'echo "holberton soft nofile 4096" >> /etc/security/limits.conf && echo "holberton hard nofile 4096" >> /etc/security/limits.conf',
  unless  => '/bin/grep -q "holberton soft nofile 4096" /etc/security/limits.conf',
}

exec { 'apply_limits':
  command => 'echo "session required pam_limits.so" >> /etc/pam.d/common-session',
  unless  => '/bin/grep -q "session required pam_limits.so" /etc/pam.d/common-session',
}

