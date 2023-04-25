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
math组。该组中有用于计算arc的变换方式的函数，分别为`straight(x)``sineIn(x)``sineOut(x)``bezier(x)`。  
`x`:计算该函数的自变量
这些函数都会返回对应自变量所计算出的因变量（float），其图像如下：
