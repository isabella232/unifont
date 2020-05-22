# convert hex file from unicode official site to html code
import os,sys,datetime

if getattr(sys, 'frozen', False):
    mydir = os.path.dirname(sys.executable)
elif __file__:
    mydir = os.path.dirname(os.path.abspath(__file__))

def hexToHtml(s:str):
    hex = s.split(":",1)[0]
    return "\n&#x" + hex + ";" if len(hex)>0 else ""

print("------------mydir------------")
print(mydir)
print("------------------------")
maskdir = mydir+os.sep+"hexHtmlTxt"+os.sep
print("new files will be placed inside ",maskdir, "path")
print("------------------------")
input("cut official site downloaded unicode-***.hex file tails and collect new text file with similar html")
try:
    print(datetime.datetime.now().time())
    print("------------------ beginning ----------------------")
    fnames=[]
    for file in os.listdir(mydir):
        if file.endswith(".hex"):
            fnames+=[file]
    print(fnames)
    
    if len(fnames) > 0:
        if not os.path.exists(maskdir):
            os.makedirs(maskdir)
    
    for fname in fnames:

        adres=mydir+os.sep+fname
        print(adres)
        file = open(maskdir+fname.split(".hex")[0]+".txt","w")
        with open(adres) as f:
            breaker = 0
            for line in f:
                file.write(hexToHtml(line))
                breaker += 1
                if breaker >99:
                    breaker = 0
                    file.write("\n<br>") # that copy past html screen to txt comfort for txt editor
                
        file.close()
        print("recount complete")
        print(datetime.datetime.now().time())
        print("------------------ V ----------------------")
        
except:
    print(sys.exc_info())
input("done (готово) . That close press Enter (enter - закрыть)")
