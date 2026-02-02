"""
Function Dispatch Router

Routes user commands to their
corresponding actions
"""

def status():
    print("System Status: All systems operational")

def reset():
    print("System Reset Complete")

def shutdown():
    print("System Shutting Down...")

def help_menu():
    print("Available commands: status, reset, shutdown, help")

commands = {
    "status": status,
    "reset": reset,
    "shutdown": shutdown,
    "help": help_menu
}

def route_command(cmd):
    action = commands.get(cmd)
    if not action:
        print("Invalid Command")
        return
    action()

cmd = input("Enter command: ").strip().lower()
route_command(cmd)