
# encoding: utf-8
import os

import npyscreen
from npyscreen.wgwidget import Widget
class ASPU(npyscreen.NPSApp):
    def main_menu(self):
        F  = npyscreen.Form(name = "Welcome to ASPU",)
        F.add(npyscreen.TitleText, name = "Welcome to ASPU linux version (buildroot-2021.02.1)")
        F.add(npyscreen.TitleText, name = "Copyright (C) CFW-Project. Special thanks for checkra1n team and axi0mX.")
        F.add(npyscreen.TitleText, name = "For unexperienced users, hint: Tab to move focus to \"OK\" button,")
        F.add(npyscreen.TitleText, name = "arrow keys to move focus on other controls.")
        s=F.add(npyscreen.TitleSelectOne, max_height=8, name="Please select an option",
        values=['Jailbreak your device (iPhone 5S to iPhone X)',
        'Enter pwned DFU mode (Limited device support)',
        'Shutdown computer',
        'Reboot computer',
        'Enter shell (Advanced users only)'], scroll_exit=True)
        F.edit()
        if len(s.value) == 0:
            F  = npyscreen.Form(name = "Error",)
            F.add(npyscreen.TitleText, name = "Please select an option.")
            F.edit()
            self.main_menu()
        if s.value[0] == 0:
            F  = npyscreen.Form(name = "Jailbreak device",)
            F.add(npyscreen.TitleText, name = "Please connect your device to DFU mode to begin.")
            F.add(npyscreen.TitleText, name = "For iPhone X/8/7/7Plus, connect your iPhone to computer via the USB cable.")
            F.add(npyscreen.TitleText, name = "Press and hold the Sleep/Wake button and the Volume Down button")
            F.add(npyscreen.TitleText, name = "simultaneously for 10 seconds. Release the Sleep/Wake button")
            F.add(npyscreen.TitleText, name = "while continuing to hold the Volume Down button for 10 additional seconds.")

            F.add(npyscreen.TitleText, name = "For iPhone SE/6s Plus/6s/6 Plus/6/5S/5C/5/4S/4, hold down the Sleep button and")
            F.add(npyscreen.TitleText, name = "Home button at the same time. Keep holding Home and Power until the device ")
            F.add(npyscreen.TitleText, name = "screen turns to black. Release Power button and keep holding Home for 10 seconds.") 
            s=F.add(npyscreen.TitleSelectOne, max_height=8, name="Now please select an option",
            values=['Jailbreak your device directly',
            'Run PongoOS (for advanced users only)',
            'Demote device for debugging (for advanced users only)',
            'Boot device in verbose mode',
            '<- Go back to last menu.'], scroll_exit=True)
            F.edit()
            os.system("clear")
            if len(s.value) == 0:
                F = npyscreen.Form(name = "Error",)
                F.add(npyscreen.TitleText, name = "Please select an option.")
                F.edit()
                self.main_menu()
            if s.value[0] == 0:
                os.system("checkra1n -c -E")
                self.main_menu()
            elif s.value[0] == 1:
                os.system("checkra1n -c -p -E")
                self.main_menu()
            elif s.value[0] == 2:
                os.system("checkra1n -c -d -E")
                self.main_menu()
            elif s.value[0] == 3:
                os.system("checkra1n -c -V -E")
                self.main_menu()
            elif s.value[0] == 4:
                self.main_menu()
        elif s.value[0] == 1:
            os.system("./data/ipwndfu/ipwndfu -p")
            os.system("clear")
            self.main_menu()
        elif s.value[0] == 2:
            os.system("halt")
        elif s.value[0] == 3:
            os.system("reboot")
        elif s.value[0] == 4:
            exit(0)

    def main(self):
        self.main_menu()
       

if __name__ == "__main__":
    App = ASPU()
    App.run()
