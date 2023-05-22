function initAutocomplete() {
  var directionsRenderer = new google.maps.DirectionsRenderer();
  directionsService = new google.maps.DirectionsService;
  directionsDisplay = new google.maps.DirectionsRenderer({
    polylineOptions: {
      strokeColor: "red"
    }
  });
  markers = new Map();
  var bounds = new google.maps.LatLngBounds();

  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 42.3732, lng: -72.5199 },
    zoom: 13,
    mapTypeId: "roadmap",
  });

  directionsDisplay.setMap(map);
  directionsDisplay.setPanel(document.getElementById('directionSection'));

  // Create the search box and link it to the UI element.
  var sourceLoc = document.getElementById("sourceLoc");
  var destLoc = document.getElementById("destLoc");
  addMarkerOnMap(sourceLoc, map, markers, bounds, 'sourceLoc');
  addMarkerOnMap(destLoc, map, markers, bounds, 'destLoc');
}

function addMarkerOnMap(input, map, markers, bounds, key) {

var autocomplete = new google.maps.places.Autocomplete(input);
autocomplete.bindTo('bounds', map);

google.maps.event.addListener(autocomplete, 'place_changed', function () {
  var place = autocomplete.getPlace();

  const icon = {
    url: place.icon,
    size: new google.maps.Size(71, 71),
    origin: new google.maps.Point(0, 0),
    anchor: new google.maps.Point(17, 34),
    scaledSize: new google.maps.Size(25, 25),
  };

  var marker = new google.maps.Marker({
      map,
      icon,
      title: place.name,
      position: place.geometry.location,
    });

  var infowindow = new google.maps.InfoWindow();
  google.maps.event.addListener(marker, 'click', (function(marker) {
    return function() {
      infowindow.setContent(place.name);
      infowindow.open(map, marker);
    }
  })(marker));

  // Create a marker for each place.

  if(markers.has(key)) {
      markers.get(key).setMap(null);
      markers.delete(key);
  }
  markers.set(key, marker);
  bounds.extend(marker.position);
  map.fitBounds(bounds);
  var zoom = map.getZoom();
  map.setZoom(zoom > 15 ? 15 : zoom);
  });
}

function removeMarker() {
  markers.get('sourceLoc').setMap(null);
  markers.get('destLoc').setMap(null);
  markers.clear();
  map.setCenter({lat:42.3732, lng:-72.5199});
  map.setZoom(13);
}

function removePathFromMap(){
  //directionsDisplay.setDirections({routes: []});
  directionsDisplay.setMap(null);
  directionsDisplay.setPanel(null);
  directionsService = new google.maps.DirectionsService;
  directionsDisplay = new google.maps.DirectionsRenderer({
    polylineOptions: {
      strokeColor: "red"
    }
  });
  directionsDisplay.setMap(map);
}

function reset() {
    removeMarker();
    removePathFromMap();
    resetRouteStatistics();
    document.getElementById("userDataForm").reset();
}


function getLatLng(coordinates) {
  return new google.maps.LatLng(coordinates[0], coordinates[1]);
}


function submit(){
  
  if(!validateForm()){
    return;
  }
  $.get("http://127.0.0.1:5000/"+ encodeURIComponent($("#sourceLoc").val()) + ":"
  + encodeURIComponent($("#destLoc").val()) + ":"
  + encodeURIComponent($("#max_percent").val()) + ":"
  + encodeURIComponent($("#elevation").val())).done(function (data) {
   const startLocation = data.origin;
   const endLocation = data.des
   const path = data.path;
   const totalDistance = data.dis;
   const elevation = data.elev;

    for(var i =0; i < path.length; i++) {
        showPathOnMap(startLocation, endLocation, path[i], totalDistance, elevation);
    }
  })
}

function showPathOnMap(startLocation, endLocation, pathCoordinates, distance, elevation){
  const waypoints = getWaypoints(pathCoordinates);
  const req = {
                  origin: getLatLng(startLocation),
                  destination: getLatLng(endLocation),
                  waypoints: waypoints,
                  travelMode: 'WALKING'
                };

  directionsService.route(req, function(response, status) {
    if (status === 'OK') {
      directionsDisplay.setDirections(response);
      setRouteStatistics(distance, elevation);
    } else {
      window.alert('Directions request failed due to ' + status);
    }
  });

}

function getWaypoints(pathCoordinates) {
  const waypoints = [];

  for (let i = 3; i < pathCoordinates.length - 3; i++) {
    const waypoint = {
      location: getLatLng(pathCoordinates[i]),
      stopover: false,
    };

    waypoints.push(waypoint);
  }

  return waypoints;
}


function validateForm(){
  var start = document.getElementById("sourceLoc").value;
  var end = document.getElementById("destLoc").value;

  if(start==""){
    window.alert("Please enter the Start Location !");
    return false;
  }

  if(end==""){
    window.alert("Please enter the End Location !");
    return false;
  }
  return true;
}


function setRouteStatistics(distance, elevation) {
  distance = Math.round((distance/1609.344) * 100) / 100;
  elevation = Math.round(elevation * 100) / 100;
  const routeStats =
      "<strong>Total Distance:</strong><label style='text-align:center'> " +
      distance +
      " miles" +
      "</label><br><strong>Elevation Gain:</strong><label style='text-align:center'> " +
      elevation +
      " metres" +
      "</label>";
      document.getElementById("computedResults").innerHTML = routeStats;
}

function resetRouteStatistics() {
  document.getElementById("computedResults").innerHTML = "";
}
