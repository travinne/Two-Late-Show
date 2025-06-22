from flask import Blueprint, jsonify
from server import db
from server.models.guest import Guest

guest_bp = Blueprint('guests', __name__)

@guest_bp.route('', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([guest.to_dict() for guest in guests]), 200