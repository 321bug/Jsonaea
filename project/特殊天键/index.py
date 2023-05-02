import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
from jsonaea import *
import os

root = tk.Tk()
root.withdraw () 
#musicPath = filedialog.askopenfilename (title="加载音乐")     有点问题先不用了
arcPath = filedialog.askopenfilename (title="加载铺面") 
musicPath = "E:\project\项目4：特殊天键作铺\\1s.mp3"
print("     看这里：",musicPath)
print(os.getcwd()+"\\musicClips\\")
try:os.makedirs(os.getcwd()+"\\musicClips\\")
except:pass

arcdict = load(arcPath)
Tools.arcJson = arcdict
allarc = Tools.searchEventSubject({"type":"arc"})
arctaplist = []

for index,i in enumerate(allarc):
    arcevent = Tools.getEventSubject(i)
    if not "arctap" in arcevent:
        continue
    for time in arcevent["arctap"]:
        arctaplist.append([i,time])
    Tools.changeEvent(i,removeKey=["arctap"])
arctaplist = sorted(arctaplist,key=lambda x:x[1])
_id,index = 0,-1

clip = AudioSegment.from_mp3(musicPath)
for es,time in arctaplist:
    index += 1
    try:arctaplist[index+1]
    except:
        arctaplist[index].append(_name)
        continue
    if arctaplist[index+1][1] - time <= 0:
        arctaplist[index].append(_name)
        continue
    _name = "clip%03d.mp3"%_id
    #clip[time:arctaplist[index+1][1]].export("musicClips\\"+_name)
    arctaplist[index].append(_name)
    print("已完成:",_name)
    _id += 1

createJson(arctaplist, "./arctaplist.json")
for es,time,name in arctaplist:
    pos = Tools.cal_arc_pos(es,time,2)
    event = {
        "type":"arc",
        "startTime":time,
        "endTime":time+1,
        "startPos":pos,
        "endPos":pos,
        "arcType":"s",
        "color":"blue",
        "hitsound":name,
        "IsSkyline":True,
        "arctap":[time]
    }
    arcdict["TimingList"][es[0]]["notes"].append(event)

#dellist = Tools.searchEventSubject({"class":"notes"})
#for index,i in enumerate(dellist):
#    event = Tools.getEventSubject(i)
#    if "arctap" in event:
#        continue
#    Tools.changeEvent(i,uploadDict={"IsCreate":False})
output(arcdict,"./3.aff")