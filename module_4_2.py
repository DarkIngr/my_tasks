def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

test_function()

inner_function()

# Вызов функци inner_function() вне функции test_function приводит к появлению ошбики