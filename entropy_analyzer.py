import math
import string

def calculate_pool_size(password: str) -> int:
    """Determine the character pool size (R) based on the characters used."""
    pool_size = 0
    
    # Check for character types and add to the pool size
    if any(char.islower() for char in password):
        pool_size += 26  # a-z
    if any(char.isupper() for char in password):
        pool_size += 26  # A-Z
    if any(char.isdigit() for char in password):
        pool_size += 10  # 0-9
    if any(char in string.punctuation for char in password):
        pool_size += 32  # Special characters (!@#$ etc.)
        
    return pool_size

def calculate_entropy(password: str) -> float:
    """Calculate the Shannon Entropy of the password."""
    if not password:
        return 0.0
        
    pool_size = calculate_pool_size(password)
    password_length = len(password)
    
    # Entropy Formula: E = L * log2(R)
    entropy = password_length * math.log2(pool_size)
    return round(entropy, 2)

def evaluate_strength(entropy: float) -> str:
    """Classify the password strength based on NIST guidelines."""
    if entropy < 28:
        return "Very Weak (Instantly crackable)"
    elif entropy < 36:
        return "Weak (Cracked in minutes)"
    elif entropy < 60:
        return "Reasonable (Cracked in days/months)"
    elif entropy < 128:
        return "Strong (Takes centuries to crack)"
    else:
        return "Very Strong (Virtually uncrackable)"

# --- Execution ---
if __name__ == "__main__":
    print("🛡️ Sentinel Phase 1: Password Analyzer 🛡️")
    test_password = input("Enter a password to analyze: ")
    
    pool = calculate_pool_size(test_password)
    ent = calculate_entropy(test_password)
    strength = evaluate_strength(ent)
    
    print("\n--- Results ---")
    print(f"Password Length (L): {len(test_password)}")
    print(f"Character Pool Size (R): {pool}")
    print(f"Calculated Entropy: {ent} bits")
    print(f"Strength Rating: {strength}")