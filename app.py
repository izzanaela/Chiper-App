import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import numpy as np

class CipherApp:
    def __init__(self, master):
        self.master = master
        master.title("Aplikasi Cipher")
        master.geometry("600x500")

        # Komponen GUI
        ttk.Label(master, text="Pilih Jenis Cipher:").grid(row=0, column=0, padx=5, pady=5)
        self.cipher_type = ttk.Combobox(master, values=["Vigenere", "Playfair", "Hill"])
        self.cipher_type.grid(row=0, column=1, padx=5, pady=5)
        self.cipher_type.set("Vigenere")

        ttk.Label(master, text="Mode:").grid(row=1, column=0, padx=5, pady=5)
        self.mode = ttk.Combobox(master, values=["Enkripsi", "Dekripsi"])
        self.mode.grid(row=1, column=1, padx=5, pady=5)
        self.mode.set("Enkripsi")

        ttk.Label(master, text="Kunci (min. 12 karakter):").grid(row=2, column=0, padx=5, pady=5)
        self.key = ttk.Entry(master, width=40)
        self.key.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(master, text="Pesan:").grid(row=3, column=0, padx=5, pady=5)
        self.text = tk.Text(master, height=10, width=50)
        self.text.grid(row=3, column=1, padx=5, pady=5)

        ttk.Button(master, text="Pilih File", command=self.load_file).grid(row=4, column=0, padx=5, pady=5)
        ttk.Button(master, text="Proses", command=self.process).grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(master, text="Hasil:").grid(row=5, column=0, padx=5, pady=5)
        self.result = tk.Text(master, height=10, width=50)
        self.result.grid(row=5, column=1, padx=5, pady=5)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                self.text.delete('1.0', tk.END)
                self.text.insert(tk.END, file.read())

    def process(self):
        cipher_type = self.cipher_type.get()
        mode = self.mode.get()
        key = self.key.get()
        text = self.text.get('1.0', tk.END).strip()

        if len(key) < 12:
            messagebox.showerror("Error", "Kunci harus memiliki panjang minimal 12 karakter.")
            return

        if cipher_type == "Vigenere":
            result = self.vigenere_cipher(text, key, mode)
        elif cipher_type == "Playfair":
            result = self.playfair_cipher(text, key, mode)
        elif cipher_type == "Hill":
            result = self.hill_cipher(text, key, mode)
        else:
            messagebox.showerror("Error", "Tipe cipher tidak valid.")
            return

        self.result.delete('1.0', tk.END)
        self.result.insert(tk.END, result)

    def vigenere_cipher(self, text, key, mode):
        result = ""
        key_length = len(key)
        key = key.upper()
        for i, char in enumerate(text):
            if char.isalpha():
                shift = ord(key[i % key_length]) - ord('A')
                if mode == "Enkripsi":
                    result += chr((ord(char.upper()) - ord('A') + shift) % 26 + ord('A'))
                else:
                    result += chr((ord(char.upper()) - ord('A') - shift) % 26 + ord('A'))
            else:
                result += char
        return result

    def create_playfair_matrix(self, key):
        key = ''.join(dict.fromkeys(key.upper().replace("J", "I") + "ABCDEFGHIKLMNOPQRSTUVWXYZ"))
        return [list(key[i:i+5]) for i in range(0, 25, 5)]  
     
    def playfair_cipher(self, text, key, mode):
        matrix = self.create_playfair_matrix(key)
        text = text.upper().replace("J", "I")
        text = ''.join(char for char in text if char.isalpha())
        if len(text) % 2 != 0:
            text += "X"
        result = ""
        for i in range(0, len(text), 2):
            a, b = text[i], text[i+1]
            try:
                row_a, col_a = next((r, c) for r, row in enumerate(matrix) for c, char in enumerate(row) if char == a)
                row_b, col_b = next((r, c) for r, row in enumerate(matrix) for c, char in enumerate(row) if char == b)
            except StopIteration:
                continue
            
            if row_a == row_b:
                if mode == "Enkripsi":
                    result += matrix[row_a][(col_a + 1) % 5] + matrix[row_b][(col_b + 1) % 5]
                else:
                    result += matrix[row_a][(col_a - 1) % 5] + matrix[row_b][(col_b - 1) % 5]
            elif col_a == col_b:
                if mode == "Enkripsi":
                    result += matrix[(row_a + 1) % 5][col_a] + matrix[(row_b + 1) % 5][col_b]
                else:
                    result += matrix[(row_a - 1) % 5][col_a] + matrix[(row_b - 1) % 5][col_b]
            else:
                result += matrix[row_a][col_b] + matrix[row_b][col_a]
        return result

    def hill_cipher(self, text, key, mode):
        key_matrix = np.array([ord(c) - ord('A') for c in key.upper()[:9]]).reshape(3, 3)
        text = text.upper()
        result = ""
        for i in range(0, len(text), 3):
            chunk = text[i:i+3].ljust(3, 'X')
            chunk_vector = np.array([ord(c) - ord('A') for c in chunk])
            if mode == "Enkripsi":
                encrypted_vector = np.dot(key_matrix, chunk_vector) % 26
            else:
                key_matrix_inv = np.linalg.inv(key_matrix)
                key_matrix_inv = (key_matrix_inv * np.linalg.det(key_matrix)) % 26
                encrypted_vector = np.dot(key_matrix_inv, chunk_vector) % 26
            result += ''.join([chr(int(v) + ord('A')) for v in encrypted_vector])
        return result

if __name__ == "__main__":
    root = tk.Tk()
    app = CipherApp(root)
    root.mainloop()