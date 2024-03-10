class CsvAdaptor:

    @staticmethod
    def csv_to_html(file_path) -> list:
        with open(file_path) as file:
            file_content = file.readlines()
            header = [line.strip() for line in file_content[0].split(',')]
            rows = file_content[1:]

            result_list = []
            for row in rows:
                row = row.strip().split(',')
                mapped_data = dict(zip(header, row))
                html_entry = ''
                for key, value in mapped_data.items():
                    html_entry += f'<{key}>{value}</{key}>\n'
                result_list.append(html_entry)
            return result_list
