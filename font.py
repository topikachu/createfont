# -*- coding: utf-8 -*-  
import Image
import ImageDraw
import ImageFont
import XbmImagePlugin
import codecs,sys

fontsize=9
fontStartPos=0x4e00
fontEndPos=0x9FFF
nFont=fontEndPos-fontStartPos
numPerLine=64
imageWidth=12*numPerLine
imageHeight=12*((nFont-1)/numPerLine+1)
print "image widht %d, height %d" %(imageWidth,imageHeight)
image = Image.new("1", (imageWidth,imageHeight),1)
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("WenQuanYi Micro Hei.ttf", fontsize)
for point in xrange(fontStartPos,fontEndPos):
    char=unichr(point)
    x=(point-fontStartPos) % numPerLine *12
    y=(point-fontStartPos)/numPerLine*12    
    draw.text((x, y), char, 0, font=font)
    #print (point,x,y)
image.save('font.xbm' )
image.save('font.bmp' )