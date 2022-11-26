from os.path import join as path_join
from os.path import abspath as abs_path
from os.path import dirname as up
from flask import current_app


def getComprobantePath(filename):
    admin_path = up(abs_path(current_app.instance_path))
    return path_join(admin_path, "public", "comprobantes", filename)

def getUploadsPath(filename):
    admin_path = up(abs_path(current_app.instance_path))
    return path_join(admin_path, "public", "uploads", filename)
