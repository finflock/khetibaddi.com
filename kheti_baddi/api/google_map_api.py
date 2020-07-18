import googlemaps, json
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyDF0Ax8m7_MSENM9_HlALzW6XLHYJnM2Co')


# geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
#
# # Look up an address with reverse geocoding
# reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
#
# # Request directions via public transit
# now = datetime.now()
# directions_result = gmaps.directions("Sydney Town Hall",
#                                      "Parramatta, NSW",
#                                      mode="transit",
#                                      departure_time=now)
# print(directions_result[0])

dm = gmaps.distance_matrix('New Delhi', 'Lotus Panache Sector 110, Noida')

print(dm)

# API_KEY = 'AIzaSyDF0Ax8m7_MSENM9_HlALzW6XLHYJnM2Co'
# import requests
# import lxml.html as lh
# import pandas as pd
#
# url='https://maps.googleapis.com/maps/api/distancematrix/json?origins=Vancouver+BC|Seattle&destinations=San+Francisco|Victoria+BC&mode=bicycling&language=fr-FR&key={}'.format(API_KEY)
#
# page = requests.get(url)
#
# print(page)


# <!DOCTYPE html>
# <html>
#   <head>
#     <title>Simple Map</title>
#     <script src="https://polyfill.io/v3/polyfill.min.js?features=default"></script>
#     <script
#       src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap&libraries=&v=weekly"
#       defer
#     ></script>
#     <style type="text/css">
#       /* Always set the map height explicitly to define the size of the div
#        * element that contains the map. */
#       #map {
#         height: 100%;
#       }
#
#       /* Optional: Makes the sample page fill the window. */
#       html,
#       body {
#         height: 100%;
#         margin: 0;
#         padding: 0;
#       }
#     </style>
#     <script>
#       (function(exports) {
#         "use strict";
#
#         function initMap() {
#           exports.map = new google.maps.Map(document.getElementById("map"), {
#             center: {
#               lat: -34.397,
#               lng: 150.644
#             },
#             zoom: 8
#           });
#         }
#
#         exports.initMap = initMap;
#       })((this.window = this.window || {}));
#     </script>
#   </head>
#   <body>
#     <div id="map"></div>
#   </body>
# </html>