# erase black pixels to transparent
import os,sys,datetime
from PIL import Image

if getattr(sys, 'frozen', False):
    mydir = os.path.dirname(sys.executable)
elif __file__:
    mydir = os.path.dirname(os.path.abspath(__file__))

print("------------mydir------------")
print(mydir)
print("------------------------")
maskdir = mydir+os.sep+"mask"+os.sep
print("new files will be placed inside ",maskdir, "path")
print("------------------------")

def pv(x):
    """parse string to int value between 0...255"""
    v = int(x) or 255
    if (v<0) : v=-v
    if (v>255) : v=255
    return v
    
def black(r,g,b,a):
    return r==_r and g==_g and b==_b and a==_a

_r,_g,_b,_a=0,0,0,255 #black


print("black pixels will transparent")
try:
    print(datetime.datetime.now().time())
    print("------------------ beginning ----------------------")
    fnames=[]
    for file in os.listdir(mydir):
        if file.endswith(".png"):
            fnames+=[file]
    print(fnames)
    
    if len(fnames) > 0:
        if not os.path.exists(maskdir):
            os.makedirs(maskdir)
    
    for fname in fnames:

        adres=mydir+os.sep+fname
        print(adres)
        im = Image.open(adres).convert('RGBA')
        im.load()
        w,h=im.size
        w=range(w)
        h=range(h)

        R=list(im.getdata(0))
        G=list(im.getdata(1))
        B=list(im.getdata(2))
        alp=list(im.getdata(3)) #alpha tuple 0...255 кортеж прозрачности пикселей
        newalp=[]
        for i in list(range(len(alp))):
            if black(R[i], G[i], B[i], alp[i]):
                r = 0; g=0 ; b=0; a=0
            else:
                r=R[i]; g=G[i]; b=B[i]; a=alp[i]
            newalp.append((r,g,b,a))

        print("recount complete")
        print(datetime.datetime.now().time())
        print("------------------ V ----------------------")
        im.putdata(newalp)
        print("load image data complete")
        print(datetime.datetime.now().time())
        print("------------------ V ----------------------")
        # im.save("_"+fname)
        im.save(maskdir+fname)
        print("save image complete")
        print(datetime.datetime.now().time())
        print("------------------ V ----------------------")

except:
    print(sys.exc_info())
input("done (готово) . That close press Enter (enter - закрыть)")
