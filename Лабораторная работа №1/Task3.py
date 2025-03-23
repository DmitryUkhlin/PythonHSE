# TODO Найдите количество книг, которое можно разместить на дискете
base_V = 1.44
count_bytes_in_Mbyte = 1024*1024
symbol_size = 4
symbols_in_line = 25
line_in_page = 50
page_in_book = 100
base_V_book = (symbols_in_line * line_in_page * page_in_book * symbol_size)/(count_bytes_in_Mbyte)
books_on_floppy_disk = round(base_V // base_V_book)







print("Количество книг, помещающихся на дискету:", books_on_floppy_disk)
