filename = input("Masukkan nama file: ")

email_count = {}

try:
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('From '):
                words = line.split()
                email = words[1]
                email_count[email] = email_count.get(email, 0) + 1
except FileNotFoundError:
    print("File tidak ditemukan. Pastikan nama file sudah benar.")
    exit()

print(email_count)
