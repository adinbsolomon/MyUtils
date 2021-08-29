
import inspect

def func_name(frame_num=0):
    return inspect.getouterframes(inspect.currentframe())[frame_num+1].function
