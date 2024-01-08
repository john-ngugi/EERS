// Log "hello world!" to the console
console.log("hello world!");
var greenIcon = new L.Icon({
    iconUrl: 'https://github.com/pointhi/leaflet-color-markers/blob/234813b7dffa11eee06f41618e1f5752c6b7bd8d/img/marker-icon-2x-green.png?raw=true',
    shadowUrl: 'https://github.com/pointhi/leaflet-color-markers/blob/234813b7dffa11eee06f41618e1f5752c6b7bd8d/img/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});

var redIcon = new L.Icon({
    iconUrl: 'https://github.com/pointhi/leaflet-color-markers/blob/234813b7dffa11eee06f41618e1f5752c6b7bd8d/img/marker-icon-2x-red.png?raw=true',
    shadowUrl: 'https://github.com/pointhi/leaflet-color-markers/blob/234813b7dffa11eee06f41618e1f5752c6b7bd8d/img/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});




// Get references to DOM elements
const searchLocationInput = document.getElementById("search-location");
const locationSubmit = document.getElementById("location-submit-btn");
const form = document.getElementById("form");

// Add an event listener to the form to handle form submission
form.addEventListener("submit", (e) => {
    // Get the value entered in the search location input
    var value = searchLocationInput.value;
    console.log(value);
    // Call the getLocation function with the entered value
    getLocation(value);
    // Clear the input field
    searchLocationInput.value = "";
    // Prevent the default form submission behavior
    e.preventDefault();
})

// Create a Leaflet map and set its view
var map = L.map('map').setView([-1.3, 36.8], 12);
// Add an OpenStreetMap tile layer to the map
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);
// Log the map object to the console
console.log(map);
// Add a marker to the map at the specified coordinates
L.marker([-1.3, 36.8]).addTo(map);

// Define a function to get the location information using an API
function getLocation(location_value) {

    const location = location_value;

    // Fetch data from a weather API based on the entered location
    fetch(`http://api.weatherapi.com/v1/current.json?key=57d373c5712440f796c144428231810&q=${location} kenya&aqi=yes`)
        .then(res => res.json())
        .then(data => {
            console.log(data);

            // Extract latitude and longitude information from the API response
            var lat = data.location.lat;
            var lon = data.location.lon;
            console.log(lat);
            console.log(lon);
            // Pan the map to the specified location and set the zoom level
            // map.panTo(new L.LatLng(lat, lon));
            map.setView([lat, lon], 15, { animate: true });
            // map.setZoom(13);
        })
}

// Log "hello world two" to the console
console.log("hello world two")

const url = 'https://api.openrouteservice.org/v2/directions/driving-car?api_key=5b3ce3597851110001cf624821d7977ad17c4d3ab51df82a9d448a97&start=36.8116,-1.3012&end=36.8034,-1.2959';
const headers = {
    'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8'
};

fetch(url, {
        method: 'GET',
        headers: headers
    })
    .then(response => {
        console.log('Status:', response.status);
        console.log('Headers:', response.headers);
        return response.json(); // Parse response body as JSON
    })
    .then(data => {
        console.log('Body:', data);
        var feature = data.features;
        var first_feature = feature
        console.log(first_feature)
        console.log('coordinates', feature[0].geometry.coordinates);
        console.log(data.features);
        var point_list = feature[0].geometry.coordinates

        point_list_converted = []
        point_list.forEach(element => {
            x = element[1];
            y = element[0];

            point_list_converted.push([x, y]);

            console.log(point_list_converted)
        });
        // var path = L.polyline(point_list_converted, {
        //     color: 'red',
        //     weight: 3,
        //     smoothFactor: 1,
        // });
        // path.addTo(map);

        // var length = point_list_converted.length;
        // var center_float = length / 2;
        // centroid_point = Math.floor(center_float);

        // L.marker([-1.3012, 36.8116], { icon: redIcon }).addTo(map);
        // L.marker([-1.2959, 36.8034], { icon: greenIcon }).addTo(map);
        // map.setView([point_list_converted[centroid_point][0], point_list_converted[centroid_point][1]], 16, { animate: true });


    })
    .catch(error => {
        console.error('Error:', error);
    });


const url_markers = '/ResponseApp/markers-coordinates/'

fetch(url_markers)
    .then(res => res.json())
    .then(data => {
        console.log("marker coordinates are", data)
            // Loop through the markers in the JSON response
        data.coordinates.forEach(function(markerData) {
            var latitude = markerData[0];
            var longitude = markerData[1];
            var type = markerData[2];

            // Create a marker for each set of coordinates
            var marker = L.marker([latitude, longitude]).addTo(map);

            medicalUrl = 'https://images.unsplash.com/photo-1587745416684-47953f16f02f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjN8fGFtYnVsYW5jZXxlbnwwfHwwfHx8MA%3D%3D'
            policeUrl = 'https://images.unsplash.com/photo-1453873531674-2151bcd01707?q=80&w=1373&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
            fireUrl = 'https://images.unsplash.com/photo-1600624697183-00566baf12e6?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8ZmlyZSUyMHRydWNrfGVufDB8fDB8fHww'

            var imgURL;

            if (type == 'Fire') {
                imgURL = fireUrl;
            } else if (type == "Crime") {
                imgURL = policeUrl;
            } else {
                imgURL = medicalUrl
            }


            // You can customize the marker or bind a popup if needed
            marker.bindPopup('<div>' +
                '<p>Emergecy Type: ' + type + '</p>' +
                '<img style="max-width: 100%; max-height: 200px;" src="' + imgURL + '" alt="Marker Image">' +
                '</div>');
        });
    })
    .catch(error => {
        console.error('Error:', error);
    });