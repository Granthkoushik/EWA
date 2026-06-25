from router import process

print("===== AVATAR =====")

while True:

    command = input("You : ")

    if command.lower() == "exit":
        break

    reply = process(command)

    print("\nAVATAR :", reply)