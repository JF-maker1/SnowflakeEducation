# Skript pro zabalení obsahu souborů do jednoho textového souboru

# Název souboru s výpisem cest
input_file = 'tracked_files.txt'
# Název výstupního souboru
output_file = 'bundled_files.txt'

# Otevření výstupního souboru pro zápis
with open(output_file, 'w', encoding='utf-8') as outfile:
    # Načtení seznamu souborů ze vstupního souboru
    with open(input_file, 'r', encoding='utf-8') as infile:
        for line in infile:
            file_path = line.strip()  # Odstranění bílých znaků
            if file_path:  # Ignorování prázdných řádků
                try:
                    # Otevření a načtení obsahu souboru
                    with open(file_path, 'r', encoding='utf-8') as current_file:
                        outfile.write(f"[file name]: {file_path}\n")
                        outfile.write("[file content]:\n")
                        outfile.write(current_file.read())
                        outfile.write("\n\n")  # Oddělení souborů
                except FileNotFoundError:
                    outfile.write(f"[file name]: {file_path}\n")
                    outfile.write("[file content]: Soubor nebyl nalezen.\n\n")
                except Exception as e:
                    outfile.write(f"[file name]: {file_path}\n")
                    outfile.write(f"[file content]: Chyba při čtení souboru: {e}\n\n")

print(f"Všechny soubory byly zabaleny do {output_file}.")
