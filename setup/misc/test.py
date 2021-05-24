try:
    import MyPython.testyboi
    MyPython.testyboi.test()
except Exception as e:
    print(e)
    print("\nimport failed\n")

import sys

print(sys.path)

