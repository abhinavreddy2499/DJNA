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
  addMarkerOnMap(sourceLoc, map, markers, bounds, 'start');
  addMarkerOnMap(destLoc, map, markers, bounds, 'destination');
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

