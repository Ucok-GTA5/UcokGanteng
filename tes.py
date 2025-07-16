import time  # Untuk menghitung waktu eksekusi

# Fungsi Bubble Sort (Manual Sorting)
def bubble_sort(data):
    n = len(data)
    for i in range(n-1):
        for j in range(n-1-i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data
# Kompleksitas waktu: O(n^2)

# Fungsi Rekursif untuk Mencari Nilai Maksimum
def cari_maks(data, n):
    if n == 1:
        return data[0]
    return max(data[n-1], cari_maks(data, n-1))
# Kompleksitas waktu: O(n)

# Data awal (Tipe Data: List/Array)
data = [34, 12, 25, 9, 17]

print("Data awal:", data)

# Waktu eksekusi bubble sort
start_sort = time.time()
sorted_data = bubble_sort(data.copy())
end_sort = time.time()
print("Data setelah bubble sort:", sorted_data)
print(f"Waktu eksekusi sorting: {end_sort - start_sort:.6f} detik")

# Waktu eksekusi pencarian maksimum rekursif
start_max = time.time()
maksimum = cari_maks(data, len(data))
end_max = time.time()
print("Nilai maksimum (rekursif):", maksimum)
print(f"Waktu eksekusi pencarian maksimum: {end_max - start_max:.6f} detik")
