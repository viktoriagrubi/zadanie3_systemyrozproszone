from flask import Flask, redirect
import json

app = Flask(__name__)

# Odczyt instancji z pliku konfiguracyjnego
with open('config.json') as config_file:
    config_data = json.load(config_file)
    instances = config_data.get('instances', [])

# Licznik do śledzenia kolejnej instancji
counter = 0

# Obsługa żądania
@app.route('/')
def handle_request():
    global counter
    # Wybór instancji za pomocą Round Robin
    selected_instance = instances[counter % len(instances)]
    counter += 1
    # Przekierowanie żądania do wybranej instancji
    return redirect(selected_instance)

if __name__ == '__main__':
    # Uruchomienie aplikacji na porcie 5000
    app.run(port=5000)
