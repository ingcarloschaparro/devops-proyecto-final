from flask import Blueprint, request

from persistent.blacklist_model import Blacklist
from utils.config import Config
from utils.responses import response_ok, response_error
from business.blacklist_business import (create_blacklist,
                                         find_blacklist_by_email,
                                         delete_all_blacklist,
                                         find_all_blacklist)

blacklist_bp = Blueprint("blacklist", __name__)


@blacklist_bp.before_request
def check_bearer_token():
    print(f"check_bearer_token: {request.path}")
    if request.path == "/api/blacklists/health":
        return

    auth_header = request.headers.get('Authorization')

    if not auth_header or not auth_header.startswith('Bearer '):
        return response_error('Token no enviado', 401)

    token = auth_header.split(" ")[1]

    if token != Config.TOKEN:
        return response_error('Token no válido', 401)


@blacklist_bp.route("/health")
def health():
    return {"message": "Integración Continua exitoso y de entrega continua exitoso"}


@blacklist_bp.route("/<string:email>", methods=["GET"])
def get_by_email(email):
    if not email:
        return response_error('Email obligatorio', 400)

    blacklist = find_blacklist_by_email(email)

    if blacklist:
        return response_ok({
            "exists": True,
            "blocked_reason": blacklist.blocked_reason
        }, 200)
    else:
        return response_ok({
            "exists": False
        }, 200)


@blacklist_bp.route("/", methods=["POST"])
def add():
    data = request.get_json()

    app_uuid = data.get('app_uuid')
    email = data.get('email')
    blocked_reason = data.get('blocked_reason')
    ip_address = request.remote_addr

    if not app_uuid or not email or not blocked_reason:
        return response_error('Bad request', 400)

    blacklist = find_blacklist_by_email(email)

    if blacklist:
        return response_error("Ya existe el email en listas negras", 409)

    if not ip_address:
        ip_address = "127.0.0.1"

    blacklist = Blacklist(email, app_uuid, blocked_reason, ip_address)

    new_id = create_blacklist(blacklist)

    return response_ok({
        "id": new_id
    }, 201)


@blacklist_bp.route("/reset", methods=["DELETE"])
def reset():
    delete_all_blacklist()
    return response_ok("Tabla borrada exitosamente", 200)


@blacklist_bp.route("/", methods=["GET"])
def get_all():
    blacklists = find_all_blacklist()

    return response_ok([blacklist.to_dict() for blacklist in blacklists], 200)
