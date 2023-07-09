from flask import Flask, render_template, request
import io
import sys

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('./index.html')


@app.route('/execute', methods=['POST'])
def execute():
    code = request.form['code']

    # Создаем объект для перехвата вывода
    stdout = io.StringIO()
    sys.stdout = stdout

    try:
        # Выполняем переданный код
        exec(code)
    except Exception as e:
        # В случае ошибки выводим сообщение об ошибке
        print('Error:', e)

    # Получаем результат выполнения кода
    output = stdout.getvalue()

    # Возвращаем результат в формате JSON
    return {'output': output}


if __name__ == '__main__':
    app.run(debug=True, port=5001)
