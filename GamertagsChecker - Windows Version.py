import random
import time
import requests
import sys
import os

# Function to set the console window title
def set_console_title(title):
    if sys.platform.startswith('win'):
        import ctypes
        ctypes.windll.kernel32.SetConsoleTitleW(title)

# Function to set the console window size
def set_console_size(width, height):
    if sys.platform.startswith('win'):
        os.system(f'mode con: cols={width} lines={height}')

# Function to generate a random username
def generate_username(length):
    chars = "qwertyuiopasdfghjklzxcvbnm1234567890"
    first_char = random.choice("qwertyuiopasdfghjklzxcvbnm")
    username = first_char + ''.join(random.choice(chars) for _ in range(length - 1))
    return username

# Function to convert an RGB color to ANSI escape code
def rgb_to_ansi(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

# Function to create a gradient color effect for text with custom RGB colors
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

    colored_text += "\033[0m"  # Reset color
    return colored_text

# Function to create the ASCII art file if it does not exist
def create_file_with_ascii():
    ascii_art = r"""                                                                      
                               _____              _      _  _____ _           _                  
                              |  __ \            (_)    | |/ ____| |         | |                
                              | |  | | __ _ _ __  _  ___| | (___ | |_   _____| | __             
                              | |  | |/ _` | '_ \| |/ _ \ |\___ \| \ \ / / __| |/ /              
                              | |__| | (_| | | | | |  __/ |____) | |\ V / (__|   <             
                              |_____/ \__,_|_| |_|_|\___|_|_____/|_| \_/ \___|_|\_\             
                                                                     
                                         https://github.com/danslvck
              
"""
    # If the file does not exist, create it and write the ASCII art
    with open("Gamertags_Available.txt", "w") as file:  # Use "w" to create a new file or overwrite an existing one
        file.write(ascii_art)
        file.write("\n")  # Add a blank line after the ASCII art

# Function to check username availability and save available ones to a file
def without_list():
    count, done, error = 0, 0, 0
    length = int(input('\nEnter the length of the usernames: '))

    # Check if the file exists and create it with ASCII art if not
    if not os.path.isfile("Gamertags_Available.txt"):
        create_file_with_ascii()

    try:
        with open("Gamertags_Available.txt", "a") as file:
            while True:
                user = generate_username(length)
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
                    })
                    response_text = response.text
                    
                    if "Gamertag doesn't exist" in response_text:
                        print(f"Available: {user}")
                        done += 1
                        file.write(f"                                                   {user}\n")  # Save the available username to the file
                        file.flush()  # Force write to the file
                    else:
                        print(f"Unavailable: {user}")
                        error += 1
                        
                    count += 1

                    if count % 40 == 0:
                        print(f"\n[INFO] Pausing for 1 minute after {count} tests...")
                        time.sleep(60)  # Pause for 1 minute
                
                except requests.RequestException as e:
                    print(f"Request failed: {e}")
                
    except IOError as e:
        print(f"File error: {e}")

# Set the console title and size
set_console_title("Gamertag Checker - https://github.com/Danslvck")
set_console_size(122, 29)

# Define gradient colors
start_rgb = (70, 70, 70)  # Starting color (dark gray)
end_rgb = (240, 240, 240)  # Ending color (light gray)

# Text with gradient effect
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

print(gradient_ascii)

# Prompt for username length and start checking
without_list()
