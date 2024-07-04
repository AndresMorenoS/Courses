
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle:
    if not line.startswith("From "):  # Asegúrate de que solo procesas las líneas que empiezan con "From "
        continue
    words = line.split()
    if len(words) > 1:  # Asegúrate de que la línea tenga al menos dos palabras
        correo = words[1]
        counts[correo] = counts.get(correo, 0) + 1
# Encuentra el correo más común
max_correos = None
max_count = None

for correo, count in counts.items():
    if max_count is None or count > max_count:
        max_correos = correo
        max_count = count

print(max_correos, max_count)


