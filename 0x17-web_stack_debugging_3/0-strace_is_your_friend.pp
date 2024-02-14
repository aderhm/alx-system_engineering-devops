# Fixes bad `php` extensions

exec { 'fix-extension':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
}
