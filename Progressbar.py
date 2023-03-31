from tkinter import *
from tkinter import ttk
from tkinter import messagebox
win=Tk()

def charge():
    s.configure('white.Vertical.TProgressbar',background='white',bordercolor='black')
    p['style']='white.Vertical.TProgressbar'
    p['value']+=10
    
    if p['value']==100:
        res1=messagebox.showinfo("FULL", "Charging full, Disconnect your charger")
        # print('Charging is full, Disconnect your charger')
    else:
        p.after(2000,charge)
        
        
def use():
    p['value']-=10
    
    if p['value']==10:
        s.configure('red.Vertical.TProgressbar',background='red',bordercolor='black')
        p['style']='red.Vertical.TProgressbar'
        res2=messagebox.showinfo("LOW", "Charging is low, Connect your charger")
        
        #print("Charging is low, Connect your charger")
    else:
        p.after(2000,use)
        
s=ttk.Style()
s.theme_use('clam')
s.configure('white.Vertical.TProgressbar',background='white',bordercolor='black')

p=ttk.Progressbar(win,orient=VERTICAL,style='white.Vertical.TProgressbar',length=200,value=20,maximum=100,mode='determinate')
p.pack(padx=20,pady=20)

b1=Button(win,text="Charging",command=charge)
b1.pack(padx=10,pady=10)

b2=Button(win,text='Using',command=use)
b2.pack(padx=10,pady=10) 

win.mainloop()
