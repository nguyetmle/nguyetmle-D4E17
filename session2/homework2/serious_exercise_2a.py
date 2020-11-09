n = int(input('enter n = '))
for i in range(n):
    if i % 2 == 0:
        print('1', end = '\n')  
    else:
        print('0', end = ' ')

"""
đối số end: 
    end = ' ': khoảng cách cách ra 1 khoảng trắng rồi tới chuỗi tiếp theo -> hiển thị thông tin trên cùng 1 dòng dữ liệu
    end = '\n': xuống dòng
    end = '\t': đẩy vào 1 tab
    end = '\'' hoặc '\"': xuất trích dẫn
"""