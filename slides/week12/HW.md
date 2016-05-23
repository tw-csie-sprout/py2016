#尋人啟事之海捌樂留言版

## 作業目標

海捌樂要尋找妹妹，所以捌樂決定來。

一開始的程式碼裡面已經有一些留言了，請將留言內容顯示在網站上，並讓。

###基本功能

1. 使用者可以看到留言版上每一則留言。
2. 使用者可以填寫表單留言。

### 加分項目

3. bottle的程式重開之後，之前的留言不會消失。(提示：讀檔寫檔、JSON、shelve)
3. 使用 template 處理HTML部分。
4. 美化網站外觀。(評分者主觀加分，改了變醜不扣分(?))
5. 提升程式碼品質：包含可讀性、美觀的排版、變數命名、程式架構...讓這個程式像是一個好程式。(評分者主觀給分)


##作業架構

###上傳格式
請寫一個 python 檔案，檔名請取`main.py`，只要執行這個檔案就能讓網站 run 起來。  
如果使用了 template，請將整個資料夾壓縮成 zip 檔上傳。

加分題的部分請在上傳時填寫你實做了哪些項目(美化跟程式碼品質不用寫)

##作業內容說明

###HTML部分

請先參考我們寫好的 [留言版.html](https://gist.github.com/rilak/0e5ed6af6b3e5d19d17aba724e75e559)，這份HTML檔案長相如下：

![留言版](http://i.imgur.com/RMOsuJe.png)

請觀察裡面留言的部分

```
            <ul class="list-group">
                <li class="list-group-item"> 
                     <h4 class="list-group-item-heading"> 我是內文1 </h4>
                      <p class="list-group-item-text"> 我是作者1 </p>
                </li>
                <li class="list-group-item"> 
                     <h4 class="list-group-item-heading"> 我是內文2 </h4>
                      <p class="list-group-item-text"> 我是作者2 </p>
                </li>
                <li class="list-group-item"> 
                     <h4 class="list-group-item-heading"> 我是內文3 </h4>
                      <p class="list-group-item-text"> 我是作者3 </p>
                </li>
                <li class="list-group-item"> 
                     <h4 class="list-group-item-heading"> 我是內文4 </h4>
                      <p class="list-group-item-text"> 我是作者4 </p>
                </li>
            </ul>
```

我們可以知道每一則留言都是由下方的片段組成。

```
                <li class="list-group-item"> 
                     <h4 class="list-group-item-heading"> 我是內文1 </h4>
                      <p class="list-group-item-text"> 我是作者1 </p>
                </li>
```
所以要顯示每一則留言，只要不斷複製這個片段，並把留言的「內文」與「作者」放進去標籤的中間。

###留言部份

現在將留言的資料存在 list 當中，list的每一格都是由 (內容、作者) 組成的 tuple

```
messages = [("當愛昱熹望，投射炙熱的太陽",  "rilak"),  ("The Code never bother me anyway",  "AChin")]

for message in messages:
    comment = message[0]
    name = message[1]
```

你可以使用字串的連接將數個留言HTML片段連接在一起

```
messages = [("當愛昱熹望，投射炙熱的太陽",  "rilak"),  ("The Code never bother me anyway",  "AChin")]

HTML = "blabla" <= 前面的片段

for message in messages:
    HTML += '<li class="list-group-item">'
    HTML += '<h4 class="list-group-item-heading"> 內容 </h4>'   <= 將message[0]塞進內容欄位
    HTML += '<p class="list-group-item-text"> 作者 </p>'  <= 將 message[1] 塞進作者欄位
    HTML += '</li>'
        
HTML += "blabla"  <= 後面的片段
```


###表單部分

表單部分的HTML如下

```
             <form action="/" method="post">
                <div class="form-group">
                    <label for="name">姓名：</label>
                    <input type="text" class="form-control" id="inputText" name="name"> 
                    <label for="comment">留言內容：</label>
                    <input type="text" class="form-control" id="inputText" name="comment"> 
                </div>
                <button type="submit" class="btn btn-default">留言！</button>
            </form>
```

####表單行為
從 `<form action="/" method="post">` 這行，我們可以知道這個表單會對應到 route('/', method="post")。

####表單內容
由 `<input blabla name="name">` 和 `<input blabla name="comment">` 我們可以看到這個表單有兩個欄位，欄位名字是 name 和 comment。

####處理表單的程式

```
@route('/', method="post")
def post_comment():
    name = request.form.get("name")
    comment = request.form.get("comment")
    #將這則留言放入資料中
    return "<a href='/'>upload success</a>"
```

##程式架構
```
from bottle import route, run, request

@route('/')
def show():
    HTML = ""
    #顯示整個留言版
    return HTML
    
@route('/', method="post")
def post_comment():
    #將留言放入資料中
    return "<a href='/'>upload success</a>"
```