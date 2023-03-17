function openCity(evt, cityName)
{
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
  
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}

function download(text) 
{
  var pom = document.createElement('a');
  pom.setAttribute('href', 'data:text/plain;charset=utf-8,' + 
    encodeURIComponent(text));
  pom.setAttribute('download', 'test.txt');
  pom.style.display = 'none';
  document.body.appendChild(pom);
  pom.click();
  document.body.removeChild(pom);
}