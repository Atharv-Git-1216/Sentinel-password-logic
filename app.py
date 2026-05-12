from flask import Flask, request, jsonify
import math
import string
import bcrypt
import os
from supabase import create_client, Client

app = Flask(__name__)

# --- Supabase Configuration ---
# Replace these with your actual Supabase project credentials
SUPABASE_URL = "rnskqrjyaysyruhtecrd"
SUPABASE_KEY = "sb_publishable_1fvVaNEcSQaaZyWCl1jwsw_B4EaVVqreyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJuc2txcmp5YXlzeXJ1aHRlY3JkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzg2MDI4ODIsImV4cCI6MjA5NDE3ODg4Mn0.DOrwK7RHl19oQVlWxWJn6hD_eggtydyUY5CAXjNnjSI"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# --- Core Logic (Unchanged) ---
def calculate_pool_size(password: str) -> int:
    pool_size = 0
    if any(char.islower() for char in password): pool_size += 26
    if any(char.isupper() for char in password): pool_size += 26
    if any(char.isdigit() for char in password): pool_size += 10
    if any(char in string.punctuation for char in password): pool_size += 32
    return pool_size

def calculate_entropy(password: str) -> float:
    if not password: return 0.0
    pool_size = calculate_pool_size(password)
    return round(len(password) * math.log2(pool_size), 2)

def evaluate_strength(entropy: float) -> str:
    if entropy < 28: return "Very Weak"
    elif entropy < 36: return "Weak"
    elif entropy < 60: return "Reasonable"
    elif entropy < 128: return "Strong"
    else: return "Very Strong"

# --- New Logic: Hashing ---
def hash_password(password: str) -> str:
    # 1. Convert the password string to bytes
    password_bytes = password.encode('utf-8')
    # 2. Generate a random 'salt'
    salt = bcrypt.gensalt()
    # 3. Hash the password with the salt
    hashed_bytes = bcrypt.hashpw(password_bytes, salt)
    # 4. Convert back to a string so we can store it in the database
    return hashed_bytes.decode('utf-8')

# --- The API Endpoint ---
@app.route('/api/analyze', methods=['POST'])
def analyze_password():
    data = request.get_json()
    
    if not data or 'password' not in data:
        return jsonify({"error": "Missing 'password' field in request"}), 400
        
    password = data['password']
    
    # Calculate metrics
    ent = calculate_entropy(password)
    strength = evaluate_strength(ent)
    
    # Generate the Bcrypt Hash
    secure_hash = hash_password(password)
    
    # Save to Supabase
    try:
        db_response = supabase.table("sentinel_users").insert({
            "password_hash": secure_hash,
            "entropy_score": ent,
            "strength_rating": strength
        }).execute()
    except Exception as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500
    
    response = {
        "status": "success",
        "message": "Password analyzed, hashed, and securely stored.",
        "metrics": {
            "entropy_bits": ent,
            "strength": strength,
            "stored_hash": secure_hash # We return this just to show you what it looks like!
        }
    }
    return jsonify(response), 200

if __name__ == '__main__':
    print("🛡️ Sentinel API with Memory is booting up...")
    app.run(debug=True, port=5000)