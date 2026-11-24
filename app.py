from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def greet():
    varNama = request.form.get("nama", "").strip()
    if not varNama:
        varNama = "Anonim"
    nim = request.form.get("nim", "").strip()
    return render_template("index.html", hasil_nama=varNama, hasil_nim=nim)
#    return f"<h2>Halo, {varNama}! Selamat datang di Flask First App🚀</h2>"


if __name__ == "__main__":
    app.run(debug=True)