from bottle import route, run, view, template, static_file



@route('/')
@view('message')
def show():

    post_list = [
        {
            "title" : "AChin",
            "content" : "這是一首簡單的筱晴歌~",
            "embeded" : "vhAxXJjAQwQ"
        },
        {
            "title" : "Haibara",
            "content" : "我還你子由~",
            "embeded" : "nWb_X3ZJQjw"
        },
        {
            "title" : "Water.M",
            "content" : "愛昱熹望 <3 <3 <3",
            "embeded" : "rXhQE416lDk"
        },
        {
            "title" : "Rilak",
            "content" : "忠毅忠孝歌",
            "embeded" : "12cAwmr1F_4"
        }
    ]
    
    return {"post_list":post_list}
    

@route('/static/<filename:path>')
def server_image(filename):
    return static_file(filename, root='static/')

run(host='0.0.0.0', port=8080, debug=True)

