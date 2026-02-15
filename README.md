# 🔐 Information Security Labs

This repository contains practical implementations of classical cryptographic algorithms developed as part of Information Security lab work.

The focus of this repository is understanding substitution ciphers, encryption logic, and basic cryptographic transformations using Python.

---

## 📂 Project Structure

### 1️⃣ substitution_cypher_practical.py
Basic implementation of a Caesar Cipher (ROT-13 style) using substitution cipher logic.

- Encrypts only lowercase alphabet characters (a–z)
- Preserves spaces and special characters
- Uses modulo arithmetic (% 26)
- Implements try-except for non-alphabet handling

### 2️⃣ substitution_cipher_with_special_characters.py
Extended Caesar Cipher implementation.

- Encrypts alphabets, digits, spaces, and special characters
- Uses expanded key or ASCII-based shifting
- Demonstrates full character transformation
- Removes limitation of alphabet-only encryption

---

## 🧠 Concepts Covered

- Substitution Cipher
- Caesar Cipher
- ROT-13
- Modular Arithmetic
- ASCII-based Encryption
- Exception Handling in Python
- Encryption & Decryption Logic

---

## 🔄 How Caesar Cipher Works

Encryption Formula:

E(x) = (x + n) mod 26

Decryption Formula:

D(x) = (x - n) mod 26

Where:
- x = position of character
- n = shift value

---

## ▶️ How to Run

```bash
python substitution_cypher_practical.py
