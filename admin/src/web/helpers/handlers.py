from flask import render_template


def not_found_error(e):
    kwargs = {
        "error_name": "404 Not Found error",
        "error_description": "La url a la que quisiste acceder no existe",
    }
    return render_template("error.html", **kwargs), 404

def unauthorized(e):
    kwargs = {
        "error_name": "401 Unauthorized",
        "error_description": "Debe iniciar sesion para acceder al recurso"
    }
    return render_template("error.html", **kwargs), 404

def internal_server_error(e):
    kwargs = {
        "error_name": "500 Internal server error",
        "error_description": "Error interno del servidor",
    }
    return render_template("error.html", **kwargs), 500
