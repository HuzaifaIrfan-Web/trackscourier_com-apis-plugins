<?php

/**
 * Provide a public-facing view for the plugin
 *
 * This file is used to markup the public-facing aspects of the plugin.
 *
 * @link       http://huzaifairfan.com/
 * @since      1.0.0
 *
 * @package    Jtexpress_Ph_Scraper_Api_Plugin
 * @subpackage Jtexpress_Ph_Scraper_Api_Plugin/public/partials
 */
?>

<!-- This file should primarily consist of HTML with a little bit of PHP. -->

<?php

$jtexpress_ph_tracking_details_url= get_option('jtexpress_ph_tracking_details_url','/jtexpress-ph-shipment-details');

?>


<form method='get' action='<?php echo $jtexpress_ph_tracking_details_url; ?>'>

	<div style='display:flex;  justify-content:center;'>

		<input name='tnum' type='text' placeholder='Tracking Number' value='<?php echo isset($_REQUEST["tnum"]) ? $_REQUEST["tnum"] : ""; ?>' />
		<input type='submit' value='Track' />

	</div>
</form>