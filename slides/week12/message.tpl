<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Sprout 資訊之芽歌單</title>
    <link href="//fonts.googleapis.com/css?family=Lemon" rel="stylesheet" type="text/css">
    <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
    <link href="//djangogirlstaipei.github.io/assets/css/style.css" rel="stylesheet" type="text/css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.2/jquery.min.js"></script>
    <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
</head>

<body>

    <div class="header">
        <h1 class="site-title text-center">
            <a href="/"> Sprout Music List </a>
        </h1> 
    </div>

    <div class="container">
        % for post in post_list:
        <div class="post-wrapper">
            <div class="post">
                <div class="post-heading">
                    <h1 class="title">
                        {{ post['title'] }}
                    </h1>
                </div>

                <div class="text-center">
                    <iframe width="380" height="285" src="https://www.youtube.com/embed/{{ post['embeded'] }}" frameborder="0" allowfullscreen></iframe>
                </div>

                <div class="post-content h4">
                    <p> {{ post['content'] }} </p>
                </div>

                <div class="post-footer">
                    <a class="read-more" href="#">
                        Read More <i class="fa fa-arrow-right"></i>
                    </a>
                </div>

            </div>
        </div>
        % end
    </div>
</body>