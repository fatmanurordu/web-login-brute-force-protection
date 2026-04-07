from flask import Flask, request, render_template_string
import time

app = Flask(__name__)

# Doğru kullanıcı adı ve şifre
correct_username = "admin"
correct_password = "1234"

# Deneme sayısı ve limit
ip_attempts = {}
max_attempts = 5

# Basit login sayfası şablonu
login_page = """
<form method="POST">
  Kullanıcı adı: <input name="username"><br>
  Şifre: <input name="password" type="password"><br>
  <input type="submit" value="Giriş">
</form>
<p>{{ message }}</p>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    ip = request.remote_addr
    if ip not in ip_attempts:
        ip_attempts[ip] = 0

    message = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == correct_username and password == correct_password:
            ip_attempts[ip] = 0
            message = "Giriş başarılı!"
        else:
            ip_attempts[ip] += 1
            message = f"Hatalı giriş! Deneme sayısı: {ip_attempts[ip]}"
            time.sleep(ip_attempts[ip])  # gecikme ekleme

            if ip_attempts[ip] >= max_attempts:
                message = "Hesap kilitlendi! Daha sonra tekrar deneyin."

    return render_template_string(login_page, message=message)

if __name__ == "__main__":
    app.run(debug=True)