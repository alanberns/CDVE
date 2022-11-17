from src.web import create_app
from pathlib import Path
from flask import Flask
from flask import jsonify
from src.core import board
from src.core.board.disciplina import Disciplina



static_folder = Path(__file__).parent.joinpath("public")

app = create_app(static_folder=static_folder)

def main():
    app.run()

if __name__ == "__main__":
    main()

@app.route("/api/club/disciplines")
def get_disciplinas():
    disciplinas=Disciplina.get_disciplinas()
    return jsonify(disciplinas)

