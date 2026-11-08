from flask import Blueprint, render_template, Flask, jsonify, request

app = Flask(__name__)




def fonksiyon():
    print("Çalıştı")

@app.route("/")
def home():
    return render_template("index.html")

#@app.route("/calistir", methods=["POST"])
#def calistir():

@app.route("/hesapla", methods=["POST"])
def hesapla():
    data = request.get_json()

    ilksayi = data["ilkSayi"]
    ikincisayi = data["ikinciSayi"]
    islem = data["islem"]

    if islem == "+":
       sonuc = ilksayi + ikincisayi
    if islem == "-":
        sonuc = ilksayi - ikincisayi
    if islem == "*":
        sonuc = ilksayi * ikincisayi
    if islem == "/":
        if ilksayi == 0 or ikincisayi == 0:
            return jsonify({"sonuc": "Sıfıra bölünemez"})
        sonuc = ilksayi / ikincisayi

    return jsonify({"sonuc": sonuc})

 #   sonuc = fonksiyon()
   # return jsonify({"sonuc": sonuc})


if __name__ == "__main__":
    app.run(debug=True)