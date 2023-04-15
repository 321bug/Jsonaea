"""jsonaea的实用库，内含多种不必要但减少代码量的函数\n
使用前先设置arcJson字典`jsonaea.Tools.arcJson = ...`"""
from math import *
from enum import Enum
#Tools子库 
arcJson = ...

class easing(Enum):
    s = ("s","s")
    b = ("b","b")
    si = ("si","s")
    so = ("so","s")
    sisi = ("si","si")
    siso = ("si","so")
    sosi = ("so","si")
    soso = ("so","so")

def sort(oldJson:list) -> list:
    '''对列表字典进行时间排序'''
    newList,newJson = [],[]
    for index,i in enumerate(oldJson):
        try:
            #print(index,i,oldJson)
            newList.append([i["time"],index])
        except:
            newList.append([i["startTime"],index])
    newList = sorted(newList, key=lambda x:x[0])
    for i in newList:
        newJson.append(oldJson[i[1]])
    return newJson

class math():
    def straight(x):
        '计算straight(s)函数'
        return x
    def sineIn(x):
        '计算sineIn(si)函数'
        return (2*asin(x))/pi
    def sineOut(x):
        '计算sineOut(so)函数'
        return (2*asin(x-1))/pi+1
    def bezier(x):
        '计算bezier(x)函数'
        return 3 * (1 - x) * pow(x, 2) + pow(x, 3)

#EventSubject = [timingGroup,class,index]
def getEventSubject(EventSubject:list) -> dict:
    if EventSubject[0] >= 0:
        return arcJson["TimingList"][EventSubject[0]][EventSubject[1]][EventSubject[2]]
    else:
        return arcJson[EventSubject[1]][EventSubject[2]]

def cal_arc_pos(EventSubject:list, time:int, precision:int=1) -> list:
    '计算arc变换中的坐标'
    event = getEventSubject(EventSubject)
    if event["type"] != "arc":
        raise ValueError("note事件类型不为arc")
    if not(event["startTime"] <= time <= event["endTime"]):
        raise ValueError("参数time不在arc的开始时间和结束时间范围之内")
    percent = (time - event["startTime"])/(event["endTime"] - event["startTime"])
    arcType = easing[event["arcType"]].value
    distanceXY = [event["endPos"][0] - event["startPos"][0], event["endPos"][1] - event["startPos"][1]]
    posList = []
    for i in [0,1]:
        if arcType[i] == "s":
            y = math.straight(percent)
        if arcType[i] == "b":
            y = math.bezier(percent)
        if arcType[i] == "si":
            y = math.sineIn(percent)
        if arcType[i] == "so":
            y = math.sineOut(percent)  
        posList.append(round(event["startPos"][i]+distanceXY[i]*y,precision))
    return posList
