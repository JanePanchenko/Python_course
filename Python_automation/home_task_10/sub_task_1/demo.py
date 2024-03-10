from Python_automation.home_task_10.sub_task_1.csv_adaptor import CsvAdaptor

html_output = CsvAdaptor.csv_to_html('employees.csv')
for entry in html_output:
    print(entry.replace('\\n', '\n'))
