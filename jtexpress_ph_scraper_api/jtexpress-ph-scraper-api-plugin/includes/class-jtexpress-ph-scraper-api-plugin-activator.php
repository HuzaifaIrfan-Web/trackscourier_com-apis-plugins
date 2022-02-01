<?php

/**
 * Fired during plugin activation
 *
 * @link       http://huzaifairfan.com/
 * @since      1.0.0
 *
 * @package    Jtexpress_Ph_Scraper_Api_Plugin
 * @subpackage Jtexpress_Ph_Scraper_Api_Plugin/includes
 */

/**
 * Fired during plugin activation.
 *
 * This class defines all code necessary to run during the plugin's activation.
 *
 * @since      1.0.0
 * @package    Jtexpress_Ph_Scraper_Api_Plugin
 * @subpackage Jtexpress_Ph_Scraper_Api_Plugin/includes
 * @author     Huzaifa Irfan <huzaifairfan2001@gmail.com>
 */
class Jtexpress_Ph_Scraper_Api_Plugin_Activator {

	/**
	 * Short Description. (use period)
	 *
	 * Long Description.
	 *
	 * @since    1.0.0
	 */
	public static function activate() {


		$post = array(     
			'post_content'   => '
		   [jtexpress_ph_track_form]
		   [jtexpress_ph_track_details]

		   

			', //content of page
			'post_title'     =>'Jtexpress PH Shipment Details', //title of page
			'post_status'    =>  'publish' , //status of page - publish or draft
			'post_type'      =>  'page'  // type of post
  );
  wp_insert_post( $post ); // creates page

  
	}

}
