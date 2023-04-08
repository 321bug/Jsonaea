"""jsonaea的实用库，内含多种不必要但减少代码量的函数\n
使用前先设置arcJson字典`jsonaea.Tools.arcJson = x`"""
#Tools子库 
def __init__(self,arcJson) -> None:
    self.arcJson = arcJson

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
