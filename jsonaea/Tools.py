"""jsonaea的实用库，内含多种不必要但减少代码量的函数\n
使用前先设置arcJson字典`jsonaea.Tools.arcJson = ...`"""
from math import *
from enum import Enum
import copy
#Tools子库 
arcJson = ...
__all__ = ["sort","math","getEventSubject","cal_arc_pos","searchEventSubject","getAllEvent","changeEvent"]

class easing(Enum):
    s = ("s","s")
    b = ("b","b")
    si = ("si","s")
    so = ("so","s")
    sisi = ("si","si")
    siso = ("si","so")
    sosi = ("so","si")
    soso = ("so","so")

ESindex = {
    "timingGroup":0,
    "class":1,
    "index":2
}

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
    __all__ = ["straight","sineIn","sineOut","bezier"]
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

def searchEventSubject(RetrieveDict:dict) -> list:
    """
    通过条件字典来检索所有可能的`EventSubject`\n
    并返回`[[...],[...],...]`\n
    如果未检出任何一个`EventSubject`，即返回`None`
    """
    AllEvent = getAllEvent()
    EventSubject = []
    nowEvent = AllEvent
    for i in RetrieveDict:
        EventSubject.clear()
        for event in nowEvent:
            if i in event[0] and event[0][i] == RetrieveDict[i]:
                EventSubject.append(event)
            elif i in ["timingGroup","class","index"] and event[1][ESindex[i]] == RetrieveDict[i]:
                    EventSubject.append(event)
            else:
                try:EventSubject.remove(event)
                except:pass
        nowEvent = copy.deepcopy(EventSubject)
    if EventSubject == []:
        return None
    else:
        return [e[1] for e in EventSubject]              

def getAllEvent() -> list:
    '索取铺面所有事件'
    allEvent = []
    list1 = [arcJson["Camera"],arcJson["Scenecontrol"],"Camera","Scenecontrol"]
    for index0,list0 in enumerate(list1):
        if index0 == 2:
            break
        for index,i in enumerate(list0):
            allEvent.append([i,[-1,list1[index0+2],index]])
    for indexN,listN in enumerate(arcJson["TimingList"]):
        for listT in ["notes","timing"]:
            for index,i in enumerate(listN[listT]):
                allEvent.append([i,[indexN,listT,index]])
    return allEvent

def changeEvent(EventSubject,uploadDict={},removeDict={}):
    "通过`EventSubject`来更改事件的函数"
    event = getEventSubject(EventSubject)
    event.update(uploadDict)
    if not removeDict == {}:
        event.pop([(a,b) for a,b in list(removeDict.items())])
    if EventSubject[0] == -1:
        del ([EventSubject[1]])[EventSubject[2]]
        arcJson[EventSubject[1]].insert(EventSubject[2],event)
    else:
        del (arcJson["TimingList"][EventSubject[0]][EventSubject[1]])[EventSubject[2]]
        arcJson["TimingList"][EventSubject[0]][EventSubject[1]].insert(EventSubject[2],event)
