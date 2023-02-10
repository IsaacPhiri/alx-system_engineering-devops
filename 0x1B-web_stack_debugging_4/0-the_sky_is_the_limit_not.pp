# Increases the amount of traffic an Nginx server can handle.

# Increase limit

exec { 'fix_for_nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
  notify  => Exec['nginx_restart'],
}

# Restart nginx

exec { 'nginx_restart':
  command => 'nginx restart',
  path    => '/etc/init.d/',
  require => Exec['fix_for_nginx'],
}

