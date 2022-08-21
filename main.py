from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from web3 import Web3

class MainApp(MDApp):
    
    def build(self):
        bsc = 'https://bsc-dataseed.binance.org/'
        web3 = Web3(Web3.HTTPProvider(bsc))
   	
        if (web3.isConnected()):
            print("Connected!")
            return MDLabel(text="OK connected ! ", halign="center")
        else:
            print("KO")
            return MDLabel(text="KO ", halign="center")

MainApp().run()
