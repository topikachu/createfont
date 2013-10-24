
import struct
mapping=file("mapping","wb")
for zone in xrange(0x81,0xFE+1):
    for bit in xrange(0x40,0xFE+1):
        if bit==0x7F:
            continue
        try:
          b=bytearray(2)
          b[0] = zone
          b[1] = bit
          s = b.decode("gb18030")
          
          if len(s)!=1:
              s=""
        except:
            s=""
        if s=="":
            u= 0
        else:
            u =ord(s)
        mapping.write(struct.pack("<H",u))
mapping.close

