from bottle import route, run

@route('/')
@route('/hello')
def hello():
    return "Hello, World!";


@route('/JhonCena')
def JhonCena():
    return "登登扔燈~~~"


@route('/Haibara')
def Haibara():
    return "我還你子由~";


@route('/小情歌')
def AChin():
    return "這是一首簡單的~筱晴歌~"



@route('/<name>')
def hello(name):
    return "Hello," + name;


run(host='localhost', port=8080, debug=True)

