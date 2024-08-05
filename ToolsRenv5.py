import os
import time

import getpass

os.system("sleep 1") 
os.system("git pull") 
os.system("sleep 2")
os.system("clear") 

print ("hallo aja.  😁") 
os.system("sleep 3") 
os.system("clear") 

def print_colored_text(text, color_code):
  """Prints text with the specified color code.

  Args:
    text: The text to print.
    color_code: The ANSI escape code for the desired color.
  """
  print(f"\033[{color_code}m{text}\033[0m")
os.system("sleep 2") 

#untuk meng clear text di terminal
os.system("clear") 
os.system("sleep 2")

# Print the banner
print_colored_text(
    """
███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗
████╗░████║██╔════╝████╗░██║██║░░░██║
██╔████╔██║█████╗░░██╔██╗██║██║░░░██║
██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║
██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝
╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░

  𝐨𝐰𝐧𝐞𝙧: 𝙍𝙚𝙣9999
  𝙝𝙪𝙗𝙪𝙣𝙜𝙞 𝙨𝙖𝙮𝙖: +62895365187210
""",
    "34"
)

print()
print()

# Print the menu
print_colored_text(
    """
||=======================================||
|| 𝟏. lanjutkan ke ToolsRenv5            ||
|| 𝟐. exit                               ||
||=======================================||
user:ren
pw  :999
""",
    "38;2;0;255;0"
)

# Get user input
ren9999 = input("                PILIH MENU:")

usernames = {"ren": "999", "Ren": "9999"}

def login():
    while True:
        username = input("Enter username: ")
        if username not in usernames:
            print("USERNAME SALAH WAK")
            continue

        password = input("Enter password: ")
        if usernames[username] != password:
            print("PASSWORD SALAH WAK")
            continue

        print(f"𝐁𝐄𝐑𝐇𝐀𝐒𝐈𝐋 𝐌𝐄𝐋𝐀𝐍𝐉𝐔𝐓𝐊𝐀𝐍 SCRIPT✅ ❗❗❗") 
        break

if __name__ == "__main__":
    login()
os.system("sleep 3") 
os.system("clear") 

if ren9999 == "1":
  os.system("clear")
  time.sleep(1)
  print("loading... 3")
  time.sleep(2)
  os.system("clear")
  print("loading... 2")
  time.sleep(2)
  os.system("clear")
  print("loading... 1")
  time.sleep(2)
  os.system("clear")
  os.system("git clone https://github.com/THEOYS123/Ren_aja.git")
  os.chdir("Ren_aja")
  os.system("bash menu.sh")

elif ren9999 == "2":
  os.system("clear")
  print_colored_text(
    """
███████╗██╗░░██╗██╗████████╗
██╔════╝╚██╗██╔╝██║╚══██╔══╝
█████╗░░░╚███╔╝░██║░░░██║░░░
██╔══╝░░░██╔██╗░██║░░░██║░░░
███████╗██╔╝╚██╗██║░░░██║░░░
╚══════╝╚═╝░░╚═╝╚═╝░░░╚═╝░░░
""",
    "34"
  )
  time.sleep(1)
  print("[*] THANKS BRO👍❗❗")
  time.sleep(2)
  print("[*] TERIMAKASIH SUDAH MENGGUNAKAN TOOLS SAYA😊😊❗❗")
  time.sleep(3)
  exit()
