import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class ResepMasakanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Resep Masakan Sederhana")
        self.root.geometry("800x600")
        
        self.resep_data = [
            {
                "judul": "Nasi Goreng",
                "bahan": ["nasi", "telur", "bawang merah", "kecap", "garam"],
                "langkah": "1. Tumis bawang\n2. Masukkan nasi\n3. Tambahkan kecap",
                "waktu": 20,
                "tanggal": "2023-05-01"
            },
            {
                "judul": "Mie Goreng",
                "bahan": ["mie", "telur", "sawi", "kecap", "bawang putih"],
                "langkah": "1. Rebus mie\n2. Tumis bumbu\n3. Campur dengan mie",
                "waktu": 15,
                "tanggal": "2023-05-02"
            },
                        {
                "judul": "Nasi Cumi Hitam Pak Kris",
                "bahan": ["nasi", "cumi-cumi", "sawi", "kecap", "bawang putih","saos tiram","msg"],
                "langkah": "1. Rebus cumi\n2. Tumis bumbu\n3. Campur dengan cumi dan nasi\n4. Nikmati",
                "waktu": 35,
                "tanggal": "2023-05-02"
            }
        ]
        
        self.setup_ui()
        self.riwayat_hapus = []
    
    def setup_ui(self):
        # Frame utama
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Frame pencarian
        search_frame = ttk.LabelFrame(main_frame, text="Pencarian Resep", padding="10")
        search_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(search_frame, text="Cari berdasarkan:").grid(row=0, column=0, padx=5)
        self.search_type = tk.StringVar(value="judul")
        ttk.Radiobutton(search_frame, text="Judul", variable=self.search_type, value="judul").grid(row=0, column=1, padx=5)
        ttk.Radiobutton(search_frame, text="Bahan", variable=self.search_type, value="bahan").grid(row=0, column=2, padx=5)
        
        self.search_entry = ttk.Entry(search_frame, width=40)
        self.search_entry.grid(row=0, column=3, padx=5)
        ttk.Button(search_frame, text="Cari", command=self.cari_resep).grid(row=0, column=4, padx=5)
        
        # Frame pengurutan
        sort_frame = ttk.LabelFrame(main_frame, text="Pengurutan", padding="10")
        sort_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(sort_frame, text="Urutkan berdasarkan:").grid(row=0, column=0, padx=5)
        self.sort_type = tk.StringVar(value="judul")
        ttk.Radiobutton(sort_frame, text="Judul (A-Z)", variable=self.sort_type, value="judul").grid(row=0, column=1, padx=5)
        ttk.Radiobutton(sort_frame, text="Waktu Masak (tercepat)", variable=self.sort_type, value="waktuC").grid(row=0, column=2, padx=5)
        ttk.Radiobutton(sort_frame, text="Waktu Masak (terlama)", variable=self.sort_type, value="waktuL").grid(row=0, column=3, padx=5)
        ttk.Button(sort_frame, text="Urutkan", command=self.urutkan_resep).grid(row=0, column=4, padx=5)
        
        # Frame daftar resep
        list_frame = ttk.LabelFrame(main_frame, text="Daftar Resep", padding="10")
        list_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Treeview untuk daftar resep
        self.tree = ttk.Treeview(list_frame, columns=("Judul", "Bahan", "Waktu", "Tanggal"), show="headings")
        self.tree.heading("Judul", text="Judul")
        self.tree.heading("Bahan", text="Bahan Utama")
        self.tree.heading("Waktu", text="Waktu (menit)")
        self.tree.heading("Tanggal", text="Tanggal Ditambahkan")
        
        self.tree.column("Judul", width=150)
        self.tree.column("Bahan", width=150)
        self.tree.column("Waktu", width=80)
        self.tree.column("Tanggal", width=100)
        
        self.tree.pack(fill=tk.BOTH, expand=True)
        self.tree.bind("<Double-1>", self.tampilkan_detail_resep)
        
        # Frame tombol aksi
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(button_frame, text="Tambah Resep", command=self.tambah_resep).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Edit Resep", command=self.edit_resep).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Hapus Resep", command=self.hapus_resep).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Riwayat Hapus", command=self.tampilkan_riwayat_hapus).pack(side=tk.LEFT, padx=5)
        
        # Memuat data awal2
        self.tampilkan_daftar_resep(self.resep_data)
    
##############################################################################################################################
    
    def tampilkan_daftar_resep(self, resep_list):
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        for resep in resep_list:
            bahan_utama = ", ".join(resep["bahan"][:2]) + ("..." if len(resep["bahan"]) > 2 else "") #hiasan untuk tampilan yg lebih dri 2 bahan
            self.tree.insert("", tk.END, values=(
                resep["judul"],
                bahan_utama,
                resep["waktu"],
                resep["tanggal"]
            ))
    
##############################################################################################################################

    def tampilkan_detail_resep(self, event=None):
        selected_item = self.tree.focus()
        if not selected_item:
            return
        
        item_data = self.tree.item(selected_item)
        judul = item_data["values"][0]
        
        # Cari resep yang sesuai
        resep = next((r for r in self.resep_data if r["judul"] == judul), None)
        if not resep:
            return
        
        # Buat window detail
        detail_window = tk.Toplevel(self.root)
        detail_window.title(f"Detail Resep: {judul}")
        detail_window.geometry("600x400")
        
        # Frame detail
        detail_frame = ttk.Frame(detail_window, padding="10")
        detail_frame.pack(fill=tk.BOTH, expand=True)
        
        # Judul
        ttk.Label(detail_frame, text=resep["judul"], font=("Arial", 14, "bold")).pack(pady=5)
        
        # Bahan-bahan
        bahan_frame = ttk.LabelFrame(detail_frame, text="Bahan-bahan", padding="10")
        bahan_frame.pack(fill=tk.X, pady=5)
        
        for bahan in resep["bahan"]:
            ttk.Label(bahan_frame, text=f"- {bahan}").pack(anchor=tk.W)
        
        # Langkah-langkah
        langkah_frame = ttk.LabelFrame(detail_frame, text="Langkah-langkah", padding="10")
        langkah_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        langkah_text = tk.Text(langkah_frame, wrap=tk.WORD, height=10)
        langkah_text.insert(tk.END, resep["langkah"])
        langkah_text.config(state=tk.DISABLED)
        langkah_text.pack(fill=tk.BOTH, expand=True)
        
        # Info tambahan
        info_frame = ttk.Frame(detail_frame)
        info_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(info_frame, text=f"Waktu memasak: {resep['waktu']} menit").pack(side=tk.LEFT)
        ttk.Label(info_frame, text=f"Ditambahkan pada: {resep['tanggal']}", padding=(10, 0)).pack(side=tk.LEFT)
        
##############################################################################################################################

    def cari_resep(self):
        keyword = self.search_entry.get().lower()
        search_type = self.search_type.get()
        
        if not keyword:
            self.tampilkan_daftar_resep(self.resep_data)
            return
        
        hasil_pencarian = []
        for resep in self.resep_data:
            if search_type == "judul" and keyword in resep["judul"].lower():
                hasil_pencarian.append(resep)
            elif search_type == "bahan" and any(keyword in bahan.lower() for bahan in resep["bahan"]):
                hasil_pencarian.append(resep)
        
        self.tampilkan_daftar_resep(hasil_pencarian)
        
##############################################################################################################################

##############################################################################################################################

    def urutkan_resep(self):
        sort_type = self.sort_type.get()
    
        if sort_type == "judul":
            sorted_resep = self.quick_sort_str(self.resep_data.copy(), key=lambda x: x["judul"])
        elif sort_type == "waktuC":
            sorted_resep = self.quick_sort_asc(self.resep_data.copy(), key=lambda x: x["waktu"])
        elif sort_type == "waktuL":
            sorted_resep = self.quick_sort_desc(self.resep_data.copy(), key=lambda x: x["waktu"])
        else:
            sorted_resep = self.resep_data.copy()
    
        self.tampilkan_daftar_resep(sorted_resep)

    def quick_sort_str(self, data, key=lambda x: x):
        """Quick Sort untuk string (case-insensitive ascending)"""
        if len(data) <= 1:
            return data
    
        pivot = data[len(data) // 2]
        left = [x for x in data if key(x).lower() < key(pivot).lower()]
        middle = [x for x in data if key(x).lower() == key(pivot).lower()]
        right = [x for x in data if key(x).lower() > key(pivot).lower()]
    
        return self.quick_sort_str(left, key) + middle + self.quick_sort_str(right, key)

    def quick_sort_asc(self, data, key=lambda x: x):
        """Quick Sort untuk angka (ascending)"""
        if len(data) <= 1:
            return data
    
        pivot = data[len(data) // 2]
        left = [x for x in data if key(x) < key(pivot)]
        middle = [x for x in data if key(x) == key(pivot)]
        right = [x for x in data if key(x) > key(pivot)]
    
        return self.quick_sort_asc(left, key) + middle + self.quick_sort_asc(right, key)

    def quick_sort_desc(self, data, key=lambda x: x):
        """Quick Sort untuk angka (descending)"""
        if len(data) <= 1:
            return data
    
        pivot = data[len(data) // 2]
        left = [x for x in data if key(x) > key(pivot)]
        middle = [x for x in data if key(x) == key(pivot)]
        right = [x for x in data if key(x) < key(pivot)]
    
        return self.quick_sort_desc(left, key) + middle + self.quick_sort_desc(right, key)
    
##############################################################################################################################

##############################################################################################################################

    #CREATE
    def tambah_resep(self):
        self.form_resep_window("Tambah Resep Baru")
    #UPDATE
    def edit_resep(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Silakan pilih resep yang akan diedit")
            return
        
        item_data = self.tree.item(selected_item)
        judul = item_data["values"][0]
        
        resep = next((r for r in self.resep_data if r["judul"].lower() == judul.lower()), None)
        if not resep:
            return
        
        self.form_resep_window("Edit Resep", resep)
    #DELETE
    def hapus_resep(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Silakan pilih resep yang akan dihapus")
            return
        
        item_data = self.tree.item(selected_item)
        judul = item_data["values"][0]        

        if messagebox.askyesno("Konfirmasi", f"Apakah Anda yakin ingin menghapus resep '{judul}'?"):
            # Cari resep yang akan dihapus
            resep_dihapus = next((r for r in self.resep_data if r["judul"] == judul), None)
            
            if resep_dihapus:
                # Pindahkan ke riwayat hapus
                self.riwayat_hapus.append(resep_dihapus)
                
                # Hapus dari data aktif
                self.resep_data = [r for r in self.resep_data if r["judul"] != judul]
                self.tampilkan_daftar_resep(self.resep_data)
                messagebox.showinfo("Info", "Resep berhasil dihapus")

    def form_resep_window(self, title, resep=None):
        is_edit = resep is not None
        
        form_window = tk.Toplevel(self.root)
        form_window.title(title)
        form_window.geometry("500x600")
        
        # Frame form
        form_frame = ttk.Frame(form_window, padding="10")
        form_frame.pack(fill=tk.BOTH, expand=True)
        
        # Judul
        ttk.Label(form_frame, text="Judul Resep:").pack(anchor=tk.W, pady=(5, 0))
        judul_entry = ttk.Entry(form_frame, width=40)
        judul_entry.pack(fill=tk.X, pady=(0, 10))
        
        # Bahan-bahan
        ttk.Label(form_frame, text="Bahan-bahan (pisahkan dengan koma):").pack(anchor=tk.W, pady=(5, 0))
        bahan_text = tk.Text(form_frame, height=5, wrap=tk.WORD)
        bahan_text.pack(fill=tk.X, pady=(0, 10))
        
        # Langkah-langkah
        ttk.Label(form_frame, text="Langkah-langkah:").pack(anchor=tk.W, pady=(5, 0))
        langkah_text = tk.Text(form_frame, height=10, wrap=tk.WORD)
        langkah_text.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Waktu masak
        waktu_frame = ttk.Frame(form_frame)
        waktu_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(waktu_frame, text="Waktu masak (menit):").pack(side=tk.LEFT)
        waktu_entry = ttk.Entry(waktu_frame, width=10)
        waktu_entry.pack(side=tk.LEFT, padx=5)
        
        # Tombol simpan/batal
        button_frame = ttk.Frame(form_frame)
        button_frame.pack(fill=tk.X, pady=10)
        
        #simpan resep
        ttk.Button(button_frame, text="Simpan", command=lambda: self.simpan_resep(
            form_window,
            judul_entry.get(),
            bahan_text.get("1.0", tk.END).strip(),
            langkah_text.get("1.0", tk.END).strip(),
            waktu_entry.get(),
            is_edit,
            resep["judul"] if is_edit else None
        )).pack(side=tk.RIGHT, padx=5)
        
        ttk.Button(button_frame, text="Batal", command=form_window.destroy).pack(side=tk.RIGHT)
        
        #tampilin data klo lagi ngedit
        if is_edit:
            judul_entry.insert(0, resep["judul"])
            bahan_text.insert(tk.END, ", ".join(resep["bahan"]))
            langkah_text.insert(tk.END, resep["langkah"])
            waktu_entry.insert(0, str(resep["waktu"]))

    def tampilkan_riwayat_hapus(self):
        if not self.riwayat_hapus:
            messagebox.showinfo("Info", "Tidak ada resep yang dihapus")
            return
            
        # Buat window baru untuk menampilkan riwayat
        riwayat_window = tk.Toplevel(self.root)
        riwayat_window.title("Riwayat Resep Dihapus")
        riwayat_window.geometry("600x400")
        
        # Frame untuk daftar resep dihapus
        list_frame = ttk.Frame(riwayat_window, padding="10")
        list_frame.pack(fill=tk.BOTH, expand=True)
        
        # Treeview untuk menampilkan resep dihapus
        tree = ttk.Treeview(list_frame, columns=("Judul", "Waktu", "Tanggal"), show="headings")
        tree.heading("Judul", text="Judul")
        tree.heading("Waktu", text="Waktu (menit)")
        tree.heading("Tanggal", text="Tanggal Ditambahkan")
        
        tree.column("Judul", width=200)
        tree.column("Waktu", width=100)
        tree.column("Tanggal", width=100)
        
        tree.pack(fill=tk.BOTH, expand=True)
        
        # Isi data
        for resep in self.riwayat_hapus:
            tree.insert("", tk.END, values=(
                resep["judul"],
                resep["waktu"],
                resep["tanggal"]
            ))
        
        # Frame untuk tombol aksi
        button_frame = ttk.Frame(riwayat_window)
        button_frame.pack(fill=tk.X, pady=5)
        
        # Tombol restore
        ttk.Button(button_frame, text="Restore Resep", 
                  command=lambda: self.restore_resep(tree)).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(button_frame, text="Tutup", 
                  command=riwayat_window.destroy).pack(side=tk.RIGHT, padx=5)

    def restore_resep(self, tree):
        selected_item = tree.focus()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Silakan pilih resep yang akan dikembalikan")
            return
            
        item_data = tree.item(selected_item)
        judul = item_data["values"][0]
        
        resep = next((r for r in self.riwayat_hapus if r["judul"] == judul), None)
        
        if resep:
            self.resep_data.append(resep)

            self.riwayat_hapus = [r for r in self.riwayat_hapus if r["judul"] != judul]
            
            self.tampilkan_daftar_resep(self.resep_data)

            if not self.riwayat_hapus:
                tree.master.destroy()
                
            messagebox.showinfo("Info", f"Resep '{judul}' berhasil dikembalikan")
            
##############################################################################################################################
    

    
    def simpan_resep(self, window, judul, bahan_str, langkah, waktu_str, is_edit, old_judul=None):

        if not judul or not bahan_str or not langkah or not waktu_str:
            messagebox.showwarning("Peringatan", "Semua field harus diisi!")
            return
        
        try:
            waktu = int(waktu_str)
            if waktu <= 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Peringatan", "Waktu masak harus berupa angka positif!")
            return
        
        bahan_list = [b.strip() for b in bahan_str.split(",") if b.strip()]
        if not bahan_list:
            messagebox.showwarning("Peringatan", "Masukkan minimal satu bahan!")
            return
        
        if (not is_edit and any(r["judul"].lower() == judul.lower() for r in self.resep_data)) or \
           (is_edit and judul.lower() != old_judul.lower() and any(r["judul"].lower() == judul.lower() for r in self.resep_data)):
            messagebox.showwarning("Peringatan", "Resep dengan judul tersebut sudah ada!")
            return
        
        resep_baru = {
            "judul": judul,
            "bahan": bahan_list,
            "langkah": langkah,
            "waktu": waktu,
            "tanggal": datetime.now().strftime("%Y-%m-%d")
        }
        
        if is_edit:
            #Edit resep
            for i, resep in enumerate(self.resep_data):
                if resep["judul"] == old_judul:
                    self.resep_data[i] = resep_baru
                    break
            messagebox.showinfo("Info", "Resep berhasil diperbarui")
        else:
            #Tambah resep 
            self.resep_data.append(resep_baru)
            messagebox.showinfo("Info", "Resep baru berhasil ditambahkan")
        
        window.destroy()
        self.tampilkan_daftar_resep(self.resep_data)

if __name__ == "__main__":
    root = tk.Tk()
    app = ResepMasakanApp(root)
    root.mainloop()