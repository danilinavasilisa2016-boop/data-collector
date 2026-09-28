# data_reader.py
def get_data():
    
    # Пока Arduino не подключена,
    # используем тестовую строку
    
    test_data = "25,60,700"
    
    # Разделяем строку на отдельные значения
    data = test_data.split(",")
    
    # Возвращаем полученные данные
    return data
