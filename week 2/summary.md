# 函數

- import,
- from ..... import,
- import .... as .....
- penup()
- pendown()
- pensize()
- pencolor()
- fd()
- circle()
- seth()

# turtle 庫的使用

## turtle 庫概述

- turtle（海龜）庫是turtle繪圖系統的python實現
- 有一隻海龜，其實在窗體正中心，在畫布上游走
- 它走過的軌跡就形成了繪製的圖形
- 海龜由程式控制，可以變換顏色、改變寬度等
	- turtle.setup() 窗體設置
	- turtle.setup(winth，height，statrX，startY)

## 設定視窗大小和啟動位置座標

- 後兩個參數可選（不設定時，窗體在螢幕正中心）
- 啟動座標是窗體左上角相對於電腦螢幕左上角的座標，此函數非必須

## turtle座標體系

-	包含絕對座標和海龜座標兩種
		- 絕對座標：相對於畫布正中心的座標。最開始「海龜」(畫筆) 在畫布（窗體）正中心，座標是(0, 0)，向右是x軸，向上是y軸。
		- turtle.goto(x, y) 去到該座標

## 海龜座標

- 相對於‘海龜’ 當下位置的座標，有前進方向、後退方向、左側方向、右側方向。
- turtle.fd(d) 表示向前方向
	- d 行進距離，單位px
- turtle.bk(d) 表示向后方向
	- d 行進距離，單位px
- turtle.circle() 表示以海龜左側的某一點為圓心繪制曲線

## 角度坐標體系

- 逆時針角度值為正數，順時針角度值為負數！
- x軸 表示 0 或 360度
- -x軸 表示 180 或 -180 度
- y軸 表示 90 或 -270度
- -y軸 表示 270 或 -90 度
- turtle.seth(angle) 按照角度改變海龜行進方向
	- 不在畫布繪制任何信息，只是改變行進方向
	- angle 絕對角度
	- turtle.left(angle) 向左方向行進
	- turtle.right(angle) 向右方向行進

# 庫引用與import

## 引用import

- 擴充python程序功能的方式叫庫引用。
- 使用import關鍵字來完成庫引用，釆用 <庫名>.<函數名>()編碼風格
	- import <庫名>
	- <庫名>.<函數名>(<函數參數>)

## 使用 from 和 import

- 使用from和import關鍵字共同完成
- 語法：
	- from <庫名> import <函數名>  單獨導入庫中的某個函數
或
	- from <庫名> import *   導入庫中的全部函數
	- <函數名1>(<函數參數>)
	- <函數名2>(<函數參數>)
	- 可以理解為把庫中的函數，導入到當前程序，因此在當前程序可以直接使用庫中才有的函數。

## 使用import和as

- 語法：
	- import <庫名> as <庫別名>
	- <庫別名>.<函數名>(<函數參數>)
	- 給庫起個小名。
		- 給調用的外部庫關聯一個更短、更適合自己的名，對編寫程序帶來便利。
- 三種import用法的比較
	- 第一種方式：
		- import <庫名>
		- <庫名>.<函數名>(<函數參數>)
		- <庫名>.<函數名> 意思是 庫（新程序）中的函數，如庫是turtle，即turtle中的函數。使用此方式就不會出現函數重名的問題
	- 第二種方式：
		- from <庫名> import <函數名>或
		- from <庫名> import *
		- <函數名1>(<函數參數>)
		- <函數名2>(<函數參數>)
		- 使用這種方式有可能導致庫中的函數與當前程序自定義的函數重名，那么就會發生沖突
	- 第三種方式：
		- 語法：
		- import <庫名> as <庫別名>
		- <庫別名>.<函數名>(<函數參數>)
		- 使用這種方式不用擔心函數重名問題，也可以減少代碼量。
	- 如果程序很小，只使用一個庫，沒有自己定義的函數，可以使用第二種方式。否則，為了避免函數重名，又能減少代碼量推荐使用第三種方式。

## turtle畫筆控制函數

	- turtle.penup() 別名 turtle.pu()
		- 抬起畫筆，海龜（畫筆）在飛行，此時運行畫筆將不形成軌跡。
	- turtle.pendown() 別名 turtle.pd()
		- 落下畫筆，海龜（畫筆）在爬行，此時行進畫筆將形成軌跡。
	- turtle.pensize(width) 別名 turtle.width(width)
		- 畫筆大小（寬度）
	- turtle.pencolor(color)
		- 畫筆顏色，字符串顏色名或rgb值
		- 顏色字符串：turtle.pencolor('purple')
		- RGB小數值：turtle.pencolor(0.63, 0.13, 0.94)
		- RGB元祖值：turtle.pencolor((0.63, 0.13, 0.94))

## turtle運動控制函數

- 控制畫筆的行進：走直線&走曲線
	- turtle.forward(d) 別名 turtle.fd(d)
		- 向前行進，走直線。
		- d：表示行進距離，單位像素，可以是負數。
	- turtle.circle(r, extent=Node)
		- 根據半徑r，繪制extent角度的弧形
		- r：默認圓心在海龜左側r距離的位置
		- extent：繪制角度，默認是360度整圓
	- turtle.circle(100) 
		- 以左側距離100像素為圓心，畫360整圓
	- turtle.circle(-100)
		- 以右側距離100像素為圓心，畫360整圓

## turtle方向控制函數

- 控制海龜面對的方向：絕對角度&海龜角度
	- turtle.setheading(angle) 別名 turtle.seth(angle)
		- 改變行進方向，海龜的角度
		- angle： 絕對角度值，逆時針正數，順時針負數。
		- urtle.seth(45) # x軸向上的45°
		- turtle.seth(-135)  
		- x軸的向下135°，即x軸順時針走135°
	- turtle.left(angle)
		- 海龜向左轉
		- angle: 海龜當前方向上旋轉的角度（相對角度）
	- turtle.right(angle)
	- 海龜向右轉
	- angle: 海龜當前方向上旋轉的角度（相對角度）
	- 注意：方向控制函數只改變海龜的方向，并不會形成軌跡。

# 循環語句和range()函數

## 循環語句

- 按照一定次數循環執行的一組語句，使用for和in關鍵字來實現
- 語法
	- for <變量> in range(<參數>):
    	- <被循環執行的語句>
		- <變量>：表示每次循環的計數，0 到 <次數>-1
		- <參數>：循環的次數
	- 例:
		- for i in range(5):
		- print(i)
		- 打印：0 1 2 3 4

## range()函數

- 產生循環計數序列
- range(N)
- 產生0 到 N-1 的整數序列，共N個。
	- range(5)
	- 0,1,2,3,4
- range(M, N)
	- 產生M到N-1的整數序列，共N-M個。
	- range(2, 5)
	- 2,3,4