import base64
from emoji_map import emoji_map, reverse_map

# ---------- Poly Encryption ----------
def poly_encrypt(text, key):
    out = []
    for i, ch in enumerate(text):
        shift = ord(key[i % len(key)]) % 256
        out.append(chr((ord(ch) + shift) % 256))
    return ''.join(out)

def poly_decrypt(text, key):
    out = []
    for i, ch in enumerate(text):
        shift = ord(key[i % len(key)]) % 256
        out.append(chr((ord(ch) - shift) % 256))
    return ''.join(out)

# ---------- Confusion / Diffusion ----------
def confuse(s, key):
    return ''.join(chr(ord(c) ^ len(key)) for c in s)

def unconfuse(s, key):
    return ''.join(chr(ord(c) ^ len(key)) for c in s)

# ---------- Emoji Encoding ----------
def to_emoji(b64):
    return ''.join(emoji_map[c] for c in b64)

def from_emoji(txt):
    # Greedy parse from reverse_map
    result = ""
    i = 0
    symbols = sorted(reverse_map.keys(), key=len, reverse=True)

    while txt:
        matched = False
        for sym in symbols:
            if txt.startswith(sym):
                result += reverse_map[sym]
                txt = txt[len(sym):]
                matched = True
                break
        if not matched:
            raise ValueError("Invalid ciphertext: unknown emoji")
    return result

# ---------- Final Encrypt ----------
def encrypt(text, key):
    p = poly_encrypt(text, key)
    c = confuse(p, key)
    b = base64.b64encode(c.encode()).decode()
    e = to_emoji(b)
    return e

# ---------- Final Decrypt ----------
def decrypt(emojis, key):
    b64 = from_emoji(emojis)
    c = base64.b64decode(b64).decode()
    p = unconfuse(c, key)
    text = poly_decrypt(p, key)
    return text


