# Employee Payroll Management System
from tkinter import *
from tkinter import messagebox
import pymysql  # pip install pymysql
import time


def check_connection():
    try:
        con = pymysql.connect(host='localhost', user='root', password='', db='pms')
        cur = con.cursor()
        cur.execute("SELECT * FROM emp_salary")
        cur.fetchall()
        con.close()

    except Exception as ex:
        messagebox.showerror("Error", f'Error due to this: {str(ex)}')


class EmployeeSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Payroll Management System")
        self.root.geometry("1380x700+300+150")
        self.root.config(bg="#E5E4E2")
        Label(self.root, text="Payroll Management System", font=("times new roman", 28, "bold"), bg="black", fg="white",
              anchor="w", padx=8).place(x=0, y=0, relwidth=1)

        # variable
        self.var_emp_code = StringVar()
        self.var_designation = StringVar()
        self.var_name = StringVar()
        self.var_age = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_proof = StringVar()
        self.var_contact = StringVar()
        self.var_status = StringVar()
        self.var_experience = StringVar()
        self.var_blood_group = StringVar()
        self.var_account_no = StringVar()
        self.var_ifsc_code = StringVar()
        self.var_month = StringVar()
        self.var_year = StringVar()
        self.var_salary = StringVar()
        self.var_days = StringVar()
        self.var_absent = StringVar()
        self.var_medical = StringVar()
        self.var_pf = StringVar()
        self.var_convince = StringVar()
        self.var_net_salary = StringVar()

        # ---------------FRAME 1------------------
        frame1 = Frame(self.root, bd=2, relief=RIDGE, bg="#e3faff")
        frame1.place(x=10, y=65, width=750, height=620)
        Label(frame1, text="Employee Details", font=("times new roman", 20),
              bg="#f5f3f4", fg="black", anchor="w", padx=8).place(x=0, y=0, relwidth=1)

        Label(frame1, text="Employee Id:", font=(
            "times new roman", 20), bg="#e3faff", fg="black", ).place(x=10, y=70)
        Entry(frame1, font=("times new roman", 15),
              textvariable=self.var_emp_code, bg="#FEFEFA", fg="black", ).place(x=170, y=78)
        Button(frame1, text="Search", font=("times new roman", 16), bg="#1E90FF",
               fg="black", bd=2, relief="raised", ).place(x=580, y=60, height=40, width=120)

        # Row1
        Label(frame1, text="Designation:", font=(
            "times new roman", 20), bg="#e3faff", fg="black", ).place(x=10, y=120)
        Entry(frame1, font=("times new roman", 15), textvariable=self.var_designation,
              bg="#FEFEFA", fg="black", ).place(x=170, y=125, width=200)

        Label(frame1, text="D.O.B:", font=(
            "times new roman", 20), bg="#e3faff", fg="black", ).place(x=420, y=120)
        Entry(frame1, font=("times new roman", 15),
              textvariable=self.var_dob, bg="#FEFEFA", fg="black", ).place(x=520, y=125)

        # Row2
        Label(frame1, text="Name:", font=(
            "times new roman", 20), bg="#e3faff", fg="black", ).place(x=10, y=170)
        Entry(frame1, font=("times new roman", 15), textvariable=self.var_name,
              bg="#FEFEFA", fg="black", ).place(x=120, y=172, width=200)

        Label(frame1, text="D.O.Joining:", font=(
            "times new roman", 20), bg="#e3faff", fg="black", ).place(x=360, y=170)
        Entry(frame1, font=("times new roman", 15),
              textvariable=self.var_doj, bg="#FEFEFA", fg="black", ).place(x=520, y=172)

        # Row3
        Label(frame1, text="Age:", font=(
            "times new roman", 20), bg="#e3faff", fg="black", ).place(x=10, y=220)
        Entry(frame1, font=("times new roman", 15), textvariable=self.var_age,
              bg="#FEFEFA", fg="black", ).place(x=120, y=221, width=200)

        Label(frame1, text="Experience:", font=(
            "times new roman", 20), bg="#e3faff", fg="black", ).place(x=360, y=220)
        Entry(frame1, font=(
            "times new roman", 15), textvariable=self.var_experience, bg="#FEFEFA", fg="black", ).place(x=520, y=221)

        # Row4
        Label(frame1, text="Gender:", font=(
            "times new roman", 20), bg="#e3faff", fg="black", ).place(x=10, y=270)
        Entry(frame1, font=("times new roman", 15), textvariable=self.var_gender,
              bg="#FEFEFA", fg="black", ).place(x=120, y=272, width=200)

        Label(frame1, text="Proof Id:", font=(
            "times new roman", 20), bg="#e3faff", fg="black", ).place(x=360, y=270)
        Entry(frame1, font=("times new roman", 15),
              textvariable=self.var_proof, bg="#FEFEFA", fg="black", ).place(x=520, y=272)

        # Row5
        Label(frame1, text="Email:", font=(
            "times new roman", 20), bg="#e3faff", fg="black", ).place(x=10, y=320)
        Entry(frame1, font=("times new roman", 15), textvariable=self.var_email,
              bg="#FEFEFA", fg="black", ).place(x=120, y=324, width=200)

        Label(frame1, text="Contact No:", font=(
            "times new roman", 20), bg="#e3faff", fg="black", ).place(x=360, y=320)
        Entry(frame1, font=(
            "times new roman", 15), textvariable=self.var_contact, bg="#FEFEFA", fg="black", ).place(x=520, y=324)

        # Row6
        Label(frame1, text="Status:", font=(
            "times new roman", 20), bg="#e3faff", fg="black", ).place(x=10, y=370)
        Entry(frame1, font=("times new roman", 15), textvariable=self.var_status,
              bg="#FEFEFA", fg="black", ).place(x=120, y=376, width=200)

        Label(frame1, text="Blood Group:", font=(
            "times new roman", 20), bg="#e3faff", fg="black", ).place(x=360, y=370)
        Entry(frame1, font=(
            "times new roman", 15), textvariable=self.var_blood_group, bg="#FEFEFA", fg="black", ).place(x=520, y=376)

        # Row7
        Label(frame1, text="Account:", font=(
            "times new roman", 20), bg="#e3faff", fg="black", ).place(x=10, y=420)
        Entry(frame1, font=("times new roman", 15), textvariable=self.var_account_no,
              bg="#FEFEFA", fg="black", ).place(x=120, y=426, width=200)

        Label(frame1, text="IFSC Code:", font=(
            "times new roman", 20), bg="#e3faff", fg="black", ).place(x=360, y=420)
        Entry(frame1, font=("times new roman", 15),
              textvariable=self.var_ifsc_code, bg="#FEFEFA", fg="black", ).place(x=520, y=426)

        # Row8
        Label(frame1, text="Address:", font=(
            "times new roman", 20), bg="#e3faff", fg="black", ).place(x=10, y=470)
        self.txt_address = Text(frame1, font=(
            "times new roman", 15,), bg="#FEFEFA", fg="black", )
        self.txt_address.place(x=120, y=479, width=600, height=90)

        # --------------------FRAME 2--------------------

        frame2 = Frame(self.root, bd=2, relief=RIDGE, bg="#e3faff")
        frame2.place(x=770, y=65, width=600, height=300)
        Label(frame2, text="Employee Salary Details", font=(
            "times new roman", 20), bg="#f5f3f4", fg="black", anchor="w", padx=8).place(x=0, y=0, relwidth=1)

        # Row1
        Label(frame2, text="Month:", font=(
            "times new roman", 17), bg="#e3faff", fg="black", ).place(x=10, y=60)
        Entry(frame2, font=("times new roman", 15), textvariable=self.var_month,
              bg="#FEFEFA", fg="black", ).place(x=90, y=62, width=100)

        Label(frame2, text="Year:", font=(
            "times new roman", 17), bg="#e3faff", fg="black", ).place(x=210, y=60)
        Entry(frame2, font=("times new roman", 15), textvariable=self.var_year,
              bg="#FEFEFA", fg="black", ).place(x=270, y=62, width=100)

        Label(frame2, text="Salary:", font=(
            "times new roman", 17), bg="#e3faff", fg="black", ).place(x=390, y=60)
        Entry(frame2, font=("times new roman", 15), textvariable=self.var_salary,
              bg="#FEFEFA", fg="black", ).place(x=490, y=62, width=100)

        # Row2
        Label(frame2, text="Total Days:", font=(
            "times new roman", 18), bg="#e3faff", fg="black", ).place(x=10, y=100)
        Entry(frame2, font=("times new roman", 15), textvariable=self.var_days,
              bg="#FEFEFA", fg="black", ).place(x=140, y=105, width=150)

        Label(frame2, text="Absent:", font=(
            "times new roman", 18), bg="#e3faff", fg="black", ).place(x=320, y=100)
        Entry(frame2, font=("times new roman", 15), textvariable=self.var_absent,
              bg="#FEFEFA", fg="black", ).place(x=440, y=105, width=150)

        # Row3
        Label(frame2, text="Medical:", font=(
            "times new roman", 18), bg="#e3faff", fg="black", ).place(x=10, y=140)
        Entry(frame2, font=("times new roman", 15), textvariable=self.var_medical,
              bg="#FEFEFA", fg="black", ).place(x=140, y=145, width=150)

        Label(frame2, text="P. Fund:", font=(
            "times new roman", 18), bg="#e3faff", fg="black", ).place(x=320, y=140)
        Entry(frame2, font=("times new roman", 15), textvariable=self.var_pf,
              bg="#FEFEFA", fg="black", ).place(x=440, y=145, width=150)

        # Row4
        Label(frame2, text="Convince:", font=(
            "times new roman", 18), bg="#e3faff", fg="black", ).place(x=10, y=180)
        Entry(frame2, font=("times new roman", 15), textvariable=self.var_convince,
              bg="#FEFEFA", fg="black", ).place(x=140, y=185, width=150)

        Label(frame2, text="Net salary:", font=(
            "times new roman", 18), bg="#e3faff", fg="black", ).place(x=320, y=180)
        Entry(frame2, font=("times new roman", 15), textvariable=self.var_net_salary,
              bg="#FEFEFA", fg="black", ).place(x=440, y=185, width=150)

        # Row5
        Button(frame2, text="Add", command=self.calculate, font=(
            "times new roman", 16), bg="#1E90FF", fg="black", bd=2, relief="raised", ).place(x=90, y=230, width=100)
        Button(frame2, text="Save", command=self.add, font=("times new roman", 16),
               bg="#1E90FF", fg="black", bd=2, relief="raised", ).place(x=285, y=230, width=100)
        Button(frame2, text="Clear", font=("times new roman", 16), bg="#1E90FF",
               fg="black", bd=2, relief="raised", ).place(x=480, y=230, width=100)

        # frame3
        frame3 = Frame(self.root, bd=2, relief=RIDGE, bg="#e3faff")
        frame3.place(x=770, y=375, width=600, height=310)

        # calculator frame
        self.var_txt = StringVar()
        self.var_operator = ''

        def btn_click(num):
            self.var_operator = self.var_operator + str(num)
            self.var_txt.set(self.var_operator)

        def result():
            res = str(eval(self.var_operator))
            self.var_txt.set(res)
            self.var_operator = ''

        def clear_cal():
            self.var_txt.set('')
            self.var_operator = ''

        cal_frame = Frame(frame3, bg="#e3faff", bd=2, relief=RIDGE)
        cal_frame.place(x=2, y=2, width=250, height=300)

        Entry(cal_frame, bg="#FEFEFA", textvariable=self.var_txt, font=(
            "times new roman", 20, "bold"), justify=RIGHT).place(x=0, y=0, relwidth=1, height=50)

        # calculator button Row1
        Button(cal_frame, text='7', command=lambda: btn_click(
            7), font=("times new roman", 20)).place(x=2, y=51, w=60, h=60)
        Button(cal_frame, text='8', command=lambda: btn_click(
            8), font=("times new roman", 20)).place(x=63, y=51, w=60, h=60)
        Button(cal_frame, text='9', command=lambda: btn_click(
            9), font=("times new roman", 20)).place(x=124, y=51, w=60, h=60)
        Button(cal_frame, text='/', command=lambda: btn_click('/'), font=("times new roman", 20),
               bg="#1E90FF", fg="black", bd=2, relief="raised", ).place(x=185, y=51, w=60, h=60)

        # calculator button Row2
        Button(cal_frame, text='4', command=lambda: btn_click(
            4), font=("times new roman", 20)).place(x=2, y=112, w=60, h=60)
        Button(cal_frame, text='5', command=lambda: btn_click(
            5), font=("times new roman", 20)).place(x=63, y=112, w=60, h=60)
        Button(cal_frame, text='6', command=lambda: btn_click(
            6), font=("times new roman", 20)).place(x=124, y=112, w=60, h=60)
        Button(cal_frame, text='*', command=lambda: btn_click('*'), font=("times new roman", 20),
               bg="#1E90FF", fg="black", bd=2, relief="raised", ).place(x=185, y=112, w=60, h=60)

        # Calculator button Row3
        Button(cal_frame, text='1', command=lambda: btn_click(
            1), font=("times new roman", 20)).place(x=2, y=172, w=60, h=60)
        Button(cal_frame, text='2', command=lambda: btn_click(
            2), font=("times new roman", 20)).place(x=63, y=172, w=60, h=60)
        Button(cal_frame, text='3', command=lambda: btn_click(
            3), font=("times new roman", 20)).place(x=124, y=172, w=60, h=60)
        Button(cal_frame, text='-', command=lambda: btn_click('-'), font=("times new roman", 20),
               bg="#1E90FF", fg="black", bd=2, relief="raised", ).place(x=185, y=172, w=60, h=60)

        # calculator button Row4
        Button(cal_frame, text='0', command=lambda: btn_click(0), font=(
            "times new roman", 20), bg="#1E90FF", fg="black", bd=2, relief="raised", ).place(x=2, y=232, w=60, h=60)
        Button(cal_frame, text='C', command=clear_cal, font=("times new roman", 20),
               bg="#1E90FF", fg="black", bd=2, relief="raised", ).place(x=63, y=232, w=60, h=60)
        Button(cal_frame, text='+', command=lambda: btn_click('+'), font=("times new roman", 20),
               bg="#1E90FF", fg="black", bd=2, relief="raised", ).place(x=124, y=232, w=60, h=60)
        Button(cal_frame, text='=', command=result, font=("times new roman", 20),
               bg="#1E90FF", fg="black", bd=2, relief="raised", ).place(x=185, y=232, w=60, h=60)

        # ------------------Salary Frame------------------
        sal_frame = Frame(frame3, bg="#e3faff", bd=2, relief=RIDGE)
        sal_frame.place(x=255, y=2, width=340, height=300)
        Label(sal_frame, text="Salary Receipt", font=(
            "times new roman", 20), bg="#f5f3f4", fg="black", anchor="w", padx=8).place(x=0, y=-3, relwidth=1)

        sal_frame2 = Frame(sal_frame, bg="#e3faff", bd=2, relief=RIDGE)
        sal_frame2.place(x=0, y=30, relwidth=1, height=230)

        # ------------- SALARY RECEIPT -------------
        sample = f'''\tCompany Name, XYZ\n\tAddress: Xyz, Floor4
--------------------------------------------------
 Employee ID\t\t:    
 Salary Of\t\t:   MON-YYYY
 Generated On\t\t:   DD-MM-YYYY
--------------------------------------------------
 Total Days\t\t:   DD
 Total Present\t\t:   DD
 Total Absent\t\t:   DD
 convince\t\t:   Rs.----
 Medical\t\t:   Rs.----
 PF\t\t:   Rs.----
 Gross Payment\t\t:   Rs.-------
 Net Salary\t\t:   Rs.--------
--------------------------------------------------
 This is computer generated slip, 
 not required any signature
'''

        scroll_y = Scrollbar(sal_frame2, orient=VERTICAL)
        scroll_y.pack(fill=Y, side=RIGHT)

        self.txt_salary_receipt = Text(sal_frame2, font=(
            "times new roman", 13), bg='#FEFEFA', yscrollcommand=scroll_y.set)
        self.txt_salary_receipt.pack(fill=BOTH, expand=1)
        scroll_y.config(command=self.txt_salary_receipt.yview)
        self.txt_salary_receipt.insert(END, sample)

        Button(sal_frame, text="Print", font=("times new roman", 18), bg="#1E90FF",
               fg="black", bd=2, relief="raised", ).place(x=230, y=262, width=100, height=32)

        check_connection()

    def add(self):
        if self.var_name.get() == '' or self.var_email.get() == '' or self.var_net_salary.get() == '':
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                con = pymysql.connect(
                    host='localhost', user='root', password='', db='pms')
                cur = con.cursor()
                cur.execute("SELECT * FROM emp_salary WHERE emp_code = %s",
                            (self.var_emp_code.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror(
                        'Error', 'This employee ID is already available in our records, try again with another ID',
                        parent=self.root)
                else:
                    # Convert numeric fields to appropriate types
                    try:
                        age = int(self.var_age.get())
                        experience = float(self.var_experience.get())
                        salary = float(self.var_salary.get())
                        days = int(self.var_days.get())
                        absent = int(self.var_absent.get())
                        medical = float(self.var_medical.get())
                        pf = float(self.var_pf.get())
                        convince = float(self.var_convince.get())
                        net_salary = float(self.var_net_salary.get())
                    except ValueError as e:
                        messagebox.showerror(
                            "Error", f"Invalid numeric value: {str(e)}")
                        return

                    cur.execute(
                        "INSERT INTO emp_salary (emp_code, designation, name, age, gender, email, status, dob, "
                        "doj, experience, proof, contact, blood_group, account_no, ifsc_code, address, month, year, "
                        "salary, days, absent, medical, pf, convince, net_salary) VALUES (%s, %s, %s, %s, %s, %s, %s,"
                        " %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        (
                            self.var_emp_code.get(),
                            self.var_designation.get(),
                            self.var_name.get(),
                            age,
                            self.var_gender.get(),
                            self.var_email.get(),
                            self.var_status.get(),
                            self.var_dob.get(),
                            self.var_doj.get(),
                            experience,
                            self.var_proof.get(),
                            self.var_contact.get(),
                            self.var_blood_group.get(),
                            self.var_account_no.get(),
                            self.var_ifsc_code.get(),
                            self.txt_address.get("1.0", END).strip(),
                            self.var_month.get(),
                            self.var_year.get(),
                            salary,
                            days,
                            absent,
                            medical,
                            pf,
                            convince,
                            net_salary
                        )
                    )
                    con.commit()
                    con.close()
                    file_ = open("salary_receipt/" +
                                 str(self.var_emp_code.get()) + ".txt", 'w')
                    file_.write(self.txt_salary_receipt.get('1.0', END))
                    file_.close()
                    messagebox.showinfo(
                        'Success', 'Record added successfully', parent=self.root)

            except Exception as ex:
                messagebox.showerror("Error!", f'Error due to this: {str(ex)}')

    def calculate(self):
        if self.var_month.get() == '' or self.var_year.get() == '' or self.var_salary.get() == '':
            messagebox.showerror('Error', 'All fields are required')
        else:
            per_day = int(self.var_salary.get()) / int(self.var_days.get())
            work_day = int(self.var_days.get()) - int(self.var_absent.get())
            sal_ = per_day * work_day
            deduct = int(self.var_medical.get()) + int(self.var_pf.get())
            addition = int(self.var_convince.get())
            net_sal = sal_ - deduct + addition
            self.var_net_salary.set(str(round(net_sal, 2)))
            # update the receipt
            new_sample = f'''\tCompany Name, XYZ\n\tAddress: Xyz, Floor4
--------------------------------------------------
 Employee ID\t\t:    {self.var_emp_code.get()}
 Salary Of\t\t:   {self.var_month.get()}-{self.var_year.get()}
 Generated On\t\t:   {str(time.strftime("%d-%m-%y"))}
--------------------------------------------------
 Total Days\t\t:   {self.var_days.get()}
 Total Present\t\t:   {int(self.var_days.get()) - int(self.var_absent.get())}
 Total Absent\t\t:   {self.var_absent.get()}
 convince\t\t:   Rs.{self.var_convince.get()}
 Medical\t\t:   Rs.{self.var_medical.get()}
 PF\t\t:   Rs.{self.var_pf.get()}
 Gross Payment\t\t:   Rs.{self.var_salary.get()}
 Net Salary\t\t:   Rs.{self.var_net_salary.get()}
--------------------------------------------------
     This is computer generated slip, 
     not required any signature
'''

            self.txt_salary_receipt.delete('1.0', END)
            self.txt_salary_receipt.insert(END, new_sample)


root = Tk()
obj = EmployeeSystem(root)
root.mainloop()
