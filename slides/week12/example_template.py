from bottle import route, run, view, template

@route('/')
def show():    
    return template('mytitle', {"title":"我的標題"})
    

    #或 return template('title', {"title":"我的標題"})



@route('/show/<name>')
@view('mytitle')
def show(name):
    return {"title":name}

run(host='localhost', port=8080, debug=True)