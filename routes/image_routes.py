from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from models import db, Image

image_bp = Blueprint('images', __name__)

@image_bp.route('/upload', methods=['POST'])
def upload_image():
    file = request.files['image']
    filename = secure_filename(file.filename)
    size = len(file.read())
    file.seek(0)  # Reset file pointer
    format = file.content_type

    # Save metadata
    image = Image(filename=filename, size=size, format=format)
    db.session.add(image)
    db.session.commit()

    # Placeholder for S3 upload
    # s3_client.upload_fileobj(file, S3_BUCKET, filename)

    return jsonify({"message": "Image uploaded successfully!", "filename": filename})

# ... additional endpoints like GET /images, GET /image/{id}, DELETE /image/{id} ...
