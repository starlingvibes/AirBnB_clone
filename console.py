#!/usr/bin/python3
""" A module for the entry point of the command interpreter """
import cmd
import sys
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ The command interpreter class inheriting from the `Cmd` class """
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = {'BaseModel': BaseModel}

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

    def do_create(self, args):
        """ Creates and saves a new instance of BaseModel to JSON file"""
        if not args:
            print("** class name missing **")
            return
        elif args not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[args]()
        storage.save()
        print(new_instance.id)
        storage.save()

    def do_show(self, args):
        """ Prints the string representation of an instance based on class name """
        # Splitting the multiple arguments
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]

        # handling extra spaces
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id
        try:
            print(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """ Deletes an instance based on class name and id, writing the change into a JSON file """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]

        if c_id and ' ' in c_id:
            c_id = c_id.partition(" ")[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id
        try:
            del(storage.all()[key])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, args):
        """ Prints the string representation of all instances based or not on the class name """
        print_list = []

        if args:
            # remove trailing arguments
            args = args.split(" ")[0]
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for key, value in storage._FileStorage__objects.items():
                if k.split(".")[0] == args:
                    print_list.append(str(value))
        else:
            for key, value in storage._FileStorage__objects.items():
                print_list.append(str(value))

        print(print_list)

    def do_update(self, args):
        """
        updates an instance based on class name and id by adding or updating attributes (whilst saving changes into the JSON file
        """
        c_name = c_id = att_name = att_val = kwargs = ''

        # isolating cls from id/args; ex: (<cls>, delimiter, <id/args>)
        args = args.partition(" ")
        if args[0]:
            c_name = args[0]
        # if class name isn't present
        else:
            print("** class name missing **")
            return
        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        # isolating id from rest of args
        args = args[2].partition(" ")
        if args[0]:
            c_id = args[0]
        # if id isn't present
        else:
            print("** instance id missing **")
            return

        # generating key from class name and id
        key = c_name + "." + c_id

        # determine if key is present
        if key not in storage.all():
            print("** no instance found **")
            return


if __name__ == "__main__":
    HBNBCommand().cmdloop()
