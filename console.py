#!/usr/bin/python3
""" A module for the entry point of the command interpreter """
import cmd
import sys
# from models import storage
# from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ The command interpreter class inheriting from the `Cmd` class """
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    def do_quit(self, command):
        """ Method to exit the console """
        exit()

    def do_EOF(self, command):
        """ Method to handle EOF """
        print()
        exit()

    def emptyline(self):
        """ Do nothing for empty command """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
