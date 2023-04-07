***Jsonaea*** *script by* ***Begloon.***  
***version***:b230402
# 简介
**Jsonaea**为可将Arcaea游戏中铺面文件（``x.aff``）转换为json文件 / 字典，亦可将json文件 / 字典转换回铺面文件的实用库。  
其理论上可读取并转换aff文件中的任何语句（目前除注释外），并无损地将其互相转换。  
此库使用``Python``编写。  
此库还有一个``Tools``附加库，内含多种不必要但减少代码量的实用函数。

## 快速使用
首先从PyPi上安装jsonaea：  
```
pip install jsonaea  
```
如需要也可在github本项目上直接下载后手动安装。

---
在py文件中导入库：  
```python
import jsonaea
```
---
使用load函数生成json文件 / 字典：
```python
jsonaea.load(arcPath,IsCreateJson,JsonPath)
```
``arcPath``: Arcaea铺面文件导入路径  
``IsCreateJson``: 是否导出json文件，使用json库辅助导出  
``JsonPath``: 如果导出json文件（``IsCreateJson=True``），设置导出的json文件路径  
此函数将返回一个字典。

---
导出生成的json文件 / 字典为``.aff``文件：
```python
jsonaea.output(arcJson,arcPath)
```
``arcJson``: 提供的json文件（字典）  
``arcPath``: Arcaea铺面文件导出路径  
此函数不返回值，会创建一个``.aff``文件。

### 示例
jsonaea库使用的具体示例，以下代码可将铺面中的arc全部转化为蛇：  
```python
import jsonaea
import tkinter as tk
from tkinter import filedialog

#生成铺面导入窗口
root = tk.Tk()
root.withdraw () 
arcPath = filedialog.askopenfilename () 

#导入铺面
J = jsonaea.load(arcPath,IsCreateJson=True,JsonPath="./this.json")

#处理铺面
for i1,tl in enumerate(J["TimingList"]):
    #遍历该timinggroup中的所有note
    for i2,note in enumerate(tl["notes"]):
        #判断该note是否为arc
        if note["type"] == "arc":
            #将该arc改为蛇
            J["TimingList"][i1]["notes"][i2]["IsSkyline"] = False

#导出铺面
jsonaea.output(J,"./this.aff")
input("已完成")
```

# json文件 / 字典格式
```json
{
  "META":{},
  "Camera":[],
  "Scenecontrol":[],
  "TimingList":[
    {
      "tags":[],
      "notes":[],
      "timing":[],
    }
  ]
}
```
- META字典：  
  存储铺面文件头，如:
  ```json
  "AudioOffset": 0,
  "TimingPointDensityFactor":2
  ```
- Camera列表：  
  存储铺面摄像头信息，如：
  ```json
  "time": 0,
  "transverse": 0.0,
  "bottomzoom": 0.0,
  "linezoom": 0.0,
  "steadyangle": 0.0,
  "topzoom": 0.0,
  "angle": 0.0,
  "easing": "reset",
  "lastingtime": 1
  ```
  详见 [ARCAEA中文维基](https://wiki.arcaea.cn/) 中对谱面格式的介绍  
  多个字典以列表形式存储
