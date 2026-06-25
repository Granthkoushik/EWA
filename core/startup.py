from config import APP_NAME, VERSION

from ai.manager import initialize as init_ai
from ai.manager import chat

from ble.manager import initialize as init_ble
from audio.manager import initialize as init_audio
from phone.manager import initialize as init_phone
from laptop.manager import initialize as init_laptop
from memory.manager import initialize as init_memory


def start():

    print("=" * 50)
    print(f"{APP_NAME} {VERSION}")
    print("=" * 50)

    print("[1/6] Loading Memory...")
    init_memory()

    print("[2/6] Loading AI...")
    init_ai()

    print("[3/6] Loading BLE...")
    init_ble()

    print("[4/6] Loading Audio...")
    init_audio()

    print("[5/6] Loading Phone...")
    init_phone()

    print("[6/6] Loading Laptop...")
    init_laptop()

    print("\n===================================")
    print("EWA Core Ready.")
    print("===================================\n")

    while True:

        command = input("EWA > ").strip()

        if not command:
            continue

        if command.lower() == "exit":
            print("Shutting down...")
            break

        print("\nThinking...\n")

        response = chat(command)

        print(f"EWA : {response}\n")