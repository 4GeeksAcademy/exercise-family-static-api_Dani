"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Create the Jackson family object
jackson_family = FamilyStructure("Jackson")

# Initial members
initial_members = [
    {"first_name": "John", "age": 33, "lucky_numbers": [7, 13, 22]},
    {"first_name": "Jane", "age": 35, "lucky_numbers": [10, 14, 3]},
    {"first_name": "Jimmy", "age": 5, "lucky_numbers": [1]}
]

for member in initial_members:
    jackson_family.add_member(member)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code




@app.route('/')
def sitemap():
    return generate_sitemap(app)




@app.route('/members/<int:id>', methods=['GET'])
def get_member(id):
    member = jackson_family.get_member(id)  
    if not member:
        return jsonify({"error": "Member not found"}), 404
    return jsonify(member), 200




@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200




@app.route('/members', methods=['POST'])
def new_member():
    data = request.get_json()
    if not data.get("first_name") or not data.get("age"):
        return jsonify({"error": "Missing required fields"}), 400

    new_member = {
        "first_name": data["first_name"],
        "age": data["age"],
        "lucky_numbers": data.get("lucky_numbers", [])
    }

    
    added_member = jackson_family.add_member(new_member)

    return jsonify(added_member), 201




@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    member = jackson_family.get_member(id)
    if not member:
        return jsonify({"error": "Member not found"}), 404  

    jackson_family.delete_member(id)  
    return jsonify({"message": "Member deleted successfully"}), 200








if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
