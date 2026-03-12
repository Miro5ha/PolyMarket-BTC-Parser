# РУКОВОДСТВО НА РУССКОМ ЯЗЫКЕ (RUSSIAN LANGUAGE GUIDE)
# Чем он полезен?
Этот парсер был создан для сбора информации со страницы https://polymarket.com/event/what-price-will-bitcoin-hit-before-2027, а конкретно страйков (например 1,000,000 и т.д.) и цен (например 2% и т.д.).
Его главной особенностью является то что каждый час он не создает другой exel файл, а сразу добавляет новые данные которые были получены через час в этот же файл!
# Что нужно для пользования?
Во первых установить все библиотеки из файла requirements.txt.
После чего вы можете запускать парсер. В консоли будет регулярно (каждый час) выводится "None" - что означает что парсер работает. Также на 45 строчке вы можете изменить значение переменной file_path, что изменит путь к файлу.

# ENGLISH LANGUAGE GUIDE (РУКОВОДСТВО НА АНГЛИЙСКОМ ЯЗЫКЕ)
# How is it useful?
This parser was created to collect information from the page https://polymarket.com/event/what-price-will-bitcoin-hit-before-2027, specifically strike prices (e.g., 1,000,000, etc.) and prices (e.g., 2%, etc.).
Its main feature is that it doesn't create a new Excel file every hour, but immediately appends the new data received every hour to the same file!
# What do you need to use it?
First, install all the libraries from the requirements.txt file.
After that, you can run the parser. The console will regularly (every hour) display "None," indicating that the parser is running. You can also change the value of the file_path variable on line 45, which will change the path to the file.
