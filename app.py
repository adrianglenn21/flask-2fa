from flask import Flask, render_template, request, redirect, url_for, session
import pyotp
import qrcode
import io
import base64

app = Flask(__name__)
app.secret_key = "super-secret-key"  # change in production

# Fake user database (demo only)
USER = {"username": "admin", "password": "admin", "totp_secret": pyotp.random_base32()}  # plaintext for demo only


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == USER["username"] and password == USER["password"]:
            session["pre_2fa"] = True
            return redirect(url_for("verify_2fa"))

    return render_template("login.html")


@app.route("/verify", methods=["GET", "POST"])
def verify_2fa():
    if not session.get("pre_2fa"):
        return redirect(url_for("login"))

    totp = pyotp.TOTP(USER["totp_secret"])

    if request.method == "POST":
        code = request.form["code"]
        if totp.verify(code):
            session.pop("pre_2fa")
            session["logged_in"] = True
            return redirect(url_for("dashboard"))

    # Generate QR code (only needed once, but fine for demo)
    uri = totp.provisioning_uri(name=USER["username"], issuer_name="Flask2FA Demo")

    qr = qrcode.make(uri)
    buf = io.BytesIO()
    qr.save(buf, format="PNG")
    qr_b64 = base64.b64encode(buf.getvalue()).decode()

    return render_template("verify.html", qr_code=qr_b64)


@app.route("/dashboard")
def dashboard():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("dashboard.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
