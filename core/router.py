from skills import time
from skills import battery
from skills import weather
from skills import phone
from skills import laptop

from ollama import ask


def process(command):

    cmd = command.lower().strip()

    if cmd == "time":
        return time.handle()

    elif cmd == "battery":
        return battery.handle()

    elif cmd == "weather":
        return weather.handle()

    elif cmd.startswith("phone"):
        return phone.handle(command)

    elif cmd.startswith("laptop"):
        return laptop.handle(command)

    else:
        return ask(command)