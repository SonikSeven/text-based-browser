import os
import sys
import requests

from collections import deque
from bs4 import BeautifulSoup
from colorama import Fore


if not os.access(sys.argv[1], os.F_OK):
    os.mkdir(sys.argv[1])
os.chdir(sys.argv[1])
journal = deque()

while True:
    command = input()

    if command in os.listdir():
        with open(command, encoding="utf-8") as article_file:
            print(article_file.read())
        continue
    elif command == "back":
        if len(journal) > 1:
            journal.pop()
            print(journal.pop())
        continue
    elif command == "exit":
        os.chdir(os.path.dirname(os.getcwd()))
        break

    command = "https://" + command.lstrip("https://")

    try:
        soup = BeautifulSoup(requests.get(command).content, 'html.parser')
    except requests.exceptions.ConnectionError:
        print("Error! Incorrect URL!")
        continue

    result = ""
    for i in soup.find_all(("p", "h1", "h2", "h3", "h4", "h5", "h6", "a", "ul", "ol", "li")):
        j = i.text.strip()
        if j:
            if i.name == "a":
                result += "".join(("\n" + Fore.BLUE, j, Fore.RESET))
            else:
                result += "\n" + j

    print(result)
    file_name = command.split(".")[1]
    with open(file_name, "w", encoding="utf-8") as article_file:
        print(result, file=article_file)
    journal.append(result)
