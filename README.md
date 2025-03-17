# Artwork Database

This project manages AI-generated artworks for the automated creation of print-on-demand products.

## Prerequisites

- Python 3.8 or higher
- Virtual environment (recommended)
- Dependencies in `requirements.txt` (see below)
- AWS credentials for S3 integration

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd artwork_database
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   Create a `.env` file in the project directory and add the following variables:
   ```
   DATABASE_URI=sqlite:///artwork.db
   AWS_ACCESS_KEY_ID=<Your AWS Access Key>
   AWS_SECRET_ACCESS_KEY=<Your AWS Secret Key>
   AWS_REGION=us-east-1
   S3_BUCKET_NAME=<Your S3 Bucket Name>
   ```

## Usage

1. **Initialize the database**:
   The database is automatically created when the app is started.

2. **Start the app**:
   ```bash
   python app.py
   ```

3. **API Endpoints**:
   The API is available at `/api`. Further details can be found in the file `routes/image_routes.py`.

## S3 Integration

The app uses AWS S3 to store files. Ensure that your AWS credentials are correct and the S3 bucket exists.

## Demo Data

When the app is started for the first time, demo data is automatically inserted into the database.

## License

This project is licensed under the MIT License. For more information, see the file `LICENSE`.