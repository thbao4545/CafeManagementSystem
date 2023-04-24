from tkinter import * 
from tkinter import ttk
from StaffList import *
from Staff import *

roof = Tk()
roof.title('Quan ly quan cafe')
roof.geometry('700x640')

nv_list = StaffList(0, [])
login_frame = Frame(roof)
login_frame.grid(row = 0, column= 0)

main_frame = Frame(roof)
nhanv_frame = Frame(roof)

def loginn():
    a = passw.get()
    if a == '1' :
        login_frame.destroy()
        main_frame.grid(row=0, column = 0)
def change_frame(frame1, frame2):
    frame2.grid_forget()
    frame1.grid(row = 0, column = 0)
    
#login_frame
Label(login_frame, text='Ung dung quan li quan cafe', fg = 'red',font = ('cambria',16),width=25).grid(row=0,column=0)
Label(login_frame,text = 'Tên đăng nhập', bg = 'pink').grid(row=1,column=0)
Label(login_frame,text = 'Mật Khẩu', bg ='pink').grid(row=2,column=0)
id = Entry(login_frame,width=30)
id.grid(row = 1, column = 1)
passw = Entry(login_frame,width=30)
passw.grid(row = 2, column = 1)
Button(login_frame,text = 'Login', width=15, command = loginn).grid(row=3,column=1)

#main_frame
Label(main_frame, text='Trang chủ', fg = 'red',font = ('cambria',16),width=25).grid(row=0,column=0)
Button(main_frame,text = 'Nhân viên', width=15, command=lambda : change_frame(nhanv_frame,main_frame)).grid(row=0,column=1)
Button(main_frame,text = 'Đặt món', width=15).grid(row=1,column=1)
Button(main_frame,text = 'Doanh thu', width=15).grid(row=2,column=1)

#nhanvien_frame
#bảng nhân viên
Label(nhanv_frame, text = 'Quản lí nhân viên', fg = 'red',font = ('cambria',16),width=25).grid(row=0,column=0)
tree = ttk.Treeview(nhanv_frame, columns=("ID", "Name" , "Gender" , "Birthday" , "Address", "Starting Day" , "Department"))
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
    nv_list.addStaff(nv_id.get(),nv_name.get(),nv_gen.get(),nv_bdate.get(),nv_add.get(),nv_Sdate.get(),nv_de.get())
    show_nv(nv_list)

def xoa_nhan_vien():
    nv_list.remove_nhanvien(nv_id_xoa.get())
    show_nv(nv_list)

def search_nhanvien():
    if nv_search.get() == 'Tên' :
        a = nv_list.getByName(nv_key_search.get())
        show_nv(a)
    elif nv_search.get() == 'Năm Sinh':
        a = nv_list.getByBirthday(nv_key_search.get())
        show_nv(a)
    elif nv_search.get() == 'Địa chỉ':
        a = nv_list.getByAddress(nv_key_search.get())
        show_nv(a)
    elif nv_search.get() == 'ID' :
        a = nv_list.getByID(nv_key_search.get())
        show_nv(a)

def sort_nhanvien():
    if nv_sort.get() == 'ID' : 
        nv_list.sort_id()
        show_nv(nv_list)


Label(nhanv_frame,text = 'ID', bg = 'pink').grid(row=2,column=0, sticky= 'w')
nv_id = Entry(nhanv_frame)
nv_id.grid(row = 2, column = 1, columnspan= 3, sticky= "we")

Label(nhanv_frame,text = 'Họ và Tên', bg ='pink').grid(row=3,column=0, sticky= 'w')
nv_name = Entry(nhanv_frame)
nv_name.grid(row = 3, column = 1, columnspan= 3, sticky= "we")

Label(nhanv_frame,text = 'Giới tính', bg = 'pink').grid(row=4,column=0, sticky= 'w')
nv_gen = ttk.Combobox(nhanv_frame, textvariable=1, width=30)
nv_gen['values'] = ('Nam', 'Nữ' , 'Khác')
nv_gen.grid(row = 4, column = 1, columnspan= 3, sticky= "we")

Label(nhanv_frame,text = 'Ngày sinh', bg ='pink').grid(row=5,column=0, sticky= 'w')
nv_bdate = Entry(nhanv_frame)
nv_bdate.grid(row = 5, column = 1, columnspan= 3, sticky= "we")

Label(nhanv_frame,text = 'Địa chỉ', bg = 'pink').grid(row=6,column=0, sticky= 'w')
nv_add = Entry(nhanv_frame)
nv_add.grid(row = 6, column = 1, columnspan= 3, sticky= "we")

Label(nhanv_frame,text = 'Ngày vào làm', bg ='pink').grid(row=7,column=0, sticky='w')
nv_Sdate = Entry(nhanv_frame)
nv_Sdate.grid(row = 7, column = 1, columnspan= 3, sticky= "we")

Label(nhanv_frame,text = 'Bộ Phận', bg = 'pink').grid(row=8,column=0, sticky= 'w')
nv_de = Entry(nhanv_frame)
nv_de.grid(row = 8, column = 1, columnspan= 3, sticky= "we")

#Thêm 
Button(nhanv_frame,text = 'Thêm', width=15,borderwidth=2, relief="groove", command= add_nhan_vien).grid(row=9,column=1)

#Xóa
Label(nhanv_frame,text = 'Xóa nhân viên có ID :', bg = 'pink').grid(row=10,column=0, sticky= 'w')
nv_id_xoa = Entry(nhanv_frame)
nv_id_xoa.grid(row = 10, column = 1, columnspan= 3, sticky= "we")
Button(nhanv_frame,text = 'Xóa', width=15,borderwidth=2, relief="groove", command=xoa_nhan_vien).grid(row=11,column=1)

#Search
Label(nhanv_frame,text = 'Tìm nhân viên :', bg = 'pink').grid(row=12,column=0, sticky= 'w')
nv_search = ttk.Combobox(nhanv_frame, textvariable=2, width=30)
nv_search['values'] = ('Tên', 'Năm Sinh' , 'Địa chỉ' , 'ID')
nv_search.grid(row = 12, column = 1, columnspan= 3, sticky= "we")
Label(nhanv_frame,text = 'Giá trị cần tìm:', bg = 'pink').grid(row=13,column=0, sticky= 'w')
nv_key_search = Entry(nhanv_frame)
nv_key_search.grid(row = 13, column = 1, columnspan= 3, sticky= "we")
Button(nhanv_frame,text = 'Tìm', width=15,borderwidth=2, relief="groove", command= search_nhanvien).grid(row=14,column=1)

#Sort
Label(nhanv_frame,text = 'Sắp xếp :', bg = 'pink').grid(row=15,column=0, sticky= 'w')
nv_sort = ttk.Combobox(nhanv_frame, textvariable=3, width=30)
nv_sort['values'] = ('ID', 'Năm Sinh')
nv_sort.grid(row = 15, column = 1, columnspan= 3, sticky= "we")
Button(nhanv_frame,text = 'Sắp xếp', width=15,borderwidth=2, relief="groove", command= sort_nhanvien).grid(row=16,column=1)

Button(nhanv_frame,text = 'ReLoad', width=15, borderwidth=2, relief="groove", command=show_nv(nv_list)).grid(row=18,column=0)
Button(nhanv_frame,text = 'Save', width=15, borderwidth=2, relief="groove", command=lambda : change_frame(main_frame,nhanv_frame)).grid(row=18,column=1)

Button(nhanv_frame,text = 'Back home', width=15, borderwidth=2, relief="groove", command=lambda : change_frame(main_frame,nhanv_frame)).grid(row=19,column=0,sticky="e")

roof.mainloop()
