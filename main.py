import kivy
from kivy_garden.mapview import MapView
from kivymd.app import MDApp
from mapmain import MapMain



class MainApp(MDApp):

    def plus_pressed(self):
        print('PLUS IS PRESSED')
        MapMain().add_pin_by_pressing()



    def dots_pressed(self):
        print('dots are pressed')


MainApp().run()