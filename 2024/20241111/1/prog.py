class Omnibus:
    attr_count = dict()

    def __setattr__(self, attr, val):
        if not attr.startswith("_"):
            if attr in Omnibus.attr_count:
                Omnibus.attr_count[attr] += 1
            else:
                Omnibus.attr_count[attr] = 1
        
    def __delattr__(self, attr):
        if not attr.startswith("_"):
            if attr in Omnibus.attr_count:
                Omnibus.attr_count[attr] -= 1
                if Omnibus.attr_count[attr] == 0:
                    del Omnibus.attr_count[attr]
        
    def __getattr__(self, attr):
        return Omnibus.attr_count.get(attr, 0)

import sys
exec(sys.stdin.read())
