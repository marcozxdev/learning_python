



import json
import os




def add(args):
    print("\n".join(args))


def mark_done(args):
    pass


def mark_in_progress(args):
    pass


def list():
    pass


def list_done():
    pass


def list_in_progress():
    pass



commands = {
    "add": add,
    "mark-done": mark_done,
    "mark-progress": mark_in_progress,
    "list": list,
    "list-done": list_done,
    "list-in-progress": list_in_progress
}


def menu():

    while True:    
        print("Bienvenido a Task Traker")
        print("Que desea hacer?")
        print("add <task>")
        print("mark-done <ID>")
        print("mark-in-progress <ID>")
        print("list")
        print("list-done")
        print("list-in-progress")
        print("exit")

        opc = input('task-cli ')
        

        if not opc:
            print("please write")

        if opc == "exit":
            print("bye...")
            break

        # logica de ejecutar comandos

        parts = opc.split()

        if not parts:
            continue

        comando = parts[0]
        arguments = parts[1:]

        if comando in commands:
            commands[comando](arguments)
        else:
            print("error command ")











menu()






























