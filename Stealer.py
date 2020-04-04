from pyrogram import Client
from colorama import Fore, Style
import sys
from time import sleep
from colorama import init, Fore, Style
from os import system, name
from random import choice
from threading import Thread
from requests import get
init()

client = Client("spad_sec", api_id=1330873, api_hash="f854515b6daca37d58563fbc2132ed81")
client.start()

is_steal = False


class SpadSec:
    colors = [Fore.RED, Fore.BLUE, Fore.WHITE, Fore.GREEN, Fore.CYAN, Fore.YELLOW]
    def cleaner(self):
        if name == "nt":
            system("cls")
        else:
            system("clear")
    
    def logo_printer(self):
        self.cleaner()
        logo = """
███████╗██████╗  █████╗ ██████╗ ███████╗███████╗ ██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
███████╗██████╔╝███████║██║  ██║███████╗█████╗  ██║     
╚════██║██╔═══╝ ██╔══██║██║  ██║╚════██║██╔══╝  ██║     
███████║██║     ██║  ██║██████╔╝███████║███████╗╚██████╗
╚══════╝╚═╝     ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝ ╚═════╝
            Telegram Username Stealer v1.0
                  github.com/L0C4L
                    t.me/SpadSEC

        """
        _logo_enumer = 0
        for char in logo:
            if _logo_enumer <= 343:
                sys.stdout.write(f"{choice(self.colors)}{char}{Style.RESET_ALL}")
                sys.stdout.flush()
                _logo_enumer +=1
                sleep(0.002)
            else:
                sys.stdout.write(f"{self.colors[3]}{char}{Style.RESET_ALL}")
                sys.stdout.flush()
                sleep(0.002)


class Stealer:
    def CreateChannel(self, username):
        client.start()
        channel = client.create_channel("SpadStealer", "SpadUsernameStealer")
        client.update_chat_username(channel.id, username)
        client.stop()
        global is_steal
        is_steal = True


def checker(user):
    _conn = get(f"https://t.me/{user}", timeout=5)
    if "</a> right away." in _conn.text:
        print("Stealed")
        steal = Stealer()
        steal.CreateChannel(user)

if __name__ == "__main__":
    try:
        client.stop()
        logo = SpadSec()
        logo.logo_printer()
        try:
            username = sys.argv[1]
        except IndexError:
            print(f"{Fore.YELLOW}Usage: {Fore.GREEN}python {Fore.CYAN}{sys.argv[0]} {Fore.GREEN}username{Style.RESET_ALL}")
            sys.exit(True)

        while not is_steal:
            Thread(target=checker, args=(username,)).start()
            sleep(1)
    except KeyboardInterrupt:
        print("\nGoodBye <3")
