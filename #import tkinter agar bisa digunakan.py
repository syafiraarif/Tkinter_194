#import tkinter agar bisa digunakan 
import tkinter as tk
#setelah mengimport tkinter import juga untuk messagebox dari tkinternya 
from tkinter import messagebox

#buat fungsi untuk memvalidasi input dan menampilkan hasil prediksi
def hasilprediksi():
    try:
        #membuat loop untuk memeriksa setiap entry dalam entries
        for entry in entries:
            #memberikan type data untuksetiap entry berupa type int
            nilai = int(entry.get())
            #nilai harus antara 0 sampai 100 aja, kalo ga nnti program bakal manggil exception 
            if not (0<= nilai <= 100):
                raise ValueError("Nilai harus antara 0 dan 100.")
        #menampilkan hasil prediksi jika nilai yang di input sesuai dengan syarat yang ada
        hasil_label.config(text ="prediksi prodi: Teknologi Informasi")
    except ValueError as ve:
        #memberikan pesan error jika nilai yang di masukan tidak sesuai
        messagebox.showerror("input error", "pastikan semua input adalah angka antara 0 sampai 100 ")


#buat objek utama 
root = tk.Tk()
#membuat judul untuk aplikasi yang letaknya di atas jendela
root.title("aplikasi prediksi prodi pilihan")
#membuat ukuran jendela
root.geometry("500x600")
#membuat background
root.configure(bg="#f0f0f0")

#membuat label judul
judul_label = tk.Label(root, text ="aplikasi prediksi prodi pilihan", font =("arial", 16))
# Menempatkan label judul di jendela dengan padding
judul_label.pack(pady = 20)


#frame untuk input nilai mata pelajaran
frame_input = tk.Frame(root, bg="#f0f0f0")
# Menempatkan frame di jendela dengan padding
frame_input.pack(pady =10)


#entries untuk menyimpan entry input nilai
entries = []
# Loop untuk membuat 10 input nilai mata pelajaran
for i in range(10):
     # Membuat label untuk setiap input mata pelajaran
    label = tk.Label(frame_input, text=f"nilai mata pelajaran {i+1}:", font=("Arial", 12))
    # Menempatkan label di grid frame
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
    # Membuat entry untuk menginput nilai
    entry = tk.Entry(frame_input, width=10, font=("Arial", 12))
    # Menempatkan entry di grid frame
    entry.grid(row=i, column=1, padx=10, pady=5)
    # Menambahkan entry ke dalam list entries
    entries.append(entry)


# Membuat tombol untuk mengaktifkan fungsi hasilprediksi
prediksi_button = tk.Button(root, text="hasil prediksi", command=hasilprediksi, font=("arial", 12))
# Menempatkan tombol di jendela dengan padding
prediksi_button.pack(pady=30)

# Label untuk menampilkan hasil prediksi setelah tombol ditekan
hasil_label = tk.Label(root, text="", font=("arial", 14, "italic", "bold"), fg="green", bg="#f0f0f0")
# Menempatkan label hasil di jendela dengan padding
hasil_label.pack(pady=20)

#menjalankan program
root.mainloop()