import sys

s = sys.stdin.buffer.read(44)

if s[0:4] == b"RIFF" and s[8:12] == b"WAVE" and s[36:40] == b"data":
    size = int.from_bytes(s[4:8], byteorder='little')
    format_type = int.from_bytes(s[20:22], byteorder='little')
    channels = int.from_bytes(s[22:24], byteorder='little')
    rate = int.from_bytes(s[24:28], byteorder='little')
    bits_per_sample = int.from_bytes(s[34:36], byteorder='little')
    data_size = int.from_bytes(s[40:44], byteorder='little')

    print(f"Size={size}, Type={format_type}, Channels={channels}, Rate={rate}, Bits={bits_per_sample}, Data size={data_size}")
else:
    print("NO")
