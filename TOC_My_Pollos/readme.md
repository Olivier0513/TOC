# TOC Project--My Pollos
## 概念介紹
我們每天都會需要覓食，但很容易遇到不知道要吃什麼的選擇障礙，於是，我設計了My Pollos，他能夠幫我們選擇餐點以及飲料，省去決定要吃什麼的大量時間。
## 開始使用My Pollos
輸入Bot basic ID或掃描QR code來加入My Pollos：
![](https://i.imgur.com/2TpaHN1.png)
## 使用說明
- 基本操作：
    - 所有用到英文的指令大小寫皆通用
    - 隨時輸入重新開始即可從頭開始使用
    - 輸入格式不符合時，會跳出「輸入格式有誤」的訊息：
    - ![](https://i.imgur.com/tF2F5ZZ.jpg)
- 初始訊息：
    - 第一次加入My Pollos時，會跳出基本操作訊息：
    -  ![](https://i.imgur.com/4Dym10R.png)
    -  在每次點擊重新開始時，也會再次跳出使用方式說明：
    -  ![](https://i.imgur.com/yPnPCSP.jpg)
- 功能1_餐點選擇：
    - 輸入任何含有「餓」的訊息，例如：「肚子餓」、「好餓，好想吃東西」，My Pollos會跳出讓您選擇「銅板美食」或「高檔餐廳」的訊息：
    -  ![](https://i.imgur.com/5E1kxMl.jpg)
    -  選擇「銅板美食」或「高檔餐廳」，My Pollos會從內部的list中隨機挑選一間作為您的選擇：
    - ![](https://i.imgur.com/JCWMSQH.jpg)
    - 此功能的操作到此已完成，輸入重新開始即可重新使用My Pollos
- 功能2_飲料選擇：
    -  輸入任何含有「渴」的訊息，例如：「我渴了」、「好渴，想喝點涼的」， My Pollos會直接從內部list中選擇一杯飲料給您：
    -  ![](https://i.imgur.com/Mo3t60a.jpg)
    -  此功能的操作到此已完成，輸入重新開始即可重新使用My Pollos
- 彩蛋：
    - 如果使用者在選擇完畢後輸入任何含有「謝謝」的訊息，My Pollos的老闆Gustavo Fring先生會親自出來答謝您：
    -  ![](https://i.imgur.com/TC9SDzQ.jpg)
- FSM：
![](https://i.imgur.com/Sn79Ez9.png)
- state說明：
    - user：一開始的初始state，輸入「餓」或「渴」，也可以查看fsm
    - eat：輸入「銅板美食」或「高檔餐廳」
    - drink：輸出選擇飲料
    - small：輸出選擇銅板美食
    - big：輸出選擇高檔餐廳
    - thank：輸出感謝圖片
    - show_fsm：輸出fsm架構圖


