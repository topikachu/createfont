# -*- coding: utf-8 -*-  
import Image
import ImageDraw
import ImageFont
import XbmImagePlugin
import codecs,sys
#pix:pSund
fontSizeMap={8:6.5,10:7.5,12:9,14:10.5,16:12,18:14,20:15,21:16,24:18,29:22,32:24,34:26,48:36,56:42}
fontpix=12
alignedFontWidth=((fontpix-1)/8+1)*8
fontSize=fontSizeMap[fontpix]
fontStartPos=0x4e00
fontEndPos=0x9FFF
nFont=fontEndPos-fontStartPos
numPerLine=64
imageWidth=alignedFontWidth*numPerLine
imageHeight=fontpix*((nFont-1)/numPerLine+1)
print "image widht %d, height %d" %(imageWidth,imageHeight)
image = Image.new("1", (imageWidth,imageHeight),1)
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("WenQuanYi Micro Hei.ttf", fontSize)
for point in xrange(fontStartPos,fontEndPos):
    char=unichr(point)
    x=(point-fontStartPos) % numPerLine *alignedFontWidth
    y=(point-fontStartPos)/numPerLine*fontpix    
    draw.text((x, y), char, 0, font=font)
    print (point,x,y)
image.save('font.xbm' )
image.save('font.bmp' )

