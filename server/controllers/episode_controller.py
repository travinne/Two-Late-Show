from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from server import db
from server.models.episode import Episode
from server.models.appearance import Appearance

episode_bp = Blueprint('episodes', __name__)

@episode_bp.route('', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([episode.to_dict() for episode in episodes]), 200

@episode_bp.route('/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    appearances = Appearance.query.filter_by(episode_id=id).all()
    episode_data = episode.to_dict()
    episode_data['appearances'] = [appearance.to_dict() for appearance in appearances]
    return jsonify(episode_data), 200

@episode_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return jsonify({'message': 'Episode deleted successfully'}), 200