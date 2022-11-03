from src import create_app
from pathlib import Path
from flask import Flask
from flask import jsonify


static_folder = Path(__file__).parent.joinpath("public")

app = create_app(static_folder=static_folder)

def main():
    app.run()

#definimos una ruta Get /api/club/disciplines
@app.route('/api/club/disciplines', methods=['GET'])

def get_discipline():
    response = {'name': "lista de disciplinas"}
    return jsonify(response)

if __name__ == "__main__":
    main()


