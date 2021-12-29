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
 * @package           Jtexpress_My_Scraper_Api_Plugin
 *
 * @wordpress-plugin
 * Plugin Name:       JTExpress.my Scraper API Plugin
 * Plugin URI:        http://huzaifairfan.com/
 * Description:       Display JTExpress.my Tracking Details on your Wordpress Website
 * Version:           1.0.0
 * Author:            Huzaifa Irfan
 * Author URI:        http://huzaifairfan.com/
 * License:           GPL-2.0+
 * License URI:       http://www.gnu.org/licenses/gpl-2.0.txt
 * Text Domain:       jtexpress-my-scraper-api-plugin
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
define( 'JTEXPRESS_MY_SCRAPER_API_PLUGIN_VERSION', '1.0.0' );

/**
 * The code that runs during plugin activation.
 * This action is documented in includes/class-jtexpress-my-scraper-api-plugin-activator.php
 */
function activate_jtexpress_my_scraper_api_plugin() {
	require_once plugin_dir_path( __FILE__ ) . 'includes/class-jtexpress-my-scraper-api-plugin-activator.php';
	Jtexpress_My_Scraper_Api_Plugin_Activator::activate();



 

	      $post = array(     
             'post_content'   => '
            [jtexpress_my_track_form]
            [jtexpress_my_track_details]

			

             ', //content of page
             'post_title'     =>'Jtexpress MY Shipment Details', //title of page
             'post_status'    =>  'publish' , //status of page - publish or draft
             'post_type'      =>  'page'  // type of post
   );
   wp_insert_post( $post ); // creates page


}

/**
 * The code that runs during plugin deactivation.
 * This action is documented in includes/class-jtexpress-my-scraper-api-plugin-deactivator.php
 */
function deactivate_jtexpress_my_scraper_api_plugin() {
	require_once plugin_dir_path( __FILE__ ) . 'includes/class-jtexpress-my-scraper-api-plugin-deactivator.php';
	Jtexpress_My_Scraper_Api_Plugin_Deactivator::deactivate();
}

register_activation_hook( __FILE__, 'activate_jtexpress_my_scraper_api_plugin' );
register_deactivation_hook( __FILE__, 'deactivate_jtexpress_my_scraper_api_plugin' );

/**
 * The core plugin class that is used to define internationalization,
 * admin-specific hooks, and public-facing site hooks.
 */
require plugin_dir_path( __FILE__ ) . 'includes/class-jtexpress-my-scraper-api-plugin.php';

/**
 * Begins execution of the plugin.
 *
 * Since everything within the plugin is registered via hooks,
 * then kicking off the plugin from this point in the file does
 * not affect the page life cycle.
 *
 * @since    1.0.0
 */
function run_jtexpress_my_scraper_api_plugin() {

	$plugin = new Jtexpress_My_Scraper_Api_Plugin();
	$plugin->run();

}
run_jtexpress_my_scraper_api_plugin();





// Plugin Code Start




// Plugin Admin Page


function jtexpress_my_scraper_admin(){
    add_menu_page('JTExpress.my Scraper Admin','JTExpress.my Scraper Admin','manage_options','jtexpress-my-scraper-admin','jtexpress_my_scraper_admin_page','',200);
}

add_action('admin_menu','jtexpress_my_scraper_admin');


function jtexpress_my_scraper_admin_page(){

if(array_key_exists('submit_api_url', $_POST)){
    update_option('jtexpress_my_tracking_api_url',$_POST['api_url']);
    update_option('jtexpress_my_tracking_details_url',$_POST['details_url']);

?>
<div id="setting-error-settings-updated" class="updated settings-error notice is-dismissible">
<strong>API URL Saved!!</strong>
</div>

<?php

}




    $jtexpress_my_tracking_api_url= get_option('jtexpress_my_tracking_api_url','http://localhost:5000/track/jtexpress_my_scraper_api');
    $jtexpress_my_tracking_details_url= get_option('jtexpress_my_tracking_details_url','/index.php/jtexpress-my-shipment-details/');


?>


<h2>
JTExpress.my Scraper API Plugin Admin Page
</h2>



<form method="post" action="">

<label for="api_url">API URL:</label>
<input type="text" name="api_url" value="<?php print $jtexpress_my_tracking_api_url; ?>"/>
<br/>
<label for="details_url">Tracking Details URL:</label>
<input type="text" name="details_url" value="<?php print $jtexpress_my_tracking_details_url; ?>"/>
<br/>
<input type="submit" name="submit_api_url" class="button button-primary">
</form>

<?php


}





// Plugin Tracking Form ShortCode




function jtexpress_my_track_form_func(){

    if (isset($_GET['tnum']))
{
    $tnum = $_GET['tnum'];
}else{

    $tnum = '';
}


 $jtexpress_my_tracking_details_url= get_option('jtexpress_my_tracking_details_url','/index.php/jtexpress-my-shipment-details/');


    $content = "

   
<form method='get' action='
";

 $content .=$jtexpress_my_tracking_details_url;

 $content .="
'>

<div style='display:flex;  justify-content:center;'>

<input name='tnum' type='text'  placeholder='Tracking Number'
value='
";

 $content .= $tnum;


 $content .="
'

/>
<input  type='submit' value='Track'/>

</div>
</form>



    ";




    return $content;
}

add_shortcode('jtexpress_my_track_form','jtexpress_my_track_form_func');





// Plugin Tracking Deatils ShortCode




function jtexpress_my_track_details_func(){


if (isset($_GET['tnum']))
{
    $tnum = $_GET['tnum'];
}else{

    $tnum = '';
}




$content="";



    if($tnum ==''){
    
$content .="

<h2 align='center'>
Please Enter a Valid Tracking Number
</h2>



";


    }else{



    $jtexpress_my_tracking_api_url= get_option('jtexpress_my_tracking_api_url','http://localhost:5000/track/jtexpress_my_scraper_api');


$jtexpress_my_tracking_api_url .= $tnum;




// make request
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $jtexpress_my_tracking_api_url); 
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1); 
$output = curl_exec($ch);   



// handle error; error output
if(curl_getinfo($ch, CURLINFO_HTTP_CODE) !== 200) {

  // var_dump($output);
}

$res = json_decode($output, true);



// $response=file_get_contents($jtexpress_my_tracking_api_url);


// convert response

// print_r($res);
curl_close($ch);




if($res == false){

$content .="
<h2 align='center'>
Please Enter a Valid Tracking Number
</h2>
";

}else{



$content .="
<br />
<br />
<div class='jumbotron'>
<h2 align='center'>
Tracking Numeber : 
";

$content .=$res['tnum'];

$content .="
</h2>
";




if(isset($res['origin'])){


$content .="

<h5 align='center'>
Origin : 
";

$content .=$res['origin'];

$content .="
</h5>
";

}

if(isset($res['destination'])){


$content .="

<h5 align='center'>
Destination : 
";

$content .=$res['destination'];

$content .="
</h5>
";

}

if(isset($res['status'])){


$content .="

<h5 align='center'>
Status : 
";

$content .=$res['status'];

$content .="
</h5>
";
}



if(isset($res['status_history']) == false){

$content .="
<h3 align='center'>
Nothing Found!!!
</h3>
";
}else{






								$content .="
								<h2 align='center'>
								Status History:
								</h2>
								";



								foreach($res['status_history'] as $status_history) 
								{

								$content .="

								<h3 align='center'>

								";

								$content .=$status_history['date'];

								$content .="
								</h3>
								";





								$content .='
								<table class="table table-hover">
								<thead>
								  <tr>
								    <th>
								        <h3 align="center">
								        Time
								        </h3>
								    </th>

								    <th>
								        <h3 align="center">
								        Status
								        </h3>
								    </th>

								    <th>
								    <h3 align="center">
								    Location
								    </h3>
								</th>
								  </tr>
								</thead>
								<tbody>
								';

								foreach($status_history['statuses'] as $status) 

								{










								$content .='
								  <tr class="list-item" >
								    <td align="center">
								    ';

								$content .=$status['time'];

								$content .='
								    </td>
								    <td align="center">
								   ';

								$content .=$status['status'];


								$content .='
								    </td>

								    <td align="center">
								   ';

								$content .=$status['location'];


								$content .='

								    </td>

								    </tr>

								   ';











								}



								$content .='
								</tbody>
								</table>


								   ';




								}


}

$content .='


</div>

   ';


    }






};


    return $content;
};

add_shortcode('jtexpress_my_track_details','jtexpress_my_track_details_func');
















?>
