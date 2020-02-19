#!/usr/bin/python3
""" HBNB Console """
import cmd

class HBNBCommand(cmd.Cmd):
    """ Class HBNB """
    prompt = "(hbnb) "

    def do_quit(self, inp):
        """Quit command"""
        return True

    def do_EOF(self, inp):
        """End OF FILE"""
        return True

    def emptyline(self):
        """ Nothing when an empty line occurs """
        pass