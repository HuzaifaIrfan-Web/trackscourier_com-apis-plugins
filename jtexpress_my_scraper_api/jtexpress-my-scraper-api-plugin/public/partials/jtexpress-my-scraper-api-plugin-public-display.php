<?php

/**
 * Provide a public-facing view for the plugin
 *
 * This file is used to markup the public-facing aspects of the plugin.
 *
 * @link       http://huzaifairfan.com/
 * @since      1.0.0
 *
 * @package    Jtexpress_My_Scraper_Api_Plugin
 * @subpackage Jtexpress_My_Scraper_Api_Plugin/public/partials
 */
?>

<!-- This file should primarily consist of HTML with a little bit of PHP. -->




<?php if (isset($_REQUEST["tnum"]) && !($_REQUEST["tnum"] == '')) : ?>




        <?php


    $jtexpress_my_tracking_api_url = get_option('jtexpress_my_tracking_api_url', 'http://localhost:5000/track/jtexpress_my_scraper_api');

    $jtexpress_my_tracking_api_url .= '?tnum=';
    $jtexpress_my_tracking_api_url .= $_REQUEST['tnum'];



    // print_r($jtexpress_my_tracking_api_url);

    // make request
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $jtexpress_my_tracking_api_url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    $output = curl_exec($ch);



    // handle error; error output
    if (curl_getinfo($ch, CURLINFO_HTTP_CODE) !== 200) {

        //   var_dump($output);
    }

    $res = json_decode($output, true);



    // $response=file_get_contents($jtexpress_my_tracking_api_url);


    // convert response

    curl_close($ch);




    if ($res == false) {

    ?>
        <h2 align='center'>
            Please Enter a Valid Tracking Number
        </h2>

    <?php
    } else {



    ?>
        <br />
        <br />
        <div class='jumbotron' style='overflow-x:scroll;'>
            <h2 align='center'>
                Tracking Number :
                <?php

                echo $res['tnum'];

                ?>
            </h2>
            <?php




            if (isset($res['origin'])) {


            ?>

                <h5 align='center'>
                    Origin :
                    <?php

                    echo $res['origin'];

                    ?>
                </h5>
            <?php

            }

            if (isset($res['destination'])) {

            ?>

                <h5 align='center'>
                    Destination :
                    <?php

                    echo $res['destination'];

                    ?>
                </h5>
            <?php

            }

            if (isset($res['status'])) {

            ?>

                <h5 align='center'>
                    Status :
                    <?php

                    echo $res['status'];

                    ?>
                </h5>
            <?php
            }



            if (isset($res['status_history']) == false) {

            ?>
                <h3 align='center'>
                    Nothing Found!!!
                </h3>
            <?php
            } else {






            ?>
                <h2 align='center'>
                    Status History:
                </h2>
                <?php



                foreach ($res['status_history'] as $status_history) {

                ?>

                    <h3 align='center'>

                        <?php

                        echo $status_history['date'];

                        ?>
                    </h3>






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
                            <?php
                            foreach ($status_history['statuses'] as $status) {










                            ?>
                                <tr class="list-item">
                                    <td align="center">
                                        <?php

                                        echo $status['time'];

                                        ?>
                                    </td>
                                    <td align="center">
                                        <?php

                                        echo $status['status'];


                                        ?>
                                    </td>

                                    <td align="center">
                                        <?php

                                        echo $status['location'];


                                        ?>
                                    </td>

                                </tr>

                            <?php


                            }

                            ?>
                        </tbody>
                    </table>


            <?php




                }
            }

            ?>


        </div>

<?php


    }
?>
    <?php else : ?>

        <h2 align='center'>
            Please Enter a Valid Tracking Number
        </h2>
    
        <?php endif; ?>
      



