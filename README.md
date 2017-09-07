## SikuliTool

基于[pyjnius](https://github.com/kivy/pyjnius)，实现了对Sikuli的sikulixapi.jar的一层封装，可以在CPython中直接调用，方便和现有项目进行集成，灵感来自[sikuli_cpython](https://github.com/kevlened/sikuli_cpython)。

在Python3.5.2下运行通过。

### 相关依赖

- JDK
- Cython
- pyjnius

> 环境变量需要配置JAVA_HOME

![](http://jianbing.github.io/images/sikuli-tool/java_home.png)

> Path里边，需要加入jvm.dll所在目录

![](http://jianbing.github.io/images/sikuli-tool/path.png)

###演示

> 例子1：拖动，双击对象。

```python
from sikulitool.sikuli import *

s = Screen()
s.dragDrop("as.png", "dir.png")
s.sleep(0.5)
s.dragDrop("qq.png", "dir.png")
s.find("dir.png").highlight().sleep(1).doubleClick()
```

![](http://jianbing.github.io/images/sikuli-tool/drag.gif)

> 例子2：通过similar方法设置相似度，在屏幕中查找多个相似度为50%的对象。

```python
from sikulitool.sikuli import *

s = Screen()
for i in s.findAll(Pattern('doc.png').similar(0.5)):
	i.highlight().sleep(1).hover()
```
![](http://jianbing.github.io/images/sikuli-tool/findall.gif)


