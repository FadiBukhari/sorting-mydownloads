import os;
import time;
from pathlib import Path
import shutil
while(1):
  p=input("Enter Path to sort: ").replace('\\','/')
  if not os.path.exists(p):
    print("Wrong Path, try again!")
  else: os.chdir(p); break;
if not os.path.exists("Word"):
  os.mkdir("Word");
if not os.path.exists("Images"):
  os.mkdir("Images");
if not os.path.exists("Torrents"):
  os.mkdir("Torrents");
if not os.path.exists("Excel"):
  os.mkdir("Excel");
if not os.path.exists("PDF"):
  os.mkdir("PDF");
if not os.path.exists("PowerPoint"):
  os.mkdir("PowerPoint");
if not os.path.exists("Compressed"):
  os.mkdir("Compressed");
if not os.path.exists("Jar"):
  os.mkdir("Jar");
if not os.path.exists("Videos"):
  os.mkdir("Videos");
if not os.path.exists("Sounds"):
  os.mkdir("Sounds");
if not os.path.exists("Executables"):
  os.mkdir("Executables");

images = [".png" , ".jpg" , "jpng" , ".jfif" , ".wepmp"]

def isimage(e):
  return e in images
path =p;
for file in os.listdir():
  # file.rename("sdafasd.exe") rename file
  name , ext = os.path.splitext(file)
  ext=ext.lower();
  
  if isimage(ext):
    if os.path.isfile(path+"/Images"+'/'+file):
      os.remove(path+"/Images"+'/'+file)
    else: shutil.move(file,"Images");
  
  elif ext ==".torrent":
    if os.path.isfile(path+"/Torrents"+'/'+file):
      os.remove(path+"/Torrents"+'/'+file)
    else: shutil.move(file,"Torrents");
  
  elif ext ==".docx" or ext==".doc":
    if os.path.isfile(path+"/Word"+'/'+file):
      os.remove(path+"/Word"+'/'+file)
    else: shutil.move(file,"Word"); 
  
  elif ext ==".xlsx":
    if os.path.isfile(path+"/Excel"+'/'+file):
      os.remove(path+"/Excel"+'/'+file)
    else: shutil.move(file,"Excel"); 
  
  elif ext ==".pdf":
    if os.path.isfile(path+"/PDF"+'/'+file):
      os.remove(path+"/PDF"+'/'+file)
    else: shutil.move(file,"PDF"); 
  
  elif ext ==".ppt" or ext==".ppsx" or ext==".pptx":
    if os.path.isfile(path+"/PowerPoint"+'/'+file):
      os.remove(path+"/PowerPoint"+'/'+file)
    else: shutil.move(file,"PowerPoint"); 
  
  elif ext ==".zip" or ext==".rar":
    if os.path.isfile(path+"/Compressed"+'/'+file):
      os.remove(path+"/Compressed"+'/'+file)
    else: shutil.move(file,"Compressed");
  
  elif ext ==".jar":
    if os.path.isfile(path+"/Jar"+'/'+file):
      os.remove(path+"/Jar"+'/'+file)
    else: shutil.move(file,"Jar");
  
  elif ext ==".mp4":
    if os.path.isfile(path+"/Videos"+'/'+file):
      os.remove(path+"/Videos"+'/'+file)
    else: shutil.move(file,"Videos");
  
  elif ext ==".mp3" or ext==".mpeg" or ext==".m4a":
    if os.path.isfile(path+"/Sounds"+'/'+file):
      os.remove(path+"/Sounds"+'/'+file)
    else: shutil.move(file,"Sounds");
  
  elif ext ==".exe":
    if os.path.isfile(path+"/Executables"+'/'+file):
      os.remove(path+"/Executables"+'/'+file)
    else: shutil.move(file,"Executables");


print("Sorted Successfully")
time.sleep(5);
# shutil.rmtree("data") remove file called data