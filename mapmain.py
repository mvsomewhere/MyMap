import sqlite3
from kivy_garden.mapview import MapView
from kivy.app import App
from mapmarker import MapMarker
import database

#markers are items that i interact with before adding them onto the map
#pins are items that are already have been placed on a map

class MapMain(MapView):
    marker_tracker=[]
    market_x=0
    current_map_lat=''
    current_map_lon=''

    def update_map_center(self, lat,lon):
        MapMain.current_map_lat=lat
        MapMain.current_map_lon=lon



    def import_marker_from_db(self):
        conn = sqlite3.connect('MainDataBase')
        c = conn.cursor()
        c.execute("SELECT * FROM markers")
        list_of_markers = (c.fetchall())
        market_from_db=list_of_markers[self.market_x]
        market_name=(market_from_db[0])
        market_lat=(market_from_db[1])
        market_lon=(market_from_db[2])


        for i in list_of_markers:
            self.display_pin(market_name, market_lat, market_lon)
        if len(list_of_markers)>self.market_x+1:
            self.market_x+=1


    def display_pin(self, name, lat, lon):
        if name in self.marker_tracker:
            pass
        else:
            marker = MapMarker(lat=lat, lon=lon,
                                source="icon5.png")  # it goes to mapmarker class to set up a popup
            marker.size = (40, 40)  # i've tried other ways but didnt work out
            self.add_widget(marker) # this adds a popup to MapView
            self.marker_tracker.append(name)
            print('added')

    def add_pin_by_pressing(self):

        lat=(MapMain.current_map_lat)
        lon=(MapMain.current_map_lon)
        database.add_marker_to_database(lat,lon)









    #def start_getting_markets_in_fov(self):

     #   newmarker = MapMarker(lat=59.94, lon=30.307, source="image.png")
      #  self.add_marker(newmarker)


    #marker = MapMarker(lat=59.94, lon=30.307, source = "image.png"
#    def add_marker(self, newmarker):

 #       self.add_widget(newmarker)


