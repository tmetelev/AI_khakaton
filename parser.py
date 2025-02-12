import csv

def convert(input_tsv_file, output_csv_file):
    # Открываем TSV файл для чтения и CSV файл для записи
    with open(input_tsv_file, mode="r", newline='', encoding="utf-8") as tsv_file:
        tsv_reader = csv.reader(tsv_file, delimiter="\t")
        
        with open(output_csv_file, mode="w", newline='', encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=",")
            
            # Перенос каждой строки из TSV в CSV
            for row in tsv_reader:
                csv_writer.writerow(row)

    print(f"Данные успешно перенесены из '{input_tsv_file}' в '{output_csv_file}'")


for name in ["history", 'users', 'validate', 'validate_answers']:
    convert(name + '.tsv', name + '.csv')