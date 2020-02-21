#!/usr/bin/python3
""" HBNB Console """
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Class HBNB """

    prompt = "(hbnb) "
    mycl = {"BaseModel",
               "User",
               "State",
               "City",
               "Amenity",
               "Place",
               "Review"}

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
            return
        if inp not in self.mycl:
            print("** class doesn't exist **")
            return
        else:
            obj = eval(inp)
            print(obj.id)
            storage.save()

    def do_show(self, inp):
        """ Shows the string representation of an instance """
        arg = inp.split()
        if not arg:
            print("** class name missing **")
            return
        elif arg[0] not in self.mycl:
            print("** class doesn't exist **")
            return
        elif len(arg) < 2:
            print("** instance id missing **")
            return
        obj = storage.all()
        for v in obj.values():
            if v.__class__.__name__ == arg[0] and v.id == arg[1]:
                print(v)
                return
        print("** no instance found **")

    def do_destroy(self, inp):
        """Command to Destroy an instance"""
        arg = inp.split()
        if not arg:
            print("** class name missing **")
            return
        elif arg[0] not in self.mycl:
            print("** class doesn't exist **")
            return
        elif len(arg) == 1:
            print("** instance id missing **")
            return
        obj = storage.all()
        k = arg[0] + "." + arg[1]
        if k in obj:
            storage.delete(k)
            storage.save()
            return
        print("** no instance found **")

    def do_all(self, inp):
        """Shows all the instances"""
        inst = storage.all()
        list = []
        if inp:
            try:
                Model = inp.split(" ")[0]
                if Model in self.mycl:
                    for i in inst:
                        if i.split(".")[0] == Model:
                            list.append(str(inst[i]))
                    print(list)
                else:
                    raise NameError
            except NameError:
                print("** class doesn't exist **")
        else:
            for i in inst:
                list.append(str(inst[i]))
            print(list)
    


if __name__ == '__main__':
    HBNBCommand().cmdloop()
