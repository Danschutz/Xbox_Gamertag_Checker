import random
import time
import requests
import sys
import os

# Function to set the console title on Windows
def set_console_title(title):
    if sys.platform.startswith('win'):
        import ctypes
        ctypes.windll.kernel32.SetConsoleTitleW(title)

# Function to set the console size on Windows
def set_console_size(width, height):
    if sys.platform.startswith('win'):
        os.system(f'mode con: cols={width} lines={height}')

# Function to generate a random username of a specified length
def generate_username(length):
    chars = "qwertyuiopasdfghjklzxcvbnm1234567890"  # Characters used for generating usernames
    first_char = random.choice("qwertyuiopasdfghjklzxcvbnm")  # Ensure the first character is a letter
    username = first_char + ''.join(random.choice(chars) for _ in range(length - 1))  # Generate the username
    return username

# Function to convert RGB color values to ANSI escape codes for text color
def rgb_to_ansi(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

# Function to create a gradient effect for text
def gradient_text(text, start_rgb, end_rgb):
    start_r, start_g, start_b = start_rgb
    end_r, end_g, end_b = end_rgb

    colored_text = ""
    text_length = len(text)
    
    for i, char in enumerate(text):
        if char == '\n':
            colored_text += '\n'
        else:
            ratio = i / text_length
            r = int(start_r + (end_r - start_r) * ratio)
            g = int(start_g + (end_g - start_g) * ratio)
            b = int(start_b + (end_b - start_b) * ratio)
            colored_text += f"{rgb_to_ansi(r, g, b)}{char}"

    colored_text += "\033[0m"  # Reset color to default
    return colored_text

# Function to send a message to a Discord webhook
def send_to_discord(user, webhook_url):
    data = {
        "content": f"Available: {user}",  # Message content
        "username": "GamertagsCheckers",  # Username for the Discord bot
        "avatar_url": "https://cdn.discordapp.com/attachments/1280218440598294651/1280219887343501434/401579_xbox_icon.png?ex=66d7492e&is=66d5f7ae&hm=46e16fdfe9453de862eb8acb3d4e7e2c890a05114507cc3656737b886e7a2900&"  # Avatar URL for the Discord bot
    }
    try:
        response = requests.post(webhook_url, json=data)  # Send POST request to Discord webhook
        if response.status_code == 204:
            return True
        else:
            print(f"Error sending result to Discord: {response.status_code}")  # Print error if status code is not 204
            return False
    except requests.RequestException as e:
        print(f"Request failed: {e}")  # Print error if request fails
        return False

# Function to generate and check usernames
def without_list():
    count, done, error = 0, 0, 0  # Initialize counters
    length = int(input('\nEnter the length of the usernames: '))  # Get username length from user
    webhook_url = input('Webhook: ')  # Get Discord webhook URL from user
    
    print()  # Print a blank line after entering the webhook URL
    
    available_users = set()  # Set to store unique available usernames
    
    try:
        while True:
            user = generate_username(length)  # Generate a random username
            try:
                response = requests.get(f"https://xboxgamertag.com/search/{user}", headers={
                    'Host': 'xboxgamertag.com',
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
                    'Accept-Encoding': 'gzip, deflate',
                    'Upgrade-Insecure-Requests': '1',
                    'Sec-Fetch-Dest': 'document',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'none',
                    'Sec-Fetch-User': '?1',
                    'Cache-Control': 'max-age=0',
                    'Te': 'trailers'
                })  # Send GET request to check if username is available
                response_text = response.text
                
                if "Gamertag doesn't exist" in response_text:
                    if user not in available_users:
                        available_users.add(user)  # Add to set if not already present
                        print(f"Available: {user}")  # Print available username
                        send_to_discord(user, webhook_url)  # Send message to Discord
                else:
                    print(f"Unavailable: {user}")  # Print unavailable username
                    error += 1
                    
                count += 1

                if count % 40 == 0:
                    print(f"\n[INFO] Pausing for 1 minute after {count} tests...")  # Print info message
                    time.sleep(60)  # Pause for 60 seconds
            
            except requests.RequestException as e:
                print(f"Request failed: {e}")  # Print error if request fails
            
    except IOError as e:
        print(f"File error: {e}")  # Print error if file operation fails

# Set the console title and size
set_console_title("Gamertag Checker - https://github.com/Danslvck")
set_console_size(122, 29)

# Define gradient colors for the text
start_rgb = (70, 70, 70)  # Starting color (dark gray)
end_rgb = (240, 240, 240)  # Ending color (light gray)

# Create gradient effect for the text
gradient_ascii = gradient_text(
    r"""
                                                                               ███████████████          
                                                                                █████████████       
                                                                           ███      █████      ████    
                                                                         ████████           ████████   
                                                                        ███████████       ████████████ 
    _____              _      _  _____ _           _                   ███████████         ███████████ 
   |  __ \            (_)    | |/ ____| |         | |                 ███████████     █      ██████████
   | |  | | __ _ _ __  _  ___| | (___ | |_   _____| | __              █████████     ██████    █████████
   | |  | |/ _` | '_ \| |/ _ \ |\___ \| \ \ / / __| |/ /              ████████    ██████████    ███████
   | |__| | (_| | | | | |  __/ |____) | |\ V / (__|   <               ███████   █████████████    ██████
   |_____/ \__,_|_| |_|_|\___|_|_____/|_| \_/ \___|_|\_\              ██████  █████████████████   █████
                                                                       ████  ████████████████████  ███ 
              https://github.com/danslvck                               ██  ██████████████████████  ██ 
                                                                         █ ████████████████████████    
                                                                           ███████████████████████     
                                                                             ███████████████████       
                                                                                ████████████     
    """, start_rgb, end_rgb
)

print(gradient_ascii)  # Print the gradient ASCII art

# Start the username checking process
without_list()
