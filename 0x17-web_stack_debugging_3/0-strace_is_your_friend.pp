# Fixes bad `php` extensions
exec {'fix-extension':
    command => 'sed -i s/phpp/php/ /var/www/html/wp-settings.php',
    provider => 'shell',
}
