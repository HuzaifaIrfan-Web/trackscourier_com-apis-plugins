<?php

/**
 * The file that defines the core plugin class
 *
 * A class definition that includes attributes and functions used across both the
 * public-facing side of the site and the admin area.
 *
 * @link       http://huzaifairfan.com/
 * @since      1.0.0
 *
 * @package    Jtexpress_My_Scraper_Api_Plugin
 * @subpackage Jtexpress_My_Scraper_Api_Plugin/includes
 */

/**
 * The core plugin class.
 *
 * This is used to define internationalization, admin-specific hooks, and
 * public-facing site hooks.
 *
 * Also maintains the unique identifier of this plugin as well as the current
 * version of the plugin.
 *
 * @since      1.0.0
 * @package    Jtexpress_My_Scraper_Api_Plugin
 * @subpackage Jtexpress_My_Scraper_Api_Plugin/includes
 * @author     Huzaifa Irfan <huzaifairfan2001@gmail.com>
 */

 
class Jtexpress_My_Scraper_Api_Plugin_Shortcode
{

	public static function run()
	{



function jtexpress_my_track_form_func(){


	ob_start();
	include_once plugin_dir_path(dirname(__FILE__)) . 'public/partials/jtexpress-my-scraper-api-plugin-form-display.php';
	$output = ob_get_contents();
	ob_end_clean();

	return $output;
}

add_shortcode('jtexpress_my_track_form','jtexpress_my_track_form_func');





// Plugin Tracking Deatils ShortCode




function jtexpress_my_track_details_func(){


	ob_start();
	include_once plugin_dir_path(dirname(__FILE__)) . 'public/partials/jtexpress-my-scraper-api-plugin-public-display.php';
	$output = ob_get_contents();
	ob_end_clean();

	return $output;
};

add_shortcode('jtexpress_my_track_details','jtexpress_my_track_details_func');



	}
}

Jtexpress_My_Scraper_Api_Plugin_Shortcode::run();




