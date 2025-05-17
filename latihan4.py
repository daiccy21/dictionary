def count_domains(filename):
    domain_count = {}
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('From '):
                words = line.split()
                email = words[1]
                domain = email.split('@')[1]
                if domain in domain_count:
                    domain_count[domain] += 1
                else:
                    domain_count[domain] = 1
    return domain_count
filename = input("Masukkan nama file: ")
result = count_domains(filename)
print(result)
