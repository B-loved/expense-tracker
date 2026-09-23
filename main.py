import csv

# Khởi tạo các biến để lưu trữ dữ liệu tính toán
total_expense = 0
category_expenses = {}

# Đọc file CSV
with open("data/expenses.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        # Chuyển đổi số tiền từ chuỗi (string) sang số nguyên (integer) để tính toán
        amount = int(row['amount'])
        category = row['category']
        
        # 1. Cộng dồn vào tổng chi tiêu
        total_expense += amount
        
        # 2. Gom nhóm và cộng dồn chi tiêu theo từng category
        if category in category_expenses:
            category_expenses[category] += amount
        else:
            category_expenses[category] = amount

# 3. Tìm category tiêu nhiều nhất dựa vào giá trị lớn nhất trong dictionary
highest_category = max(category_expenses, key=category_expenses.get)



print("Tổng chi tiêu")
print(f"Total expense: {total_expense}")
print()

print("Chi tiêu theo category")
for cat, amt in category_expenses.items():
    print(f"{cat}: {amt}")
print()

print("Category tiêu nhiều nhất")
print(f"Highest spending category: {highest_category}")
