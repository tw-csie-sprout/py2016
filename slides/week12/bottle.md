Bottle
==

基本架構
---

先從最簡單的範例開始

```
from bottle import route, run

@route('/hello')
def index():
    return "Hello, world!"

run(host='localhost', port=8080)
```

第一行：import 等等需要的 bottle 元素  
第三行：`@route('/hello')` 會 match 到 `http://localhost:8080/hello` 這個網址  
第四行：將剛剛 `route('/hello')` match的路徑對應到 index() 這個函式        
第五行：函式 index() 會回傳 `"Hello, world!"` 這個字串給使用者   
第七行：`run(host='localhost', port=8080)` 會執行這個網站，然後只在本機上執行(其他人連不到你的網站)，並執行在8080的port上。所以網站的基本網址就會是`http://localhost:8080`。

route 路徑
----

注意這裡的 route() 會對應到的只有 `http://localhost:8080/hello`這個網址，在hello前後做任何修改都會讓 route() match 不到，例如`http://localhost:8080/hello/` 這個是連不到網頁的。

在route可以加入類似變數的概念。我們用 `<變數名稱>` 來表示一串文字，下面是一個範例。

#### `@route('/hello/<name>')`

這個 route 可以match   
`http://localhost:8080/hello/AChin`  
`http://localhost:8080/hello/WateMelon`   
`http://localhost:8080/hello/blabla`

但不會match到  
`http://localhost:8080/hello/`   <= 後面沒有任何文字   
`http://localhost:8080/hello/WateMelon/`   <= 後面多了一個斜線 /      
`http://localhost:8080/hey/AChin`  <= 前面的 /hello/ 沒有對應到   

因為不同的網址會有不同的name   
我們可以告訴Python 函式使用者在網址的name欄位輸入了什麼   

```
from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return "Hello", name
    
run(host='localhost', port=8080)
```

第三行： `route('/hello/<name>')` 有一個標籤 `<name>`。    
第四行： `def index(name)` 函式有一個參數 name，跟上面的`<name>`對應。   

所以當使用者輸入 `http://localhost:8080/hello/AChin` 時，route會match這個網址，然後把網址中`AChin`對應到標籤 `<name>`，然後執行 `index("AChin")` 這個函式。   

第五行：函式執行`return "Hello", name`，在這個範例中`name="AChin"`。

更多舉例：

 `http://localhost:8080/hello/WaterM`   =>  `name = "WaterM"`    
 `http://localhost:8080/hello/Rilak`   =>  `name = "Rilak"`     
  
  
  
表單與POST  
---


首先要有表單可以給使用者輸入

```
<form action="/" method="post">
    Your Message: <input name="message" type="text" />
</form>
```

<form action="/" method="post">
    Your Message: <input name="message" type="text" />
</form>

上面是一個表單，表單的行為被定義在 `<form action="/" method="post">` 中。    

`action = "/"` ：表示這個表單會被傳送到 "/" 這個路徑    
`method = "post"` ：表示這個表單使用post上傳    

表單的內容在裡面用 `name="message"` 表示 

如果Bottle要處理這個表單，就必須用 route 去接住使用者的post，有兩種寫法，效果是一樣的。    

```
@route("/", method="post")
```

或

```
from bottle import post 
@post("/")
```     

使用者傳上來的表單會在他的 request 當中

```
from bottle import request
```

接下來在函式內呼叫 request.form 去尋找表單內容   

```
request.forms.get('message')
```

###完整範例    

```
@route('/')
def show():
    return "<h1>" + message + "</h1>"
        <form action="/" method="post">
            Your Message: <input name="message" type="text" />
        </form>
    '''


@route('/', method="post")
def submit():
    message = request.forms.get('message')
    return "You post a message : ", message
```
