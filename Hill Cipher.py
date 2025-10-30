import numpy as np

# Fungsi enkripsi
def hill_encrypt(text, key):
    text = text.upper().replace(" ", "")
    n = int(len(key) ** 0.5)
    key = np.array(key).reshape(n, n)

    # Padding jika panjang text tidak kelipatan n
    while len(text) % n != 0:
        text += "X"

    result = ""
    for i in range(0, len(text), n):
        block = [ord(c) - 65 for c in text[i:i+n]]
        cipher = np.dot(key, block) % 26
        result += "".join(chr(c + 65) for c in cipher)
    return result

# Fungsi dekripsi
def hill_decrypt(cipher, key):
    cipher = cipher.upper().replace(" ", "")
    n = int(len(key) ** 0.5)
    key = np.array(key).reshape(n, n)

    # Invers matrix mod 26
    det = int(np.round(np.linalg.det(key)))
    det_inv = pow(det % 26, -1, 26)
    adj = np.round(det * np.linalg.inv(key)).astype(int) % 26
    inv_key = (det_inv * adj) % 26

    result = ""
    for i in range(0, len(cipher), n):
        block = [ord(c) - 65 for c in cipher[i:i+n]]
        plain = np.dot(inv_key, block) % 26
        result += "".join(chr(int(p) + 65) for p in plain)
    return result

# Fungsi simpan file otomatis
def save_to_txt(original, encrypted, decrypted):
    filename = "hasil_hill_cipher.txt"
    with open(filename, "w") as file:
        file.write("=== HILL CIPHER RESULT ===\n")
        file.write(f"Plaintext      : {original}\n")
        file.write(f"Encrypt        : {encrypted}\n")
        file.write(f"Decrypt        : {decrypted}\n")
    print(f"\n✅ Hasil otomatis disimpan ke {filename}")

# MAIN PROGRAM
text = input("Masukkan teks: ")
key = [3, 3, 2, 5]  # Key 2x2 dari dosen

encrypted = hill_encrypt(text, key)
decrypted = hill_decrypt(encrypted, key)

print("\n=== HILL CIPHER RESULT ===")
print(f"Plaintext      : {text.upper()}")
print(f"Encrypt        : {encrypted}")
print(f"Decrypt        : {decrypted}")

# Auto save tanpa pertanyaan
save_to_txt(text.upper(), encrypted, decrypted)
