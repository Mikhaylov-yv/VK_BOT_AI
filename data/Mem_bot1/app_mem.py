def app(mem_data_app,csv_path):
    string = open(csv_path, 'a')
    mem_data_app = ';'.join(map(str, mem_data_app)) + '\n'
    string.write(mem_data_app)
    string.close()





