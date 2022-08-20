from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from web3 import Web3

class MainApp(MDApp):
    def build(self):

    bsc = “https://bsc-dataseed.binance.org/"
    web3 = Web3(Web3.HTTPProvider(bsc)
    print(web3.isConnected())    
    return MDLabel(text="Hello, World", halign="center")


MainApp().run()
