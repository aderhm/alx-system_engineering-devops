# Install flask from pip3i
class install_flask {

  package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
  }
}

include install_flask
