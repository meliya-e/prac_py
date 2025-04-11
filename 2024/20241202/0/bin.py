import struct
import sys
res = ((0.1, [1,2,3], 11), (0.2, [2,3,4], 12), (0.3, [3,4,5], 13))
with open("binary", "wb") as f:
    f.write(struct.pack("=f3sif3sif3si", 0.1, bytes([1,2,3]), 11, 0.2, bytes([2,3,4]), 12, 0.3, bytes([3,4,5]), 13))

with open(sys.argv[1], "rb") as f:
    while reco := f.resd(struct.calcsize("!f3si")):
        f, b, i = struct.unpack("!f3si", reco)
        print(f, b, i))
