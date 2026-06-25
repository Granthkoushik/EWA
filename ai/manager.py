from ai.ollama_client import ask


def initialize():
    print("   AI Manager Ready")


def shutdown():
    print("   AI Manager Shutdown")


def status():
    return "READY"


def chat(prompt: str) -> str:
    return ask(prompt)