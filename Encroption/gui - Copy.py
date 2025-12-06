# gui.py - Gen-Z Dark Theme GUI (works with your existing encroption.encrypt/decrypt)
import tkinter as tk
from tkinter import scrolledtext, messagebox
from encroption import encrypt, decrypt

# Theme/colors/fonts
BG = "#0b0b0f"
CARD = "#14141a"
ACCENT = "#9b5cf6"
ACCENT_HOVER = "#b58eff"
TEXT = "#e6e6e6"
FONT_TITLE = ("Segoe UI Black", 18, "bold")
FONT_BOLD = ("Segoe UI", 12, "bold")
FONT_MONO = ("Consolas", 12)

def create_root():
    root = tk.Tk()
    root.title("Encroption — Emoji Encryption")
    root.geometry("860x660")
    root.configure(bg=BG)
    return root

def add_hover(widget, on_color=ACCENT_HOVER, off_color=ACCENT):
    def enter(e):
        try: e.widget.configure(bg=on_color)
        except: pass
    def leave(e):
        try: e.widget.configure(bg=off_color)
        except: pass
    widget.bind("<Enter>", enter)
    widget.bind("<Leave>", leave)

def run_gui():
    root = create_root()

    # Title
    lbl_title = tk.Label(root, text="ENCROPTION  🔐  EMOJI CRYPTO",
                         fg=ACCENT, bg=BG, font=FONT_TITLE)
    lbl_title.pack(pady=(14,6))

    # Main frame (center card)
    card = tk.Frame(root, bg=BG)
    card.pack(padx=16, pady=6)

    # Input label + box
    lbl_in = tk.Label(card, text="Enter Text / Emoji Ciphertext:", fg=TEXT, bg=BG, font=FONT_BOLD)
    lbl_in.grid(row=0, column=0, sticky="w", padx=6, pady=(6,0))

    input_box = scrolledtext.ScrolledText(card, width=96, height=8, bg=CARD, fg=TEXT, font=FONT_MONO, insertbackground=TEXT)
    input_box.grid(row=1, column=0, padx=6, pady=(6,10))

    # Key label + entry
    lbl_key = tk.Label(card, text="Key (hidden):", fg=TEXT, bg=BG, font=FONT_BOLD)
    lbl_key.grid(row=2, column=0, sticky="w", padx=6, pady=(4,0))

    key_entry = tk.Entry(card, show="●", width=36, bg=CARD, fg="#cfc6ff", font=FONT_MONO, insertbackground=TEXT)
    key_entry.grid(row=3, column=0, sticky="w", padx=6, pady=(6,10))

    # Output label + box
    lbl_out = tk.Label(card, text="Output / Debug Messages:", fg=TEXT, bg=BG, font=FONT_BOLD)
    lbl_out.grid(row=4, column=0, sticky="w", padx=6, pady=(4,0))

    output_box = scrolledtext.ScrolledText(card, width=96, height=10, bg=CARD, fg=TEXT, font=FONT_MONO, insertbackground=TEXT)
    output_box.grid(row=5, column=0, padx=6, pady=(6,10))

    # Buttons frame
    btn_frame = tk.Frame(card, bg=BG)
    btn_frame.grid(row=6, column=0, pady=8)

    # Encrypt button
    def on_encrypt():
        text = input_box.get("1.0", "end").strip()
        key = key_entry.get().strip()
        if not text:
            messagebox.showwarning("Missing input", "Please enter plaintext to encrypt.")
            return
        if not key:
            messagebox.showwarning("Missing key", "Please enter the key.")
            return
        try:
            out = encrypt(text, key)
            output_box.delete("1.0", "end")
            output_box.insert("end", out)
        except Exception as e:
            output_box.delete("1.0", "end")
            output_box.insert("end", f"Encryption error:\n{e}")

    btn_encrypt = tk.Button(btn_frame, text="ENCRYPT 🔒", command=on_encrypt,
                            bg=ACCENT, fg="white", font=FONT_BOLD, width=18, relief="flat", bd=0)
    btn_encrypt.grid(row=0, column=0, padx=8)
    add_hover(btn_encrypt)

    # Decrypt button
    def on_decrypt():
        text = input_box.get("1.0", "end").strip()
        key = key_entry.get().strip()
        if not text:
            messagebox.showwarning("Missing input", "Please paste emoji ciphertext to decrypt.")
            return
        if not key:
            messagebox.showwarning("Missing key", "Please enter the key.")
            return
        try:
            out = decrypt(text, key)
            output_box.delete("1.0", "end")
            output_box.insert("end", out)
        except Exception as e:
            output_box.delete("1.0", "end")
            output_box.insert("end", f"Decryption error:\n\n{e}")
            messagebox.showerror("Decryption failed", "See output box for details.")

    btn_decrypt = tk.Button(btn_frame, text="DECRYPT 🔓", command=on_decrypt,
                            bg=ACCENT, fg="white", font=FONT_BOLD, width=18, relief="flat", bd=0)
    btn_decrypt.grid(row=0, column=1, padx=8)
    add_hover(btn_decrypt)

    # Inspect codepoints button
    def on_inspect():
        txt = input_box.get("1.0", "end").strip()
        if not txt:
            messagebox.showwarning("Missing input", "Paste some emoji/text into the input box first.")
            return
        snippet = txt[:60]
        lines = [f"{i}: {repr(ch)}  →  U+{ord(ch):04X}" for i, ch in enumerate(snippet)]
        output_box.delete("1.0", "end")
        output_box.insert("end", "First characters and their Unicode codepoints:\n\n" + "\n".join(lines))

    btn_inspect = tk.Button(btn_frame, text="INSPECT CODEPOINTS 🧪", command=on_inspect,
                            bg="#3aa0ff", fg="white", font=FONT_BOLD, width=22, relief="flat", bd=0)
    btn_inspect.grid(row=0, column=2, padx=8)
    add_hover(btn_inspect, on_color="#60c8ff", off_color="#3aa0ff")

    # Copy output button
    def on_copy_output():
        out = output_box.get("1.0", "end").strip()
        if not out:
            messagebox.showinfo("Nothing to copy", "Output box is empty.")
            return
        root.clipboard_clear()
        root.clipboard_append(out)
        messagebox.showinfo("Copied", "Output copied to clipboard.")

    btn_copy = tk.Button(btn_frame, text="COPY OUTPUT 📋", command=on_copy_output,
                         bg="#22c55e", fg="white", font=FONT_BOLD, width=16, relief="flat", bd=0)
    btn_copy.grid(row=0, column=3, padx=8)
    add_hover(btn_copy, on_color="#43e77b", off_color="#22c55e")

    # Clear all button
    def on_clear():
        input_box.delete("1.0", "end")
        output_box.delete("1.0", "end")
        key_entry.delete(0, "end")

    btn_clear = tk.Button(btn_frame, text="CLEAR ✖", command=on_clear,
                          bg="#ef4444", fg="white", font=FONT_BOLD, width=12, relief="flat", bd=0)
    btn_clear.grid(row=0, column=4, padx=8)
    add_hover(btn_clear, on_color="#ff6b6b", off_color="#ef4444")

    root.mainloop()

if __name__ == "__main__":
    run_gui()
