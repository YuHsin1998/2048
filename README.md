# 2048
使用Pygame实现2048

## 背景
最近入手新游戏：《Threes》，2048的前身，难度比2048大，这个游戏的命运比较悲哀，App上架没几天，便被人仿制出与之类似、入手更快的《2048》，2048获得了巨大的成功，无论App store 还是Android 市场，下载量都远远超过千万，但是《Threes》却不为人所知。

就这几天的游戏体验来说，threes的体验更好一些，恰好java课设临近DDL	，便准备编码《Threes》，因此先尝试2048，在2048的基础上编码threes.
## 环境
    Ubuntu 16.04.2
## 工具
    Python 3.5.2
    Pygame
    Gcolor2
    Firefox
## 逻辑

```mermaid
flowchat
s=>start: 开始
en=>end: 退出
st=>operation: 游戏开始
e=>operation: 游戏结束
op=>operation: 玩家操作
cond=>condition: 是否可操作？
leagel=>condition: 合法？
merge=>operation: 数字移动
again=>condition:  重新游戏

s->st->op->leagel
leagel(yes)->merge
leagel(no)->op
merge->cond
cond(yes)->op
cond(no)->e
e->again
again(yes)->st
again(no)->en

```

##  逻辑实现

```
游戏状态=未结束 
棋盘上随机两格置2

while 游戏状态=未结束:

    接收到滑动
    if(该方向可以滑动):
        for 序列 in 棋盘作平行于该方向的切分:
            for 元素 in 反序序列:
                if 元素不为空:
                    if 左边存在相隔n个零的相同元素(n>=0):
                        自身数值翻倍
                        总分=总分+合并后该元素的值
                        被合并的格子置空
                    while 右边元素为空:
                        自身右移一格
    if 当前棋盘有剩余空位:
        在空位中随机出现数字2或4
    if 棋盘上存在格子的值为2048:
        游戏状态=胜利
    elif 棋盘上存在剩余空格 或者 棋盘上依然存在可以合并的元素:
        游戏状态=未结束
    else:
        游戏状态=失败

```

## 效果图
![这里写图片描述](http://img.blog.csdn.net/20170621191732772?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvWWFuY3lf/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
## 步骤  
1.了解Pygame。第一次使用GUI，用了一个下午看了一下pygame，[强烈安利一个博客](http://eyehere.net/2011/python-pygame-novice-professional-index/)，翻译的很详细，基本上看完以后就大致了解了pygame的图形化过程，screen完全是由不同的Surface堆上去的，Surface就相当于是贴纸，直接在screen上贴就可以，不管是字体、图片、图形，都是Surface，想要用什么界面自己不断把Surface往上贴就可以。

2.了解pygame时间的事件过程，对于键盘按键，鼠标移动，亦或是鼠标点击，都称之为事件，在每个有效事件发生后，对事件进行处理，处理的过程无非就是改变一些数据的数值，然后在继续给screen贴上新的Surface，然后在display一下

3.2048的逻辑见上图，下面主要说一下图形形成的逻辑，虽然我们在玩游戏的时候画面一部分是静态的，但是实际上所有画面
都是动态的，每时每刻都在形成画面，称为screen display，实际上计算机每做一些事，都要显示一下画面，由于计算机运行速
度比较快，所以我们肉眼观察不到画面变化


```
while True:
    for event in pygame.event.get():
           #  对于每个事件进行处理
           map_init()
    map_init()  //screen display
```

这样一个很简陋额的2048就出现了：

![简陋版](http://img.blog.csdn.net/20170621192925510?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvWWFuY3lf/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

4.考虑优化它，首先是至少有个标题吧，上面可以加一些东西，比如说什么最高分、悔棋（其实实现这个功能不难，多开个数
组就可以，但个人感觉最好不能悔棋，便没有去实现），以及各数字的颜色应该不同，这个去网上查一下各颜色的RGB的值，
字体的Surface设置一下就好以及各数字的颜色应该不同，这个去网上查一下各颜色的RGB的值，字体的Surface设置一下就好

5.上面空白处放几个按钮，无奈pygame并没有button这个类，在网上查了些资料，发现可以自己编写button的class，监听按钮的类可以有两个条件判断，第一个鼠标点击事件，第二个是此刻监听鼠标的位置，判断点击的点是否在框内即可，有不足（可以
ps图片）

```
class Button(object):
	def __init__(self, name, col,position, size):
		self.name = name
                self.col = col
                self.size = size
		self.position = position
	def isOver(self):
		point_x,point_y = pygame.mouse.get_pos()
		x, y = self. position
		w, h = self.size
		in_x = x - w < point_x < x
		in_y = y - h < point_y < y
		return in_x and in_y
	def render(self):
		w, h = self.size
		x, y = self.position
                pygame.draw.rect(screen, self.col, ((x - w, y - h), (w, h)), 0)
		num_font = pygame.font.Font(None, h - 1)
                font_test=num_font.render(self.name, True, (255, 255, 255))
                fsetting = font_test.get_rect()
                fsetting.center = (x - w / 2, y - h / 2)
                screen.blit(font_test,fsetting)
```

6.上网看了一下2048游戏各个数字的颜色，本来肉眼找每个颜色的RGB，但是效果特别差劲，对，大概就
是这个样子，无奈。。。。。。
	![这里写图片描述](http://img.blog.csdn.net/20170621193432799?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvWWFuY3lf/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)



8.恰巧让舍友看到了，便安利我一个软件：

![这里写图片描述](http://img.blog.csdn.net/20170621193642123?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvWWFuY3lf/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

是一个屏幕取色器，通过这个软件，点击屏幕的颜色，可以直接分析出来RGB（神器），不过相同的RGB，在网页上与在pygame还是有色差的，我最后会说解决方法，嘻嘻，然后自己的2048就变样了

![这里写图片描述](http://img.blog.csdn.net/20170621193716427?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvWWFuY3lf/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

9.这样就剩下最上面按钮的处理上了，无奈自己一直找不到好看的样式，便直接在网上找了张图片

![这里写图片描述](http://img.blog.csdn.net/20170621193812560?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvWWFuY3lf/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

把这个图片当做Surface贴到screen中就可以，注意原来的按钮NEW、Menu位置对应到图片上来，嘻
嘻，然后我滴2048就变成这个样子了

![这里写图片描述](http://img.blog.csdn.net/20170621193849035?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvWWFuY3lf/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

10.我们把这两个按钮的颜色调成图片原按钮的颜色，然后把两个数字Surface贴上去就可以
嘻嘻，这个是成品：

![这里写图片描述](http://img.blog.csdn.net/20170621193912169?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvWWFuY3lf/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
## 技巧

1.想要自己做的画面好看，千万不要想着通过自己通过GUI画图形，很难得，直接从网上找图片，然后PPP，直接把图片当做surface贴到screen上来就可以，贼爽，比如按钮的图案，比如游戏的背景等等

2.关于色差问题，既然是因为同样的RGB在不同画面上有微小差距，那我们把网页截图，然后convert，
把png转成surface显示到pygame，这是再次使用Gcolor就可以了

3.游戏逻辑，在编码之前要想好，我本来感觉逻辑很清晰，结果编码过程中产生了好多疑惑，甚至在最后时发现游戏的一个大bug，

## 代码链接

[Python代码](http://paste.ubuntu.com/24923535/)

# 分析

### 优点：
1.界面优美（后面的背景图是截图p过来的，（逃 ）

2.支持记录最高分与重新开始

3.不支持悔棋，没错，我感觉这就是优点

4.python支持面向对象，便写了button的一个类，嘻嘻，下面的编程过程轻松了不少

### 不足：

1.对按钮处理不够仔细，其实完全可以p出来两个不同背景色的相同按钮，这样鼠标移动到按钮上显示一个颜色，否则背景是另一种颜色

2.编码不够条理，其实字体，图形等都可以设置成一个类，直接继承就好，代码长度会减少，犯错几率变得更小

3.对pygame的坐标系不熟悉，把行当做x轴，列当做y轴，然后就GG了，出现了下面这些反人类的代码

```
if  event.key == K_LEFT:
                  push_up()
           elif  event.key == K_RIGHT:
                  push_down()
           elif  event.key == K_UP:
                  push_left()
           elif  event.key == K_DOWN: 
                  push_right()
```

## 总结

1.第一次用pygame编游戏，感觉还不错，这次主要写的是图形化画面的东西，2048逻辑编码没怎么写，玩着自己编的游戏感觉美滋滋，嘻嘻， 自己玩游戏不是娱乐，是在测试。。。。是的，没错

2.DDL就是第一生产力，从产生编2048的想法，到最终实现，完全是DDL在给我施压，同样，这两天感觉过得很充实

3.PS要学好，PS要学好，PS要学好，重要的事情说三遍，自己以后的游戏画面全靠它了

4.明后天抽空把这个游戏改成《Threes》，恩，立个Flag， 宛如戏台上的老将军，背后插满了flag

5.正经脸。。。自己这次用python时，因为语法错误耽误了好长时间，果然手生。。以后没事要常用python搞搞事情
