from flask import jsonify


def response_ok(data, status=200):
    response = jsonify({
        "status": "success",
        "data": data
    })
    response.status_code = status
    response.headers["X-API-Version"] = "1.0"
    response.headers["X-Developer"] = "ca.chaparros1@uniandes.edu.co"
    return response


def response_error(message, status=400):
    response = jsonify({
        "status": "error",
        "message": message
    })
    response.status_code = status
    return response
