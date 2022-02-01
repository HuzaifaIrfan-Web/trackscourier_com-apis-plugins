<?php

/**
 * The plugin bootstrap file
 *
 * This file is read by WordPress to generate the plugin information in the plugin
 * admin area. This file also includes all of the dependencies used by the plugin,
 * registers the activation and deactivation functions, and defines a function
 * that starts the plugin.
 *
 * @link              http://huzaifairfan.com/
 * @since             1.0.0
 * @package           Jtexpress_Ph_Scraper_Api_Plugin
 *
 * @wordpress-plugin
 * Plugin Name:       JTExpress.ph Scraper API Plugin
 * Plugin URI:        http://huzaifairfan.com/
 * Description:       Display JTExpress.ph Tracking Details on your Wordpress Website
 * Version:           1.0.0
 * Author:            Huzaifa Irfan
 * Author URI:        http://huzaifairfan.com/
 * License:           GPL-2.0+
 * License URI:       http://www.gnu.org/licenses/gpl-2.0.txt
 * Text Domain:       jtexpress-ph-scraper-api-plugin
 * Domain Path:       /languages
 */

// If this file is called directly, abort.
// If this file is called directly, abort.
if ( ! defined( 'WPINC' ) ) {
	die("Hey, what are you doing here? You silly human!");
}


/**
 * Currently plugin version.
 * Start at version 1.0.0 and use SemVer - https://semver.org
 * Rename this for your plugin and update it as you release new versions.
 */
define( 'Jtexpress_Ph_Scraper_Api_Plugin_VERSION', '1.0.0' );

/**
 * The code that runs during plugin activation.
 * This action is documented in includes/class-jtexpress-ph-scraper-api-plugin-activator.php
 */
function activate_Jtexpress_Ph_Scraper_Api_Plugin() {
	require_once plugin_dir_path( __FILE__ ) . 'includes/class-jtexpress-ph-scraper-api-plugin-activator.php';
	Jtexpress_Ph_Scraper_Api_Plugin_Activator::activate();
}

/**
 * The code that runs during plugin deactivation.
 * This action is documented in includes/class-jtexpress-ph-scraper-api-plugin-deactivator.php
 */
function deactivate_Jtexpress_Ph_Scraper_Api_Plugin() {
	require_once plugin_dir_path( __FILE__ ) . 'includes/class-jtexpress-ph-scraper-api-plugin-deactivator.php';
	Jtexpress_Ph_Scraper_Api_Plugin_Deactivator::deactivate();
}

register_activation_hook( __FILE__, 'activate_Jtexpress_Ph_Scraper_Api_Plugin' );
register_deactivation_hook( __FILE__, 'deactivate_Jtexpress_Ph_Scraper_Api_Plugin' );

/**
 * The core plugin class that is used to define internationalization,
 * admin-specific hooks, and public-facing site hooks.
 */
require plugin_dir_path( __FILE__ ) . 'includes/class-jtexpress-ph-scraper-api-plugin.php';

/**
 * Begins execution of the plugin.
 *
 * Since everything within the plugin is registered via hooks,
 * then kicking off the plugin from this point in the file does
 * not affect the page life cycle.
 *
 * @since    1.0.0
 */
function run_Jtexpress_Ph_Scraper_Api_Plugin() {

	$plugin = new Jtexpress_Ph_Scraper_Api_Plugin();
	$plugin->run();

}
run_Jtexpress_Ph_Scraper_Api_Plugin();





// Plugin Code Start

