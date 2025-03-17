# This project is designed to manage AI-generated artwork for automated print-on-demand product creation.

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import boto3  # For S3 integration
from botocore.exceptions import NoCredentialsError

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///artwork.db')  # Placeholder for environment variable
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['AWS_ACCESS_KEY_ID'] = os.getenv('AWS_ACCESS_KEY_ID')
    app.config['AWS_SECRET_ACCESS_KEY'] = os.getenv('AWS_SECRET_ACCESS_KEY')
    app.config['AWS_REGION'] = os.getenv('AWS_REGION', 'us-east-1')
    app.config['S3_BUCKET_NAME'] = os.getenv('S3_BUCKET_NAME')

    # Initialization
    db.init_app(app)
    migrate.init_app(app, db)

    # Create S3 client
    def get_s3_client():
        try:
            s3_client = boto3.client(
                's3',
                aws_access_key_id=app.config['AWS_ACCESS_KEY_ID'],
                aws_secret_access_key=app.config['AWS_SECRET_ACCESS_KEY'],
                region_name=app.config['AWS_REGION']
            )
            return s3_client
        except NoCredentialsError:
            print("AWS credentials are missing or invalid.")
            return None

    app.s3_client = get_s3_client()

    # Register blueprints
    from routes.image_routes import image_bp
    app.register_blueprint(image_bp, url_prefix='/api')

    with app.app_context():
        from models import Artwork  # Import the model
        db.create_all()  # Create the database if it does not exist

        # Add demo content
        if not Artwork.query.first():  # Only add if the table is empty
            demo_artworks = [
                Artwork(title="Mona Lisa", artist="Leonardo da Vinci", year=1503),
                Artwork(title="Starry Night", artist="Vincent van Gogh", year=1889),
                Artwork(title="The Scream", artist="Edvard Munch", year=1893)
            ]
            db.session.bulk_save_objects(demo_artworks)
            db.session.commit()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
