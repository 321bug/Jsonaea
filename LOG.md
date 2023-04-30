# 更新日志
### b230430
- 将Tools分库中的changeEvent函数中removeDict参数改为removeKey,现在删除事件中元素可以直接通过元素中key值移除了
- 删除主库中__version__版本变量

### b230424
- 新增searchEventSubject函数、changeEvent函数，现在可通过EventSubject直接修改铺面
- 修复了主库在输出铺面时有时创建空的arctap列表
- 在主库中分离了load函数与createJson函数，现在不能通过load函数直接创建json文件了，但可以通过createJson创建

### b230415  
- 新增EventSubject对象，可直接对铺面中的对象进行获取
- 在Tools中增加getEventSubject函数、cal_arc_pos函数以及math函数库
- 稳定了主库代码的可读性及结构

### b230402  
- jsonaea项目创建  
