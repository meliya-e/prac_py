from itertools import islice
from itertools import dropwhile

print(islice(dropwhile(lambda x: x<=1.6, f()), 10))
