<?php

/**
 * Provide a admin area view for the plugin
 *
 * This file is used to markup the admin-facing aspects of the plugin.
 *
 * @link       http://huzaifairfan.com/
 * @since      1.0.0
 *
 * @package    Jtexpress_My_Scraper_Api_Plugin
 * @subpackage Jtexpress_My_Scraper_Api_Plugin/admin/partials
 */
?>

<!-- This file should primarily consist of HTML with a little bit of PHP. -->

<?php

// Plugin Admin Page


if(array_key_exists('submit_api_url', $_POST)){
    update_option('jtexpress_my_tracking_api_url',$_POST['api_url']);
    update_option('jtexpress_my_tracking_details_url',$_POST['form_action_url']);

?>
<div id="setting-error-settings-updated" class="updated settings-error notice is-dismissible">
<strong>Plugin URLs Saved!!</strong>
</div>

<?php

}




    $jtexpress_my_tracking_api_url= get_option('jtexpress_my_tracking_api_url','http://localhost:5000/track/jtexpress_my_scraper_api');
$jtexpress_my_tracking_details_url= get_option('jtexpress_my_tracking_details_url','/jtexpress-my-shipment-details');


?>


<h2>
JTExpress.my Scraper API Plugin Admin Page
</h2>



<form method="post" action="">

<label for="api_url">API URL:</label>
<input type="text" name="api_url" value="<?php echo $jtexpress_my_tracking_api_url; ?>"/>
<br/>
<label for="form_action_url">Form Action URL:</label>
<input type="text" name="form_action_url" value="<?php echo $jtexpress_my_tracking_details_url; ?>"/>
<br/>
<input type="submit" name="submit_api_url" class="button button-primary">
</form>


