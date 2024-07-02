#!/usr/bin/python3
"""a program contains the entry point of the command interpreter"""

import cmd
import json
import re


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


if __name__ == '__main__':
    SHEENCommand().cmdloop()