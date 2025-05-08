from flask import Flask, url_for


app = Flask(__name__)


@app.route('/')
def mission():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def slogan():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    text = '''Человечество вырастает из детства.
    Человечеству мала одна планета.
    Мы сделаем обитаемыми безжизненные пока планеты.
    И начнем с Марса!
    Присоединяйся!'''
    return '<br>'.join(text.split('\n'))


@app.route('/image_mars')
def image_mars():
    return f'''
    <html>
        <head>
            <title>Привет, Марс!</title>
        </head>
        <body>
            <h1>Жди нас, Марс!</h1>
            <img src="{url_for('static', filename='mars.jpg')}" alt="Марс">
            <p><b>Вот она какая, красная планета.</b></p>
        </body>
    </html>
    '''


@app.route('/promotion_image')
def promotion_image():
    html = f"""
    <!doctype html>
    <html lang="ru">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Колонизация</title>

        <link rel="stylesheet" 
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
        crossorigin="anonymous">

        <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
    </head>
    <body>
        <div>
            <h1>Жди нас, Марс!</h1>
            <img src="{url_for('static', filename='img/mars.jpg')}" alt="Марс">

            <div class="alert alert alert-dark" role="alert">
                <p>Человечество вырастает из детства.</p>
            </div>
            <div class="alert alert alert-success" role="alert">
                <p class="text-success">Человечеству мала одна планета.</p>
            </div>
            <div class="alert alert alert-secondary" role="alert">
                <p class="text-secondary">Мы сделаем обитаемыми безжизненные пока планеты.</p>
            </div>
            <div class="alert alert alert-warning" role="alert">
                <p class="text-warning">И начнем с Марса!</p>
            </div> 
            <div class="alert alert alert-danger" role="alert">
                <p class="text-danger">Присоединяйся!</p>
            </div>
        </div>
    </body>
    </html>
    """
    return html


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
