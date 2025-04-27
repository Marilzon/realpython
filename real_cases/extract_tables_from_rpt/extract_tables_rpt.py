class ExtractTableFromRPT:
    def __init__(self, text_file, output_path, columns, table_name):
        self.text_file = text_file
        self.output_path = output_path
        self.columns = columns
        self.table_name = table_name
        self.content = ""
        self.content_without_bad_lines = ""
        self.content_with_comma_sep = ""
        self.taget_table = ""

    def __read_text_file(self):
        with open(self.text_file, "r") as file:
            self.content = file.read()

    def __remove_bad_lines(self, bad_words):
        bad_words_set = set(bad_words)
        self.content_without_bad_lines = "\n".join(
            line for line in self.content.splitlines()
            if not any(bad_word in line for bad_word in bad_words_set)
        )

    def __transform_spaces_to_comma(self):
        self.content_with_comma_sep = "\n".join(
            ','.join(line.split())
            for line in self.content_without_bad_lines.splitlines()
        )

    def __detect_table(self):
        content_lines = self.content_with_comma_sep.split("\n")
        header = False
        data = []

        for line in content_lines:
            stripped_line = line.strip()

            if not header:
                if self.columns in stripped_line:
                    header = True
                    data.append(stripped_line)
            else:
                if not stripped_line:
                    break
                data.append(stripped_line)

        if header:
            self.target_table = "\n".join(data)
        else:
            self.target_table = None

    def __write_csv_file(self):
        with open(self.output_path, "w") as file:
            file.write(self.target_table)

    def execute_etl(self):
        self.__read_text_file()
        self.__remove_bad_lines(["---", "affected", "TABLE", "sql"])
        self.__transform_spaces_to_comma()
        self.__detect_table()
        self.__write_csv_file()


input_path = "real_cases/extract_tables_from_rpt/data/data.rpt"
output_path = "real_cases/extract_tables_from_rpt/data/SALES.csv"
columns = "ID,PRODUCT_NAME,AMOUNT,SELLER_ID"
table_name = "SALES"

extract_tables_from_rpt = ExtractTableFromRPT(input_path, output_path, columns, table_name)

extract_tables_from_rpt.execute_etl()

