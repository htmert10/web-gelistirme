from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Hesaplama fonksiyonu
def result_calculate(size, lights, device):
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5

    base_consumption = size * home_coef + lights * light_coef + device * devices_coef

    eco_bonus = 1.0
    if lights == 15:
        eco_bonus *= 0.6
    if device == 10:
        eco_bonus *= 0.5

    return base_consumption * eco_bonus

# Ana sayfa
@app.route('/')
def index():
    return render_template('index.html')

# İkinci sayfa - lambalar
@app.route('/<int:size>')
def lights_page(size):
    return render_template('lights.html', size=size)

# Üçüncü sayfa - cihazlar
@app.route('/<int:size>/<int:lights>')
def electronics(size, lights):
    return render_template('electronics.html', size=size, lights=lights)

# Hesaplama sayfası
@app.route('/<int:size>/<int:lights>/<int:device>')
def end(size, lights, device):
    result = result_calculate(size, lights, device)
    return render_template('end.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
