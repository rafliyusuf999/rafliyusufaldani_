import math

def haversine(lat1, lon1, lat2, lon2):
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    delta_lat = lat2_rad - lat1_rad
    delta_lon = lon2_rad - lon1_rad

    a = math.sin(delta_lat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    R = 6371.0

    distance = R * c
    return distance

lat1 = float(input("Masukkan bujur kota 1: "))  
lon1 = float(input("Masukkan lintang kota 1: ")) 
lat2 = float(input("Masukkan bujur kota 2: "))
lon2 = float(input("Masukkan lintang kota 2: ")) 

jarak = haversine(lat1, lon1, lat2, lon2)

# Menampilkan hasil 
print("Jarak antara titik 1 dan titik 2 adalah:", jarak, "km")
