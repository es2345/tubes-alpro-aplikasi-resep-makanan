import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class Resep:
    def __init__(self, judul="", bahan=None, langkah="", waktu=0, tanggal=""):
        self.judul = judul
        self.bahan = bahan if bahan is not None else [""]*10  # Array statis bahan (max 10)
        self.jumlah_bahan = 0
        self.langkah = langkah
        self.waktu = waktu
        self.tanggal = tanggal

class ResepMasakanApp:
    MAX_RESEP = 100  # Batas maksimal resep
    
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Resep Masakan Sederhana")
        self.root.geometry("800x600")
        
        # Array statis untuk resep
        self.resep_data = [Resep() for _ in range(self.MAX_RESEP)]
        self.jumlah_resep = 10  # Resep awal yang diisi
        
        # Inisialisasi resep awal
        self._init_resep_awal()
        
        # Array untuk riwayat hapus
        self.riwayat_hapus = [Resep() for _ in range(self.MAX_RESEP)]
        self.jumlah_riwayat = 0
        
        self.setup_ui()
    
    def _init_resep_awal(self):
        # Resep 1
        self.resep_data[0].judul = "Nasi Goreng"
        self.resep_data[0].bahan = ["nasi", "telur", "bawang merah", "kecap", "garam"] + [""]*5
        self.resep_data[0].jumlah_bahan = 5
        self.resep_data[0].langkah = "1. Tumis bawang\n2. Masukkan nasi\n3. Tambahkan kecap"
        self.resep_data[0].waktu = 20
        self.resep_data[0].tanggal = "2023-05-01"
        
        # Resep 2
        self.resep_data[1].judul = "Mie Goreng"
        self.resep_data[1].bahan = ["mie", "telur", "sawi", "kecap", "bawang putih"] + [""]*5
        self.resep_data[1].jumlah_bahan = 5
        self.resep_data[1].langkah = "1. Rebus mie\n2. Tumis bumbu\n3. Campur dengan mie"
        self.resep_data[1].waktu = 15
        self.resep_data[1].tanggal = "2023-05-02"
        
        # Resep 3
        self.resep_data[2].judul = "Nasi Cumi Hitam Pak Kris"
        self.resep_data[2].bahan = ["nasi", "cumi-cumi", "sawi", "kecap", "bawang putih", "saos tiram", "msg"] + [""]*3
        self.resep_data[2].jumlah_bahan = 7
        self.resep_data[2].langkah = "1. Rebus cumi\n2. Tumis bumbu\n3. Campur dengan cumi dan nasi\n4. Nikmati"
        self.resep_data[2].waktu = 35
        self.resep_data[2].tanggal = "2023-05-02"
        
        # Resep 4
        self.resep_data[3].judul = "Soto Ayam Lamongan"
        self.resep_data[3].bahan = ["ayam", "bihun", "kol", "seledri", "bawang goreng", "koya", "jeruk nipis"] + [""]*3
        self.resep_data[3].jumlah_bahan = 7
        self.resep_data[3].langkah = "1. Rebus ayam dengan bumbu\n2. Saring kuah\n3. Sajikan dengan pelengkap"
        self.resep_data[3].waktu = 60
        self.resep_data[3].tanggal = "2023-05-03"

        # Resep 5
        self.resep_data[4].judul = "Rendang Daging Padang"
        self.resep_data[4].bahan = ["daging sapi", "santan", "kelapa parut", "cabe merah", "bawang merah", "lengkuas", "daun jeruk"] + [""]*3
        self.resep_data[4].jumlah_bahan = 7
        self.resep_data[4].langkah = "1. Tumis bumbu halus\n2. Masukkan daging\n3. Masak hingga empuk dan kering"
        self.resep_data[4].waktu = 180
        self.resep_data[4].tanggal = "2023-05-04"

        # Resep 6
        self.resep_data[5].judul = "Gado-Gado Jakarta"
        self.resep_data[5].bahan = ["lontong", "tahu", "tempe", "sayuran", "telur", "kerupuk", "bumbu kacang"] + [""]*3
        self.resep_data[5].jumlah_bahan = 7
        self.resep_data[5].langkah = "1. Rebus sayuran\n2. Goreng tahu/tempe\n3. Siram dengan bumbu kacang"
        self.resep_data[5].waktu = 45
        self.resep_data[5].tanggal = "2023-05-05"

        # Resep 7
        self.resep_data[6].judul = "Rawon Daging Sapi"
        self.resep_data[6].bahan = ["daging sapi", "keluak", "daun bawang", "tauge", "sambal", "telur asin", "bawang goreng"] + [""]*3
        self.resep_data[6].jumlah_bahan = 7
        self.resep_data[6].langkah = "1. Rebus daging dengan bumbu\n2. Tambahkan keluak\n3. Sajikan dengan pelengkap"
        self.resep_data[6].waktu = 90
        self.resep_data[6].tanggal = "2023-05-06"

        # Resep 8
        self.resep_data[7].judul = "Pempek Palembang"
        self.resep_data[7].bahan = ["ikan giling", "tepung sagu", "telur", "air", "garam", "cuka", "cuko"] + [""]*3
        self.resep_data[7].jumlah_bahan = 7
        self.resep_data[7].langkah = "1. Campur bahan adonan\n2. Bentuk pempek\n3. Rebus/goreng\n4. Sajikan dengan cuko"
        self.resep_data[7].waktu = 75
        self.resep_data[7].tanggal = "2023-05-07"

        # Resep 9
        self.resep_data[8].judul = "Bakso Malang"
        self.resep_data[8].bahan = ["daging sapi", "tepung tapioka", "bawang putih", "garam", "mi kuning", "tahu", "kuah kaldu"] + [""]*3
        self.resep_data[8].jumlah_bahan = 7
        self.resep_data[8].langkah = "1. Buat adonan bakso\n2. Rebus bulatan bakso\n3. Sajikan dengan mi dan kuah"
        self.resep_data[8].waktu = 65
        self.resep_data[8].tanggal = "2023-05-08"

        # Resep 10
        self.resep_data[9].judul = "Sate Madura"
        self.resep_data[9].bahan = ["daging ayam", "kacang tanah", "kecap", "bawang merah", "jeruk limau", "lontong", "sambal"] + [""]*3
        self.resep_data[9].jumlah_bahan = 7
        self.resep_data[9].langkah = "1. Tusuk daging\n2. Bakar sate\n3. Sajikan dengan bumbu kacang"
        self.resep_data[9].waktu = 50
        self.resep_data[9].tanggal = "2023-05-09"
    
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
        
        self.tampilkan_daftar_resep()
        
    def tampilkan_daftar_resep(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i in range(self.jumlah_resep):
            resep = self.resep_data[i]
            bahan_utama = ", ".join(resep.bahan[:2]) + ("..." if resep.jumlah_bahan > 2 else "")
            self.tree.insert("", tk.END, values=(
                resep.judul,
                bahan_utama,
                resep.waktu,
                resep.tanggal
            ))
    
    def cari_resep(self):
        keyword = self.search_entry.get().lower()
        search_type = self.search_type.get()
    
        if not keyword:
            self.tampilkan_daftar_resep()
            return

        hasil = [0] * self.MAX_RESEP
        jumlah_hasil = 0
    
        for i in range(self.jumlah_resep):
            resep = self.resep_data[i]
            found = False
        
            if search_type == "judul":
                if keyword in resep.judul.lower():
                    found = True
            elif search_type == "bahan":
                for j in range(resep.jumlah_bahan):
                    if keyword in resep.bahan[j].lower():
                        found = True
                        break
        
            if found and jumlah_hasil < self.MAX_RESEP:
                hasil[jumlah_hasil] = i
                jumlah_hasil += 1
    
    # Tampilkan hasil
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for k in range(jumlah_hasil):
            idx = hasil[k]
            resep = self.resep_data[idx]
            bahan_utama = ", ".join(resep.bahan[:2]) + ("..." if resep.jumlah_bahan > 2 else "")
            self.tree.insert("", tk.END, values=(
                resep.judul,
                bahan_utama,
                resep.waktu,
                resep.tanggal
            ))
    
    def tampilkan_detail_resep(self, event):
        selected_item = self.tree.selection()
        if not selected_item:
            return
            
        item = self.tree.item(selected_item[0])
        judul = item['values'][0]
        
        for resep in self.resep_data[:self.jumlah_resep]:
            if resep.judul == judul:
                detail = f"Judul: {resep.judul}\n\n"
                detail += f"Bahan:\n- " + "\n- ".join(resep.bahan[:resep.jumlah_bahan]) + "\n\n"
                detail += f"Langkah:\n{resep.langkah}\n\n"
                detail += f"Waktu: {resep.waktu} menit\n"
                detail += f"Tanggal: {resep.tanggal}"
                
                messagebox.showinfo("Detail Resep", detail)
                break
    
    def urutkan_resep(self):
        sort_type = self.sort_type.get()
        
        if sort_type == "judul":
            #berdasarkan judul 
            for i in range(self.jumlah_resep - 1):
                for j in range(self.jumlah_resep - i - 1):
                    if self.resep_data[j].judul.lower() > self.resep_data[j+1].judul.lower():
                        self.resep_data[j], self.resep_data[j+1] = self.resep_data[j+1], self.resep_data[j]
        elif sort_type == "waktuC":
            #berdasarkan waktu (tercepat)
            for i in range(self.jumlah_resep - 1):
                for j in range(self.jumlah_resep - i - 1):
                    if self.resep_data[j].waktu > self.resep_data[j+1].waktu:
                        self.resep_data[j], self.resep_data[j+1] = self.resep_data[j+1], self.resep_data[j]
        elif sort_type == "waktuL":
            #berdasarkan waktu (terlama)
            for i in range(self.jumlah_resep - 1):
                for j in range(self.jumlah_resep - i - 1):
                    if self.resep_data[j].waktu < self.resep_data[j+1].waktu:
                        self.resep_data[j], self.resep_data[j+1] = self.resep_data[j+1], self.resep_data[j]
        
        self.tampilkan_daftar_resep()
    
    def tambah_resep(self):
        self._show_resep_form(is_edit=False)

    def edit_resep(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih resep yang akan diedit!")
            return
            
        item = self.tree.item(selected_item[0])
        judul = item['values'][0]
        self._show_resep_form(is_edit=True, old_judul=judul)

    def _show_resep_form(self, is_edit, old_judul=None):
        form_window = tk.Toplevel(self.root)
        form_window.title("Edit Resep" if is_edit else "Tambah Resep")
        form_window.geometry("500x400")
        
        # Cari resep yang akan diedit
        resep_to_edit = None
        if is_edit:
            for resep in self.resep_data[:self.jumlah_resep]:
                if resep.judul == old_judul:
                    resep_to_edit = resep
                    break
        
        # Frame form
        form_frame = ttk.Frame(form_window, padding="10")
        form_frame.pack(fill=tk.BOTH, expand=True)
        
        # Judul
        ttk.Label(form_frame, text="Judul Resep:").grid(row=0, column=0, sticky=tk.W, pady=5)
        judul_entry = ttk.Entry(form_frame, width=40)
        judul_entry.grid(row=0, column=1, pady=5)
        
        # Bahan
        ttk.Label(form_frame, text="Bahan (pisahkan dengan koma):").grid(row=1, column=0, sticky=tk.W, pady=5)
        bahan_entry = tk.Text(form_frame, width=40, height=5)
        bahan_entry.grid(row=1, column=1, pady=5)
        
        # Langkah
        ttk.Label(form_frame, text="Langkah Pembuatan:").grid(row=2, column=0, sticky=tk.W, pady=5)
        langkah_entry = tk.Text(form_frame, width=40, height=8)
        langkah_entry.grid(row=2, column=1, pady=5)
        
        # Waktu
        ttk.Label(form_frame, text="Waktu Masak (menit):").grid(row=3, column=0, sticky=tk.W, pady=5)
        waktu_entry = ttk.Entry(form_frame, width=10)
        waktu_entry.grid(row=3, column=1, sticky=tk.W, pady=5)
        
        # Isi form jika edit
        if is_edit and resep_to_edit:
            judul_entry.insert(0, resep_to_edit.judul)
            bahan_entry.insert(tk.END, ", ".join(resep_to_edit.bahan[:resep_to_edit.jumlah_bahan]))
            langkah_entry.insert(tk.END, resep_to_edit.langkah)
            waktu_entry.insert(0, str(resep_to_edit.waktu))
        
        # Tombol simpan
        save_button = ttk.Button(
            form_frame, 
            text="Simpan", 
            command=lambda: self.simpan_resep(
                form_window,
                judul_entry.get(),
                bahan_entry.get("1.0", tk.END),
                langkah_entry.get("1.0", tk.END),
                waktu_entry.get(),
                is_edit,
                old_judul
            )
        )
        save_button.grid(row=4, column=1, sticky=tk.E, pady=10)
    
    
    
    def simpan_resep(self, window, judul, bahan_str, langkah, waktu_str, is_edit, old_judul=None):
        # Validasi input
        if not judul or not bahan_str.strip() or not langkah.strip() or not waktu_str:
            messagebox.showwarning("Peringatan", "Semua field harus diisi!")
            return
        
        try:
            waktu = int(waktu_str)
            if waktu <= 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Peringatan", "Waktu masak harus berupa angka positif!")
            return
        
        # Konversi bahan ke array statis
        bahan_array = [""]*10
        bahan_input = [b.strip() for b in bahan_str.split(",") if b.strip()]
        if not bahan_input:
            messagebox.showwarning("Peringatan", "Masukkan minimal satu bahan!")
            return
        
        jumlah_bahan = min(len(bahan_input), 10)  # Maksimal 10 bahan
        for i in range(jumlah_bahan):
            bahan_array[i] = bahan_input[i]
        
        # Cek duplikasi judul
        for i in range(self.jumlah_resep):
            if (not is_edit and self.resep_data[i].judul.lower() == judul.lower()) or \
               (is_edit and judul.lower() != old_judul.lower() and 
                self.resep_data[i].judul.lower() == judul.lower()):
                messagebox.showwarning("Peringatan", "Resep dengan judul tersebut sudah ada!")
                return
        
        if is_edit:
            # Edit resep yang ada
            for i in range(self.jumlah_resep):
                if self.resep_data[i].judul == old_judul:
                    self.resep_data[i].judul = judul
                    self.resep_data[i].bahan = bahan_array
                    self.resep_data[i].jumlah_bahan = jumlah_bahan
                    self.resep_data[i].langkah = langkah.strip()
                    self.resep_data[i].waktu = waktu
                    break
            messagebox.showinfo("Info", "Resep berhasil diperbarui")
        else:
            # Tambah resep baru
            if self.jumlah_resep >= self.MAX_RESEP:
                messagebox.showerror("Error", "Batas maksimal resep telah tercapai")
                return
                
            self.resep_data[self.jumlah_resep].judul = judul
            self.resep_data[self.jumlah_resep].bahan = bahan_array
            self.resep_data[self.jumlah_resep].jumlah_bahan = jumlah_bahan
            self.resep_data[self.jumlah_resep].langkah = langkah.strip()
            self.resep_data[self.jumlah_resep].waktu = waktu
            self.resep_data[self.jumlah_resep].tanggal = datetime.now().strftime("%Y-%m-%d")
            self.jumlah_resep += 1
            messagebox.showinfo("Info", "Resep baru berhasil ditambahkan")
        
        window.destroy()
        self.tampilkan_daftar_resep()

    def hapus_resep(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih resep yang akan dihapus!")
            return
            
        item = self.tree.item(selected_item[0])
        judul = item['values'][0]
        
        for i in range(self.jumlah_resep):
            if self.resep_data[i].judul == judul:

                self.riwayat_hapus[self.jumlah_riwayat] = self.resep_data[i]
                self.jumlah_riwayat += 1
                
                for j in range(i, self.jumlah_resep-1):
                    self.resep_data[j] = self.resep_data[j+1]
                
                self.jumlah_resep -= 1
                self.tampilkan_daftar_resep()
                messagebox.showinfo("Info", "Resep berhasil dihapus")
                return
        
        messagebox.showwarning("Peringatan", "Resep tidak ditemukan!")

    def tampilkan_riwayat_hapus(self):
        if self.jumlah_riwayat == 0:
            messagebox.showinfo("Info", "Tidak ada riwayat penghapusan")
            return
        
        riwayat_window = tk.Toplevel(self.root)
        riwayat_window.title("Riwayat Penghapusan Resep")
        riwayat_window.geometry("600x400")
        
        tree = ttk.Treeview(riwayat_window, columns=("Judul", "Bahan", "Waktu", "Tanggal"), show="headings")
        tree.heading("Judul", text="Judul")
        tree.heading("Bahan", text="Bahan Utama")
        tree.heading("Waktu", text="Waktu (menit)")
        tree.heading("Tanggal", text="Tanggal Ditambahkan")
        
        tree.column("Judul", width=150)
        tree.column("Bahan", width=150)
        tree.column("Waktu", width=80)
        tree.column("Tanggal", width=100)
        
        tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        for i in range(self.jumlah_riwayat):
            resep = self.riwayat_hapus[i]
            bahan_utama = ", ".join(resep.bahan[:2]) + ("..." if resep.jumlah_bahan > 2 else "")
            tree.insert("", tk.END, values=(
                resep.judul,
                bahan_utama,
                resep.waktu,
                resep.tanggal
            ))

        
if __name__ == "__main__":
    root = tk.Tk()
    app = ResepMasakanApp(root)
    root.mainloop()
