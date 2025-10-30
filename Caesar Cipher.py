def caesar_encrypt(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# ==== AUTO EXECUTE ====
plain_text = input("Masukkan teks: ")
shift = int(input("Masukkan shift (angka): "))

encrypted_text = caesar_encrypt(plain_text, shift)
decrypted_text = caesar_decrypt(encrypted_text, shift)

print("\n===== HASIL =====")
print(f"Plaintext  : {plain_text}")
print(f"Shift      : {shift}")
print(f"Encrypt    : {encrypted_text}")
print(f"Decrypt    : {decrypted_text}")

# Save to TXT
with open("hasil_caesar.txt", "w") as file:
    file.write(f"Plaintext  : {plain_text}\n")
    file.write(f"Shift      : {shift}\n")
    file.write(f"Encrypt    : {encrypted_text}\n")
    file.write(f"Decrypt    : {decrypted_text}\n")

print("\nHasil disimpan ke file 'hasil_caesar.txt' ✅")
