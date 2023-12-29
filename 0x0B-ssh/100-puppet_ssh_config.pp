# Set up client configuration file

file { '/etc/ssh/ssh_config':
	content => "IdentityFile ~/.ssh/school\n  PasswordAuthentication no"
}
