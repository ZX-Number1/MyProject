from flask import Flask,request,render_template_string

app = Flask(__name__)
#Flask 是 建立一個 Flask 網站應用程式的類別。
#__name__ 是 Python 的內建變數，代表目前這個檔案的名稱。
#Flask 需要這個參數來知道你的應用程式在哪裡（路徑、資源位置）
#app是空間，flask是室內設計師

UserData={
    "testuser" : "admin123"
}
#設定已經存在的帳密

HTML = """
<form method ="post">
Username: <input type="text" name="username"><br>
Password: <input type="passwodr" name="password"<br>
<input type="submit" value="Login">
</from>
{% if message %}
<p> {{message}} </p>
{% endif %}
"""

@app.route("/login", methods = ["GET", "POST"])
#定義 /login 這個網址，能接受 GET 和 POST 請求。

def login():
    message = ""
    if request.method == "POST":
        usermane = request.form.get("username")
        password = request.form.get("password")
        if usermane in UserData and UserData[usermane] == password:
            message = f"Welcome {usermane}!"
        else:
            message = "Login failed."
    return render_template_string(HTML, message = message)
    #render_template_string(HTML, message=message)→ 把 HTML 網頁和訊息顯示給使用者。

if __name__ == "__main__":
    app.run(debug=True)
    #debug=True → 開啟除錯模式，修改程式後會自動重啟。