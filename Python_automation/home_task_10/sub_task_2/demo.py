from Python_automation.home_task_10.sub_task_2.proxy import ProxyReaderWriter

proxy_rw = ProxyReaderWriter('test_file.txt')

proxy_rw.read()
proxy_rw.read()
proxy_rw.read()

proxy_rw.write('asd')
proxy_rw.write('asd')
proxy_rw.write('asd2')
proxy_rw.write('asd')
proxy_rw.read()

print(proxy_rw.data)
