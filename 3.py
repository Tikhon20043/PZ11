#Приложение КОММАНДИРОВОЧНЫЕ РАСХОДЫ для автоматизированного
# контроля на предприятии. БД должна содержать таблицу Статьи расходов,
#имеющую следующую структуру записи: № приказа, Фамилия, Место командировки,
#Оплата, Аванс, Вид расходов, Сумма расходов

import sqlite3

# Создание соединения с базой данных
conn = sqlite3.connect('expenses.db')
cursor = conn.cursor()

# Создание таблицы Статьи расходов
cursor.execute('''
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY,
    order_number INTEGER,
    employee_name TEXT,
    destination TEXT,
    payment REAL,
    advance REAL,
    expense_type TEXT,
    expense_amount REAL
)
''')

# Функция для добавления новой записи в таблицу
def add_expense():
    order_number = int(input("Введите номер приказа: "))
    employee_name = input("Введите фамилию сотрудника: ")
    destination = input("Введите место командировки: ")
    payment = float(input("Введите сумму оплаты: "))
    advance = float(input("Введите сумму аванса: "))
    expense_type = input("Введите вид расходов: ")
    expense_amount = float(input("Введите сумму расходов: "))

    cursor.execute('''
        INSERT INTO expenses (order_number, employee_name, destination, payment, advance, expense_type, expense_amount)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (order_number, employee_name, destination, payment, advance, expense_type, expense_amount))
    conn.commit()

# Функция для поиска записи в таблице
def search_expense():
    order_number = int(input("Введите номер приказа для поиска: "))
    cursor.execute('''
        SELECT * FROM expenses
        WHERE order_number = ?
    ''', (order_number,))
    result = cursor.fetchone()
    if result:
        print("Найденная запись:")
        print(f"№ приказа: {result[1]}")
        print(f"Фамилия: {result[2]}")
        print(f"Место командировки: {result[3]}")
        print(f"Оплата: {result[4]}")
        print(f"Аванс: {result[5]}")
        print(f"Вид расходов: {result[6]}")
        print(f"Сумма расходов: {result[7]}")
    else:
        print("Запись не найдена.")

# Функция для удаления записи из таблицы
def delete_expense():
    order_number = int(input("Введите номер приказа для удаления: "))
    cursor.execute('''
        DELETE FROM expenses
        WHERE order_number = ?
    ''', (order_number,))
    conn.commit()
    print("Запись успешно удалена.")

# Функция для редактирования записи в таблице
def edit_expense():
    order_number = int(input("Введите номер приказа для редактирования: "))
    cursor.execute('''
        SELECT * FROM expenses
        WHERE order_number = ?
    ''', (order_number,))
    result = cursor.fetchone()
    if result:
        print("Найденная запись:")
        print(f"№ приказа: {result[1]}")
        print(f"Фамилия: {result[2]}")
        print(f"Место командировки: {result[3]}")
        print(f"Оплата: {result[4]}")
        print(f"Аванс: {result[5]}")
        print(f"Вид расходов: {result[6]}")
        print(f"Сумма расходов: {result[7]}")

        new_order_number = int(input("Введите новый номер приказа (оставьте пустым, если не изменяется): "))
        if new_order_number:
            cursor.execute('''
                UPDATE expenses
                SET order_number = ?
                WHERE order_number = ?
            ''', (new_order_number, order_number))
        new_employee_name = input("Введите новую фамилию сотрудника (оставьте пустым, если не изменяется): ")
        if new_employee_name:
            cursor.execute('''
                UPDATE expenses
                SET employee_name = ?
                WHERE order_number = ?
            ''', (new_employee_name, order_number))
        new_destination = input("Введите новое место командировки (оставьте пустым, если не изменяется): ")
        if new_destination:
            cursor.execute('''
                UPDATE expenses
                SET destination = ?
                WHERE order_number = ?
            ''', (new_destination, order_number))
        new_payment = float(input("Введите новую сумму оплаты (оставьте пустым, если не изменяется): "))
        if new_payment:
            cursor.execute('''
                UPDATE expenses
                SET payment = ?
                WHERE order_number = ?
            ''', (new_payment, order_number))
        new_advance = float(input("Введите новую сумму аванса (оставьте пустым, если не изменяется): "))
        if new_advance:
            cursor.execute('''
                UPDATE expenses
                SET advance = ?
                WHERE order_number = ?
            ''', (new_advance, order_number))
        new_expense_type = input("Введите новый вид расходов (оставьте пустым, если не изменяется): ")
        if new_expense_type:
            cursor.execute('''
                UPDATE expenses
                SET expense_type = ?
                WHERE order_number = ?
            ''', (new_expense_type, order_number))
        new_expense_amount = float(input("Введите новую сумму расходов (оставьте пустым, если не изменяется): "))
        if new_expense_amount:
            cursor.execute('''
                UPDATE expenses
                SET expense_amount = ?
                WHERE order_number = ?
            ''', (new_expense_amount, order_number))
        conn.commit()
        print("Запись успешно отредактирована.")
    else:
        print("Запись не найдена.")

# Главное меню программы
while True:
    print("\n1. Добавить запись")
    print("2. Поиск записи")
    print("3. Удалить запись")
    print("4. Редактировать запись")
    print("5. Выйти из программы")
    choice = int(input("Выберите операцию: "))

    if choice == 1:
        add_expense()
    elif choice == 2:
        search_expense()
    elif choice == 3:
        delete_expense()
    elif choice == 4:
        edit_expense()
    elif choice == 5:
        break
    else:
        print("Неверный выбор. Пожалуйста, выберите одну из доступных операций.")

# Закрытие соединения с базой данных
conn.close()