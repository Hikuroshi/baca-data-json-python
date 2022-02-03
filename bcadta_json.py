import json

# Buka file JSON
file_json = open("beljson\dataku.json")

# prsing data JSON
data = json.loads(file_json.read())

# Cetak isi data JSON
print(f"Nama: {data['name']}")
print(f"Social Media:")
print(f"- Facebook: {data['social_media']['facebook']}")
print(f"- Instagram: {data['social_media']['instagram']}")