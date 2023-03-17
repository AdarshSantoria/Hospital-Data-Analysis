<?php

$insert = false;
if(isset($_POST['Hospital']))
{
    $server = "localhost";
    $username = "root";
    $password = "";
    $dbname = "hospital data";

    $con = mysqli_connect($server, $username, $password, $dbname);
    if(!$con){
        die("Connection to database failed due to". mysqli_connect_error());
    }
    $Hospital = $_POST['Hospital'];
    $City = $_POST['City'];
    $District = $_POST['District'];
    $State = $_POST['State'];
    $Country = $_POST['Country'];
    $Date = $_POST['Date'];
    $Patients = $_POST['Patients'];
    $Beds = $_POST['Beds'];
    $Deaths = $_POST['Deaths'];
    $Cancer = $_POST['Cancer'];
    $Tuberculosis = $_POST['Tuberculosis'];
    $Pneumonia = $_POST['Pneumonia'];
    $Covid = $_POST['Covid'];

    $sql = "INSERT INTO `hospital data`. `dataset` (`Hospital`, `City`, `District`, `State`, `Country`, `Date`, `Patients`, `Beds`, `Deaths`,
            `Cancer`, `Tuberculosis`, `Pneumonia`, `Covid`) VALUES ('$Hospital', '$City', '$District', '$State', '$Country',
            '$Date', '$Patients', '$Beds', '$Deaths', '$Cancer', '$Tuberculosis', '$Pneumonia', '$Covid');";
    // echo "<pre>"; /
    // print_r($con);
    if($con -> query($sql) == true){
        $insert = true;
    }
    else {
        echo "ERROR: $sql <br> $con -> error";
    }
    $con -> close();
}
?>

<!DOCTYPE html>
<html lang = "en">

<head>
    <title> Hospital Data Analysis </title>
    <link rel = "stylesheet" type = "text/css" href = "css.css">
    <script src = "js.js" async defer> </script>
    <link rel = "icon" type = "image/x-icon" href = "Data_stuff.ico">
</head>

<body>
    <div class = "header">
        <img src = "poster.jpg">
        <div class = "tab">
            <button class = "tablinks" onclick = "openCity(event, 'Data Entry')"> Data Entry </button>
            <button class = "tablinks" onclick = "openCity(event, 'Data Analysis')"> Data Analysis </button>
            <button class = "tablinks" onclick = "openCity(event, 'Notes')"> Notes </button>
        </div>
    </div>
    <br>
    <div id = "Data Entry" class = "tabcontent">
        <form class = "myfrm" action = "index.php" method = "post">
            <div class = "form-grp"> <label> Hospital Name </label>
                <input type = "text" name = "Hospital" id = "Hospital">
            </div>
            <div class = "address">
                <label > City </label>
                <label class = "district"> District </label>
                <label> State </label>
                <label class = "country"> Country </label>
            </div>
            <div class = "address">
                <input type = "text" name = "City" id = "City">
                <input type = "text" name = "District" id = "District">
                <input type = "text" name = "State" id = "State">
                <input type = "text" name = "Country" id = "Country">
            </div>
            <div class = "date"> <label> Date </label>
                <input type = "date" name = "Date" id = "Date">
            </div>
            <br><br>
            <div class = "diseases">
                <label > Patients </label>
                <label class = "beds"> Beds </label>
                <label class = "deaths"> Deaths </label>
                <label class = "cancer"> Cancer </label>
                <label class = "tuberculosis"> Tuberculosis </label>
                <label class = "pneumonia"> Pneumonia </label>
                <label class = "covid"> Covid </label>
            </div>
            <div class = "diseases">
                <input type = "text" name = "Patients" id = "Patients" >
                <input type = "text" name = "Beds" id = "Beds" >
                <input type = "text" name = "Deaths" id = "Deaths" >
                <input type = "text" name = "Cancer" id = "Cancer">
                <input type = "text" name = "Tuberculosis" id = "Tuberculosis" >
                <input type = "text" name = "Pneumonia" id = "Pneumonia" >
                <input type = "text" name = "Covid" id = "Covid" >
            </div>
            <?php
                if($insert == true)
                {
                    echo "<p class='submitMsg'> Data saved successfully </p>";
                }
            ?>
            <button type  = "submit" name = "submit"> Submit </button>
        </form>
    </div>
    <div id = "Data Analysis" class = "tabcontent">
        <h3> This section will be completed soon. </h3>
    </div>
    
    <div id = "Notes" class = "tabcontent">
        <form onsubmit = "download(this['notes'].value)">
            <div>
                <textarea name = "notes"> </textarea>
                <button type  = "submit" value="Download" class = "notes"> Saves </button>
                </div>
            </div>
        </form>
    </div>
</body>

</html>