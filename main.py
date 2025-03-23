import json, random, time, httpx, sys, os
from concurrent.futures import ThreadPoolExecutor
import threading
from colorama import Fore, Style
from time import strftime, localtime

sent, errored = 0, 0

# Config Load
with open("config.json") as config:
   data = json.load(config)
   delay = data["delay"]
   lastUsername = data["lastUsername"]
   lastCount = data["lastCount"]

# Random Questions Load 
if os.path.exists("questions.txt"):
  with open("questions.txt", 'r') as file:
    questions = file.readlines() 
    questions = [question.strip() for question in questions]
else: 
  questions = []

def saveData(key, value):
   with open("config.json", "r+") as file:
     data = json.load(file)
     data[key] = value
     file.seek(0)
     json.dump(data, file, indent=2)
     file.truncate()

class Console:
   @staticmethod
   def Logger(content: str, status: bool) -> None:
     lock = threading.Lock()
     green = "[" + Fore.GREEN + Style.BRIGHT + "+" + Style.RESET_ALL + "] "
     red = "[" + Fore.RED + Style.BRIGHT + "-" + Style.RESET_ALL + "] "
     yellow = "[" + Fore.YELLOW + Style.BRIGHT + "!" + Style.RESET_ALL + "] "
     with lock:
       if status == "g":
         sys.stdout.write(f'{green}{content}\n')
       elif status == "r":
         sys.stdout.write(f'{red}{content}\n')
       elif status == "y":
         sys.stdout.write(f'{yellow}{content}\n')
   @staticmethod
   def clear() -> None:
     os.system("cls" if os.name == "nt" else "clear")

def main(username, message, deviceid, randomQuestion):
   global errored, sent
   headers = {
      "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:104.0) Gecko/20100101 Firefox/104.0",
    }
   Client = httpx.Client(headers=headers)
   try:
     postresp = Client.post("https://ngl.link/api/submit",data={"username": username,"question": message,"deviceId": deviceid})
     if postresp.status_code == 200:
       sent += 1
       Console.Logger(f"Sent: {sent} | Errored: {errored} {f'\n~ {message}\n' if randomQuestion else ''}", status="g")
     elif postresp.status_code == 404:
       errored += 1
       Console.Logger(f"User {username} does not exist", status="r")
       exit()
     elif postresp.status_code == 429:
       errored += 1
       Console.Logger(f"User {username} is rate limited", status="r")
     else:
       errored += 1
       Console.Logger(f"{postresp.text} {postresp.status_code}", status="r")
   except Exception as e:
     errored += 1
     Console.Logger(f"Error: {e}", status="y")

def deviceid():
   return "".join(random.choice("0123456789abcdefghijklmnopqrstuvwxyz") for i in range(36))

def Main():
   Console.clear()
   from colorama import Fore, Style
   print(
    Fore.CYAN + f"{'NGL Spammer':^20}" +
    Fore.MAGENTA + r"""
 __    __   ______   __                 
/  \  /  | /      \ /  |  
$$  \ $$ |/$$$$$$  |$$ |       __    __ 
$$$  \$$ |$$ | _$$/ $$ |      /  \  /  |
$$$$  $$ |$$ |/    |$$ |      $$  \/$$/ 
$$ $$ $$ |$$ |$$$$ |$$ |       $$  $$<  
$$ |$$$$ |$$ \__$$ |$$ |_____  /$$$$  \ 
$$ | $$$ |$$    $$/ $$       |/$$/ $$  |
$$/   $$/  $$$$$$/  $$$$$$$$/ $$/   $$/ 
""" +
    Fore.YELLOW + "Created by Brainless Dip\n" +  # Highlight creator in yellow
    f"Current delay: {delay}\n" +
    Fore.GREEN + f"Loaded {len(questions)} Questions\n" +  # Highlight loaded questions in green
    Fore.CYAN + "Change the delay from config.json\n" +  # Change delay info in cyan
    Style.RESET_ALL  # Reset color and style at the end
)
   while True:
    username = input(f"[~] Enter username {Fore.GREEN}({lastUsername if lastUsername else 'None'}){Style.RESET_ALL}: ").strip()
    if username:
       saveData("lastUsername",username)
       break
    elif not username and lastUsername:
      username = lastUsername
      break
    Console.Logger("Username cannot be empty. Please enter a valid username", status="y")
   while True:
     messagecount = input(f"[~] Enter message count {Fore.GREEN}({lastCount}){Style.RESET_ALL}: ")
     if messagecount.isdigit():
       messagecount = max(int(messagecount),1)
       saveData("lastCount", messagecount)
       break
     elif not messagecount:
       messagecount = int(lastCount)
       break
     else:
       Console.Logger("Invalid input. Please enter a valid integer", status="y")
   while True:
    randomQuestion = False
    Console.Logger(f"{Fore.GREEN}Press enter for random questions{Style.RESET_ALL}", status="y")
    message = input("[~] Enter message: ").strip()
    if message:
       break
    elif not message and questions:
       randomQuestion = True
       break
    Console.Logger("Message cannot be empty", status="y")
   print()
   with ThreadPoolExecutor(max_workers=messagecount) as executor:
     for x in range(messagecount):
       message = random.choice(questions) if randomQuestion else message
       executor.submit(main, username, message, deviceid(),randomQuestion)
       time.sleep(delay)
   print()
   Console.Logger(f"Sent {sent} messages to {username} | {errored} Errored messages", status="y")

if __name__ == "__main__":
   Main()