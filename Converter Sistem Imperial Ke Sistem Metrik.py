import tkinter as tk
from tkinter import ttk


class UnitConverter:
    def __init__(self):
        self.history = []  # Stack untuk menyimpan riwayat 

    # Setter dan Getter untuk riwayat
    def set_history(self, value):
        self.history.append(value)
    
    def get_history(self):
        return self.history

    # Fungsi untuk normalisasi input unit
    def normalize_unit(self, unit):
        if unit:
            return unit.strip().lower()
        return unit

    # Fungsi konversi untuk ukuran (massa)
    def convert_size(self, value, from_unit, to_unit):
        conversions = {
            ("pound", "kilogram"): 0.453592,
            ("pound", "gram"): 453.592, 
            ("ons", "gram"): 28.3495,
            ("ons", "kilogram"): 0.0283495,  
        }
        from_unit = self.normalize_unit(from_unit)
        to_unit = self.normalize_unit(to_unit)
        factor = conversions.get((from_unit, to_unit))
        if factor is not None:
            return value * factor
        else:
            return None

    # Fungsi konversi untuk panjang
    def convert_length(self, value, from_unit, to_unit):
        conversions = {
            ("inci", "sentimeter"): 2.54,
            ("inci", "meter"): 0.0254,
            ("inci", "kilometer"): 0.0000254,
            ("kaki", "meter"): 0.3048,
            ("kaki", "kilometer"): 0.0003048,
            ("kaki", "sentimeter"): 30.48,
            ("yard", "sentimeter"): 91.44,
            ("yard", "meter"): 0.9144,
            ("yard", "kilometer"): 0.0009144,
            ("mil", "kilometer"): 1.60934,
            ("mil", "meter"): 1609.34,
            ("mil", "sentimeter"): 160934,  
        }
        from_unit = self.normalize_unit(from_unit)
        to_unit = self.normalize_unit(to_unit)
        factor = conversions.get((from_unit, to_unit))
        if factor is not None:
            return value * factor
        else:
            return None

    # Fungsi konversi untuk kecepatan
    def convert_speed(self, value, from_unit, to_unit):
        conversions = {
            ("mil/jam", "kilometer/jam"): 1.60934,
        }
        from_unit = self.normalize_unit(from_unit)
        to_unit = self.normalize_unit(to_unit)
        factor = conversions.get((from_unit, to_unit))
        if factor is not None:
            return value * factor
        else:
            return None

# Fungsi untuk konversi panjang
def on_convert_length():
    try:
        value = float(length_entry.get())
        from_unit = length_from_combobox.get()
        to_unit = length_to_combobox.get()
        
        if not from_unit or not to_unit:
            length_result_label.config(text="Pilih unit untuk konversi.")
            return

        result = converter.convert_length(value, from_unit, to_unit)
        if result is not None:
            length_result_label.config(text=f"Hasil: {result:.2f}")
            converter.set_history(f"{value} {from_unit} = {result:.2f} {to_unit}")
        else:
            length_result_label.config(text="Konversi tidak valid. Periksa unit.")
    except ValueError:
        length_result_label.config(text="Masukkan angka yang valid.")

# Fungsi untuk konversi massa
def on_convert_size():
    try:
        value = float(size_entry.get())
        from_unit = size_from_combobox.get()
        to_unit = size_to_combobox.get()
        
        if not from_unit or not to_unit:
            size_result_label.config(text="Pilih unit untuk konversi.")
            return

        result = converter.convert_size(value, from_unit, to_unit)
        if result is not None:
            size_result_label.config(text=f"Hasil: {result:.2f}")
            converter.set_history(f"{value} {from_unit} = {result:.2f} {to_unit}")
        else:
            size_result_label.config(text="Konversi tidak valid. Periksa unit.")
    except ValueError:
        size_result_label.config(text="Masukkan angka yang valid.")

# Fungsi untuk konversi kecepatan
def on_convert_speed():
    try:
        value = float(speed_entry.get())
        from_unit = speed_from_combobox.get()
        to_unit = speed_to_combobox.get()
        
        if not from_unit or not to_unit:
            speed_result_label.config(text="Pilih unit untuk konversi.")
            return

        result = converter.convert_speed(value, from_unit, to_unit)
        if result is not None:
            speed_result_label.config(text=f"Hasil: {result:.2f}")
            converter.set_history(f"{value} {from_unit} = {result:.2f} {to_unit}")
        else:
            speed_result_label.config(text="Konversi tidak valid. Periksa unit.")
    except ValueError:
        speed_result_label.config(text="Masukkan angka yang valid.")

# Fungsi untuk menampilkan riwayat
def show_history():
    history = converter.get_history()
    history_window = tk.Toplevel(window)
    history_window.title("Riwayat Konversi")
    history_window.geometry("515x300")
    history_window.resizable(False, False)
    history_window.attributes('-topmost', 1)

    if not history:
        tk.Label(history_window, text="Kosong Ngab", bg='lightblue').pack()
        return

    history_listbox = tk.Listbox(history_window, width=50, height=10)
    for item in history:
        history_listbox.insert(tk.END, item)
    history_listbox.pack()

# Membuat objek UnitConverter
converter = UnitConverter()

# Membuat GUI
window = tk.Tk()
window.title("Unit Converter")
window.geometry("515x300")
window.resizable(False, False)

# GUI Konversi Panjang
length_frame = tk.LabelFrame(window, text="Konversi Panjang", bg='lightblue')
length_frame.grid(row=0, column=0, padx=10, pady=10)

tk.Label(length_frame, text="Masukkan Nilai:", bg='lightblue').grid(row=0, column=0)
length_entry = tk.Entry(length_frame)
length_entry.grid(row=0, column=1)

tk.Label(length_frame, text="Dari Unit:", bg='lightblue').grid(row=1, column=0)
length_from_combobox = ttk.Combobox(length_frame, values=["Inci", "Kaki", "Yard", "Mil"])
length_from_combobox.grid(row=1, column=1)

tk.Label(length_frame, text="Ke Unit:", bg='lightblue').grid(row=2, column=0)
length_to_combobox = ttk.Combobox(length_frame, values=["Sentimeter", "Meter", "Kilometer"])
length_to_combobox.grid(row=2, column=1)

tk.Button(length_frame, text="Konversi", command=on_convert_length).grid(row=3, column=0, columnspan=2)
length_result_label = tk.Label(length_frame, text="Hasil: ", bg='lightblue')
length_result_label.grid(row=4, column=0, columnspan=2)

# GUI Konversi Massa
size_frame = tk.LabelFrame(window, text="Konversi Massa", bg='lightblue')
size_frame.grid(row=0, column=1, padx=10, pady=10)

tk.Label(size_frame, text="Masukkan Nilai:", bg='lightblue').grid(row=0, column=0)
size_entry = tk.Entry(size_frame)
size_entry.grid(row=0, column=1)

tk.Label(size_frame, text="Dari Unit:", bg='lightblue').grid(row=1, column=0)
size_from_combobox = ttk.Combobox(size_frame, values=["Pound", "Ons"])
size_from_combobox.grid(row=1, column=1)

tk.Label(size_frame, text="Ke Unit:", bg='lightblue').grid(row=2, column=0)
size_to_combobox = ttk.Combobox(size_frame, values=["Kilogram", "Gram"])
size_to_combobox.grid(row=2, column=1)

tk.Button(size_frame, text="Konversi", command=on_convert_size).grid(row=3, column=0, columnspan=2)
size_result_label = tk.Label(size_frame, text="Hasil: ", bg='lightblue')
size_result_label.grid(row=4, column=0, columnspan=2)

# GUI Konversi Kecepatan
speed_frame = tk.LabelFrame(window, text="Konversi Kecepatan", bg='lightblue')
speed_frame.grid(row=1, column=0, padx=10, pady=10)

tk.Label(speed_frame, text="Masukkan Nilai:", bg='lightblue').grid(row=0, column=0)
speed_entry = tk.Entry(speed_frame)
speed_entry.grid(row=0, column=1)

tk.Label(speed_frame, text="Dari Unit:", bg='lightblue').grid(row=1, column=0)
speed_from_combobox = ttk.Combobox(speed_frame, values=["Mil/Jam"])
speed_from_combobox.grid(row=1, column=1)

tk.Label(speed_frame, text="Ke Unit:", bg='lightblue').grid(row=2, column=0)
speed_to_combobox = ttk.Combobox(speed_frame, values=["Kilometer/Jam"])
speed_to_combobox.grid(row=2, column=1)

tk.Button(speed_frame, text="Konversi", command=on_convert_speed).grid(row=3, column=0, columnspan=2)
speed_result_label = tk.Label(speed_frame, text="Hasil: ", bg='lightblue')
speed_result_label.grid(row=4, column=0, columnspan=2)

# Tombol Riwayat
tk.Button(window, text="Lihat Riwayat", command=show_history).grid(row=1, column=1, pady=0)

window.mainloop()
