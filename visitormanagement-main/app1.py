import requests
import os
import qrcode
from io import BytesIO
from flask import Flask, render_template, redirect, send_file, request
from flask_sqlalchemy import SQLAlchemy
from pyzbar.pyzbar import decode
from PIL import Image

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///requests.db'
db = SQLAlchemy(app)

# Database model
class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    purpose = db.Column(db.String(200), nullable=False)
    approved = db.Column(db.Boolean, default=False)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/verify', methods=['POST'])
def verify():
    if 'file' not in request.files:
        return 'No file uploaded'

    qr_code = request.files['file']

    # Check if the uploaded file is a valid image
    if qr_code.filename == '':
        return 'Invalid file'

    # Save the uploaded file to a temporary location
    temp_path = f'temp/{qr_code.filename}'
    qr_code.save(temp_path)

    # Perform QR code verification
    verified, visitor_id = verify_qr_code(temp_path)

    if verified:
        # Retrieve the visitor details from the database
        visitor = Request.query.get(visitor_id)
        return f"Visitor ID: {visitor.id}<br>Name: {visitor.name}<br>Address: {visitor.address}<br>Email: {visitor.email}<br>Phone: {visitor.phone_number}<br>Purpose: {visitor.purpose}"
    else:
        return 'Invalid QR code'
    

def verify_qr_code(qr_code_path):
    # Perform QR code scanning and verification logic here
    qr_data = decode(Image.open(qr_code_path))
    
    if qr_data:
        extracted_data = qr_data[0].data.decode('utf-8')

        # Assuming the extracted data follows the format:
        # 'Name: {name}\nAddress: {address}\nEmail: {email}\nPhone: {phone_number}\nPurpose: {purpose}\nVisitor ID: {visitor_id}'
        extracted_info = {}
        for line in extracted_data.split('\n'):
            key, value = line.split(': ')
            extracted_info[key] = value
        
        # Compare the extracted data with the database records to verify the QR code validity
        visitor_id = extracted_info.get('Visitor ID')
        request = Request.query.get(visitor_id)
        
        if request:
            # Compare other extracted fields with the request record if necessary
            if extracted_info['Name'] == request.name and extracted_info['Address'] == request.address:
                # QR code is valid
                return True, visitor_id
    
    # QR code is not valid or verification failed
    return False, None

# @app.route('/verify', methods=['POST'])
# def verify():
#     if 'file' not in request.files:
#         return 'No file uploaded'

#     qr_code = request.files['file']

#     # Check if the uploaded file is a valid image
#     if qr_code.filename == '':
#         return 'Invalid file'

#     # Save the uploaded file to a temporary location
#     temp_path = f'temp/{qr_code.filename}'
#     qr_code.save(temp_path)

#     # Perform QR code verification
#     verified, visitor_id = verify_qr_code(temp_path)

#     if verified:
#         # Retrieve the visitor details from the database
#         visitor = Request.query.get(visitor_id)
#         return f"Visitor ID: {visitor.id}<br>Name: {visitor.name}<br>Address: {visitor.address}<br>Email: {visitor.email}<br>Phone: {visitor.phone_number}<br>Purpose: {visitor.purpose}"
#     else:
#         return 'Invalid QR code'
    

# def verify_qr_code(qr_code_path):
#     # Perform QR code scanning and verification logic here
#     qr_data = decode(Image.open(qr_code_path))
    
#     if qr_data:
#         extracted_data = qr_data[0].data.decode('utf-8')

#         # Assuming the extracted data follows the format:
#         # 'Name: {name}\nAddress: {address}\nEmail: {email}\nPhone: {phone_number}\nPurpose: {purpose}\nVisitor ID: {visitor_id}'
#         extracted_info = {}
#         for line in extracted_data.split('\n'):
#             key, value = line.split(': ')
#             extracted_info[key] = value
        
#         # Compare the extracted data with the database records to verify the QR code validity
#         visitor_id = extracted_info.get('Visitor ID')
#         request = Request.query.get(visitor_id)
        
#         if request:
#             # Compare other extracted fields with the request record if necessary
#             if extracted_info['Name'] == request.name and extracted_info['Address'] == request.address:
#                 # QR code is valid
#                 return True, visitor_id
    
#     # QR code is not valid or verification failed
#     return False, None



# Admin side - route to approve requests
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == 'admin':
            requests = Request.query.all()
            return render_template('admin.html', requests=requests)
        else:
            return 'Invalid username or password'

    return render_template('admin_login.html')

@app.route('/approve/<int:request_id>')
def approve(request_id):
    request = Request.query.get(request_id)
    request.approved = True
    db.session.commit()

    # Generate QR code and get the file path
    qr_code_path = generate_qr_code(request)

    # Download the QR code file
    return send_file(qr_code_path, as_attachment=True)



def generate_qr_code(request):
    # Generate a unique number
    unique_number = request.id  # Assuming `request.id` is already unique

    # Generate QR code data
    qr_code_data = f'Name: {request.name}\nAddress: {request.address}\nEmail: {request.email}\nPhone: {request.phone_number}\nPurpose: {request.purpose}\nVisitor ID: {unique_number}'

    # Generate QR code image
    qr_code_path = f'qrcodes/qr_code_{request.id}.png'
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(qr_code_data)
    qr.make(fit=True)
    qr_image = qr.make_image(fill="black", back_color="white")
    qr_image.save(qr_code_path)

    return qr_code_path


@app.route('/validate_qr_code', methods=['POST'])
def validate_qr_code():
    qr_code_file = request.files['qr_code_file']
    if qr_code_file:
        # Save the uploaded QR code image
        qr_code_path = os.path.join(app.config['UPLOAD_FOLDER'], qr_code_file.filename)
        qr_code_file.save(qr_code_path)

        # Validate the QR code
        qr_code_valid, visitor_id = verify_qr_code(qr_code_path)

        if qr_code_valid:
            # Perform any desired actions for a valid QR code
            # For example, update the corresponding request record in the database
            qr_request = Request.query.get(visitor_id)
            qr_request.approved = True
            db.session.commit()
            return f'Success! QR code for visitor ID {visitor_id} is valid.'

    return 'Error: Invalid QR code or no QR code file uploaded.'


# Client side - form submission
@app.route('/client', methods=['GET', 'POST'])
def client():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        email = request.form['email']
        phone_number = request.form['phone_number']
        purpose = request.form['purpose']

        new_request = Request(name=name, address=address, email=email, phone_number=phone_number, purpose=purpose)
        db.session.add(new_request)
        db.session.commit()
        return redirect('/')

    return render_template('client.html')

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = 'uploads'
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)