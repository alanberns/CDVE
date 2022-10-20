from admin.src.core.board import disciplinas
from flask import Blueprint
from flask import render_template
from flask import request

from src.core import board

disciplinas_blueprint = Blueprint("disciplinas", __name__, url_prefix="/disciplinas")

@disciplinas_blueprint.get("/")
def disciplinas_index():
      disciplinas = board.list_disciplinas()
      return render_template(disciplinas.html, disciplinas=disciplinas)






