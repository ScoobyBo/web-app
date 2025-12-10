from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def temp():
    try:
        t = requests.get("http://wttr.in/Tver?format=%t", timeout=30).text.strip()
    except:
        t = "Ошибка получения данных"
    return t

if __name__ == "__main__":
    print("Запуск Flask...")
    app.run(host="0.0.0.0", port=5000)