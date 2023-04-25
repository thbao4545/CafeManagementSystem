from tkinter import *
from datetime import datetime
from tkinter import ttk
from StaffList import *
from Menu import *
from Department import *
root = Tk()
root.geometry("700x740")
root.title('Quản lý tiệm cà phê')

login_frame = Frame(root)
login_frame.pack(padx=20, pady=20)
main_frame = Frame(root)

def login():
    a = pasw.get()
    login_frame.destroy()
    main_frame.grid(row=0, column = 0)
def change_frame(frame1, frame2):
    frame2.grid_forget()
    frame1.grid(row = 0, column = 0)


title_label = Label(login_frame, text='Quản lý tiệm cà phê', fg='red', font=('Calibri', 20), width=25)
title_label.grid(row=0, column=0, columnspan=2, pady=10)

username_label = Label(login_frame, text='Tên đăng nhập', font=('Calibri', 12))
username_label.grid(row=1, column=0, padx=(0, 10), pady=(10, 5), sticky=E)

password_label = Label(login_frame, text='Mật khẩu', font=('Calibri', 12))
password_label.grid(row=2, column=0, padx=(0, 10), pady=(5, 10), sticky=E)

id_entry = Entry(login_frame, width=30)
id_entry.grid(row=1, column=1, pady=(10, 5))

pasw = Entry(login_frame, width=30, show="*")
pasw.grid(row=2, column=1, pady=(5, 10))

login_button = Button(login_frame, text='Đăng nhập', width=15, font=('Calibri', 12), command=login)
login_button.grid(row=3, column=1, pady=10)


Label(main_frame, text='Trang chủ', fg = 'red',font = ('cambria',16),width=25).grid(row=0,column=0)


#Department Frame
department_frame = Frame(root)
Label(department_frame, text='Quản lí bộ phận', fg='red', font=('cambria', 16), width=25).grid(row=0, column=0)
Button(main_frame, text='Phòng ban', width=15, command=lambda: change_frame(department_frame, main_frame)).grid(row=0, column=1)

department_list = [
Department("Thu ngân", "Xử lý các đơn hàng"),
Department("Pha chế", "Pha chế đồ uống"),
Department("Nhà bếp", "Chuẩn bị đồ ăn"),
Department("Quản lý", "Quản lý cửa hàng")
]

department_tree = ttk.Treeview(department_frame, columns=("Name", "Description"))
department_tree.heading("#0", text="STT")
department_tree.heading("Name", text="Tên")
department_tree.heading("Description", text="Mô tả")
department_tree.column("#0", width=35)
department_tree.column("#1", width=100)
department_tree.column("#2", width=180)
department_tree.grid(row=1, column=0, columnspan=2, sticky=W)

def load_department_data():
    for index, item in enumerate(department_list):
        department_tree.insert("", index, text=str(index + 1), values=(item.get_name(), item.get_description()))
load_department_data()

Button(department_frame, text='Quay về', width=15, borderwidth=2, relief="groove", command=lambda: change_frame(main_frame, department_frame)).grid(row=3, column=0, sticky="e")



# Staff Frame
staff_list = StaffList(0, [])
Button(main_frame,text = 'Nhân viên', width=15, command=lambda : change_frame(staff_frame,main_frame)).grid(row=1,column=1)

staff_frame = Frame(root)
Label(staff_frame, text = 'Quản lí nhân viên', fg = 'red',font = ('cambria',16),width=25).grid(row=0,column=0)
tree = ttk.Treeview(staff_frame, columns=("ID", "Name" , "Gender" , "Birthday" , "Address", "Starting Day" , "Department"))
tree.heading("#0", text="STT")
tree.heading("ID", text="ID")
tree.heading("Name", text="Họ và Tên")
tree.heading("Gender", text="Giới tính")
tree.heading("Birthday", text="Ngày sinh")
tree.heading("Address", text="Địa chỉ")
tree.heading("Starting Day", text="Ngày vào làm")
tree.heading("Department", text = "Bộ Phận")
tree.column("#0", width=27)
tree.column("#1", width=50)
tree.column("#2", width=100)
tree.column("#3", width=100)
tree.column("#4", width=100)
tree.column("#5", width=100)
tree.column("#6", width=100)
tree.column("#7", width=100)
tree.grid(row=1, column=0,columnspan=2,sticky="nsew")
#Ham them nhan vien
def show_nv(nv_l):
    for item in tree.get_children():
      tree.delete(item)
    a = 0
    for i in nv_l.list:
        tree.insert(parent='', index='end', iid=a, text=str(a+1), values=(i.get_ID(),i.get_name(),i.get_gender(),i.get_birthday(),i.get_address(),i.get_startingDay(),i.get_department()))
        a +=1
def add_nhan_vien():
    staff_list.addStaff(nv_id.get(),nv_name.get(),nv_gen.get(),nv_bdate.get(),nv_add.get(),nv_Sdate.get(),nv_de.get())
    show_nv(staff_list)

def xoa_nhan_vien():
    staff_list.remove_nhanvien(nv_id_xoa.get())
    show_nv(staff_list)

def search_nhanvien():
    if nv_search.get() == 'Tên' :
        a = staff_list.getByName(nv_key_search.get())
        show_nv(a)
    elif nv_search.get() == 'Năm Sinh':
        a = staff_list.getByBirthday(nv_key_search.get())
        show_nv(a)
    elif nv_search.get() == 'Địa chỉ':
        a = staff_list.getByAddress(nv_key_search.get())
        show_nv(a)
    elif nv_search.get() == 'ID' :
        a = staff_list.getByID(nv_key_search.get())
        show_nv(a)

def sort_nhanvien():
    if nv_sort.get() == 'ID' : 
        staff_list.sort_id()
        show_nv(staff_list)


Label(staff_frame,text = 'ID', bg = 'pink').grid(row=2,column=0, sticky= 'w')
nv_id = Entry(staff_frame)
nv_id.grid(row = 2, column = 1, columnspan= 3, sticky= "we")

Label(staff_frame,text = 'Họ và Tên', bg ='pink').grid(row=3,column=0, sticky= 'w')
nv_name = Entry(staff_frame)
nv_name.grid(row = 3, column = 1, columnspan= 3, sticky= "we")

Label(staff_frame,text = 'Giới tính', bg = 'pink').grid(row=4,column=0, sticky= 'w')
nv_gen = ttk.Combobox(staff_frame, textvariable=1, width=30)
nv_gen['values'] = ('Nam', 'Nữ' , 'Khác')
nv_gen.grid(row = 4, column = 1, columnspan= 3, sticky= "we")

Label(staff_frame,text = 'Ngày sinh', bg ='pink').grid(row=5,column=0, sticky= 'w')
nv_bdate = Entry(staff_frame)
nv_bdate.grid(row = 5, column = 1, columnspan= 3, sticky= "we")

Label(staff_frame,text = 'Địa chỉ', bg = 'pink').grid(row=6,column=0, sticky= 'w')
nv_add = Entry(staff_frame)
nv_add.grid(row = 6, column = 1, columnspan= 3, sticky= "we")

Label(staff_frame,text = 'Ngày vào làm', bg ='pink').grid(row=7,column=0, sticky='w')
nv_Sdate = Entry(staff_frame)
nv_Sdate.grid(row = 7, column = 1, columnspan= 3, sticky= "we")

Label(staff_frame,text = 'Bộ Phận', bg = 'pink').grid(row=8,column=0, sticky= 'w')
nv_de = Entry(staff_frame)
nv_de.grid(row = 8, column = 1, columnspan= 3, sticky= "we")

#Thêm 
Button(staff_frame,text = 'Thêm', width=15,borderwidth=2, relief="groove", command= add_nhan_vien).grid(row=9,column=1)

#Xóa
Label(staff_frame,text = 'Xóa nhân viên có ID :', bg = 'pink').grid(row=10,column=0, sticky= 'w')
nv_id_xoa = Entry(staff_frame)
nv_id_xoa.grid(row = 10, column = 1, columnspan= 3, sticky= "we")
Button(staff_frame,text = 'Xóa', width=15,borderwidth=2, relief="groove", command=xoa_nhan_vien).grid(row=11,column=1)

#Search
Label(staff_frame,text = 'Tìm nhân viên :', bg = 'pink').grid(row=12,column=0, sticky= 'w')
nv_search = ttk.Combobox(staff_frame, textvariable=2, width=30)
nv_search['values'] = ('Tên', 'Năm Sinh' , 'Địa chỉ' , 'ID')
nv_search.grid(row = 12, column = 1, columnspan= 3, sticky= "we")
Label(staff_frame,text = 'Giá trị cần tìm:', bg = 'pink').grid(row=13,column=0, sticky= 'w')
nv_key_search = Entry(staff_frame)
nv_key_search.grid(row = 13, column = 1, columnspan= 3, sticky= "we")
Button(staff_frame,text = 'Tìm', width=15,borderwidth=2, relief="groove", command= search_nhanvien).grid(row=14,column=1)

#Sort
Label(staff_frame,text = 'Sắp xếp :', bg = 'pink').grid(row=15,column=0, sticky= 'w')
nv_sort = ttk.Combobox(staff_frame, textvariable=3, width=30)
nv_sort['values'] = ('ID', 'Năm Sinh')
nv_sort.grid(row = 15, column = 1, columnspan= 3, sticky= "we")
Button(staff_frame,text = 'Sắp xếp', width=15,borderwidth=2, relief="groove", command= sort_nhanvien).grid(row=16,column=1)

Button(staff_frame,text = 'Tải lại', width=15, borderwidth=2, relief="groove", command=show_nv(staff_list)).grid(row=18,column=0)
Button(staff_frame,text = 'Lưu', width=15, borderwidth=2, relief="groove", command=lambda : change_frame(main_frame,staff_frame)).grid(row=18,column=1)

Button(staff_frame,text = 'Quay về', width=15, borderwidth=2, relief="groove", command=lambda : change_frame(main_frame,staff_frame)).grid(row=19,column=0,sticky="e")

# Menu Frame
menu_frame = Frame(root)
Label(menu_frame, text='Quản lí thực đơn', fg='red', font=('cambria', 16), width=25).grid(row=0, column=0)
Button(main_frame, text='Thực đơn', width=15, command=lambda: change_frame(menu_frame, main_frame)).grid(row=2, column=1)
drink_number = 5
food_number = 5
drink_list = [
    Drink("Phở gà", 50000, True, "Cả ngày", True),
    Drink("Bún chả", 40000, True, "Cả ngày", False),
    Drink("Cơm tấm", 35000, True, "Cả ngày", True),
    Drink("Bánh mì  ", 20000, True, "Cả ngày", True),
    Drink("Gỏi cuốn", 25000, True, "Cả ngày", False)
]
food_list = [
    Food("Trà đá", 2000, True, "Cả ngày", False),
    Food("Cà phê đen", 20000, True, "Cả ngày", True),
    Food("Cà phê sữa", 20000, True, "Cả ngày", False),
    Food("Bạc xỉu", 22000, True, "Cả ngày", True),
    Food("Nước mía", 15000, True, "Cả ngày", False)
]

menu = Menu(drink_number, food_number, drink_list, food_list)


menu_tree = ttk.Treeview(menu_frame, columns=("Name", "Price"))
menu_tree.heading("#0", text="STT")
menu_tree.heading("Name", text="Tên")
menu_tree.heading("Price", text="Giá")
menu_tree.column("#0", width=35)
menu_tree.column("#1", width=100)
menu_tree.column("#2", width=100)
menu_tree.grid(row=1, column=0, columnspan=2, sticky=W)

def load_menu_data():
    for index, item in enumerate(menu.get_drink_list()):
        menu_tree.insert("", index, text=str(index + 1), values=(item.get_name(), item.get_price()))

    food_offset = len(menu.get_drink_list())
    for index, item in enumerate(menu.get_food_list()):
        menu_tree.insert("", index + food_offset, text=str(index + food_offset + 1), values=(item.get_name(), item.get_price()))
load_menu_data()

def clear_inputs():
    item_name_entry.delete(0, END)
    item_price_entry.delete(0, END)

def get_selected_item():
    selected_item = menu_tree.focus()
    item_data = menu_tree.item(selected_item)
    return selected_item, item_data

def update_menu_tree():
    menu_tree.delete(*menu_tree.get_children())
    load_menu_data()

Label(menu_frame, text="Tên:").grid(row=4, column=0)
item_name_entry = Entry(menu_frame)
item_name_entry.grid(row=4, column=1)
Label(menu_frame, text="Đồ ăn").grid(row=4, column=2)
item_type_var = IntVar()
item_type = Checkbutton(menu_frame, variable=item_type_var)
item_type.grid(row=4, column=3)
Label(menu_frame, text="Giá tiền:").grid(row=5, column=0)
item_price_entry = Entry(menu_frame)
item_price_entry.grid(row=5, column=1)

def add_menu_item():
    name = item_name_entry.get()
    price = float(item_price_entry.get())
    type = bool(item_type_var.get())
    if type:
        menu.add_food2(name, price)
    else:
        menu.add_drink2(name, price)

    clear_inputs()
    update_menu_tree()

def edit_menu_item():
    
    clear_inputs()
    update_menu_tree()

def delete_menu_item():
    
    clear_inputs()  
    update_menu_tree()

add_button = Button(menu_frame, text="Thêm", width=15, command=add_menu_item)
add_button.grid(row=6, column=0, pady=10)
# Label(menu_frame, text="STT:").grid(row=7, column=0)
# item_entry = Entry(menu_frame)
# item_entry.grid(row=7, column=1)
edit_button = Button(menu_frame, text="Sửa", width=15, command=edit_menu_item)
edit_button.grid(row=7, column=0, pady=10)

delete_button = Button(menu_frame, text="Xóa", width=15, command=delete_menu_item)
delete_button.grid(row=8, column=0, pady=10)

back_button_menu = Button(menu_frame, text="Quay lại", width=15, command=lambda: change_frame(main_frame, menu_frame))
back_button_menu.grid(row=9, column=0, columnspan=2, pady=10)

# Order Frame

order_frame = Frame(root)
Label(order_frame, text='Quản lí thực đơn', fg='red', font=('cambria', 16), width=25).grid(row=0, column=0)
Button(main_frame, text='Đặt đồ', width=15, command=lambda: change_frame(order_frame, main_frame)).grid(row=3, column=1)
def get_current_date():
    return datetime.now().strftime("%Y-%m-%d")
date_label = Label(order_frame, text=get_current_date(), font=('cambria', 12))
date_label.grid(row=0, column=1, pady=10)

order_tree = ttk.Treeview(order_frame, columns=("Name", "Price", "Available", "SellingTime"))
order_tree.heading("#0", text="STT")
order_tree.heading("Name", text="Tên")
order_tree.heading("Price", text="Giá")
order_tree.heading("Available", text="Còn hàng")
order_tree.heading("SellingTime", text="Thời gian bán")
order_tree.column("#0", width=27)
order_tree.column("#1", width=100)
order_tree.column("#2", width=100)
order_tree.column("#3", width=100)
order_tree.column("#4", width=100)
order_tree.grid(row=1, column=0, columnspan=2, sticky=W)
def load_order_data():
    for index, item in enumerate(menu.get_drink_list()):
        order_tree.insert("", index, text=str(index + 1), values=(item.get_name(), item.get_price(), item.get_available(), item.get_selling_time()))

    food_offset = len(menu.get_drink_list())
    for index, item in enumerate(menu.get_food_list()):
        order_tree.insert("", index + food_offset, text=str(index + food_offset + 1), values=(item.get_name(), item.get_price(), item.get_available(), item.get_selling_time()))

load_order_data()

Label(order_frame, text="Số lượng:").grid(row=3, column=0)
quantity_entry = Entry(order_frame)
quantity_entry.grid(row=3, column=1)
Label(order_frame, text="Có đá?/Làm chay?").grid(row=4, column=0)
extra_info_var = IntVar()
extra_info = Checkbutton(order_frame, variable=extra_info_var)
extra_info.grid(row=4, column=1)
add_button = Button(order_frame, text="Add", width=15, command=lambda: add_order_item())
add_button.grid(row=5, column=0, pady=10)
ordered_tree = ttk.Treeview(order_frame, columns=("Name", "Price", "Quantity", "Total", "ExtraInfo"))
ordered_tree.heading("#0", text="STT")
ordered_tree.heading("Name", text="Tên")
ordered_tree.heading("Price", text="Giá")
ordered_tree.heading("Quantity", text="Số lượng")
ordered_tree.heading("ExtraInfo", text="Có đá?/Làm chay?")
ordered_tree.heading("Total", text="Thành tiền")
ordered_tree.column("#0", width=35)
ordered_tree.column("#1", width=100)
ordered_tree.column("#2", width=100)
ordered_tree.column("#3", width=100)
ordered_tree.column("#4", width=100)
ordered_tree.column("#5", width=150)
ordered_tree.grid(row=6, column=0, columnspan=2, sticky=W)

def update_order_tree():
    ordered_tree.delete(*ordered_tree.get_children())
    for index, item in enumerate(ordered_items):
        ordered_tree.insert("", index, text=str(index + 1), values=item)

ordered_items = []
def on_order_tree_click(event):
    global selected_item, item_data  
    selected_item = order_tree.selection()
    if selected_item:
        item_data = order_tree.item(selected_item)
        print(item_data)


order_tree.bind("<ButtonRelease-1>", on_order_tree_click)
def add_order_item():
    global selected_item, item_data
    item_name = item_data["values"][0]
    item_price = float(item_data["values"][1])  # Convert the price to float
    quantity = int(quantity_entry.get())
    extra_info_value = "Có" if extra_info_var.get() else "Không"

    total_price = item_price * quantity

    ordered_item = (item_name, item_price, quantity, total_price, extra_info_value)
    ordered_items.append(ordered_item)

    total_price_value.set(str(calculate_total_price()))

    update_order_tree()



def delete_ordered_item():
    selected_item = ordered_tree.selection()
    if selected_item:
        item_index = ordered_tree.index(selected_item)
        ordered_tree.delete(selected_item)
        ordered_items.pop(item_index)
        update_order_tree()


delete_button = Button(order_frame, text='Xóa', command=delete_ordered_item)
delete_button.grid(row=6, column=3)
def calculate_total_price():
    total_price = 0
    for item in ordered_items:
        total_price += item[3]  # The total price is at index 3
    return total_price
total_price_label = Label(order_frame, text="Tổng tiền: ", font=('cambria', 12))
total_price_label.grid(row=7, column=0, pady=10)

total_price_value = StringVar()
total_price_value.set(str(calculate_total_price()))
total_price_value_label = Label(order_frame, textvariable=total_price_value, font=('cambria', 12))
total_price_value_label.grid(row=7, column=1, pady=10)

ordered_items_with_date = []

def save_ordered_items():
    global ordered_items_with_date, ordered_items
    if ordered_items:
        if not ordered_items_with_date:
            ordered_items_with_date = [(datetime.now(), *item) for item in ordered_items]
        else:
            ordered_items_with_date += [(datetime.now(), *item) for item in ordered_items]
        # Clear the ordered_items list after saving
        ordered_items.clear()
        # Update the ordered_tree and total_price_value
        update_order_tree()
        total_price_value.set(str(calculate_total_price()))
    else:
        print("No items to save")

        
order_button = Button(order_frame, text='Đặt', command=save_ordered_items)
order_button.grid(row=8, column=3)


Button(order_frame, text='Quay về',command=lambda: change_frame(main_frame, order_frame)).grid(row=15, column = 0)

# Revenue Frame
revenue_frame = Frame(root)
Button(main_frame, text='Doanh thu', width=15, command=lambda: change_frame(revenue_frame, main_frame)).grid(row=4, column=1)
revenue_frame = Frame(root)
Label(revenue_frame, text='Thống kê doanh thu', fg='red', font=('cambria', 16), width=25).grid(row=0, column=0)
revenue_tree = ttk.Treeview(revenue_frame, columns=("Date", "Name", "Price", "Quantity", "Total", "ExtraInfo"))
revenue_tree.heading("#0", text="STT")
revenue_tree.heading("Date", text="Ngày")
revenue_tree.heading("Name", text="Tên")
revenue_tree.heading("Price", text="Giá")
revenue_tree.heading("Quantity", text="Số lượng")
revenue_tree.heading("Total", text="Thành tiền")
revenue_tree.heading("ExtraInfo", text="Thông tin thêm")
revenue_tree.column("#0", width=35)
revenue_tree.column("#1", width=100)
revenue_tree.column("#2", width=100)
revenue_tree.column("#3", width=100)
revenue_tree.column("#4", width=100)
revenue_tree.column("#5", width=60)
revenue_tree.grid(row=2, column=0, columnspan=3, sticky=W)

day_var = StringVar()
month_var = StringVar()

day_option = OptionMenu(revenue_frame, day_var, *range(1, 32))
day_option.grid(row=1, column=0)
month_option = OptionMenu(revenue_frame, month_var, *range(1, 13))
month_option.grid(row=1, column=1)

def display_matching_ordered_items():
    selected_day = int(day_var.get())
    selected_month = int(month_var.get())
    current_year = datetime.today().year
    selected_date = datetime(current_year, selected_month, selected_day).date()

    revenue_tree.delete(*revenue_tree.get_children())
    for index, item in enumerate(ordered_items_with_date):
        if item[0].date() == selected_date:
            revenue_tree.insert("", index, text=str(index + 1), values=item)
        else:
            print("No matching items for the selected date")



display_button = Button(revenue_frame, text='Display', command=display_matching_ordered_items)
display_button.grid(row=1, column=2)

Button(revenue_frame, text='Quay về',command=lambda: change_frame(main_frame, revenue_frame)).grid(row=15, column = 0)


root.mainloop()