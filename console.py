#!/usr/bin/python3
""" HBNB Console """
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Class HBNB """
    prompt = "(hbnb) "

    def emptyline(self):
        """ Nothing when an empty line occurs """
        pass

    def do_quit(self, inp):
        """Quit command"""
        return True

    def do_EOF(self, inp):
        """End OF FILE"""
        return True

    def do_create(self, inp):
        """ Create New Instance of BaseModel """
        if not inp:
            print("** class name missing **")
        for key in self.__class__.__name__:
            if key not in self.__class__.__name__:
                print("** class doesn't exist **")
            
        myclass = BaseModel()
        myclass.save()
        print(myclass.id)

    def do_show(self, inp):
        """ Shows the string representation of an instance """



if __name__ == '__main__':
    HBNBCommand().cmdloop()
