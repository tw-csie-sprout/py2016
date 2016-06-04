from bottle import route, run , request , response

cur_name = None

@route( '/whoami' )
def whoami():
    html = ""
    if request.cookies.get( 'name' ):
        html += "<p>哩嘻 %s</p>" % request.cookies.get( 'name' )
    html +=  '''
        <form action="/whoami" method="post">
            哩瞎祕狼？: <input name="name" type="text" />
        </form>
    '''
    return html

@route( '/whoami' , method='POST' )
def submit():
    global cur_name
    cur_name = request.forms.name
    response.status = 303
    response.set_cookie( 'name' , cur_name )
    response.set_header( 'Location' , '/whoami' )
    return "<a href='/whoami'>upload success</a>"

run(host='localhost', port=8080, debug=True)


