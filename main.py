import os
import json
import colorama
from pystyle import Colorate, Colors
import subprocess
import webbrowser
import sys
import requests
from tkinter import filedialog as fd
import base64
import time

black = "\033[1;30m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
purple = "\033[1;35m"
cyan = "\033[1;36m"
white = "\033[1;37m"
invalidurl = f"{red}[! MinTool !]{white} Invalid url!"

def clear():
    os.system(
        'clear' if os.name != 'nt' else 'cls')  # should be a better one-liner, because let's be real if its unsupported they are on some next wacky shit
    # if os.name == 'posix':  # Unix/Linux/MacOS
    #     os.system('clear')
    # elif os.name == 'nt':  # Windows
    #     os.system('cls')
    # else:
    #     print("Unsupported operating system")
    #     raise SystemExit

# # might make this idk or might remove it
# def sendembed(url):
#     tit = input(f"{yellow}[? MinTool ?]{white}Title for the embed: ")
#     des = input(f"{yellow}[? MinTool ?]{white}Description: ")
#     color = input(f"{yellow}[? MinTool ?]{white}Hex-Color: ")
#     colormain = f"0x{color}"
#     embed = discord.Embed(title=tit, description=des, color=colormain)
#     requests.post(url,json={"embed":embed})
# '''

def changepfp(url):
    input(f"{yellow}[? MinTool ?]{white} Press enter to select file or skip this to input the path/url")
    image_path = fd.askopenfilename(filetypes=[("Profile Pictures", "*.png;*.jpg;*.jpeg")])
    if image_path is None or image_path == "":
        clear()
        image_path = input(f"{yellow}[? MinTool ?]{white} Path/URL to image: ")
    
    try:
        if image_path.startswith(('http://', 'https://')):
            response = requests.get(image_path)
            response.raise_for_status()
            encoded_image = base64.b64encode(response.content).decode('utf-8')
        else:
            with open(image_path, "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

        data = {
            "avatar": f"data:image/jpeg;base64,{encoded_image}"
        }
        response = requests.patch(url, json=data)
        response.raise_for_status()
        print(f"{green}[+ MinTool +]{white} Profile picture changed successfully.")
    except FileNotFoundError:
        print(f"{red}[! MinTool !] File not found. Please provide a valid file path or image url.")
    except requests.exceptions.HTTPError as errh:
        print(f"{red}[! MinTool !] HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"{red}[! MinTool !] Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"{red}[! MinTool !] Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"{red}[! MinTool !] Request Exception: {err}")

def deletehook(url):
    print(f"{cyan}[+ MinTool +]{white} Trying to delete webhook...")
    try:
        response = requests.delete(url)
        response.raise_for_status()  # Raises HTTPError for bad responses
        print(f"{green}[+ MinTool +]{white} Webhook deleted successfully.")
    except requests.exceptions.HTTPError as errh:
        print(f"{red}[! MinTool !] HTTP Error: {errh}")

    except requests.exceptions.ConnectionError as errc:
        print(f"{red}[! MinTool !] Error Connecting: {errc}")

    except requests.exceptions.Timeout as errt:
        print(f"{red}[! MinTool !] Timeout Error: {errt}")

    except requests.exceptions.RequestException as err:
        print(f"{red}[! MinTool !] Request Exception: {err}")

def sendmessage(url):
    msg = input(f"{yellow}[? MinTool ?]{white} Message: ")
    try:
        response = requests.post(url, json={"content": msg})
        response.raise_for_status()
        print(f"{green}[+ MinTool +]{white} Message sent successfully.")

    except requests.exceptions.HTTPError as errh:
        print(f"{red}[! MinTool !] HTTP Error: {errh}")

    except requests.exceptions.ConnectionError as errc:
        print(f"{red}[! MinTool !] Error Connecting: {errc}")

    except requests.exceptions.Timeout as errt:
        print(f"{red}[! MinTool !] Timeout Error: {errt}")

    except requests.exceptions.RequestException as err:
        print(f"{red}[! MinTool !] Request Exception: {err}")

def renamehook(url):
    name = input(f"{yellow}[? MinTool ?]{white} Webhook Name: ")
    print(f"{cyan}[+ MinTool +]{white} Trying to change username...")
    try:
        response = requests.patch(url, json={"name": name})
        response.raise_for_status()
        print(f"{green}[+ MinTool +]{white} Webhook name changed successfully.")

    except requests.exceptions.HTTPError as errh:
        print(f"{red}[! MinTool !] HTTP Error: {errh}")

    except requests.exceptions.ConnectionError as errc:
        print(f"{red}[! MinTool !] Error Connecting: {errc}")

    except requests.exceptions.Timeout as errt:
        print(f"{red}[! MinTool !] Timeout Error: {errt}")

    except requests.exceptions.RequestException as err:
        print(f"{red}[! MinTool !] Request Exception: {err}")

def spamhook(url):
    print(f"{cyan}[+ MinTool +]{white} Trying to spam webhook...")
    msg = input(f"{yellow}[? MinTool ?]{white} Spam Text: ")
    timeout = float(input(f"{yellow}[? MinTool ?]{white} Timeout (to avoid api-ratelimit): "))
    try:
        print(f"{red}[! MinTool !] Spam has started, Relaunch the tool to stop spam and use it again.")
        while True:
            response = requests.post(url, json={"content": msg})
            response.raise_for_status()
            print(f"{green}[+ MinTool +]{white} Sent message")
            time.sleep(timeout)
    except requests.exceptions.HTTPError as errh:
        print(f"{red}[! MinTool !] HTTP Error: {errh}")

    except requests.exceptions.ConnectionError as errc:
        print(f"{red}[! MinTool !] Error Connecting: {errc}")

    except requests.exceptions.Timeout as errt:
        print(f"{red}[! MinTool !] Timeout Error: {errt}")

    except requests.exceptions.RequestException as err:
        print(f"{red}[! MinTool !] Request Exception: {err}")


modules = [
    "os",
    "json",
    "colorama",
    "pystyle",
    "webbrowser",
    "subprocess"

]

def installer_modules():
    for module in modules:
        try:
            __import__(module)
        except ImportError:
            print(f"Module {module} is not installed. Installation in progress...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", module])
            print(f"{module} was installed successfully!")

if __name__ == "__main__":
    installer_modules()

def open_discord_invite():
    invite_url = "https://discord.gg/minimal"
    webbrowser.open(invite_url)

if __name__ == "__main__":
    print('idek tbh')
def check_requirements():
    utils_folder = './utils'
    config_file = os.path.join(utils_folder, 'config.json')

    if not os.path.isdir(utils_folder):
        raise FileNotFoundError(f"Required file '{utils_folder}' is missing.")

    if not os.path.isfile(config_file):
        raise FileNotFoundError(f"Configuration file '{config_file}' is missing.")

    with open(config_file, 'r') as f:
        try:
            config = json.load(f)
            if (config.get('github') != "https://github.com/AnonymousElixir" or
                config.get('discord') != "https://discord.gg/minimal"):
                raise ValueError("Configuration file does not contain expected values.")
        except json.JSONDecodeError:
            raise ValueError("Configuration file decoding error.")

    print("Configuration Valid.")

def main():
    print(colored_ascii_art)

if __name__ == "__main__":
    
    colorama.init()

    color =  "\033[93m"

    interface = f"""
    ░▒▓██████████████▓▒░░▒▓█▓▒░▒▓███████▓▒░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░        
    ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
    ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
    ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
    ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
    ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
    ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░ 
                                                                                            
                                ┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                                ┃Github :  AnonymousElixir ┃
                                ┃Discord: .gg/Minimal      ┃
                                ┃--------------------------┃
                                ┃ Made By ByteSizedFile :P ┃
                                ┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛

              ┏━━━━━━━━Discord Tools━━━━━━━━┓  ┏━━━━━━━━Webhook Tools━━━━━━━━┓
              ┃   (01) [Token] Information  ┃  ┃      (09) [WHook] Info      ┃
              ┃   (02) [Token] Checker      ┃  ┃      (10) [WHook] Spammer   ┃
              ┃   (03) [Token] DM_ALL       ┃  ┃      (11) [WHook] Rename    ┃
              ┃   (04) [Token] Raid         ┃  ┃      (12) [WHook] Delete    ┃
              ┃   (05) [Token] Name         ┃  ┃      (13) [WHook] Send Msg  ┃
              ┃   (06) [Token] Hypesquad    ┃  ┃      (14) [WHook] Pfp       ┃
              ┃   (07) [Token] Bio          ┃  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛    
              ┃   (08) [Tool]  info         ┃
              ┃                             ┃   Join the discord .gg/minimal
              ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛  
"""

    colored_ascii_art = Colorate.Vertical(Colors.blue_to_purple, interface)
    main()

while True:
    os.system('cls')
    print(colored_ascii_art)
    
    gg = input("""
┌──(user@minimal)-[~/Home]
│                      
└─$> """)
    
    if gg.isdigit():
        gg = int(gg)
    
        if gg == 1:
            import requests
            import os
            import sys
            import time
            import json
            from datetime import datetime, timezone
            from pystyle import Colorate, Colors, Center

            def Continue():
                input("\nPress Enter to continue...")

            def Reset():
                os.system('cls' if os.name == 'nt' else 'clear')

            def ErrorModule(e):
                print(f"Error importing module: {e}")

            def Error(e):
                print(f"An error occurred: {e}")

            def print_text_slowly(text, delay=0.1):
                # Diviser le texte en lignes
                lines = text.splitlines()
                
                # Afficher chaque ligne avec un délai
                for line in lines:
                    print(line)
                    time.sleep(delay)
                
                # Ajouter une ligne vide à la fin si nécessaire
                print()

            def color_gradient(text, start_color, end_color):
                # Crée un dégradé de couleurs pour le texte
                gradient_text = Colorate.Horizontal(start_color, end_color, text)
                return gradient_text

            # Nettoyer l'écran au début
            Reset()

            # Exemple d'utilisation
            text = """
                ░▒▓██████████████▓▒░░▒▓█▓▒░▒▓███████▓▒░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░ 
                                                                                                        
                                            ┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                                            ┃Github :  AnonymousElixir ┃
                                            ┃Discord: .gg/Minimal      ┃
                                            ┃--------------------------┃
                                            ┃ Made By ByteSizedFile :P ┃
                                            ┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛

            """
            textv2 = Colorate.Horizontal(Colors.blue_to_purple, text)
            print_text_slowly(textv2)

            try:
                print()
                token_discord = input(Colorate.Horizontal(Colors.blue_to_purple, "Enter Discord token -> "))
                print(Colorate.Horizontal(Colors.blue_to_purple, "Information Recovery..."))

                headers = {'Authorization': token_discord, 'Content-Type': 'application/json'}
                user = requests.get('https://discord.com/api/v8/users/@me', headers=headers).json()
                r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)

                status = "Valid" if r.status_code == 200 else "Invalid"

                username_discord = user.get('username', "None") + '#' + user.get('discriminator', "None")
                display_name_discord = user.get('global_name', "None")
                user_id_discord = user.get('id', "None")
                email_discord = user.get('email', "None")
                email_verified_discord = str(user.get('verified', "None"))
                phone_discord = str(user.get('phone', "None"))
                mfa_discord = str(user.get('mfa_enabled', "None"))
                country_discord = user.get('locale', "None")

                created_at_discord = "None"
                if 'id' in user:
                    created_at_discord = datetime.fromtimestamp(((int(user['id']) >> 22) + 1420070400000) / 1000, timezone.utc)

                nitro_discord = {0: 'False', 1: 'Nitro Classic', 2: 'Nitro Boosts', 3: 'Nitro Basic'}.get(user.get('premium_type'), 'None')

                avatar_url_discord = f"https://cdn.discordapp.com/avatars/{user_id_discord}/{user.get('avatar')}.png"
                if requests.get(avatar_url_discord).status_code != 200:
                    avatar_url_discord = "None"

                avatar_discord = user.get('avatar', "None")
                avatar_decoration_discord = str(user.get('avatar_decoration_data', "None"))
                public_flags_discord = str(user.get('public_flags', "None"))
                flags_discord = str(user.get('flags', "None"))
                banner_discord = user.get('banner', "None")
                banner_color_discord = user.get('banner_color', "None")
                accent_color_discord = user.get("accent_color", "None")
                nsfw_discord = str(user.get('nsfw_allowed', "None"))
                linked_users_discord = ' / '.join([str(linked_user) for linked_user in user.get('linked_users', [])]) or "None"
                bio_discord = "\n" + user.get('bio', "None")

                authenticator_types_discord = ' / '.join([str(authenticator_type) for authenticator_type in user.get('authenticator_types', [])]) or "None"

                guilds_response = requests.get('https://discord.com/api/v9/users/@me/guilds?with_counts=true', headers=headers)
                guild_count = "None"
                owner_guild_count = "None"
                owner_guilds_names = "None"

                if guilds_response.status_code == 200:
                    guilds = guilds_response.json()
                    guild_count = len(guilds)
                    owner_guilds = [guild for guild in guilds if guild['owner']]
                    owner_guild_count = f"({len(owner_guilds)})"
                    owner_guilds_names = "\n" + "\n".join([f"{guild['name']} ({guild['id']})" for guild in owner_guilds])

                billing_discord = requests.get('https://discord.com/api/v6/users/@me/billing/payment-sources', headers=headers).json()
                payment_methods_discord = ' / '.join(['CB' if method['type'] == 1 else 'Paypal' if method['type'] == 2 else 'Other' for method in billing_discord]) or "None"

                friends_response = requests.get('https://discord.com/api/v8/users/@me/relationships', headers=headers)
                friends_discord = "None"

                if friends_response.status_code == 200:
                    friends = friends_response.json()
                    friends_list = [f"{friend['user']['username']}#{friend['user']['discriminator']} ({friend['user']['id']})" for friend in friends if friend['type'] not in [64, 128, 256, 1048704]]
                    friends_discord = ' / '.join(friends_list) or "None"

                    # Writing friends list to a file with UTF-8 encoding
                    with open('friends_list.txt', 'w', encoding='utf-8') as file:
                        for friend in friends_list:
                            file.write(friend + '\n')

                gift_codes_response = requests.get('https://discord.com/api/v9/users/@me/outbound-promotions/codes', headers=headers)
                gift_codes_discord = "None"

                if gift_codes_response.status_code == 200:
                    gift_codes = gift_codes_response.json()
                    codes = [f"Gift: {gift_code['promotion']['outbound_title']}\nCode: {gift_code['code']}" for gift_code in gift_codes]
                    gift_codes_discord = '\n\n'.join(codes) if codes else "None"

                info = (
                    f"Status: {status}\n"
                    f"Username: {username_discord}\n"
                    f"Display Name: {display_name_discord}\n"
                    f"User ID: {user_id_discord}\n"
                    f"Email: {email_discord}\n"
                    f"Email Verified: {email_verified_discord}\n"
                    f"Phone: {phone_discord}\n"
                    f"MFA Enabled: {mfa_discord}\n"
                    f"Country: {country_discord}\n"
                    f"Created At: {created_at_discord}\n"
                    f"Nitro: {nitro_discord}\n"
                    f"Avatar URL: {avatar_url_discord}\n"
                    f"Avatar: {avatar_discord}\n"
                    f"Avatar Decoration: {avatar_decoration_discord}\n"
                    f"Public Flags: {public_flags_discord}\n"
                    f"Flags: {flags_discord}\n"
                    f"Banner: {banner_discord}\n"
                    f"Banner Color: {banner_color_discord}\n"
                    f"Accent Color: {accent_color_discord}\n"
                    f"NSFW Allowed: {nsfw_discord}\n"
                    f"Linked Users: {linked_users_discord}\n"
                    f"Bio: {bio_discord}\n"
                    f"Authenticator Types: {authenticator_types_discord}\n"
                    f"Guild Count: {guild_count}\n"
                    f"Owner Guild Count: {owner_guild_count}\n"
                    f"Owner Guilds Names: {owner_guilds_names}\n"
                    f"Payment Methods: {payment_methods_discord}\n"
                    f"Friends: {friends_discord}\n"
                    f"Gift Codes: {gift_codes_discord}\n"
                )

                # Write the info to a file with UTF-8 encoding
                with open('discord_info.txt', 'w', encoding='utf-8') as file:
                    file.write(info)



            except Exception as e:
                Error(e)
                time.sleep(10)

        elif gg == 2:
            import json
            import os
            import requests
            import time
            import threading
            import ctypes
            import concurrent.futures
            from pathlib import Path
            from pystyle import Colors, Colorate
            import random

            def print_text_slowly(text, delay=0.1):
                """Affiche le texte lentement, ligne par ligne."""
                lines = text.splitlines()
                for line in lines:
                    print(Colorate.Horizontal(Colors.blue_to_purple, line))
                    time.sleep(delay)
                print()

            def load_proxies():
                """Charge les proxies depuis le fichier proxies.txt."""
                proxies_file_path = current_path.parent.parent / 'proxies.txt'
                if proxies_file_path.exists():
                    with open(proxies_file_path, 'r') as f:
                        proxies = [line.strip() for line in f if line.strip()]
                    print(f"Loaded proxies: {proxies}")  # Debug message
                    return proxies
                print("Proxies file not found.")  # Debug message
                return []

            def get_random_proxy(proxies):
                """Retourne un proxy aléatoire à partir de la liste des proxies."""
                return random.choice(proxies) if proxies else None

            def cls():
                """Nettoie l'écran."""
                os.system('cls' if os.name == 'nt' else 'clear')

            # Définir le chemin du répertoire de travail (deux niveaux au-dessus du répertoire actuel)
            current_path = Path(__file__).resolve().parent
            tokens_file_path = current_path.parent.parent / 'tokens.txt'
            config_file = current_path / 'config.js'

            # Définir le dossier de sortie
            OUTPUT_FOLDER = f'{current_path.parent.parent}/output/{time.strftime("%Y-%m-%d_%H-%M-%S")}'
            os.makedirs(OUTPUT_FOLDER, exist_ok=True)

            # Configuration
            CONFIG = {
                "threads": 10
            }
            SETTINGS = {
                "nitro": True,
                "age": True,
                "type": True,
                "flagged": True
            }

            # Lire le fichier de configuration
            def load_config():
                if not config_file.is_file():
                    print(f"Configuration file {config_file} is missing.")
                    exit(1)

                with open(config_file, 'r') as f:
                    config_data = json.load(f)

                expected_config = {
                    "github": "Github Yozoxir/TraceEye",
                    "discord": "discord.gg/traceye"
                }

                if config_data != expected_config:
                    print("Configuration file does not match the expected format.")
                    exit(1)

            load_config()

            # Nettoyer l'écran au début
            cls()

            # Affichage introductif
            intro_text = """\
                ░▒▓██████████████▓▒░░▒▓█▓▒░▒▓███████▓▒░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░ 
                                                                                                        
                                            ┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                                            ┃Github :  AnonymousElixir ┃
                                            ┃Discord: .gg/Minimal      ┃
                                            ┃--------------------------┃
                                            ┃ Made By ByteSizedFile :P ┃
                                            ┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛
            """
            print_text_slowly(intro_text)

            # Lire les tokens
            if not tokens_file_path.exists():
                raise FileNotFoundError(f"Token file not found at {tokens_file_path}")

            with open(tokens_file_path, 'r') as f:
                tokens = f.readlines()
            tokens = list(set([token.strip() for token in tokens]))

            # Demander si les proxies doivent être utilisés
            use_proxies = input("Use proxies? (yes/no) -> ").strip().lower() == 'yes'
            proxies = load_proxies() if use_proxies else []

            valid = 0
            invalid = 0
            locked = 0
            nitro = 0
            flagged = 0
            total = len(tokens)
            current = 0
            done = False

            def check_token(token):
                global current, valid, invalid, locked, nitro, flagged
                headers = {
                    "Authorization": token
                }
                
                proxy = get_random_proxy(proxies) if use_proxies else None
                proxy_dict = {"http": f"http://{proxy}", "https": f"https://{proxy}"} if proxy else None
                if proxy_dict:
                    print(f"Using proxy: {proxy}")  # Debug message

                try:
                    response = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers, proxies=proxy_dict)
                    if response.status_code == 429:
                        print(f"Rate limited: {token}")
                        return

                    current += 1
                    if response.status_code == 401:
                        invalid += 1
                        with open(f"{OUTPUT_FOLDER}/invalid.txt", "a") as f:
                            f.write(token + "\n")
                        print(f"[/] [Token: {token}] Age: N/A Billing: N/A Nitro: N/A Flagged: N/A Valid: Invalid", end='\r')
                        return

                    if response.status_code == 403:
                        locked += 1
                        with open(f"{OUTPUT_FOLDER}/locked.txt", "a") as f:
                            f.write(token + "\n")
                        print(f"[/] [Token: {token}] Age: N/A Billing: N/A Nitro: N/A Flagged: N/A Valid: Locked", end='\r')
                        return

                    if response.status_code == 200:
                        # Get user details
                        user_response = requests.get("https://discord.com/api/v9/users/@me", headers=headers, proxies=proxy_dict)
                        user_data = user_response.json()

                        user_id = user_data["id"]
                        user_email = user_data.get("email")
                        user_phone = user_data.get("phone")
                        user_flags = user_data.get("flags", 0)

                        account_type = "unclaimed"
                        if user_email:
                            account_type = "email verified"
                        if user_phone:
                            if account_type == "email verified":
                                account_type = "fully verified"
                            else:
                                account_type = "phone verified"

                        # Save valid token
                        valid += 1
                        with open(f"{OUTPUT_FOLDER}/valid.txt", "a") as f:
                            f.write(token + "\n")

                        # Check Nitro subscription
                        billing = False
                        if SETTINGS["nitro"]:
                            billing_response = requests.get("https://discord.com/api/v9/users/@me/billing/subscriptions", headers=headers, proxies=proxy_dict)
                            if billing_response.status_code == 200:
                                subscriptions = billing_response.json()
                                if subscriptions:
                                    billing = True
                                    with open(f"{OUTPUT_FOLDER}/billing.txt", "a") as f:
                                        f.write(token + "\n")

                        # Check account age
                        age = "Unknown"
                        if SETTINGS["age"]:
                            created_at = ((int(user_id) >> 22) + 1420070400000) / 1000
                            age_days = (time.time() - created_at) / 86400
                            age_months = age_days / 30
                            age = f"{age_months:.0f} months" if age_months < 12 else f"{age_months / 12:.0f} years"
                            age_folder = f"{OUTPUT_FOLDER}/age/{age}"
                            os.makedirs(age_folder, exist_ok=True)
                            with open(f"{age_folder}/{account_type}.txt", "a") as f:
                                f.write(token + "\n")

                        # Check account flags
                        flagged_status = "No"
                        if SETTINGS["flagged"] and user_flags & 1048576 == 1048576:
                            flagged += 1
                            flagged_status = "Yes"
                            with open(f"{OUTPUT_FOLDER}/flagged.txt", "a") as f:
                                f.write(token + "\n")

                        # Print result
                        validity = "Valid" if response.status_code == 200 else "Invalid"
                        color = Colors.green if validity == "Valid" else Colors.red
                        print(f"[/] [Token: {token}] Age: {age} Billing: {'Yes' if billing else 'No'} Nitro: {'Yes' if billing else 'No'} Flagged: {flagged_status} Valid: {Colorate.Vertical(color, validity)}", end='\r')

                    # Ajouter un délai pour éviter les problèmes de rate limiting
                    time.sleep(1)

                except Exception as e:
                    print(f"Error checking token {token}: {e}")

            def update_title():
                global done, current, total
                try:
                    while not done:
                        time.sleep(0.1)
                        percentage = (current / total * 100) if total != 0 else 0
                        title = f"Token Checker | Valid: {valid} | Invalid: {invalid} | Locked: {locked} | Remaining: {len(tokens)} | Checked: {percentage:.2f}%"
                        ctypes.windll.kernel32.SetConsoleTitleW(title)
                except ZeroDivisionError:
                    print("Error: No tokens to check.")

            def main():
                global done
                update = threading.Thread(target=update_title)
                update.start()

                with concurrent.futures.ThreadPoolExecutor(max_workers=CONFIG["threads"]) as executor:
                    executor.map(check_token, tokens)

                done = True
                update.join()
                print(f"Checked {current} tokens")
                print(f"Valid tokens: {valid}")
                print(f"Invalid tokens: {invalid}")
                print(f"Locked tokens: {locked}")
                print(f"Tokens with Nitro: {nitro}")
                print(f"Flagged tokens: {flagged}")

            if __name__ == "__main__":
                main()

        elif gg == 3:
            import os
            import json
            import requests
            import time
            import threading
            from pystyle import Colorate, Colors

            ascii_art = """
                ░▒▓██████████████▓▒░░▒▓█▓▒░▒▓███████▓▒░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░ 
                                                                                                        
                                            ┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                                            ┃Github :  AnonymousElixir ┃
                                            ┃Discord: .gg/Minimal      ┃
                                            ┃--------------------------┃
                                            ┃ Made By ByteSizedFile :P ┃
                                            ┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛
            """

            def print_text_slowly(text, delay=0.1):
                # Diviser le texte en lignes
                lines = text.splitlines()
                
                # Afficher chaque ligne avec un délai
                for line in lines:
                    print(Colorate.Horizontal(Colors.blue_to_purple, line))
                    time.sleep(delay)
                
                # Ajouter une ligne vide à la fin si nécessaire
                print()

            def get_dm_channel_ids(token_discord):
                try:
                    response = requests.get("https://discord.com/api/v9/users/@me/channels", headers={'Authorization': token_discord})
                    
                    if response.status_code == 200:
                        channels = response.json()
                        dm_channel_ids = [channel['id'] for channel in channels if channel['type'] == 1]
                        return dm_channel_ids
                    else:
                        print(Colorate.Horizontal(Colors.blue_to_purple, f"[ERROR] Status code {response.status_code}: Unable to fetch DM channels."))
                        return []

                except Exception as e:
                    print(Colorate.Horizontal(Colors.blue_to_purple, f"[ERROR] Error fetching DM channel IDs: {e}"))
                    return []

            def save_ids_to_json(dm_channel_ids, filename):
                with open(filename, 'w') as f:
                    json.dump(dm_channel_ids, f, indent=4)

            def MassDM(token_discord, dm_channel_ids, message):
                try:
                    for channel_id in dm_channel_ids:
                        response = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages",
                                                headers={'Authorization': token_discord, 'Content-Type': 'application/json'},
                                                json={"content": message})
                        if response.status_code == 200:
                            print(Colorate.Horizontal(Colors.blue_to_purple, f"[INFO] Message sent to channel ID: {channel_id}"))
                        else:
                            print(Colorate.Horizontal(Colors.blue_to_purple, f"[ERROR] Status code {response.status_code}: Unable to send message to channel ID: {channel_id}"))

                except Exception as e:
                    print(Colorate.Horizontal(Colors.blue_to_purple, f"[ERROR] Error sending message: {e}"))

            if __name__ == "__main__":
                try:
                    # Nettoyage de l'écran
                    os.system('cls')  # Utilisez 'clear' pour Linux/Mac
                    
                    # Afficher l'art ASCII une seule fois avec effet blue_to_purple
                    print_text_slowly(ascii_art)
                    
                    token_discord = input(Colorate.Horizontal(Colors.blue_to_purple, "Token -> ")).strip()
                    message = input(Colorate.Horizontal(Colors.blue_to_purple, "Message -> ")).strip()
                    output_file = "dm_channel_ids.json"

                    dm_channel_ids = get_dm_channel_ids(token_discord)

                    if not dm_channel_ids:
                        print(Colorate.Horizontal(Colors.blue_to_purple, "[INFO] No DM channel IDs collected. Exiting."))
                        exit(0)

                    save_ids_to_json(dm_channel_ids, output_file)
                    print(Colorate.Horizontal(Colors.blue_to_purple, f"[INFO] Saved all DM channel IDs to {output_file}."))
                    print(Colorate.Horizontal(Colors.blue_to_purple, f"[INFO] Total DM channel IDs collected: {len(dm_channel_ids)}"))

                    proceed = input(Colorate.Horizontal(Colors.blue_to_purple, "Do you want to send the message to all collected DM channels? (y/n)")).strip().lower()

                    if proceed == 'y':
                        for channel_id in dm_channel_ids:
                            t = threading.Thread(target=MassDM, args=(token_discord, [channel_id], message))
                            t.start()
                            t.join()
                            print(Colorate.Horizontal(Colors.blue_to_purple, f"[INFO] Finished sending messages to channel {channel_id}."))
                    else:
                        print(Colorate.Horizontal(Colors.blue_to_purple, "Exiting without sending messages."))

                except Exception as e:
                    print(Colorate.Horizontal(Colors.blue_to_purple, f"[ERROR] {e}"))

        elif gg == 4:
            import os
            import json
            import threading
            import requests
            from pystyle import Colorate, Colors
            import time

            # Nettoyage de l'écran
            os.system('cls')  # Utilisez 'clear' pour Linux/Mac

            ascii_art = """
                ░▒▓██████████████▓▒░░▒▓█▓▒░▒▓███████▓▒░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░ 
                                                                                                        
                                            ┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                                            ┃Github :  AnonymousElixir ┃
                                            ┃Discord: .gg/Minimal      ┃
                                            ┃--------------------------┃
                                            ┃ Made By ByteSizedFile :P ┃
                                            ┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛
            """

            def print_text_slowly(text, delay=0.1):
                lines = text.splitlines()
                for line in lines:
                    print(Colorate.Horizontal(Colors.blue_to_purple, line))
                    time.sleep(delay)

            def ErrorModule(e):
                print(Colorate.Horizontal(Colors.blue_to_purple, f"[ERROR] Module Error: {e}"))

            def log_result(result):
                with open("raid_log.txt", "a") as log_file:
                    log_file.write(result + "\n")

            def main():
                # Affiche l'art ASCII ligne par ligne avec effet blue_to_purple
                print_text_slowly(ascii_art)

                token_discord = input(Colorate.Horizontal(Colors.blue_to_purple, "Enter your Discord token -> ")).strip()
                channel_id = input(Colorate.Horizontal(Colors.blue_to_purple, "Enter the Discord channel ID -> ")).strip()
                raid_type = input(Colorate.Horizontal(Colors.blue_to_purple, "Choose the raid type (message/mention/joinleave) -> ")).strip().lower()
                
                if raid_type not in ["message", "mention", "joinleave"]:
                    print(Colorate.Horizontal(Colors.blue_to_purple, "Error: Invalid raid type."))
                    exit(1)

                message = input(Colorate.Horizontal(Colors.blue_to_purple, "Spam Message -> ")).strip()
                message_sensur = message[:10] + "..." if len(message) > 10 else message

                threads_number = 0
                while True:
                    try:
                        threads_number = int(input(Colorate.Horizontal(Colors.blue_to_purple, "Threads Number (recommended: 2, 4) -> ")))
                        break
                    except ValueError:
                        print(Colorate.Horizontal(Colors.blue_to_purple, "Error: Invalid input for number of threads."))

                delay = float(input(Colorate.Horizontal(Colors.blue_to_purple, "Delay between messages (seconds) -> ")).strip())

                def get_all_members(server_id):
                    headers = {
                        'Authorization': token_discord
                    }
                    members = []
                    after = None

                    while True:
                        url = f"https://discord.com/api/v9/guilds/{server_id}/members?limit=1000"
                        if after:
                            url += f"&after={after}"
                        response = requests.get(url, headers=headers)
                        response.raise_for_status()
                        data = response.json()
                        members.extend(data)
                        if len(data) < 1000:
                            break
                        after = data[-1]['user']['id']

                    return [member['user']['id'] for member in members]

                def raid_message():
                    try:
                        headers = {
                            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
                            'Authorization': token_discord
                        }
                        response = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages",
                                                json={'content': message},
                                                headers=headers)
                        response.raise_for_status()
                        result = f"Message: {message_sensur} | Channel: {channel_id} | Status: Send"
                        print(Colorate.Horizontal(Colors.blue_to_purple, result))
                        log_result(result)
                    except requests.exceptions.RequestException as e:
                        result = f"Message: {message_sensur} | Channel: {channel_id} | Status: Error {e}"
                        print(Colorate.Horizontal(Colors.blue_to_purple, result))
                        log_result(result)

                def raid_mention():
                    try:
                        server_id = channel_id  # Assuming channel_id is the same as server_id
                        member_ids = get_all_members(server_id)
                        headers = {
                            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
                            'Authorization': token_discord
                        }

                        for member_id in member_ids:
                            mention_message = f"<@{member_id}> {message}"
                            response = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages",
                                                    json={'content': mention_message},
                                                    headers=headers)
                            response.raise_for_status()
                            result = f"Mention Message: {mention_message[:10]}... | Channel: {channel_id} | Status: Send"
                            print(Colorate.Horizontal(Colors.blue_to_purple, result))
                            log_result(result)
                            time.sleep(delay)
                    except requests.exceptions.RequestException as e:
                        result = f"Mention Message: {mention_message[:10]}... | Channel: {channel_id} | Status: Error {e}"
                        print(Colorate.Horizontal(Colors.blue_to_purple, result))
                        log_result(result)

                def request():
                    threads = []
                    try:
                        for _ in range(threads_number):
                            if raid_type == "message":
                                t = threading.Thread(target=raid_message)
                            elif raid_type == "mention":
                                t = threading.Thread(target=raid_mention)
                            t.start()
                            threads.append(t)
                            time.sleep(delay)
                    except ValueError:
                        print(Colorate.Horizontal(Colors.blue_to_purple, "Error: Invalid input for number of threads."))

                    for thread in threads:
                        thread.join()

                while True:
                    request()

            if __name__ == "__main__":
                try:
                    main()
                except Exception as e:
                    ErrorModule(e)

        elif gg == 5:
            import requests
            import json
            import time
            from pystyle import Colors, Colorate, Center
            import os

            os.system ('cls')

            def print_text_slowly(text, delay=0.1):
                """Displays text slowly, line by line."""
                lines = text.splitlines()
                for line in lines:
                    print(Colorate.Horizontal(Colors.blue_to_purple, line))
                    time.sleep(delay)
                print()

            ascii_art = """
                ░▒▓██████████████▓▒░░▒▓█▓▒░▒▓███████▓▒░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░ 
                                                                                                        
                                            ┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                                            ┃Github :  AnonymousElixir ┃
                                            ┃Discord: .gg/Minimal      ┃
                                            ┃--------------------------┃
                                            ┃ Made By ByteSizedFile :P ┃
                                            ┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛

            """

            def change_username(token, new_username):
                url = 'https://discord.com/api/v9/users/@me'
                headers = {
                    'Authorization': f'Bearer {token}',
                    'Content-Type': 'application/json',
                }
                data = {
                    'username': new_username
                }

                try:
                    response = requests.patch(url, headers=headers, data=json.dumps(data))
                    response.raise_for_status()
                    print_text_slowly(f"Username changed to {new_username}")
                except requests.exceptions.HTTPError as err:
                    print_text_slowly(f"Error changing username -> {err}")
                except Exception as e:
                    print_text_slowly(f"Error : {e}")

            if __name__ == "__main__":
                print_text_slowly(ascii_art)

                token = input(Colorate.Horizontal(Colors.blue_to_purple, "Enter Discord account token -> "))
                new_username = input(Colorate.Horizontal(Colors.blue_to_purple, "Enter the new username -> "))

                change_username(token, new_username)

        elif gg == 6:
            import requests
            import json
            import time
            from pystyle import Colors, Colorate, Center
            import os 

            os.system('cls')

            # Fonction pour afficher le texte lentement
            def print_text_slowly(text, delay=0.1):
                """Affiche le texte lentement, ligne par ligne."""
                lines = text.splitlines()
                for line in lines:
                    print(Colorate.Horizontal(Colors.blue_to_purple, line))
                    time.sleep(delay)
                print()

            # ASCII Art
            ascii_art = """
                ░▒▓██████████████▓▒░░▒▓█▓▒░▒▓███████▓▒░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░ 
                                                                                                        
                                            ┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                                            ┃Github :  AnonymousElixir ┃
                                            ┃Discord: .gg/Minimal      ┃
                                            ┃--------------------------┃
                                            ┃ Made By ByteSizedFile :P ┃
                                            ┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛
            """

            def change_hypesquad_badge(token, badge_id):
                url = 'https://discord.com/api/v9/users/@me/hypesquad/online'
                headers = {
                    'Authorization': f'Bearer {token}',
                    'Content-Type': 'application/json',
                }
                data = {
                    'house': badge_id
                }

                try:
                    response = requests.post(url, headers=headers, data=json.dumps(data))
                    response.raise_for_status()
                    print_text_slowly(f"HypeSquad badge changed to ID {badge_id}")
                except requests.exceptions.HTTPError as err:
                    print_text_slowly(f"Error changing HypeSquad badge : {err}")
                except Exception as e:
                    print_text_slowly(f"Error : {e}")

            if __name__ == "__main__":
                print_text_slowly(ascii_art)

                token = input(Colorate.Horizontal(Colors.blue_to_purple, "Enter the Discord account token -> "))
                badge_id = input(Colorate.Horizontal(Colors.blue_to_purple, "Enter HypeSquad badge ID (1: Bravery, 2: Brilliance, 3: Balance) -> "))

                if badge_id not in ['1', '2', '3']:
                    print_text_slowly("Invalid HypeSquad badge ID. Please enter 1, 2 or 3.")
                else:
                    change_hypesquad_badge(token, badge_id)

        elif gg == 7:
            import requests
            import json
            import time
            from pystyle import Colors, Colorate, Center

            # Fonction pour afficher le texte lentement
            def print_text_slowly(text, delay=0.1):
                """Affiche le texte lentement, ligne par ligne."""
                lines = text.splitlines()
                for line in lines:
                    print(Colorate.Horizontal(Colors.blue_to_purple, line))
                    time.sleep(delay)
                print()

            # ASCII Art
            ascii_art = """
                ░▒▓██████████████▓▒░░▒▓█▓▒░▒▓███████▓▒░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░ 
                                                                                                        
                                            ┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                                            ┃Github :  AnonymousElixir ┃
                                            ┃Discord: .gg/Minimal      ┃
                                            ┃--------------------------┃
                                            ┃ Made By ByteSizedFile :P ┃
                                            ┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛
            """

            def change_bio(token, new_bio):
                url = 'https://discord.com/api/v9/users/@me'
                headers = {
                    'Authorization': f'Bearer {token}',
                    'Content-Type': 'application/json',
                }
                data = {
                    'bio': new_bio
                }

                try:
                    response = requests.patch(url, headers=headers, data=json.dumps(data))
                    response.raise_for_status()
                    print_text_slowly("Bio updated successfully !")
                except requests.exceptions.HTTPError as err:
                    print_text_slowly(f"Error updating bio: {err}")
                except Exception as e:
                    print_text_slowly(f"Error : {e}")

            if __name__ == "__main__":
                print_text_slowly(ascii_art)

                token = input(Colorate.Horizontal(Colors.blue_to_purple, "Enter the Discord account token -> "))
                new_bio = input(Colorate.Horizontal(Colors.blue_to_purple, "Enter the new bio -> "))

                change_bio(token, new_bio)

        elif gg == 8:
            import pystyle
            from pystyle import Colors, Colorate

            def afficher_informations():
                auteur = "ByteSizedFile"
                discord = "discord.gg/minimal"
                version = "1.0.0"
                tool    = "MinTool"

                info = f"""
                Author     : {auteur}
                Discord    : {discord}
                Version    : {version}
                Tool       : {tool}
                Site       : cassidycamp.work/minimal
                """

                print(Colorate.Horizontal(Colors.blue_to_purple, info))

            if __name__ == "__main__":
                afficher_informations()

            input("Enter to exit")

        elif gg == 9:
            import json
            import os
            import requests
            import time
            from pystyle import Colors, Colorate, Center

            # Nettoyer l'écran (fonction pour Windows)
            def cls():
                os.system('cls' if os.name == 'nt' else 'clear')

            # Fonction pour afficher le texte lentement
            def print_text_slowly(lines, delay=0.1):
                """Affiche les lignes lentement, une par une."""
                for line in lines:
                    print(Colorate.Horizontal(Colors.blue_to_purple, line))
                    time.sleep(delay)
                print()

            # ASCII Art
            ascii_art = """
                ░▒▓██████████████▓▒░░▒▓█▓▒░▒▓███████▓▒░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░ 
                                                                                                        
                                            ┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                                            ┃Github :  AnonymousElixir ┃
                                            ┃Discord: .gg/Minimal      ┃
                                            ┃--------------------------┃
                                            ┃ Made By ByteSizedFile :P ┃
                                            ┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛                       
            """

            def Title(text):
                lines = text.splitlines()
                print_text_slowly(lines)

            def info_webhook(webhook_url):
                headers = {
                    'Content-Type': 'application/json',
                }

                try:
                    response = requests.get(webhook_url, headers=headers)
                    response.raise_for_status() 
                    webhook_info = response.json()
                    print_text_slowly(["\nInformation Webhook:"])

                    print_text_slowly([f"ID      : {webhook_info['id']}"])
                    print_text_slowly([f"Token   : {webhook_info['token']}"])
                    print_text_slowly([f"Name    : {webhook_info['name']}"])
                    print_text_slowly([f"Avatar  : {webhook_info['avatar']}"])
                    print_text_slowly([f"Type    : {'bot' if webhook_info['type'] == 1 else 'user webhook'}"])
                    print_text_slowly([f"Channel ID : {webhook_info['channel_id']}"])
                    print_text_slowly([f"Server ID  : {webhook_info['guild_id']}"])
                    input("\033[0;38mPress Enter to continue...")
                    print_text_slowly(["\nUser information associated with the Webhook:"])
                    if 'user' in webhook_info and webhook_info['user']:
                        user_info = webhook_info['user']
                        print_text_slowly([f"ID          : {user_info['id']}"])
                        print_text_slowly([f"Name        : {user_info['username']}"])
                        print_text_slowly([f"DisplayName : {user_info['global_name']}"])
                        print_text_slowly([f"Number      : {user_info['discriminator']}"])
                        print_text_slowly([f"Avatar      : {user_info['avatar']}"])
                        print_text_slowly([f"Flags       : {user_info['flags']} Publique: {user_info['public_flags']}"])
                        print_text_slowly([f"Color       : {user_info['accent_color']}"])
                        print_text_slowly([f"Decoration  : {user_info['avatar_decoration_data']}"])
                        print_text_slowly([f"Banner      : {user_info['banner_color']}"])
                        print("")
                        input("\033[0;38mPress Enter to continue...")
                    else:
                        print_text_slowly(["\nNo user information associated with the Webhook."])

                except requests.exceptions.RequestException as e:
                    Error(e)

            def Error(e):
                print_text_slowly([f"[ERROR] {e}"])

            if __name__ == "__main__":
                cls()
                Title(ascii_art)

                try:
                    webhook_url = input(Colorate.Horizontal(Colors.blue_to_purple, "\nWebhook URL -> "))
                    info_webhook(webhook_url)

                except Exception as e:
                    Error(e)

        elif gg == 10:
            url = input(f"{yellow}[? MinTool ?]{white} Webhook URL > ")
            spamhook(url)
        elif gg == 11:
            url = input(f"{yellow}[? MinTool ?]{white} Webhook URL > ")
            renamehook(url)
        elif gg == 12:
            url = input(f"{yellow}[? MinTool ?]{white} Webhook URL > ")
            deletehook(url)
        elif gg == 13:
            url = input(f"{yellow}[? MinTool ?]{white} Webhook URL > ")
            sendmessage(url)
        elif gg == 14:
            url = input(f"{yellow}[? MinTool ?]{white} Webhook URL > ")
            changepfp(url)
        
        else:
            print("\033[39mPlease enter a valid number")
            input("\033[0;38mPress Enter to continue...")
