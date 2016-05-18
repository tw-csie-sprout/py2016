from bottle import route, run, request

message = "No submissions"

@route('/')
def show():
    html = "<h1>" + message + "</h1>"
    html +=  '''
        <form action="/" method="post">
            Your Message: <input name="message" type="text" />
        </form>
    '''
    return html



@route('/', method="post")
def submit():
    global message
    message = request.forms.get('message')
    return "<a href='/'>upload success</a>"


run(host='localhost', port=8080, debug=True)

