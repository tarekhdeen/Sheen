#!/usr/bin/python3
"""a program contains the entry point of the command interpreter"""

import cmd
import json
import re
import app.models
from app.models import storage
from app.models.base_model import BaseModel
from app.models.appointment import Appointment
from app.models.clinic import Clinic
from app.models.doctor import Doctor
from app.models.patient import Patient
from app.models.procedure import Procedure
from app.models.user import User


class SHEENCommand(cmd.Cmd):
    """a class for command interpreter"""
    prompt = "(sheen) "

    def do_EOF(self, line):
        """EOF to exit the program"""
        print()
        return True

    def do_quit(self, line):
        """quit to exit the program"""
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass
    
    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it and prints the id"""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        
        class_name = args[0]
        class_attrs = {}
        
        for attr in args[1:]:
            key_value = attr.split("=")
            if len(key_value) == 2:
                key, value = key_value
                class_attrs[key] = value.strip('"')
        
        try:
            cls = globals()[class_name]
        except KeyError:
            print("** class doesn't exist **")
            return
        
        new_instance = cls(**class_attrs)
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance based on the class name and id"""
        args = args.split()
        if len(args) < 2:
            print("** class name or id missing **")
            return
        try:
            key = f"{args[0]}.{args[1]}"
            obj = storage.all()[key]
            print(obj)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        args = args.split()
        if len(args) < 2:
            print("** class name or id missing **")
            return
        try:
            key = f"{args[0]}.{args[1]}"
            del storage.all()[key]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances based on the class name"""
        if not args:
            print([str(obj) for obj in storage.all().values()])
        else:
            try:
                cls = eval(args)
                print([str(obj) for obj in storage.all().values() if isinstance(obj, cls)])
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        args = args.split()
        if len(args) < 4:
            print("** class name, id, attribute name or value missing **")
            return
        try:
            key = f"{args[0]}.{args[1]}"
            obj = storage.all()[key]
            setattr(obj, args[2], args[3])
            obj.save()
        except KeyError:
            print("** no instance found **")

if __name__ == '__main__':
    SHEENCommand().cmdloop()