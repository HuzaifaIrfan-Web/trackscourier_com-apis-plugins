<?php

/**
 * Define the internationalization functionality
 *
 * Loads and defines the internationalization files for this plugin
 * so that it is ready for translation.
 *
 * @link       http://huzaifairfan.com/
 * @since      1.0.0
 *
 * @package    Jtexpress_My_Scraper_Api_Plugin
 * @subpackage Jtexpress_My_Scraper_Api_Plugin/includes
 */

/**
 * Define the internationalization functionality.
 *
 * Loads and defines the internationalization files for this plugin
 * so that it is ready for translation.
 *
 * @since      1.0.0
 * @package    Jtexpress_My_Scraper_Api_Plugin
 * @subpackage Jtexpress_My_Scraper_Api_Plugin/includes
 * @author     Huzaifa Irfan <huzaifairfan2001@gmail.com>
 */
class Jtexpress_My_Scraper_Api_Plugin_i18n {


	/**
	 * Load the plugin text domain for translation.
	 *
	 * @since    1.0.0
	 */
	public function load_plugin_textdomain() {

		load_plugin_textdomain(
			'jtexpress-my-scraper-api-plugin',
			false,
			dirname( dirname( plugin_basename( __FILE__ ) ) ) . '/languages/'
		);

	}



}
