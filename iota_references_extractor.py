#IOTA REFERENCES EXTRACTOR
#2023 - SCQ Devices / EA1NK
import sys

def load_iota_references(file_path):
    iota_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                iota_ref, island_name = line.split(' ', 1)
                iota_dict[iota_ref.strip()] = island_name.strip()
    return iota_dict

def parse_cabrillo(file_path, iota_references):
    iotas = set()
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith("QSO"):
                parts = line.split()
                for part in parts:
                    if "-" in part:
                        iota_ref = part.strip()
                        if iota_ref in iota_references:
                            iotas.add(iota_ref)
    return iotas

def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py iota_references.txt input_cabrillo.log output_iotas.txt")
        return

    references_file = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]

    iota_references = load_iota_references(references_file)
    iotas = parse_cabrillo(input_file, iota_references)

    if not iotas:
        print("No IOTA references found in the input file.")
        return

    with open(output_file, 'w') as file:
        file.write("IOTA REFERENCES REPORT\n")
        for iota_ref in sorted(iotas):
            island_name = iota_references.get(iota_ref, "Unknown Island")
            file.write(f"{iota_ref}, {island_name}\n")

        file.write(f"TOTAL REFERENCES: {len(iotas)}\n")

    print(f"The file with the IOTA references and their island names has been generated: {output_file}.")

if __name__ == "__main__":
    main()
