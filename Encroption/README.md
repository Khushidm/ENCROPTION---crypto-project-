Encroption – Emoji-Based Hybrid Encryption System 🔐✨
Encroption is a modern cryptographic system that blends classical polyalphabetic encryption, confusion–diffusion security layers, and emoji-based encoding to produce secure, visually disguised ciphertext.

Features
🔒 Hybrid multi-layer encryption
(Polyalphabetic + Confusion/Diffusion + Base64 + Emoji mapping)
😎 Emoji-based ciphertext
Secure output that looks harmless on chats and social media.
🔓 Lossless decryption
Encrypted text can be perfectly reversed with the correct key.

🧪 Emoji Codepoint Inspector
Debug Unicode values to detect corrupted emojis.

📁 Project Structure
Encroption/
│
├── encroption.py      → Core encryption/decryption logic
├── gui.py              → Dark theme Tkinter GUI
├── inspect_emoji.py   → Unicode inspector tool
└── README.md           → Project documentation

🛠️ Technologies Used
Python 3.10+
Tkinter (GUI)
Base64 encoding
Emoji library
Custom emoji mapping
Unicode analysis (codepoints)

📦 Installation
1. Install dependencies
pip install emoji
2. Run the GUI
python gui.py

🧠 How Encroption Works
Encroption uses a 5-stage pipeline:
1️⃣ Input Plaintext
2️⃣ Polyalphabetic Encryption (Modified Vigenère)
3️⃣ Confusion–Diffusion Layer
4️⃣ Base64 Encoding
5️⃣ Emoji Mapping → final emoji ciphertext 🎉
This layered design breaks predictable patterns and increases security.

🔑 Usage
Encrypt
Enter plaintext in the Text Box
Enter a secret key
(Key is hidden as ••••)
Click ENCRYPT
You will get emoji ciphertext like:
😅🤩😇🥳😈🤠🤖✨

Decrypt
Paste emoji ciphertext
Enter the same key
Click DECRYPT
Plaintext will be restored.
If emojis are corrupted, use INSPECT CODEPOINTS to check Unicode values.

🎨 GUI Highlights
Neon Purple Accent
Full dark background
Hover animations
Bold monospaced text boxes
Copy Output button
Clear All button
Unicode inspector

📘 Applications
Secure messaging
Steganography
Data obfuscation
Educational cryptography demos
Fun encryption for social platforms

🔮 Future Enhancements
Add AES mode (hybrid crypto)
Cloud sync support
Custom emoji packs
Clipboard auto-watch encryption
Export encrypted files

License
This project is for academic and educational use.
