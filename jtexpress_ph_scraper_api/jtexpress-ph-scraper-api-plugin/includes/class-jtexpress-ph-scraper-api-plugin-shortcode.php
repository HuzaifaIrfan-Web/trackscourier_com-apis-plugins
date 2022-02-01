<?php

/**
 * Register all actions and filters for the plugin
 *
 * @link       http://huzaifairfan.com/
 * @since      1.0.0
 *
 * @package    Jtexpress_Ph_Scraper_Api_Plugin
 * @subpackage Jtexpress_Ph_Scraper_Api_Plugin/includes
 */

/**
 * Register all actions and filters for the plugin.
 *
 * Maintain a list of all hooks that are registered throughout
 * the plugin, and register them with the WordPress API. Call the
 * run function to execute the list of actions and filters.
 *
 * @package    Jtexpress_Ph_Scraper_Api_Plugin
 * @subpackage Jtexpress_Ph_Scraper_Api_Plugin/includes
 * @author     Huzaifa Irfan <huzaifairfan2001@gmail.com>
 */

 
class Jtexpress_Ph_Scraper_Api_Plugin_Shortcode
{

	public static function run()
	{



function jtexpress_ph_track_form_func(){


	ob_start();
	include_once plugin_dir_path(dirname(__FILE__)) . 'public/partials/jtexpress-ph-scraper-api-plugin-form-display.php';
	$output = ob_get_contents();
	ob_end_clean();

	return $output;
}

add_shortcode('jtexpress_ph_track_form','jtexpress_ph_track_form_func');





// Plugin Tracking Deatils ShortCode




function jtexpress_ph_track_details_func(){


	ob_start();
	include_once plugin_dir_path(dirname(__FILE__)) . 'public/partials/jtexpress-ph-scraper-api-plugin-public-display.php';
	$output = ob_get_contents();
	ob_end_clean();

	return $output;
};

add_shortcode('jtexpress_ph_track_details','jtexpress_ph_track_details_func');



	}
}

Jtexpress_Ph_Scraper_Api_Plugin_Shortcode::run();




