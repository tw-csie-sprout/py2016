from bottle import route, run, request

all_messages = ["No submissions"]

@route('/')
def show():
    html = """<head>
        <title> 留言板 </title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    </head>
    """

    for message in all_messages:
        html += "<p><h1>" + message + "</h1></p>"
        print(message)

    html +=  '''
        <form action="/" method="post">
            Your Message: <input name="message" type="text" />
        </form>
    '''
    return html



@route('/', method="post")
def submit():
    global all_messages
    all_messages.append(request.forms.message)

    return "<a href='/'>upload success</a>"


run(host='localhost', port=8080, debug=True)

