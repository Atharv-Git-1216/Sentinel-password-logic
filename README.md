# 🛡️ Sentinel: Password Strength & Security Logic

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Framework-Flask-lightgrey.svg)](https://flask.palletsprojects.com/)
[![Database](https://img.shields.io/badge/Database-Supabase-green.svg)](https://supabase.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🌌 The Sentinel Series
This project is the **foundational module** of the **Sentinel Cyber AI**—a multi-stage roadmap designed to build a comprehensive, AI-driven cyber threat analyzer. Each repository in this series represents a specific "sensory" or "logic" layer, eventually culminating in a unified security ecosystem.

1.  👉 **Password Strength & Security Logic** (Current)
2.  🔍 Suspicious URL Detector (In Progress)
3.  📧 Phishing Email Analyzer (Planned)
4.  🤖 AI Chatbot for Cyber Awareness (Planned)

---

## 📝 Project Overview
The **Sentinel Password Logic** module focuses on the "Identity and Access" layer of cybersecurity. Moving beyond simple character-length checks, this tool utilizes Information Theory to calculate the mathematical entropy of a password and securely processes it using industry-standard cryptographic hashing.

### Key Features
*   **Entropy Calculation:** Uses the search-space entropy formula to measure password randomness in bits.
*   **Bcrypt Hashing:** Implements one-way salted hashing to ensure passwords are never stored in plain text.
*   **Flask API:** A RESTful bridge that allows other applications to consume these security metrics.
*   **Supabase Integration:** Real-time data persistence for security logs and audit trails.

---

## 🧪 The Science
The core logic measures strength using the entropy formula:

$$E = L \times \log_2(R)$$

Where:
*   **$L$** is the password length.
*   **$R$** is the pool of possible characters (lowercase, uppercase, digits, symbols).

By calculating the **bits of entropy**, we can mathematically estimate the time it would take to crack a password via brute force, providing a more objective security rating than traditional methods.

---

## 🚀 Getting Started

### Prerequisites
*   Python 3.x
*   A Supabase Project (URL and Anon Key)
*   `pip` (Python package manager)

### Installation
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/sentinel-password-logic.git](https://github.com/YOUR_USERNAME/sentinel-password-logic.git)
   cd sentinel-password-logic
