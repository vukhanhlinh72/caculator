import tkinter as tk
import math

# Xử lý các phép toán cơ bản
def button_click(value):
    current = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(0, current + value)

def clear_display():
    entry_display.delete(0, tk.END)

def calculate():
    try:
        expression = entry_display.get()
        # Tính toán biểu thức, thay thế các hàm toán học với thư viện math
        result = eval(expression, {"__builtins__": None}, math.__dict__)  # Chỉ cho phép các hàm toán học
        entry_display.delete(0, tk.END)
        entry_display.insert(0, str(result))
    except Exception:
        entry_display.delete(0, tk.END)
        entry_display.insert(0, "Error")

# Tính toán các hàm toán học
def calculate_function(func):
    try:
        value = entry_display.get()
        
        if func == "sqrt":
            result = math.sqrt(float(value))
        elif func == "sin":
            result = math.sin(math.radians(float(value)))  # Đổi sang radian
        elif func == "cos":
            result = math.cos(math.radians(float(value)))
        elif func == "tan":
            result = math.tan(math.radians(float(value)))
        elif func == "log":
            result = math.log10(float(value))
        elif func == "ln":
            if float(value) <= 0:
                raise ValueError("ln undefined for non-positive values")
            result = math.log(float(value))  # log tự nhiên
        elif func == "factorial":
            if float(value) < 0 or float(value) != int(value):
                raise ValueError("Factorial undefined for negative or non-integer values")
            result = math.factorial(int(float(value)))  # Chỉ chấp nhận số nguyên không âm
        elif func == "mod":
            # Xử lý phép toán mod, yêu cầu người dùng nhập 2 số cách nhau bằng dấu phẩy (ví dụ: 12, 5)
            numbers = value.split(',')
            if len(numbers) == 2:
                num1 = float(numbers[0].strip())
                num2 = float(numbers[1].strip())
                result = num1 % num2
            else:
                raise ValueError("Please enter two numbers separated by a comma for mod.")
        entry_display.delete(0, tk.END)
        entry_display.insert(0, str(result))
    except Exception as e:
        entry_display.delete(0, tk.END)
        entry_display.insert(0, f"Error: {str(e)}")

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Máy tính Casio fx-580")
window.geometry("400x600")
window.resizable(False, False)

# Màn hình hiển thị
entry_display = tk.Entry(window, font=("Arial", 20), bd=10, justify="right")
entry_display.grid(row=0, column=0, columnspan=5, ipadx=10, ipady=10, sticky="nsew")

# Các nút chức năng và số
buttons = [
    '7', '8', '9', '/', 'C',
    '4', '5', '6', '*', 'sqrt',
    '1', '2', '3', '-', 'sin',
    '0', '.', '=', '+', 'cos',
    '(', ')', '^', 'log', 'tan',
    'ln', '!', 'pi', 'e', 'mod'
]

# Bố trí các nút trên giao diện
row_val = 1
col_val = 0

for button in buttons:
    if button == "=":
        btn = tk.Button(window, text=button, font=("Arial", 18), bg="orange", fg="white",
                        command=calculate)
    elif button == "C":
        btn = tk.Button(window, text=button, font=("Arial", 18), bg="red", fg="white",
                        command=clear_display)
    elif button in ["sqrt", "sin", "cos", "tan", "log", "ln", "!"]:
        btn = tk.Button(window, text=button, font=("Arial", 18), bg="lightblue",
                        command=lambda func=button: calculate_function(func))
    elif button == "pi":
        btn = tk.Button(window, text=button, font=("Arial", 18), bg="lightgreen",
                        command=lambda: button_click(str(math.pi)))
    elif button == "e":
        btn = tk.Button(window, text=button, font=("Arial", 18), bg="lightgreen",
                        command=lambda: button_click(str(math.e)))
    elif button == "^":
        btn = tk.Button(window, text="^", font=("Arial", 18), bg="lightgray",
                        command=lambda: button_click("**"))  # Dùng ** cho lũy thừa
    elif button == "mod":
        btn = tk.Button(window, text=button, font=("Arial", 18), bg="lightblue",
                        command=lambda: button_click("mod"))
    else:
        btn = tk.Button(window, text=button, font=("Arial", 18), bg="lightgray",
                        command=lambda value=button: button_click(value))
    
    btn.grid(row=row_val, column=col_val, sticky="nsew", ipadx=10, ipady=10)
    col_val += 1
    if col_val > 4:
        col_val = 0
        row_val += 1

# Cấu hình lưới
for i in range(6):  # 5 hàng nút + 1 màn hình
    window.grid_rowconfigure(i, weight=1)
for j in range(5):  # 5 cột nút
    window.grid_columnconfigure(j, weight=1)

# Chạy ứng dụng
window.mainloop()
