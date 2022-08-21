from tkinter import*
root=Tk()

l1=Label(root,text='First name:',font=('Tahoma',20))
l1.pack(ipadx=5, ipady=5)
e1=Entry(root, font=('Tahoma',20),width=20,borderwidth=5)
e1.pack()
l2=Label(root,text='Last name:',font=('Tahoma',20))
l2.pack(ipadx=5, ipady=5)
e2=Entry(root, font=('Tahoma',20),width=20,borderwidth=5)
e2.pack()
l3=Label(root,text='Age:',font=('Tahoma',20))
l3.pack(ipadx=5, ipady=5)
e3=Entry(root, font=('Tahoma',20),width=20,borderwidth=5)
e3.pack()
l4=Label(root,text='Address:',font=('Tahoma',20))
l4.pack(ipadx=5, ipady=5)
e4=Entry(root, font=('Tahoma',20),width=20,borderwidth=5)
e4.pack()
l5=Label(root,text='Gender:',font=('Tahoma',20))
l5.pack(ipadx=5,ipady=5)
r1=Radiobutton(root,text='Female',font=('Tahoma',20))
r1.pack()
r2=Radiobutton(root,text='Male',font=('Tahoma',20))
r2.pack()

l5=Label(root,text='Course:',font=('Tahoma',20))
l5.pack(ipadx=5,ipady=5)

c1=Checkbutton(root,text='Web',font=('Tahoma',20))
c1.pack()
c2=Checkbutton(root,text='Programming',font=('Tahoma',20))
c2.pack()
c3=Checkbutton(root,text='Network',font=('Tahoma',20))
c3.pack()

root.mainloop()




         
