class Num:
    def __init__(self):
        self.vals = {}

    def __get__(self, obj, cls):
        return self.vals.get(obj, 0)

    def __set__(self, obj, val):
        if hasattr(val, "real"):
            self.vals[obj] = val.real
        elif hasattr(val, "__len__"):
            self.vals[obj] = len(val)
  #  def __delete__(self, obj):
   #     self.obj = 0

import sys
exec(sys.stdin.read())
