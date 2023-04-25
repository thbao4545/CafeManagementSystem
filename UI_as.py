from tkinter import * 
from tkinter import ttk
from StaffList import *
from Staff import *
from Department import Department
from Drink import Drink
from Food import Food
from Item import Item
from Menu import Menu

roof = Tk()
roof.title('Coffee Shop Management')
roof.geometry('700x640')

staff_list = StaffList(0, [])
login_frame = Frame(roof)
login_frame.pack(padx=20, pady=20)

main_frame = Frame(roof)
staff_frame = Frame(roof)

def loginn():
    a = passw.get()
    if a == '1' :
        login_frame.destroy()
        main_frame.grid(row=0, column = 0)
def change_frame(frame1, frame2):
    frame2.grid_forget()
    frame1.grid(row = 0, column = 0)
    
#login_frame
# Label(login_frame, text='Coffee Shop Management', fg = 'red',font = ('cambria',16),width=25).grid(row=0,column=0)
# Label(login_frame,text = 'User Name', bg = 'pink').grid(row=1,column=0)
# Label(login_frame,text = 'Password', bg ='pink').grid(row=2,column=0)
# id = Entry(login_frame,width=30)
# id.grid(row = 1, column = 1)
# passw = Entry(login_frame,width=30)
# passw.grid(row = 2, column = 1)
# Button(login_frame,text = 'Login', width=15, command = loginn).grid(row=3,column=1)
title_label = Label(login_frame, text='Coffee Shop Management', fg='red', font=('Calibri', 20), width=25)
title_label.grid(row=0, column=0, columnspan=2, pady=10)

username_label = Label(login_frame, text='User Name', font=('Calibri', 12))
username_label.grid(row=1, column=0, padx=(0, 10), pady=(10, 5), sticky=E)

password_label = Label(login_frame, text='Password', font=('Calibri', 12))
password_label.grid(row=2, column=0, padx=(0, 10), pady=(5, 10), sticky=E)

id_entry = Entry(login_frame, width=30)
id_entry.grid(row=1, column=1, pady=(10, 5))

passw = Entry(login_frame, width=30, show="*")
passw.grid(row=2, column=1, pady=(5, 10))

login_button = Button(login_frame, text='Login', width=15, font=('Calibri', 12), command=loginn)
login_button.grid(row=3, column=1, pady=10)
#main_frame
Label(main_frame, text='Trang chủ', fg = 'red',font = ('cambria',16),width=25).grid(row=0,column=0)
Button(main_frame,text = 'Nhân viên', width=15, command=lambda : change_frame(staff_frame,main_frame)).grid(row=0,column=1)
Button(main_frame,text = 'Đặt món', width=15).grid(row=1,column=1)
Button(main_frame,text = 'Doanh thu', width=15).grid(row=2,column=1)

#nhanvien_frame
#bảng nhân viên
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
tree.column("#0", width=25)
tree.column("#1", width=50)
tree.column("#2", width=100)
tree.column("#3", width=100)
tree.column("#4", width=100)
tree.column("#5", width=100)
tree.column("#6", width=100)
tree.column("#7", width=100)
tree.insert(parent='', index='end', iid=0, text='1', values=('001', 'Nguyen Van A', 'Nam', '01/01/1990', 'Ha Noi', '01/01/2020', 'Phong Ban A'))
tree.insert(parent='', index='end', iid=1, text='2', values=('002', 'Nguyen Thi B', 'Nu', '02/02/1995', 'Ho Chi Minh', '02/02/2021', 'Phong Ban B'))
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

Button(staff_frame,text = 'ReLoad', width=15, borderwidth=2, relief="groove", command=show_nv(staff_list)).grid(row=18,column=0)
Button(staff_frame,text = 'Save', width=15, borderwidth=2, relief="groove", command=lambda : change_frame(main_frame,staff_frame)).grid(row=18,column=1)

Button(staff_frame,text = 'Back home', width=15, borderwidth=2, relief="groove", command=lambda : change_frame(main_frame,staff_frame)).grid(row=19,column=0,sticky="e")

order_frame = Frame(roof)
Button(main_frame, text='Đặt món', width=15, command=lambda: change_frame(order_frame, main_frame)).grid(row=1, column=1)


Button(order_frame,text = 'Back home', width=15, borderwidth=2, relief="groove", command=lambda : change_frame(main_frame,order_frame)).grid(row=19,column=0,sticky="e")



doanhthu_frame = Frame(roof)
Button(main_frame, text='Doanh thu', width=15, command=lambda: change_frame(doanhthu_frame, main_frame)).grid(row=2, column=1)

roof.mainloop()
