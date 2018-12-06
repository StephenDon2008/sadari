# 编程试题

## 规则描述
Sadari(Ghostleg)是一款日本和韩国流行的一个乐趣游戏。

下面，我们来描述游戏规则。
如下图。上方选择区小写字母a-e对应5个可供玩家选择的工仔，下方大写字母A-E为不同的奖励。

- 开跑前，玩家选择工仔a-e，中间的路径和梯子被迷雾遮盖。
- 30秒倒数完成后，迷雾消失，显示被隐藏的路径，工仔开跑。
- 工仔a-e沿着自己下方的路径向下走，遇到中间的横线梯子便转弯，然后继续向下。
- 最终，每个工仔走到自己的终点并得到奖励。

说明：同一行的任意两个梯子不会相邻，不会有两个工仔到达同一个终点。
```                  
        a    b    c    d    e    
        │    │    │    │    │    
    ┌---┴----┴----┴----┴----┴---┐
    │                           │
    │                           │
    │                           │
    │         STARTING          │
    │     00:30(COUNTDOWN)      │
    │                           │
    │                           │
    │                           │
    │                           │
    └---┬----┬----┬----┬----┬---┘
        │    │    │    │    │    
        A    B    C    D    E    
```
开始前，路径被迷雾隐藏。

```                      
        a    b    c    d    e  
        │    │    │    │    │  
        │    ├----┤    ├----┤  
        │    │    │    │    │  
        ├----┤    │    │    │  
        │    │    │    │    │  
        ├----┤    ├----┤    │  
        │    │    │    │    │  
        │    ├----┤    │    │  
        │    │    │    │    │  
        ├----┤    │    ├----┤  
        │    │    │    │    │  
        │    │    │    │    │  
        │    │    │    │    │  
        A    B    C    D    E                
```
游戏开始，迷雾消失，工仔开始一起沿着自己的路径向前走。

```                      
        │    │    │    │    │  
        │    ├----┤    ├----┤  
        │    │    │    │    │  
        ├----┤    │    │    │  
        │    │    │    │    │  
        ├----┤    ├----┤    │  
        │    │    │    │    │  
        │    ├----┤    │    │  
        │    │    │    │    │  
        ├----┤    │    ├----┤  
        │    │    │    │    │  
        │    │    │    │    │  
        │    │    │    │    │  
        A(e) B(a) C(c) D(d) E(b)                
```
每个工仔到达自己的终点，得到奖励。

## 题目要求：
我们想让应试者使用react或者vue来实现这个游戏游戏过程，来考察面试者对react和vue的理解。
面试者可参考：http://okunishinishi.github.io/AMIDA/ 来理解这个过程。

提示：游戏的地图可被抽象成如下的一个二维数组，0代表没有梯子，1代表有梯子。
应试者可以参考我们的示例python代码来理解这个过程。
```javascript
let ladders = [
        [0, 1, 0, 1],
        [1, 0, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 0, 0],
        [1, 0, 0, 1],
];
```

请使用 http://okunishinishi.github.io/AMIDA/ 上的资源文件, 使用 React 或者 VUE 重新实现动画逻辑.

提交 Pull Request, 我们会即时与你联系.

你可以在这里找到面试官: https://t.me/joinchat/FJBUTRCfEDpch2frwdBFsQ
