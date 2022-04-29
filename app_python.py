from logging import disable
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivy.uix.popup import Popup
from kivymd.uix.tooltip import MDTooltip
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
import webbrowser

# Designate our .kv design file
Builder.load_file('mainpagelayout.kv')
Builder.load_file('module5.kv') ############
Builder.load_file('module4.kv')
Builder.load_file('module3.kv')
Builder.load_file('module2.kv')
Builder.load_file('module1.kv')

Window.size = (16*75,9*75)

#_________________________________#

class MyLayout(MDScreen):
    def open_facebook(self):
        webbrowser.open('http://www.facebook.com')

    def open_insta(self):
        webbrowser.open('http://www.instagram.com')

    def open_youtube(self):
        webbrowser.open('http://www.youtube.com')

class MDTooltipImage_1(MDTooltip,Image):
    pass

class MDTooltipImage_2(MDTooltip,Image):
    pass

class MDTooltipImage_3(MDTooltip,Image):
    pass

class MDTooltipImage_5(MDTooltip,Image):
    pass

class MDTooltipImage_4(MDTooltip,Image):
    pass

class ContentNavigationDrawer(BoxLayout):
    pass

class Gerenciador_de_telas(ScreenManager):
    pass

class MyPopup_Moreinfo_vorecon(Popup):
    pass

class Modulo_1(MDScreen):
    pass

class MDTooltipImage_VORECON_subsection1(MDTooltip,Image):
    pass

class MDTooltipImage_VORECON_subsection2(MDTooltip,Image):
    pass

class Modulo_5(MDScreen):
    pass

class Modulo_2(MDScreen):
    pass

class Modulo_3(MDScreen):
    pass

class Modulo_4(MDScreen):
    pass

class App_Concept(MDApp):
    def build(self,**kwargs):
        return Gerenciador_de_telas()

if __name__ == '__main__':
    App_Concept().run()


