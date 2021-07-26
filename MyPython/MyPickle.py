
import os
import pickle
from typing import TypeVar, Type

class MyPicklingException(Exception): pass
class Pickler:
    AnyType = TypeVar('AnyType')
    def __init__(self, path) -> None:
        self.path = path
    def pickle(self, object, validate=False) -> None:
        if validate and not is_picklable(object): raise MyPicklingException("This object is not picklable!")
        outfile = open(self.path, 'wb')
        pickle.dump(object, outfile)
        outfile.close()
    def unpickle(self) -> Type[AnyType]:
        infile = open(self.path, 'rb')
        temp = pickle.load(infile)
        infile.close()
        return temp
    def remove_file(self):
        if os.path.isfile(self.path):
            os.remove(self.path)
        else:
            raise MyPicklingException("This pickler's file was never initialized here!")

IS_PICKLABLE_PATH = os.path.expanduser("~") + os.path.sep + 'ispicklabletempfile'
def is_picklable(object) -> bool: # This function has a lot of overhead!
    p = Pickler(IS_PICKLABLE_PATH)
    try:
        p.pickle(object)
        temp = p.unpickle()
        return temp == object
    except: return False


        