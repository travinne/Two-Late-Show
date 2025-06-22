import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from server.app import create_app, db
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance
from server.models.user import User
from werkzeug.security import generate_password_hash
import datetime

def seed_database():
    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()

        user1 = User(
            username='admin',
            email='admin@example.com',
            password_hash=generate_password_hash('password123')
        )
        user2 = User(
            username='producer',
            email='producer@example.com',
            password_hash=generate_password_hash('password456')
        )
        db.session.add_all([user1, user2])
        db.session.commit()

        guest1 = Guest(name='Luka Benny', occupation='Developer')
        guest2 = Guest(name='Mathew Mwangi', occupation='Accountant')
        db.session.add_all([guest1, guest2])
        db.session.commit()

        episode1 = Episode(date=datetime.date(2025, 6, 20), number=81)
        episode2 = Episode(date=datetime.date(2025, 6, 21), number=82)
        db.session.add_all([episode1, episode2])
        db.session.commit()

        appearance1 = Appearance(rating=4, guest_id=1, episode_id=1)
        appearance2 = Appearance(rating=5, guest_id=2, episode_id=1)
        appearance3 = Appearance(rating=3, guest_id=1, episode_id=2)
        db.session.add_all([appearance1, appearance2, appearance3])
        db.session.commit()

        print("Database seeded successfully!")

if __name__ == "__main__":
    seed_database()