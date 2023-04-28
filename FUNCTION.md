**此页面介绍Jsonaea当前版本的所有函数、全局变量以及对象。**  
## 主库
```python
load(arcPath)
```
用于将Arcaea铺面文件（`.aff`）生成铺面总字典。  
``arcPath``: Arcaea铺面文件导入路径  
此函数将返回一个字典。
  
```python
createJson(dict,JsonPath)
```
用于通过铺面总字典生成json文件。  
`dict`:创建json文件的字典  
`JsonPath`:创建json文件的路径
此函数不返回值，会创建一个json文件。

```python
output(arcJson,arcPath)
```
用于将铺面总字典生成为Arcaea铺面文件（`.aff`）
``arcJson``: 提供的json文件（字典）  
``arcPath``: Arcaea铺面文件导出路径  
此函数不返回值，会创建一个``.aff``文件。

## Tools分库
```python
Tools.arcJson
```
该变量用于Tools分库中的大部分函数对铺面总字典的直接调用，如果使用Tools分库中的函数，就必须要设置该全局变量。  
应将该全局变量赋值为你使用`load()`函数生成的铺面总字典。  

```python
Tools.sort(oldJson:list)
```
该函数用于对带有`"time"`与`"startTime"`的字典列表进行按时间顺序正向摆列整理。  
`oldJson`:未整理的带有`"time"`与`"startTime"`的字典列表  
该函数返回整理后的字典列表。  
*ps.该函数也是Tools分库中目前唯一一个在主库中调用的函数*  

```python
Tools.math
```
math组。该组中有用于计算arc的变换方式的函数，分别为`straight(x)` `sineIn(x)` `sineOut(x)` `bezier(x)`。  
`x`:计算该函数的自变量  
这些函数都会返回对应自变量所计算出的因变量（float），其图像如下：  

<img src=https://github.com/321bug/Jsonaea/raw/main/imgs/functions.png height=340/>

### EventSubject对象  
此对象是一个索引，每个EventSubject对象都能也只能对应一个事件。  

**事件**即为铺面总字典中能对铺面产生实际效果的子字典，分为**note事件**与**全局事件**，如`{type:"arc", "startTime": 1200,...}` `{time:0, "type": "arcahvdistort", ...}`等。其中**note事件**是指玩家可以在铺面中进行交互的事件（如hold、arc）；**全局事件**是指玩家不能直接在铺面中互动，但可以感知到其对铺面的作用的事件（如timing,scenecontrol），大部分该类型事件都对铺面全局产生作用。  

**EventSubject对象**是一个含3个元素的列表，分别为**时间组索引**、**类标签**以及**事件索引**，其格式如下：  
```python
EventSubject = [timingGroup,class,index]
```
**时间组索引（timingGroup）**：int类型。如果这个事件为note事件，其值就为这个note事件所在的timingGroup组的索引，也即为该事件在[铺面总字典中TimingList](https://github.com/321bug/Jsonaea#json%E6%96%87%E4%BB%B6--%E5%AD%97%E5%85%B8%E6%A0%BC%E5%BC%8F)中的索引；如果这个事件为全局事件，其值为-1。  
**类标签（class）**：str类型。其值为这个事件的总类型，分为Camera、Scenecontrol、notes、timing四项。  
**事件索引（index）**：int类型。该事件在其父列表中的索引。  

举例：现有`[1,"note","200"]`EventSubject对象，该对象在铺面总字典的位置为：
```python
{
    ...,
    "TimingList":[
        {
          ...
        },
        {
            "tags":[...],
            "notes":[
              ...,                 #此处省略199个字典
#            {                    <——————该事件的位置
#              "type":...,               
#              ...
#            },
              ...
            ],
            "timing":[...],
        },
        ...
    ]
}
```
