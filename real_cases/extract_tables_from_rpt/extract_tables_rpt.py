from glob import glob
import time

timestr = time.strftime("%Y%m%d")


class ExtractTableFromRPT:
    def __init__(self, text_file, output_path, columns, table_name):
        self.text_file = text_file
        self.output_path = output_path
        self.columns = columns
        self.table_name = table_name
        self.content = ""
        self.content_without_bad_lines = ""
        self.content_with_comma_sep = ""
        self.target_table = ""

    def __read_text_file(self):
        print("[1/5] Reading text file...")
        with open(self.text_file, "r") as file:
            self.content = file.read()
        print(f"→ File loaded: {self.text_file}")

    def __remove_bad_lines(self, bad_words):
        print("\n[2/5] Filtering unwanted lines...")
        bad_words_set = set(bad_words)
        self.content_without_bad_lines = "\n".join(
            line
            for line in self.content.splitlines()
            if not any(bad_word in line for bad_word in bad_words_set)
        )
        print("→ Unwanted lines removed")

    def __transform_spaces_to_comma(self):
        print("\n[3/5] Converting spaces to commas...")
        self.content_with_comma_sep = "\n".join(
            ",".join(line.split())
            for line in self.content_without_bad_lines.splitlines()
        )
        print("→ CSV conversion complete")

    def __detect_table(self):
        print("\n[4/5] Extracting table...")
        content_lines = self.content_with_comma_sep.split("\n")
        header = False
        data = []

        print(f"→ Searching for header: '{self.columns}'")
        for line in content_lines:
            stripped_line = line.strip()

            if not header:
                if self.columns in stripped_line:
                    print("→ Header found!")
                    header = True
                    data.append(stripped_line)
            else:
                if not stripped_line:
                    print("→ Table end detected (empty line)")
                    break
                data.append(stripped_line)

        if header:
            self.target_table = "\n".join(data)
            print(f"→ Table extracted: {len(data)} rows captured")
        else:
            self.target_table = None
            print("→ WARNING: Header not found!")

    def __write_csv_file(self):
        print("\n[5/5] Saving CSV file...")
        with open(self.output_path, "w") as file:
            file.write(self.target_table)
        print(f"→ File saved to: {self.output_path}")

    def execute_etl(self):
        print(f"\nProcessing started for '{self.table_name}'")
        self.__read_text_file()
        self.__remove_bad_lines(["---", "affected", "TABLE", "sql"])
        self.__transform_spaces_to_comma()
        self.__detect_table()
        self.__write_csv_file()
        print("Processing completed successfully!\n")


input_path = glob("real_cases/extract_tables_from_rpt/data/*.rpt")[-1]
sales_output_path = f"real_cases/extract_tables_from_rpt/data/{timestr}_SALES.csv"
sales_columns = "ID,PRODUCT_NAME,AMOUNT,SELLER_ID"
sales_table_name = "SALES"

extract_tables_from_rpt = ExtractTableFromRPT(
    input_path, sales_output_path, sales_columns, sales_table_name
)

extract_tables_from_rpt.execute_etl()
