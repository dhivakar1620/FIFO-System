from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas 
from reportlab.lib import colors
from tkcalendar import DateEntry
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
#import matplotlib.pyplot as plt
#from tkinter import *
from tkinter import Tk,Toplevel,TRUE,BOTH,W,E 
from tkinter import Frame,Label,Entry,Button,OptionMenu,Radiobutton
from tkinter import StringVar,IntVar 
from tkinter import LEFT,RIGHT,CENTER,TOP,BOTTOM
from tkinter import messagebox,filedialog
from tkscrolledframe import ScrolledFrame
import os
import time
import datetime
import sqlite3
import pickle


flgrp=0
mm=0
mc=0
fl_na='C:/Users/YKDHIv/Desktop/pro/count/GUI'

#width = 1350
#height = 750
rot=Tk()
rot.title("running...")
rot.iconbitmap('logo.ico')
#ph_exist=PhotoImage(file='exit.png) W
height = rot.winfo_screenheight()
width = rot.winfo_screenwidth()

idd="Member"
q=0
con=sqlite3.connect('store.db')
cr=con.cursor()
bon=sqlite3.connect('disk.db')
fr=bon.cursor()
cr.execute("""CREATE TABLE IF NOT EXISTS pswdt(
                            ep_id INTEGER PRIMARY KEY NOT NULL,
                            us_na TEXT,
                            psw TEXT,
                            asc TEXT)""")
cr.execute("""CREATE TABLE IF NOT EXISTS urgenttb(
                            date TEXT NOT NULL,
                            jc_no TEXT,
                            pt_no TEXT,
                            qty INTEGER)""")
cr.execute("""CREATE TABLE IF NOT EXISTS store_out(
                            sojc_no INTEGER PRIMARY KEY NOT NULL,
                            sostr_per TEXT,
                            soloy_per TEXT,
                            sorec_qty INTEGER,
                            so_dt TEXT,
                            sodis_ti TEXT)""")
cr.execute("""CREATE TABLE IF NOT EXISTS store_in(
                            sijc_no INTEGER PRIMARY KEY NOT NULL,
                            sidc_no TEXT,
                            siloy_per TEXT,
                            simod_na TEXT,
                            sipt_no TEXT,
                            sirec_qty INTEGER,
                            sirec_per TEXT,
                            si_dt TEXT,
                            sirec_ti TEXT)""")
cr.execute("""CREATE TABLE IF NOT EXISTS logdt(
                            jc_no INTEGER PRIMARY KEY NOT NULL,
                            stg TEXT,
                            tot_qty INTEGER,
                            Ifin_qty INTEGER,
                            Idef_qty INTEGER,
                            Pfin_qty INTEGER,
                            Pdef_qty INTEGER,
                            Pmis_qty INTEGER,
                            Cfin_qty INTEGER,
                            Cdef_qty INTEGER,
                            Cmis_qty INTEGER,
                            Ffin_qty INTEGER,
                            Fdef_qty INTEGER,
                            Fmin_qty INTEGER,
                            def_qty INTEGER,
                            miss_qty INTERGER)""")
cr.execute("""CREATE TABLE IF NOT EXISTS flogdt(
                            jc_no INTEGER PRIMARY KEY NOT NULL,
                            stg TEXT,
                            tot_qty INTEGER,
                            Ifin_qty INTEGER,
                            Idef_qty INTEGER,
                            Pfin_qty INTEGER,
                            Pdef_qty INTEGER,
                            Pmis_qty INTEGER,
                            Cfin_qty INTEGER,
                            Cdef_qty INTEGER,
                            Cmis_qty INTEGER,
                            Ffin_qty INTEGER,
                            Fdef_qty INTEGER,
                            Fmin_qty INTEGER,
                            def_qty INTEGER,
                            miss_qty INTERGER)""")
cr.execute("""CREATE TABLE IF NOT EXISTS insp(
                                    injc_no INTEGER PRIMARY KEY NOT NULL,
                                    inin_per TEXT,
                                    insh_no TEXT,
                                    insp_qty INTEGER,
                                    rdin1 INTEGER,
                                    rdin2 INTEGER,
                                    rdin3 INTEGER,
                                    rdin4 INTEGER,
                                    rdin5 INTEGER,
                                    rdin6 INTEGER)""")
cr.execute("""CREATE TABLE IF NOT EXISTS pttb(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                    ptjc_no INTEGER NOT NULL,
                                    ptpt_per TEXT,
                                    ptln_no TEXT,
                                    ptpt_dt TEXT,
                                    ptpt_ti TEXT,
                                    ptpt_qty INTEGER,
                                    rdpt1 INTEGER,
                                    rdpt2 INTEGER,
                                    rdpt3 INTEGER,
                                    rdpt4 INTEGER,
                                    rdpt5 INTEGER,
                                    rdpt6 INTEGER)""")
cr.execute("""CREATE TABLE IF NOT EXISTS cbtb(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                    cbjc_no INTEGER NOT NULL,
                                    cbco_per TEXT,
                                    cbln_no TEXT,
                                    cb_dt TEXT,
                                    cb_ti TEXT,
                                    cb_qty INTEGER,
                                    cbco_ty TEXT,
                                    cbbr_st TEXT,
                                    cbbr_op TEXT,
                                    rdcb1 INTEGER,
                                    rdcb2 INTEGER,
                                    rdcb3 INTEGER,
                                    rdcb4 INTEGER,
                                    rdcb5 INTEGER,
                                    rdcb6 INTEGER)""")
cr.execute("""CREATE TABLE IF NOT EXISTS fitb(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                    fijc_no INTEGER NOT NULL,
                                    fi_per TEXT,
                                    fiin_na TEXT,
                                    ficu_no TEXT,
                                    fi_dt TEXT,
                                    fi_ti TEXT,
                                    fi_qty INTEGER,
                                    rdfi1 INTEGER,
                                    rdfi2 INTEGER,
                                    rdfi3 INTEGER,
                                    rdfi4 INTEGER,
                                    rdfi5 INTEGER,
                                    rdfi6 INTEGER)""")
cr.execute("""CREATE TABLE IF NOT EXISTS bintb(
                                    fi_dt TEXT PRIMARY KEY NOT NULL,
                                    fijc_no TEXT,
                                    rd1 INTEGER,
                                    rd2 INTEGER,
                                    rd3 INTEGER,
                                    rd4 INTEGER,
                                    rd5 INTEGER,
                                    rd6 INTEGER)""")

con.commit()
#def logger(jc,fl):
    




def topbar(wx,v):

    wx.state("zoomed")
    wx.iconbitmap('logo.ico')
    wx.geometry(str(width)+"x" + str(height) + "+0+0")
    
    Tops = Frame(wx, width=width, height=100, bd=8)#,relief='raise'
    
    Tops.pack(side=TOP)

    lblRef = Label(Tops,font=('arial',10,'bold'),text='Account ID : '+idd,bd=16,justify='left')
    lblRef.grid(row=0,column=0)

    def iExit():
            qExit = messagebox.askyesno("FIFO system","Do you want to exit the system?")
            if qExit > 0:
                    wx.destroy()
                    return
    def back():
            qExit = messagebox.askyesno("FIFO system","Do you want to go back to the dashboard ?")
            if qExit > 0:
                wx.destroy()
                db()
    def bak():
            qExit = messagebox.askyesno("FIFO system","Do you want to go back to the admin pannel ?")
            if qExit > 0:
                wx.destroy()
                admin()

    def log():
        qExit = messagebox.askyesno("FIFO system","Do you want to move to admin account?")
        if qExit > 0:
                psw(7,wx)
                
    if v==6:
        na='Final Ins DATA FEED'
    elif v==3:
        na='INSPECTION DATA FEED'
    elif v==1:
        na='PT DATA FEED'
    elif v==2:
        na='STORE DATA FEED'
    elif v==5:
        na="Coating and Brushing"
    elif v==4:
        na='STORE Dispatch DATA FEED'
    elif v==7:
        na='ADMIN PANNEL'
    elif v==11:
        na='GRAPH'
    else:
        na=""

        
    lblna = Label(Tops,fg='green',font=('arial',20,'bold'),text=na,bd=16,justify='left')#########
    lblna.grid(row=1,column=3)

    DateofOrder=StringVar()
    DateofOrder.set(time.strftime("%d/%m/%y"))
    lblDateofOrder = Label(Tops,font=('arial',10,'bold'),text='Order Date',bd=10,anchor='w')
    lblDateofOrder.grid(row=0,column=4)
    txtDateofOrder=Entry(Tops,font=('arial',10,'bold'),textvariable=DateofOrder,bd=10,insertwidth=2,justify='left')
    txtDateofOrder.grid(row=0,column=5)

    TimeofOrder=StringVar()
    TimeofOrder.set(time.strftime("%H:%M:%S"))
    lblTimeofOrder = Label(Tops,font=('arial',10,'bold'),text='Order Time',bd=10,anchor='w')
    lblTimeofOrder.grid(row=1,column=4)
    txtTimeofOrder=Entry(Tops,font=('arial',10,'bold'),textvariable=TimeofOrder,bd=10,insertwidth=2,justify='left')
    txtTimeofOrder.grid(row=1,column=5)

    #main-frame
    f1 = Frame(wx, width=width, height=700, bd=18)#INPUT BOX 
    f1.pack(expand=TRUE ,fill=BOTH)

    f1a = Frame(f1, width=width, height=380, bd=8)#,relief='raise'
    f1a.pack(side=TOP,expand=TRUE,fill=BOTH)


    f1aa = Frame(f1a, width=width, height=380, bd=8,relief='raise')#input val
    f1aa.pack(side=LEFT,expand=TRUE)
    if v!=2 and v!=4 and v!=10 and v!=11 :
        f1ab = Frame(f1a, width=width, height=380, bd=8,relief='raise')# input des
        f1ab.pack(side=RIGHT,expand=TRUE)
    if v==11:
        f1ad = Frame(f1a, width=800, height=360, bd=8)# input des
        f1ad.pack(side=RIGHT,expand=TRUE)
    if v==7:
        f1ac = Frame(f1a, width=width, height=380, bd=8,relief='raise')# input des
        f1ac.pack(side=RIGHT,expand=TRUE)
    if v==4 :
        adsumy=Button(Tops,padx=16,pady=8,bd=3,fg='red',font=('arial',16,'bold'),width=8,height=1,text='Admin Pannel',command=log).grid(row=1,column=0)
    f2ab = Frame(f1, width=width, height=320, bd=8)#,relief='raise'
    f2ab.pack(side=BOTTOM,expand=TRUE)
    

    lblInfo=Label(Tops,fg='green', font=('arial',40,'bold'),text ="  SKDD FIFO systems  ", bd=10,anchor='w')
    lblInfo.grid(row=0,column=3)


    btnback=Button(f2ab,padx=16,pady=16,bd=8,fg='blue',font=('arial',16,'bold'),width=15,text='BACK', command=back)
    btnback.grid(row=0,column=0)
    btnback.bind("<Enter>", on_re)
    btnback.bind("<Leave>", on_leave)
    wx.bind("<Key-Escape>",lambda event: back())

    if v==11:
        btnback=Button(f2ab,padx=16,pady=16,bd=8,fg='blue',font=('arial',16,'bold'),width=15,text='BACK', command=bak)
        btnback.grid(row=0,column=0)
        btnback.bind("<Enter>", on_re)
        btnback.bind("<Leave>", on_leave)
        wx.bind("<Key-Escape>",lambda event: bak())
    
    btnExit=Button(f2ab,padx=16,pady=16,bd=8,fg='red',font=('arial',16,'bold'),width=15,text='EXIT',command=iExit)
    btnExit.grid(row=0,column=3)
    btnExit.bind("<Enter>", on_ent)
    btnExit.bind("<Leave>", on_leav)
    

    if v==2 or v==4 or v==10 :
        #return(Tops,lblRef,lblna,lblDateofOrder,txtDateofOrder,lblTimeofOrder,txtTimeofOrder,lblInfo,f1aa,f2ab,btnback,btnExit)
        return(Tops,f1aa,f2ab,btnback,btnExit)
    elif v==7:
        return(Tops,f1aa,f1ab,f1ac,f2ab,btnback,btnExit)
    elif v==11:
        return(Tops,f1aa,f2ab,f1ad)
    return(Tops,f1aa,f1ab,f2ab,btnback,btnExit)

def on_enter(e):
    e.widget['background'] = 'green'
    e.widget['foreground'] = 'black'

def on_re(e):
    e.widget['background'] = 'DarkOrange2'
    
def on_ent(e):
    e.widget['background'] = 'red'
    e.widget['foreground'] = 'snow'

def on_leave(e):
    e.widget['background'] = 'SystemButtonFace'
    

def on_leav(e):
    e.widget['background'] = 'SystemButtonFace'
    e.widget['foreground'] = 'black'






#######################################################################################################################################################################
    
def sto(nam):
    rot.withdraw()
    w4=Toplevel()
    #Tops,lblRef,lblna,lblDateofOrder,txtDateofOrder,lblTimeofOrder,txtTimeofOrder,lblInfo,f1aa,f2ab,btnback,btnExit=topbar(w4,4)
    Tops,f1aa,f2ab,btnback,btnExit=topbar(w4,4)
    w4.title("ceccpl fifo Systems")

    def bine():
        w4.destroy()
        binn()
        
    # ORDER's INFO

    str_per=StringVar()
    rloy_per=StringVar()
    jc_no=StringVar()
    dis_qty=StringVar()
    dis_ti=StringVar()

    str_per.set(nam)
    rloy_per.set("")
    jc_no.set("")
    dis_ti.set(time.strftime("%H:%M:%S"))
    rloy_per.set("TN")

    lblhb8 = Label(f1aa,font=('arial',15,'bold'),text='STORE PERSON NAME',bd=16,justify='left')
    lblhb8.grid(row=0,column=1)
    txt1=Entry(f1aa,font=('arial',15,'bold'),textvariable=str_per,bd=10,insertwidth=2,justify='left')
    txt1.grid(row=1,column=1)
    
    lblhb6 = Label(f1aa,font=('arial',15,'bold'),text='LORRY NO',bd=16,justify='left')
    lblhb6.grid(row=0,column=2)
    
    #drop=OptionMenu(f1aa,rloy_per,"driver-A","driver-B","driver-C")
    #drop.grid(row=1,column=2)
    #drop.config(width = 16,font=('arial',15,'bold'))
    txt2=Entry(f1aa,font=('arial',15,'bold'),textvariable=rloy_per,bd=10,insertwidth=2,justify='left')
    txt2.grid(row=1,column=2)



    lblsb = Label(f1aa,font=('arial',15,'bold'),text='JOB NO',bd=16,justify='left')
    lblsb.grid(row=2,column=1)
    txt3=Entry(f1aa,font=('arial',15,'bold'),textvariable=jc_no,bd=10,insertwidth=2,justify='left')
    txt3.grid(row=3,column=1)
    lblsb = Label(f1aa,font=('arial',15,'bold'),text='DISPATCH QTY',bd=16,justify='left')
    lblsb.grid(row=2,column=2)
    txt4=Entry(f1aa,font=('arial',15,'bold'),textvariable=dis_qty,bd=10,insertwidth=2,justify='left')
    txt4.grid(row=3,column=2)


    lblsb = Label(f1aa,font=('arial',15,'bold'),text='DISPATCH TIME',bd=16,justify='left')
    lblsb.grid(row=4,column=1)
    txt5=Entry(f1aa,font=('arial',15,'bold'),textvariable=dis_ti,bd=10,insertwidth=2,justify='left')
    txt5.grid(row=5,column=1)
    so_dt=DateEntry(f1aa,width=16,font=('arial',15,'bold'),date_pattern='yyyy-MM-dd')
    so_dt.grid(row=4,column=2)#42
    btnExit=Button(f1aa,padx=8,pady=8,bd=5,fg='red',font=('arial',16,'bold'),width=15,text='Bin',command=bine)#,command=iExit
    btnExit.grid(row=5,column=2)
    
    def rec():
        jc_noV = str(jc_no.get())
        cr.execute("SELECT Ffin_qty FROM logdt WHERE jc_no=?",(jc_noV,))
        ch=cr.fetchone()
        if ch is not None:
            dis_qty.set(ch[0])
           #lblsb = Label(f1aa,fg="red",font=('arial',15,'bold'),text=ch[0],bd=26,justify='left')
           #lblsb.grid(row=5,column=2)
            txt4.focus()
        else:
            messagebox.showerror('Response', 'the job card is not present')
            jc_no.set("")
            txt3.focus()
        

    # ORDER's INFO BUTTONS

    def Reset():
            rloy_per.set("")
            jc_no.set("")
            dis_qty.set("")
            dis_ti.set(time.strftime("%H:%M:%S"))
            
    def check():
            flg=0
            str_perV = str(str_per.get())
            rloy_perV = str(rloy_per.get())
            jc_noV = str(jc_no.get())
            dis_qtyV = str(dis_qty.get())
            dis_tiV = str(dis_ti.get())
            so_dtV=str(so_dt.get())


            
            
            
            cr.execute("SELECT jc_no,stg,Ffin_qty FROM logdt WHERE jc_no=?",(jc_noV,))
            ch=cr.fetchone()
            con.commit()
            

            if ((ch is not None) and (ch[0]==int(jc_noV))) and ('f' in ch[1]):
                flg=1
    
            if len(str_perV) == 0:
                    messagebox.showerror("error","store person name is missing...")
            else:
                    if len(rloy_perV) == 0:
                            messagebox.showerror("error","Lorry driver name is missing...")
                    else:
                            if (len(jc_noV) == 0) or (flg==0):
                                            messagebox.showerror("error","job card number is missing...")
                            elif(jc_noV.isnumeric()):
                                    if len(dis_qtyV) == 0 :
                                            messagebox.showerror("error","dispatch qty value is missing...")
                                    elif(dis_qtyV.isnumeric()):
                                            if len(dis_tiV) == 0:
                                                    messagebox.showerror("error","dispatch time is missing...")
                                            else:
                                                    done()
                                                                    
                                    else:
                                            messagebox.showerror("error","received qty is not a number ")
                                                                    
                                            
                            else:
                                    messagebox.showerror("error","job card number is not a number ")


    def done():
        str_perV = str(str_per.get())
        rloy_perV = str(rloy_per.get())
        jc_noV = int(jc_no.get())
        dis_qtyV = int(dis_qty.get())
        so_dtV=str(so_dt.get())
        dis_tiV = str(dis_ti.get())
                    

        
                 
        
        cr.execute("SELECT Ffin_qty FROM logdt WHERE jc_no=?",(jc_noV,))
        ch=cr.fetchone()
        if ((ch is not None) and (abs(ch[0])>= dis_qtyV)):
            if ch[0]==dis_qtyV:
                qEnter = messagebox.askokcancel("war","confirm")
                if qEnter > 0:
                    cr.execute("SELECT * FROM logdt WHERE jc_no=?",(jc_noV,))
                    ch=cr.fetchone()
                    cr.execute("INSERT INTO flogdt VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(
                            ch[0],
                            ch[1],
                            ch[2],
                            ch[3],
                            ch[4],
                            ch[5],
                            ch[6],
                            ch[7],
                            ch[8],
                            ch[9],
                            ch[10],
                            ch[11],
                            ch[12],
                            ch[13],
                            ch[14],
                            ch[15]))
                    cr.execute("INSERT INTO store_out VALUES(?,?,?,?,?,?)",(
                            jc_noV,
                            str_perV,
                            rloy_perV,
                            dis_qtyV,
                            so_dtV,
                            dis_tiV))
                    con.commit()
                    
                    
                    
                    cr.execute("DELETE FROM logdt WHERE jc_no=?",(jc_noV,))
                    con.commit()
                    
                    Reset()
            else:
                messagebox.showerror("error","qty is less then finished qty...")
        else:
            messagebox.showerror("error","qty is more then finished qty...")

        
    ###close connection###
        con.commit()
        
                    
    txt1.focus()
    txt1.bind("<Return>",lambda funct1:txt2.focus())
    txt2.focus()
    txt2.bind("<Return>",lambda funct1:txt3.focus())
    txt3.focus()
    txt3.bind("<Return>",lambda funct1:rec())
    txt4.focus()
    txt4.bind("<Return>",lambda funct1:check())     

    btndone=Button(f2ab,padx=16,pady=16,bd=8,fg='blue',font=('arial',16,'bold'),width=15,text='DONE', command=check)
    btndone.grid(row=0,column=1)
    btndone.bind("<Enter>", on_enter)
    btndone.bind("<Leave>", on_leave)

    btnReset=Button(f2ab,padx=16,pady=16,bd=8,fg='black',font=('arial',16,'bold'),width=15,text='RESET',command=Reset)
    btnReset.grid(row=0,column=2)
    btnReset.bind("<Enter>", on_re)
    btnReset.bind("<Leave>", on_leave)


    w4.mainloop()


#######################################################################################################################################################################

def stn(nam):
    rot.withdraw()
    w2=Toplevel()
    w2.title("ceccpl fifo store inn Systems")
    jcno=pickle.load(open("jc_no","rb"))
    Tops,f1aa,f2ab,btnback,btnExit=topbar(w2,2)

    # ORDER's INFO
    
    
    rec_per=StringVar()
    loy_per=StringVar()
    dc_no=StringVar()
    jc_no=StringVar()
    mod_na=StringVar()
    pt_no=StringVar()
    rec_qty=StringVar()
    rec_ti=StringVar()
    
    rec_ti.set(time.strftime("%H:%M:%S"))
    jc_no.set(jcno+1)
    rec_per.set(nam)
    loy_per.set("TN")
    
    lblhb8 = Label(f1aa,font=('arial',15,'bold'),text='RECEIVED PERSON',bd=16,justify='left')
    lblhb8.grid(row=0,column=1)
    txt1=Entry(f1aa,font=('arial',15,'bold'),textvariable=rec_per,bd=10,insertwidth=2,justify='left')
    txt1.grid(row=1,column=1)
    lblhb6 = Label(f1aa,font=('arial',15,'bold'),text='LORRY NO',bd=16,justify='left')
    lblhb6.grid(row=0,column=2)
    #drop=OptionMenu(f1aa,loy_per,"driver-A","driver-B","driver-C")
    #drop.grid(row=1,column=2)
    #drop.config(width = 16,font=('arial',15,'bold')    )       
    
    txt2=Entry(f1aa,font=('arial',15,'bold'),textvariable=loy_per,bd=10,insertwidth=2,justify='left')
    txt2.grid(row=1,column=2)
    
    lblsb = Label(f1aa,font=('arial',15,'bold'),text='DC NO',bd=16,justify='left')
    lblsb.grid(row=0,column=3)
    txt3=Entry(f1aa,font=('arial',15,'bold'),textvariable=dc_no,bd=10,insertwidth=2,justify='left')
    txt3.grid(row=1,column=3)

    lblsb = Label(f1aa,font=('arial',15,'bold'),text='JOB NO',bd=16,justify='left')
    lblsb.grid(row=2,column=1)
    txt4=Entry(f1aa,font=('arial',15,'bold'),textvariable=jc_no,bd=10,insertwidth=2,justify='left')
    txt4.grid(row=3,column=1)
    lblsb = Label(f1aa,font=('arial',15,'bold'),text='MODEL NAME',bd=16,justify='left')
    lblsb.grid(row=2,column=2)
    txt5=Entry(f1aa,font=('arial',15,'bold'),textvariable=mod_na,bd=10,insertwidth=2,justify='left')
    txt5.grid(row=3,column=2)
    lblsb = Label(f1aa,font=('arial',15,'bold'),text='PART NO',bd=16,justify='left')
    lblsb.grid(row=2,column=3)
    dro=OptionMenu(f1aa,pt_no,"")
    dro.grid(row=3,column=3)
    dro.config(width = 16,font=('arial',15,'bold'))
    #txt6=Entry(f1aa,font=('arial',15,'bold'),textvariable=pt_no,bd=10,insertwidth=2,justify='left')
    #txt6.grid(row=3,column=3)

    lblsb = Label(f1aa,font=('arial',15,'bold'),text='RECEIVED TIME',bd=16,justify='left')
    lblsb.grid(row=4,column=1)
    txt7=Entry(f1aa,font=('arial',15,'bold'),textvariable=rec_ti,bd=10,insertwidth=2,justify='left')
    txt7.grid(row=5,column=1)
    lblsb = Label(f1aa,font=('arial',15,'bold'),text='RECEIVED QTY',bd=16,justify='left')
    lblsb.grid(row=4,column=2)
    txt8=Entry(f1aa,font=('arial',15,'bold'),textvariable=rec_qty,bd=10,insertwidth=2,justify='left')
    txt8.grid(row=5,column=2)
    lblsb = Label(f1aa,font=('arial',15,'bold'),text='JOB TAKEN DATE',bd=16,justify='left')
    lblsb.grid(row=4,column=3)
    si_dt=DateEntry(f1aa,width=16,font=('arial',15,'bold'),date_pattern='yyyy-MM-dd')
    si_dt.grid(row=5,column=3)


    txt1.focus()
    txt1.bind("<Return>",lambda funct1:txt2.focus())
    txt2.focus()
    txt2.bind("<Return>",lambda funct1:txt3.focus())
    txt3.focus()
    txt3.bind("<Return>",lambda funct1:txt4.focus())
    txt4.focus()
    txt4.bind("<Return>",lambda funct1:txt5.focus())
    txt5.focus()
    txt5.bind("<Return>",lambda funct1:aufil())
    
    txt7.focus()
    txt7.bind("<Return>",lambda funct1:txt8.focus())
    txt8.focus()
    txt8.bind("<Return>",lambda funct1:check())

    # ORDER's INFO BUTTONS

    def aufil():
        global mm
        global dro
        mod_naV = str(mod_na.get())
        mod_naV=mod_naV.upper()
        fr.execute("SELECT pt_no FROM disktb WHERE mod_na=?",(mod_naV,))
        fh=fr.fetchone()
        bon.commit()
        if fh is not None and (mod_naV == 'RBI' or mod_naV == 'IB'):
            pt_no.set(fh[0])
            dro=OptionMenu(f1aa,pt_no,'OU000','C8000')
            dro.grid(row=3,column=3)
            dro.config(width = 16,font=('arial',15,'bold'))
            mm=1
            txt7.focus()
        elif fh is not None and (mod_naV == 'SP2I' or mod_naV == 'SU2I'):
            pt_no.set(fh[0])
            dro=OptionMenu(f1aa,pt_no,'A0100','BV400')
            dro.grid(row=3,column=3)
            dro.config(width = 16,font=('arial',15,'bold'))
            mm=1
            txt7.focus()
        elif fh is not None and mod_naV == 'QXI':
            pt_no.set(fh[0])
            dro=OptionMenu(f1aa,pt_no,'J1500','3X000')
            dro.grid(row=3,column=3)
            dro.config(width = 16,font=('arial',15,'bold'))
            mm=1
            txt7.focus()
        elif fh is not None:
            pt_no.set(fh[0])
            dro=OptionMenu(f1aa,pt_no,"")
            dro.grid(row=3,column=3)
            dro.config(width = 16,font=('arial',15,'bold'))
            mm=1
            txt7.focus()#txt6
          
        
    def Reset():
            loy_per.set("")
            dc_no.set("")
            mod_na.set("")
            pt_no.set("")
            rec_qty.set("")
            rec_ti.set(time.strftime("%H:%M:%S"))
            mm=0
            

            
    def check():
        
            flg=0
            jc_noV = str(jc_no.get())
            rec_perV = str(rec_per.get())
            loy_perV = str(loy_per.get())
            dc_noV = str(dc_no.get())
            mod_naV = str(mod_na.get())
            mod_naV=mod_naV.upper()
            pt_noV = str(pt_no.get())
            rec_qtyV = str(rec_qty.get())
            rec_tiV = str(rec_ti.get())

            cr.execute("SELECT sijc_no FROM store_in WHERE sijc_no=?",(jc_noV,))
            ch_list=cr.fetchone()
            con.commit()
            
            

            ##match identification
            if (ch_list is not None) and (ch_list[0]==int(jc_noV)):
                    flg=1
    ###massage box#####
            if len(rec_perV) == 0:
                    messagebox.showerror("error","Received person name is missing...")
            else:
                    if len(loy_perV) == 0:
                            messagebox.showerror("error","Lorry driver name is missing...")
                    else:
                            if len(dc_noV) == 0:
                                    messagebox.showerror("error","dc number is missing...")
                            else:
                                    if (len(jc_noV) == 0 )or (flg==1):
                                            messagebox.showerror("error","job card number is missing...are job card number already exists...")
                                    elif(jc_noV.isnumeric()):
                                            if (len(mod_naV) == 0) or mm==0:
                                                    messagebox.showerror("error","model name is missing...")
                                            else:
                                                    if len(pt_noV) == 0:
                                                            messagebox.showerror("error","part number is missing...")
                                                    else:
                                                            if len(rec_qtyV) == 0:
                                                                    messagebox.showerror("error","received qty value is missing...")
                                                            elif(rec_qtyV.isnumeric()):
                                                                    if len(rec_tiV) == 0:
                                                                            messagebox.showerror("error","received time is missing...")
                                                                    else:
                                                                            done()
                                                                    
                                                            else:
                                                                    messagebox.showerror("error","received qty is not a number ")
                                                                    
                                            
                                    else:
                                            messagebox.showerror("error","job card number is not a number ")


    def done():
            qEnter = messagebox.askokcancel("war","confirm")
            if qEnter > 0:
                    rec_perV = str(rec_per.get())
                    loy_perV = str(loy_per.get())
                    dc_noV = str(dc_no.get())
                    jc_noV = int(jc_no.get())
                    mod_naV = str(mod_na.get())
                    mod_naV=mod_naV.upper()
                    pt_noV = str(pt_no.get())
                    rec_qtyV = int(rec_qty.get())
                    rec_tiV = str(rec_ti.get())
                    si_dtV= str(si_dt.get())
                    ##connection####

                    

    ###store db###
                    
                    

                    #cr.execute('DELETE FROM store_in;',)##del all rows data

                    cr.execute("INSERT INTO store_in VALUES(?,?,?,?,?,?,?,?,?)",(
                            jc_noV,
                            dc_noV,
                            loy_perV,
                            mod_naV,
                            pt_noV,
                            rec_qtyV,
                            rec_perV,
                            si_dtV,
                            rec_tiV))
    ###log db###
                    
                    
                    cr.execute("INSERT INTO logdt VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(
                            jc_noV,
                            'i',
                            rec_qtyV,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None))
                    
                            

    ###close connection###
                    con.commit()
                    pickle.dump(jc_noV,open("jc_no","wb"))                    
                    Reset()
                    jc_no.set(jc_noV+1)
    
    btndone=Button(f2ab,padx=16,pady=16,bd=8,fg='green',font=('arial',16,'bold'),width=15,text='DONE', command=check)
    btndone.grid(row=0,column=1)
    btndone.bind("<Enter>", on_enter)
    btndone.bind("<Leave>", on_leave)


    btnReset=Button(f2ab,padx=16,pady=16,bd=8,fg='black',font=('arial',16,'bold'),width=15,text='RESET',command=Reset)
    btnReset.grid(row=0,column=2)
    btnReset.bind("<Enter>", on_re)
    btnReset.bind("<Leave>", on_leave)

    w2.bind("<Key-Tab>",lambda event: Reset())



    w2.mainloop()


#######################################################################################################################################################################

def inc(nam):
    rot.withdraw()
    w3=Toplevel()
    w3.title("ceccpl fifo insption Systems")

    Tops,f1aa,f1ab,f2ab,btnback,btnExit=topbar(w3,3)

    # ORDER's INFO

    sh_no=StringVar()
    in_per=StringVar()
    jc_no=StringVar()
    sp_qty=StringVar()
    rdin1=StringVar()
    rdin2=StringVar()
    rdin3=StringVar()
    rdin4=StringVar()
    rdin5=StringVar()
    rdin6=StringVar()
    
    in_per.set(nam)
    rdin1.set(0)
    rdin2.set(0)
    rdin3.set(0)
    rdin4.set(0)
    rdin5.set(0)
    rdin6.set(0)
    if int(time.strftime("%H")) >=22 or int(time.strftime("%H")) < 6:
        sh_no.set("3rd")
    elif int(time.strftime("%H")) >=14 and int(time.strftime("%H")) < 22:
        sh_no.set("2nd")
    elif int(time.strftime("%H")) >=6 and int(time.strftime("%H")) < 14:
        sh_no.set("1st")
    
    lblhb8 = Label(f1aa,font=('arial',15,'bold'),text='SHIFT NO',bd=16,justify='left')
    lblhb8.grid(row=0,column=1)
    drop=OptionMenu(f1aa,sh_no,"1st","2nd","3rd")
    drop.grid(row=1,column=1)
    drop.config(width = 16,font=('arial',15,'bold'))
    lblhb6 = Label(f1aa,font=('arial',15,'bold'),text='INSPECTOR NAME',bd=16,justify='left')
    lblhb6.grid(row=0,column=3)
    txt1=Entry(f1aa,font=('arial',15,'bold'),textvariable=in_per,bd=10,insertwidth=2,justify='left')
    txt1.grid(row=1,column=3)

    lblsb = Label(f1aa,font=('arial',15,'bold'),text='JOB CARD NO',bd=16,justify='left')
    lblsb.grid(row=2,column=1)
    txt2=Entry(f1aa,font=('arial',15,'bold'),textvariable=jc_no,bd=10,insertwidth=2,justify='left')
    txt2.grid(row=3,column=1)
    lblsb = Label(f1aa,font=('arial',15,'bold'),text='SAMPLING QTY',bd=16,justify='left')
    lblsb.grid(row=2,column=3)
    txt3=Entry(f1aa,font=('arial',15,'bold'),textvariable=sp_qty,bd=10,insertwidth=2,justify='left')
    txt3.grid(row=3,column=3)






    lblsb = Label(f1ab,font=('arial',15,'bold'),text='REJECTION DETAILS',bd=16,justify='left')
    lblsb.grid(row=0,column=0)

    lblhb8 = Label(f1ab,font=('arial',10,'bold'),text='Part Number Miss Match',bd=16,justify='left')
    lblhb8.grid(row=1,column=0)
    txt4=Entry(f1ab,width=5,font=('arial',10,'bold'),textvariable=rdin1,bd=10,insertwidth=2,justify='left')
    txt4.grid(row=1,column=1)
    lblhb6 = Label(f1ab,font=('arial',10,'bold'),text='Rust',bd=16,justify='left')
    lblhb6.grid(row=2,column=0)
    txt5=Entry(f1ab,width=5,font=('arial',10,'bold'),textvariable=rdin2,bd=10,insertwidth=2,justify='left')
    txt5.grid(row=2,column=1)
    lblsb = Label(f1ab,font=('arial',10,'bold'),text='Damaged',bd=16,justify='left')
    lblsb.grid(row=3,column=0)
    txt6=Entry(f1ab,width=5,font=('arial',10,'bold'),textvariable=rdin3,bd=10,insertwidth=2,justify='left')
    txt6.grid(row=3,column=1)
    lblsb = Label(f1ab,font=('arial',10,'bold'),text='Paint Mark',bd=16,justify='left')
    lblsb.grid(row=4,column=0)
    txt7=Entry(f1ab,width=5,font=('arial',10,'bold'),textvariable=rdin4,bd=10,insertwidth=2,justify='left')
    txt7.grid(row=4,column=1)
    lblsb = Label(f1ab,font=('arial',10,'bold'),text='Blow Hole',bd=16,justify='left')
    lblsb.grid(row=5,column=0)
    txt8=Entry(f1ab,width=5,font=('arial',10,'bold'),textvariable=rdin5,bd=10,insertwidth=2,justify='left')
    txt8.grid(row=5,column=1)
    lblsb = Label(f1ab,font=('arial',10,'bold'),text='Machining Problem',bd=16,justify='left')
    lblsb.grid(row=6,column=0)
    txt9=Entry(f1ab,width=5,font=('arial',10,'bold'),textvariable=rdin6,bd=10,insertwidth=2,justify='left')
    txt9.grid(row=6,column=1)

    txt1.focus()
    txt1.bind("<Return>",lambda funct1:txt2.focus())
    txt2.focus()
    txt2.bind("<Return>",lambda funct1:rec())
    txt3.focus()
    txt3.bind("<Return>",lambda funct1:txt4.focus())
    txt4.focus()
    txt4.bind("<Return>",lambda funct1:txt5.focus())
    txt5.focus()
    txt5.bind("<Return>",lambda funct1:txt6.focus())
    txt6.focus()
    txt6.bind("<Return>",lambda funct1:txt7.focus())
    txt7.focus()
    txt7.bind("<Return>",lambda funct1:txt8.focus())
    txt8.focus()
    txt8.bind("<Return>",lambda funct1:txt9.focus())
    txt9.focus()
    txt9.bind("<Return>",lambda funct1:check())

    # ORDER's INFO BUTTONS
    def rec():
            jc_noV= str(jc_no.get())
            cr.execute("SELECT tot_qty,stg FROM logdt WHERE jc_no=?",(jc_noV,))
            ch=cr.fetchone()
            con.commit()
            if ch is not None and 'n' not in ch[1]:
                SP=round(ch[0]/100)
                lblsb = Label(f1aa,fg="red",font=('arial',15,'bold'),text="qty : "+ str(ch[0]),bd=26,justify='left')
                lblsb.grid(row=4,column=2)
                if SP<1:
                    SP=1
                    
                lblsb = Label(f1aa,font=('arial',15,'bold'),text="sampling qty must be : "+str(SP),bd=36,justify='left')
                lblsb.grid(row=4,column=3)
                txt3.focus()
            else:
                 messagebox.showerror("error","job card number is finished are missing.. are job card number is missing log record...")
                 jc_no.set("")
                 txt2.focus()
                 

    def Reset():

            sh_no.set("")
            jc_no.set("")
            sp_qty.set("")
            rdin1.set(0)
            rdin2.set(0)
            rdin3.set(0)
            rdin4.set(0)
            rdin5.set(0)
            rdin6.set(0)
            

    def check():
            flg=0
            sh_noV= str(sh_no.get())
            in_perV= str(in_per.get())
            jc_noV= str(jc_no.get())
            sp_qtyV= str(sp_qty.get())
            rdin1V= str(rdin1.get())
            rdin2V= str(rdin2.get())
            rdin3V= str(rdin3.get())
            rdin4V= str(rdin4.get())
            rdin5V= str(rdin5.get())
            rdin6V= str(rdin6.get())


            
            cr.execute("SELECT tot_qty,stg FROM logdt WHERE jc_no=?",(jc_noV,))
            ch=cr.fetchone()
            con.commit()
            

            
            if (ch is not None):
                ##match identification
                #and (ch[0]==int(jc_noV))
                flg=1
                SP=round(ch[0]/100)
                if SP<1:
                    SP=1

            if len(sh_noV) == 0:
                    messagebox.showerror("error","Shift number is missing...")
            else:
                    if len(in_perV) == 0:
                            messagebox.showerror("error","inceptor name is missing...")
                    else:
                            if (len(jc_noV) == 0) or (flg==0):
                                     messagebox.showerror("error","job card number is missing.. are job card number is missing log record...")
                            elif(jc_noV.isnumeric()):
                                    if( len(sp_qtyV) == 0 ):
                                            messagebox.showerror("error","sampling qty is missing...")
                                    elif(sp_qtyV.isnumeric() and int(sp_qtyV)>=SP):
                                            if len(rdin1V) == 0:
                                                    messagebox.showerror("error","rejected details is missing...")
                                            elif(rdin1V.isnumeric()):
                                                    if len(rdin2V) == 0:
                                                            messagebox.showerror("error","rejected details is missing...")
                                                    elif(rdin2V.isnumeric()):
                                                            if len(rdin3V) == 0:
                                                                    messagebox.showerror("error","rejected details is missing...")
                                                            elif(rdin3V.isnumeric()):
                                                                    if len(rdin4V) == 0:
                                                                            messagebox.showerror("error","rejected details is missing...")
                                                                    elif(rdin4V.isnumeric()):
                                                                            if len(rdin5V) == 0:
                                                                                    messagebox.showerror("error","rejected details is missing...")
                                                                            elif(rdin5V.isnumeric()):
                                                                                    if len(rdin1V) == 0:
                                                                                            messagebox.showerror("error","rejected details is missing...")
                                                                                    elif(rdin6V.isnumeric()):
                                                                                            done()
                                                                                                                    
                                                                                    else:
                                                                                            messagebox.showerror("error","rejected qty is not a number ")
                                                                            else:
                                                                                    messagebox.showerror("error","rejected qty is not a number ")
                                                                    else:
                                                                            messagebox.showerror("error","rejected qty is not a number ")
                                                            else:
                                                                    messagebox.showerror("error","rejected qty is not a number ")
                                                    else:
                                                            messagebox.showerror("error","rejected qty is not a number ")
                                            else:
                                                    messagebox.showerror("error","rejected qty is not a number ")
                                    else:
                                            messagebox.showerror("error","insufent sampling qty ")
                                                                           
                            else:
                                    messagebox.showerror("error","job card number is not a number ")


    def done():
            sh_noV= str(sh_no.get())
            in_perV= str(in_per.get())
            jc_noV= int(jc_no.get())
            sp_qtyV= int(sp_qty.get())
            rdin1V= int(rdin1.get())
            rdin2V= int(rdin2.get())
            rdin3V= int(rdin3.get())
            rdin4V= int(rdin4.get())
            rdin5V= int(rdin5.get())
            rdin6V= int(rdin6.get())
            ##connection####

            
            cr.execute("SELECT jc_no,stg,tot_qty FROM logdt WHERE jc_no=?",(jc_noV,))
            ch=cr.fetchone()
            df=(rdin1V+rdin2V+rdin3V+rdin4V+rdin5V+rdin6V)
            fi=(ch[2]-df)

            
            
            if ((ch is not None) and (ch[2]>=df) and ((fi+df)- ch[2])==0):        
                    qEnter = messagebox.askokcancel("war","confirm")
                    if qEnter > 0:
                            


            ###store db###
                            

                            #cr.execute('DELETE FROM store_in;',)##del all rows data

                            cr.execute("INSERT INTO insp VALUES(?,?,?,?,?,?,?,?,?,?)",(
                                    jc_noV,
                                    in_perV,
                                    sh_noV,
                                    sp_qtyV,
                                    rdin1V,
                                    rdin2V,
                                    rdin3V,
                                    rdin4V,
                                    rdin5V,
                                    rdin6V))
            ####takeing jc no###

                            jc=ch[0]
                            st=str(ch[1])+'n'
                            #ms=((fi+df)- ch_list[4])
                            ms=fi
                            
            ###log db###
                            
                            cr.execute("UPDATE logdt SET stg =?,Ifin_qty=?,Idef_qty=?,def_qty=?,miss_qty=? WHERE jc_no=?",(st,fi,df,df,abs(ms),jc))
                            #cr.execute("UPDATE logdt SET stg =?,Ifin_qty=?,Idef_qty=?,miss_qty=? WHERE jc_no=?",(st,fii,dff,abs(ms),jc))
                            Reset()
            else:
                     messagebox.showerror("error","defect qty is more then recived qty...")
    ###close connection###
            con.commit()
            
   
    btndone=Button(f2ab,padx=16,pady=16,bd=8,fg='green',font=('arial',16,'bold'),width=15,text='DONE', command=check)
    btndone.grid(row=0,column=1)
    btndone.bind("<Enter>", on_enter)
    btndone.bind("<Leave>", on_leave)


    btnReset=Button(f2ab,padx=16,pady=16,bd=8,fg='black',font=('arial',16,'bold'),width=15,text='RESET',command=Reset)
    btnReset.grid(row=0,column=2)
    btnReset.bind("<Enter>", on_re)
    btnReset.bind("<Leave>", on_leave)
    w3.bind("<Key-Tab>",lambda event: Reset())
    
    
    w3.mainloop()




#######################################################################################################################################################################
def pt(nam):
    rot.withdraw()
    w1 = Toplevel()
    
    w1.title("ceccpl fifo pt Systems")
    
    Tops,f1aa,f1ab,f2ab,btnback,btnExit=topbar(w1,1)

    # ORDER's INFO

    pt_per=StringVar()
    ln_no=StringVar()
    jc_no=StringVar()
    pt_dt=StringVar()
    pt_ti=StringVar()
    pt_qty=StringVar()
    rdpt1=StringVar()
    rdpt2=StringVar()
    rdpt3=StringVar()
    rdpt4=StringVar()
    rdpt5=StringVar()
    rdpt6=StringVar()
    md_na=StringVar()
    pt_ti.set(time.strftime("%H:%M:%S"))
    pt_per.set(nam)
    rdpt1.set(0)
    rdpt2.set(0)
    rdpt3.set(0)
    rdpt4.set(0)
    rdpt5.set(0)
    rdpt6.set(0)

    lblhb8 = Label(f1aa,font=('arial',15,'bold'),text='PERSON NAME',bd=16,justify='left')
    lblhb8.grid(row=0,column=1)
    txt1=Entry(f1aa,font=('arial',15,'bold'),textvariable=pt_per,bd=10,insertwidth=2,justify='left')
    txt1.grid(row=1,column=1)

    lblhb6 = Label(f1aa,font=('arial',15,'bold'),text='LINE NO',bd=16,justify='left')
    lblhb6.grid(row=0,column=2)
    drop=OptionMenu(f1aa,ln_no,"Old PT","New PT")
    drop.grid(row=1,column=2)
    drop.config(width = 16,font=('arial',15,'bold'))
    lblsb = Label(f1aa,font=('arial',15,'bold'),text='JOB CARD NO ',bd=16,justify='left')
    lblsb.grid(row=0,column=3)
    txt2=Entry(f1aa,font=('arial',15,'bold'),textvariable=jc_no,bd=10,insertwidth=2,justify='left')
    txt2.grid(row=1,column=3)
    txt2.bind("<Return>",lambda funct1:sc(3))
    
    lblsb = Label(f1aa,font=('arial',15,'bold'),text='JOB TAKEN TIME',bd=16,justify='left')
    lblsb.grid(row=2,column=1)
    txt3=Entry(f1aa,font=('arial',15,'bold'),textvariable=pt_ti,bd=10,insertwidth=2,justify='left')
    txt3.grid(row=3,column=1)
    lblsb = Label(f1aa,font=('arial',15,'bold'),text='JOB TAKEN QTY',bd=16,justify='left')
    lblsb.grid(row=2,column=2)
    txt4=Entry(f1aa,font=('arial',15,'bold'),textvariable=pt_qty,bd=10,insertwidth=2,justify='left')
    txt4.grid(row=3,column=2)
    lblsb = Label(f1aa,font=('arial',15,'bold'),text='JOB TAKEN DATE',bd=16,justify='left')
    lblsb.grid(row=2,column=3)

    pt_dt=DateEntry(f1aa,width=16,font=('arial',15,'bold'),date_pattern='yyyy-MM-dd')
    pt_dt.grid(row=3,column=3)


    lblsb = Label(f1ab,font=('arial',15,'bold'),text='REJECTION DETAILS',bd=16,justify='left')
    lblsb.grid(row=0,column=0)


    lblhb8 = Label(f1ab,font=('arial',10,'bold'),text='Part Number Miss Match',bd=16,justify='left')
    lblhb8.grid(row=1,column=0)
    txt5=Entry(f1ab,width=5,font=('arial',10,'bold'),textvariable=rdpt1,bd=10,insertwidth=2,justify='left')
    #bind('<Return>', go(7))
    txt5.grid(row=1,column=1)
    
    lblhb6 = Label(f1ab,font=('arial',10,'bold'),text='Rust',bd=16,justify='left')
    lblhb6.grid(row=2,column=0)

    txt6=Entry(f1ab,width=5,font=('arial',10,'bold'),textvariable=rdpt2,bd=10,insertwidth=2,justify='left')
    #txt7_focus()
    txt6.grid(row=2,column=1)
    
    lblsb = Label(f1ab,font=('arial',10,'bold'),text='Damaged',bd=16,justify='left')
    lblsb.grid(row=3,column=0)
    txt7=Entry(f1ab,width=5,font=('arial',10,'bold'),textvariable=rdpt3,bd=10,insertwidth=2,justify='left')
    txt7.grid(row=3,column=1)
    
    lblsb = Label(f1ab,font=('arial',10,'bold'),text='Paint Mark',bd=16,justify='left')
    lblsb.grid(row=4,column=0)
    txt8=Entry(f1ab,width=5,font=('arial',10,'bold'),textvariable=rdpt4,bd=10,insertwidth=2,justify='left')
    txt8.grid(row=4,column=1)
    
    lblsb = Label(f1ab,font=('arial',10,'bold'),text='Blow Hole',bd=16,justify='left')
    lblsb.grid(row=5,column=0)
    txt9=Entry(f1ab,width=5,font=('arial',10,'bold'),textvariable=rdpt5,bd=10,insertwidth=2,justify='left')
    txt9.grid(row=5,column=1)
    
    lblsb = Label(f1ab,font=('arial',10,'bold'),text='Machining Problem',bd=16,justify='left')
    lblsb.grid(row=6,column=0)
    txt10=Entry(f1ab,width=5,font=('arial',10,'bold'),textvariable=rdpt6,bd=10,insertwidth=2,justify='left')
    txt10.grid(row=6,column=1)

    tx=Entry(Tops,font=('arial',10,'bold'),textvariable=md_na,bd=10,width=30,insertwidth=2,justify='left')
    tx.grid(row=1,column=0)
    tx.focus()
    tx.bind("<Return>",lambda funct1:sc(7))
    
    def rec():
        jc_noV = str(jc_no.get())
        cr.execute("SELECT Ifin_qty,Pmis_qty FROM logdt WHERE jc_no=?",(jc_noV,))
        ch=cr.fetchone()
        if ch is not None:
            if ch[1] is not None:
                lblsb = Label(f1aa,fg='orange',font=('arial',25,'bold'),text= ch[1] ,bd=26,justify='left')
                lblsb.grid(row=4,column=2)
            else:
                lblsb = Label(f1aa,fg='orange',font=('arial',25,'bold'),text= ch[0] ,bd=26,justify='left')
                lblsb.grid(row=4,column=2)
        txt3.focus()
    

    # ORDER's INFO BUTTONS
    def sc(qw):
        global ptjc
        fff=0
        if qw==3:
            jc_noV = str(jc_no.get())
            cr.execute("SELECT simod_na FROM store_in WHERE sijc_no=?",(jc_noV,))
            chh=cr.fetchone()
            if chh is not None:
                ma_naV=chh[0]
                fff=1
            
        else:
            ma_naV=str(md_na.get())
            ma_naV=ma_naV.upper()
            fff=1
        if fff==1:
            cr.execute("SELECT sijc_no FROM store_in WHERE simod_na=?",(ma_naV,))
            ch=cr.fetchall()
            lift=0
            qt=0
            if ch != []:
                ch=list(ch)
                fgg=0
                for i in range(len(ch)):
                    che=list(ch[i])
                    cr.execute("SELECT Ifin_qty,Pmis_qty,stg FROM logdt WHERE jc_no=?",(che[0],))
                    chh=cr.fetchone()
                    if chh is not None and 'c' not in chh[2] and chh[1] != 0:
                        #print(chh[0],chh[1])
                        if chh[1] is not None and chh[1] != 0:
                            lift=lift+chh[1]
                            if fgg==0:
                                ptjc=che[0]
                                qt=lift
                                if qt !=0:
                                    fgg=1
                        elif chh[0] is not None and chh[0] != 0:
                            lift=lift+chh[0]
                            if fgg==0:
                                ptjc=che[0]
                                qt=lift
                                if qt !=0:
                                    fgg=1
                    #print(qt)
                    #elif qw==7:
                        #messagebox.showerror('Response', 'no job at now present')
                if qt !=0 and qw==7:
                    messagebox.showinfo('Response', " at job card no "+str(ptjc)+" has "+str(qt)+" qty and rest of "+str(lift-qt)+" qty more")
                elif qw==7:
                    messagebox.showerror('Response', 'no job at now present')
            elif qw==7 and ma_naV is  None:
                messagebox.showerror('Response', 'the model is not present')
            rec()
        else:
            messagebox.showerror('Response', 'the job card is not present')
            jc_no.set("")
            txt2.focus()
        



            
    def Reset():
            
            jc_no.set("")
            pt_ti.set(time.strftime("%H:%M:%S"))
            pt_qty.set("")
            ln_no.set("")
            rdpt1.set(0)
            rdpt2.set(0)
            rdpt3.set(0)
            rdpt4.set(0)
            rdpt5.set(0)
            rdpt6.set(0)


    def check():
            sc(3)
            txt1.focus()
            flg=0
            pt_perV = str(pt_per.get())
            ln_noV = str(ln_no.get())
            jc_noV = str(jc_no.get())
            pt_dtV = str(pt_dt.get())
            pt_tiV = str(pt_ti.get())
            pt_qtyV = str(pt_qty.get())
            rdpt1V = str(rdpt1.get())
            rdpt2V = str(rdpt2.get())
            rdpt3V = str(rdpt3.get())
            rdpt4V = str(rdpt4.get())
            rdpt5V = str(rdpt5.get())
            rdpt6V = str(rdpt6.get())


           
            cr.execute("SELECT jc_no,stg,Pmis_qty FROM logdt WHERE jc_no=?",(jc_noV,))
            ch=cr.fetchone()
            con.commit()
            

            ##match identification
            if (ch is not None) and (ch[0]==int(jc_noV)) and ('n' in ch[1]):
                    flg=1
                    #out=ch[5]
            
            if len(pt_perV) == 0:
                
                    messagebox.showerror("error","PT oprator name is missing...")#dd=
                    #w1.bind('1',lambda event: txt1.focus_set())

            else:
                    if len(ln_noV) == 0:
                            
                            messagebox.showerror("error","pt name is missing...")
                    else:
                            if (len(jc_noV) == 0) or (flg==0) :
                                    
                                    messagebox.showerror("error","job card number is missing...are job card number is missing log record... are crossed inseption")#dd = 
                                    #if dd>0:
                                        #w1.bind(lambda event: txt2.focus_set())
                            elif str(ptjc)!= jc_noV :
                                    messagebox.showerror("error","There is old job for this model, check job card no of : '"+str(ptjc)+"'  waiting in inseption")
                                     
                            elif(jc_noV.isnumeric()):
                                     
                                     if len(pt_dtV) == 0:
                                            messagebox.showerror("error","date is missing...")
                                     else:
                                            if len(pt_tiV) == 0:
                                                    txt3.focus()
                                                    messagebox.showerror("error","time is missing...")
                                                    
                                            else:
                                                    if len(pt_qtyV) == 0:
                                                            txt4.focus()
                                                            messagebox.showerror("error","out qty value is missing...")
                                                            
                                                    elif(pt_qtyV.isnumeric()):
                                                            if len(rdpt1V) == 0:
                                                                    txt5.focus()
                                                                    messagebox.showerror("error","rejected details is missing...")
                                                                    
                                                            elif(rdpt1V.isnumeric()):
                                                                    if len(rdpt2V) == 0:
                                                                            messagebox.showerror("error","rejected details is missing...")
                                                                            txt6.focus()
                                                                    elif(rdpt2V.isnumeric()):
                                                                            if len(rdpt3V) == 0:
                                                                                    messagebox.showerror("error","rejected details is missing...")
                                                                                    txt7.focus()
                                                                            elif(rdpt3V.isnumeric()):
                                                                                    if len(rdpt4V) == 0:
                                                                                            messagebox.showerror("error","rejected details is missing...")
                                                                                            txt8.focus()
                                                                                    elif(rdpt4V.isnumeric()):
                                                                                            if len(rdpt5V) == 0:
                                                                                                    messagebox.showerror("error","rejected details is missing...")
                                                                                                    txt9.focus()
                                                                                            elif(rdpt5V.isnumeric()):
                                                                                                    if len(rdpt1V) == 0:
                                                                                                            messagebox.showerror("error","rejected details is missing...")
                                                                                                            txt10.focus()
                                                                                                    elif(rdpt6V.isnumeric()):
                                                                                                            done()
                                                                                                                    
                                                                                                    else:
                                                                                                            messagebox.showerror("error","rejected qty is not a number ")
                                                                                            else:
                                                                                                    messagebox.showerror("error","rejected qty is not a number ")
                                                                                    else:
                                                                                            messagebox.showerror("error","rejected qty is not a number ")
                                                                            else:
                                                                                     messagebox.showerror("error","rejected qty is not a number ")
                                                                    else:
                                                                            messagebox.showerror("error","rejected qty is not a number ")
                                                            else:
                                                                    messagebox.showerror("error","rejected qty is not a number ")
                                                                    
                                                    else:
                                                            messagebox.showerror("error","out qty is not a number ")
                                                                    
                                            
                            else:
                                    messagebox.showerror("error","job card number is not a number ")


    def done():
            mflg=0
            pt_perV = str(pt_per.get())
            ln_noV = str(ln_no.get())
            jc_noV = int(jc_no.get())
            pt_dtV = str(pt_dt.get())
            pt_tiV = str(pt_ti.get())
            pt_qtyV = int(pt_qty.get())
            rdpt1V = int(rdpt1.get())
            rdpt2V = int(rdpt2.get())
            rdpt3V = int(rdpt3.get())
            rdpt4V = int(rdpt4.get())
            rdpt5V = int(rdpt5.get())
            rdpt6V = int(rdpt6.get())

            ##connection####

            
            cr.execute("SELECT jc_no,stg,tot_qty,Pfin_qty,Pdef_qty,def_qty,Pmis_qty,Ifin_qty FROM logdt WHERE jc_no=?",(jc_noV,))
            ch=cr.fetchone()   
            df=(rdpt1V+rdpt2V+rdpt3V+rdpt4V+rdpt5V+rdpt6V)
            fi=(pt_qtyV-df)#CH[2]
            dff=(df+ch[5])
            #print(ch,pt_qtyV,df,ch[6])
            if ch[6] is None:
                if ch[7]>=pt_qtyV:
                    mflg=1
            elif ch[6]>=pt_qtyV:
                mflg=1
            if (((ch is not None) and (pt_qtyV >= df)) and (mflg==1)):        
                    qEnter = messagebox.askokcancel("war","confirm")
                    if qEnter > 0:
                            #cr.execute('DROP TABLE pttb')
            ###store db###
                            
                            #cr.execute('DELETE FROM store_in;',)##del all rows data

                            cr.execute("INSERT INTO pttb(ptjc_no ,ptpt_per ,ptln_no ,ptpt_dt ,ptpt_ti ,ptpt_qty ,rdpt1 ,rdpt2 ,rdpt3 ,rdpt4 ,rdpt5 ,rdpt6 ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",(
                                    jc_noV,
                                    pt_perV,
                                    ln_noV,
                                    pt_dtV,
                                    pt_tiV,
                                    pt_qtyV,
                                    rdpt1V,
                                    rdpt2V,
                                    rdpt3V,
                                    rdpt4V,
                                    rdpt5V,
                                    rdpt6V))
            ####takeing jc no###

                            #cr.execute("SELECT * FROM logdt WHERE jc_no=?",(jc_noV,))
                            #ch_list=cr.fetchone()
                            jc=ch[0]
                            st=str(ch[1])+'p'
                            
                            #df=(df+ch_list[3])
                            if ch[3] is not None:
                                fi=fi+ch[3]
                            if ch[4] is not None:
                                df=ch[4]+df
                            pms=((fi+df)-ch[7])  
                            ms=((fi+dff)- ch[2])
                            
            ###log db###
                            
                            cr.execute("UPDATE logdt SET stg =?,Pfin_qty=?,Pdef_qty=?,Pmis_qty=?,def_qty=?,miss_qty=? WHERE jc_no=?",(st,fi,df,abs(pms),dff,abs(ms),jc))
                            Reset()
            else:
                     messagebox.showerror("error","given qty is more then recived qty...")
    ###close connection###
            con.commit()
            

    txt1.focus()
    txt1.bind("<Return>",lambda funct1:txt2.focus())
    txt2.focus()
    txt2.bind("<Return>",lambda funct1:sc(3))
    txt3.focus()
    txt3.bind("<Return>",lambda funct1:txt4.focus())
    txt4.focus()
    txt4.bind("<Return>",lambda funct1:txt5.focus())
    txt5.focus()
    txt5.bind("<Return>",lambda funct1:txt6.focus())
    txt6.focus()
    txt6.bind("<Return>",lambda funct1:txt7.focus())
    txt7.focus()
    txt7.bind("<Return>",lambda funct1:txt8.focus())
    txt8.focus()
    txt8.bind("<Return>",lambda funct1:txt9.focus())
    txt9.focus()
    txt9.bind("<Return>",lambda funct1:txt10.focus())
    txt10.focus()
    txt10.bind("<Return>",lambda funct1:check())
    
    btndone=Button(f2ab,padx=16,pady=16,bd=8,fg='green',font=('arial',16,'bold'),width=15,text='DONE', command=check)
    btndone.grid(row=0,column=1)
    btndone.bind("<Enter>", on_enter)
    btndone.bind("<Leave>", on_leave)

    srch =Button(Tops,padx=5,pady=5,bd=4,fg='black',font=('arial',8,'bold'),width=7,height=1,text="search",command=sc(7))#,command=sc
    srch.grid(row=1,column=1)
    
    btnReset=Button(f2ab,padx=16,pady=16,bd=8,fg='black',font=('arial',16,'bold'),width=15,text='RESET',command=Reset)
    btnReset.grid(row=0,column=2)
    btnReset.bind("<Enter>", on_re)
    btnReset.bind("<Leave>", on_leave)            
    w1.bind("<Key-Tab>",lambda event: Reset())


    w1.mainloop()





#######################################################################################################################################################################
    
def cb(nam):
    rot.withdraw()
    w5=Toplevel()
    w5.title("ceccpl fifo cb Systems")

    Tops,f1aa,f1ab,f2ab,btnback,btnExit=topbar(w5,5)

    # ORDER's INFO
    ft=Frame(f1aa,width=16,bd=8)
    ft.grid(row=3,column=1)

    co_per=StringVar()
    ln_no=StringVar()
    jc_no=StringVar()
    cb_qty=StringVar()
    cb_dt=StringVar()
    cb_ti=StringVar()
    co_ty=StringVar()
    br_op=StringVar()
    rdcb1=StringVar()
    rdcb2=StringVar()
    rdcb3=StringVar()
    rdcb4=StringVar()
    rdcb5=StringVar()
    rdcb6=StringVar()
    bs=IntVar()
    md_na=StringVar()
    cb_ti.set(time.strftime("%H:%M:%S"))
    rdcb1.set(0)
    rdcb2.set(0)
    rdcb3.set(0)
    rdcb4.set(0)
    rdcb5.set(0)
    rdcb6.set(0)

    co_per.set(nam)

    lblhb8 = Label(f1aa,font=('arial',15,'bold'),text='PERSON NAME',bd=16,justify='left')
    lblhb8.grid(row=0,column=1)
    txt1=Entry(f1aa,font=('arial',15,'bold'),textvariable=co_per,bd=10,insertwidth=2,justify='left')
    txt1.grid(row=1,column=1)
    lblhb6 = Label(f1aa,font=('arial',15,'bold'),text='LINE NO',bd=16,justify='left')
    lblhb6.grid(row=0,column=2)
    drop=OptionMenu(f1aa,ln_no,"M4","M5","M20","M30")
    drop.grid(row=1,column=2)
    drop.config(width = 16,font=('arial',15,'bold'))
    lblsb = Label(f1aa,font=('arial',15,'bold'),text='JOB CARD NO ',bd=16,justify='left')
    lblsb.grid(row=0,column=3)
    txt2=Entry(f1aa,font=('arial',15,'bold'),textvariable=jc_no,bd=10,insertwidth=2,justify='left')
    txt2.grid(row=1,column=3)

    lblsb = Label(f1aa,font=('arial',15,'bold'),text='JOB TAKEN TIME',bd=16,justify='left')
    lblsb.grid(row=2,column=1)
    
    txt3=Entry(ft,font=('arial',15,'bold'),textvariable=cb_ti,bd=10,insertwidth=2,justify='left')
    txt3.grid(row=3,column=1)
    lblsb = Label(f1aa,font=('arial',15,'bold'),text='JOB TAKEN QTY',bd=16,justify='left')
    lblsb.grid(row=2,column=2)
    txt4=Entry(f1aa,font=('arial',15,'bold'),textvariable=cb_qty,bd=10,insertwidth=2,justify='left')
    txt4.grid(row=3,column=2)
    lblsb = Label(f1aa,font=('arial',15,'bold'),text='JOB TAKEN DATE',bd=16,justify='left')
    lblsb.grid(row=2,column=3)
    cb_dt=DateEntry(f1aa,width=16,font=('arial',15,'bold'),date_pattern='yyyy-MM-dd')
    cb_dt.grid(row=3,column=3)    

    lblhb8 = Label(f1aa,font=('arial',15,'bold'),text='COATING TYPE',bd=16,justify='left')
    lblhb8.grid(row=4,column=1)
    drop=OptionMenu(f1aa,co_ty,"BDC-A","BDC-B","BDC-D")
    drop.grid(row=5,column=1)
    drop.config(width = 16,font=('arial',15,'bold'))    

    Radiobutton(f1aa,font=('arial',15,'bold'),text="Brushing Required",variable=bs,value=1).grid(row=4,column=2)
    Radiobutton(f1aa,font=('arial',15,'bold'),text="Not Required",variable=bs,value=0).grid(row=5,column=2)

   ##############################
    lblsb = Label(f1aa,font=('arial',15,'bold'),text='Brushing Operator',bd=16,justify='left')
    lblsb.grid(row=4,column=3)
    txt5=Entry(f1aa,font=('arial',15,'bold'),textvariable=br_op,bd=10,insertwidth=2,justify='left')
    txt5.grid(row=5,column=3)
    #lblsb = Label(f1aa,font=('arial',15,'bold'),text='OUT QTY',bd=16,justify='left')
    #lblsb.grid(row=1,column=4)
    

    lblsb = Label(f1ab,font=('arial',15,'bold'),text='REJECTION DETAILS',bd=16,justify='left')
    lblsb.grid(row=0,column=0)


    lblhb8 = Label(f1ab,font=('arial',10,'bold'),text='Part Number Miss Match',bd=16,justify='left')
    lblhb8.grid(row=1,column=0)
    txt6=Entry(f1ab,width=5,font=('arial',10,'bold'),textvariable=rdcb1,bd=10,insertwidth=2,justify='left')
    txt6.grid(row=1,column=1)
    lblhb6 = Label(f1ab,font=('arial',10,'bold'),text='Rust',bd=16,justify='left')
    lblhb6.grid(row=2,column=0)
    txt7=Entry(f1ab,width=5,font=('arial',10,'bold'),textvariable=rdcb2,bd=10,insertwidth=2,justify='left')
    txt7.grid(row=2,column=1)
    lblsb = Label(f1ab,font=('arial',10,'bold'),text='Damaged',bd=16,justify='left')
    lblsb.grid(row=3,column=0)
    txt8=Entry(f1ab,width=5,font=('arial',10,'bold'),textvariable=rdcb3,bd=10,insertwidth=2,justify='left')
    txt8.grid(row=3,column=1)
    lblsb = Label(f1ab,font=('arial',10,'bold'),text='Paint Mark',bd=16,justify='left')
    lblsb.grid(row=4,column=0)
    txt9=Entry(f1ab,width=5,font=('arial',10,'bold'),textvariable=rdcb4,bd=10,insertwidth=2,justify='left')
    txt9.grid(row=4,column=1)
    lblsb = Label(f1ab,font=('arial',10,'bold'),text='Blow Hole',bd=16,justify='left')
    lblsb.grid(row=5,column=0)
    txt10=Entry(f1ab,width=5,font=('arial',10,'bold'),textvariable=rdcb5,bd=10,insertwidth=2,justify='left')
    txt10.grid(row=5,column=1)
    lblsb = Label(f1ab,font=('arial',10,'bold'),text='Machining Problem',bd=16,justify='left')
    lblsb.grid(row=6,column=0)
    txt11=Entry(f1ab,width=5,font=('arial',10,'bold'),textvariable=rdcb6,bd=10,insertwidth=2,justify='left')
    txt11.grid(row=6,column=1)


    tx=Entry(Tops,font=('arial',10,'bold'),textvariable=md_na,bd=10,width=30,insertwidth=2,justify='left')
    tx.grid(row=1,column=0)
    tx.focus()
    tx.bind("<Return>",lambda funct1:sc(7))
    mm=0
    def aufil():
        global mc
        jc_noV = str(jc_no.get())
        cr.execute("SELECT simod_na,sipt_no FROM store_in WHERE sijc_no=?",(jc_noV,))
        ch=cr.fetchone()
        con.commit()
        if ch is not None:
            fr.execute("SELECT co_ty,br_st FROM disktb WHERE mod_na=? AND pt_no=?",(ch[0],ch[1]))
            fh=fr.fetchone()
            bon.commit()
            if fh is not None:
                if fh[0]==1:
                    brst="BDC-A"
                elif fh[0]==2:
                    brst="BDC-B"
                elif fh[0]==3:
                    brst="BDC-C"
                elif fh[0]==4:
                    brst="BDC-D"
                else:
                    messagebox.showerror("error","coating type is missing...")
                co_ty.set(brst)
                bs.set(fh[1])
                mc=1
                txt3.focus()
            else:
                messagebox.showerror("error","Received model name is missing...")
        rec()
            
    def rec():
        jc_noV = str(jc_no.get())
        cr.execute("SELECT Pfin_qty,Cmis_qty FROM logdt WHERE jc_no=?",(jc_noV,))
        ch=cr.fetchone()
        if ch is not None:
            if ch[1] is not None:
                lblsb = Label(f1aa,fg='orange',font=('arial',25,'bold'),text= ch[1] ,bd=26,justify='left')
                lblsb.grid(row=5,column=4)
            else:
                lblsb = Label(f1aa,fg='orange',font=('arial',25,'bold'),text= ch[0] ,bd=26,justify='left')
                lblsb.grid(row=5,column=4)
        txt3.focus()
    # ORDER's INFO BUTTONS
    def sc(qw):
        global cbjc
        fff=0
        if qw==3:
            jc_noV = str(jc_no.get())
            cr.execute("SELECT simod_na FROM store_in WHERE sijc_no=?",(jc_noV,))
            chh=cr.fetchone()
            if chh is not None:
                ma_naV=chh[0]
                fff=1
            
        else:
            ma_naV=str(md_na.get())
            ma_naV=ma_naV.upper()
            fff=1
        if fff==1:
            cr.execute("SELECT sijc_no FROM store_in WHERE simod_na=?",(ma_naV,))
            ch=cr.fetchall()
            lift=0
            qt=0
            if ch != []:
                ch=list(ch)
                fgg=0
                for i in range(len(ch)):
                    che=list(ch[i])
                    #print(ch)
                    cr.execute("SELECT Pfin_qty,Cmis_qty FROM logdt WHERE jc_no=?",(che[0],))
                    chh=cr.fetchone()
                    if chh is not None:
                        #print(che[0],chh)
                        if chh[1] is not None:
                            lift=lift+chh[1]
                            if fgg==0:
                                cbjc=che[0]
                                qt=lift
                                if qt !=0:
                                    fgg=1
                        elif chh[0] is not None:
                            lift=lift+chh[0]
                            if fgg==0:
                                cbjc=che[0]
                                qt=lift
                                if qt !=0:
                                    fgg=1
                    #elif qw==7:
                        #messagebox.showerror('Response', 'no job at now present')
                                       
                if qt !=0 and qw==7:
                    messagebox.showinfo('Response', " at job card no "+str(cbjc)+" has "+str(qt)+" qty and rest of "+str(lift-qt)+" qty more")
                elif qw==7:
                    messagebox.showerror('Response', 'no job at now present')
                
            elif qw==7 and ma_naV is None:
                messagebox.showerror('Response', 'the model is not present')
            aufil()
        else:
            messagebox.showerror('Response', 'the job card is not present')
            jc_no.set("")
            txt2.focus()
        


    
    def Reset():
            ln_no.set("")
            jc_no.set("")
            cb_qty.set("")
            cb_ti.set(time.strftime("%H:%M:%S"))
            co_ty.set("")
            br_op.set("")
            rdcb1.set(0)
            rdcb2.set(0)
            rdcb3.set(0)
            rdcb4.set(0)
            rdcb5.set(0)
            rdcb6.set(0)

            
    def check():
            #print(mc)
            sc(3)
            aufil()
            flg=0
            co_perV = str(co_per.get())
            ln_noV = str(ln_no.get())
            jc_noV = str(jc_no.get())
            cb_qtyV = str(cb_qty.get())
            cb_dtV = str(cb_dt.get())
            cb_tiV = str(cb_ti.get())
            co_tyV = str(co_ty.get())
            br_stV = str(bs.get())
            #print(br_stV)
            br_opV = str(br_op.get())
            rdcb1V = str(rdcb1.get())
            rdcb2V = str(rdcb2.get())
            rdcb3V = str(rdcb3.get())
            rdcb4V = str(rdcb4.get())
            rdcb5V = str(rdcb5.get())
            rdcb6V = str(rdcb6.get())


            
            cr.execute("SELECT jc_no,stg,Pfin_qty,Cfin_qty,Cdef_qty FROM logdt WHERE jc_no=?",(jc_noV,))
            ch=cr.fetchone()
            con.commit()
            
            

            if ((ch is not None) and (ch[0]==int(jc_noV))) and ('p' in ch[1]):
                flg=1
                if(ch[3] is not None):
                    y= ch[2]-(ch[3]+ch[4])
                else:
                    y=ch[2]
                #lblsb = Label(f1aa,fg='red',font=('arial',15,'bold'),text=y,bd=26,justify='left')
                #lblsb.grid(row=5,column=4)
            
            if len(co_perV) == 0:
                    messagebox.showerror("error","coating oprator name is missing...")
            else:
                    if len(ln_noV) == 0:
                            messagebox.showerror("error","line no missing...")
                    else:
                            if (len(jc_noV) == 0) or (flg==0) :
                                     messagebox.showerror("error","job card number is missing...")
                            elif str(cbjc)!=jc_noV :
                                     messagebox.showerror("error","there is older job on this model job card no : '"+str(cbjc) +"' waiting on PT...")
                            elif(jc_noV.isnumeric()):
                                     if len(cb_dtV) == 0:
                                            messagebox.showerror("error","date is missing...")
                                     else:
                                            if len(cb_tiV) == 0:
                                                    messagebox.showerror("error","time is missing...")
                                            else:
                                                    if len(cb_qtyV) == 0:
                                                            messagebox.showerror("error","out qty value is missing...")
                                                    elif(cb_qtyV.isnumeric()):
                                                            if (len(co_tyV) == 0) or (mc==0):
                                                                    messagebox.showerror("error","coating type is missing...")
                                                            else:
                                                                    if len(br_stV) == 0:
                                                                            messagebox.showerror("error","brushing status is missing...")
                                                                    else:
                                                                            if ((br_stV == '1') and (len(br_opV) == 0)):#if (br_stV=='Y' or br_stV=='y')and (len(br_opV) == 0):
                                                                                    messagebox.showerror("error","burshing oprator name is missing...")
                                                                            else:
                                                                                    if len(rdcb1V) == 0:
                                                                                            messagebox.showerror("error","rejected details is missing...")
                                                                                    elif(rdcb1V.isnumeric()):
                                                                                            if len(rdcb2V) == 0:
                                                                                                    messagebox.showerror("error","rejected details is missing...")
                                                                                            elif(rdcb2V.isnumeric()):
                                                                                                    if len(rdcb3V) == 0:
                                                                                                            messagebox.showerror("error","rejected details is missing...")
                                                                                                    elif(rdcb3V.isnumeric()):
                                                                                                            if len(rdcb4V) == 0:
                                                                                                                    messagebox.showerror("error","rejected details is missing...")
                                                                                                            elif(rdcb4V.isnumeric()):
                                                                                                                    if len(rdcb5V) == 0:
                                                                                                                            messagebox.showerror("error","rejected details is missing...")
                                                                                                                    elif(rdcb5V.isnumeric()):
                                                                                                                            if len(rdcb1V) == 0:
                                                                                                                                    messagebox.showerror("error","rejected details is missing...")
                                                                                                                            elif(rdcb6V.isnumeric()):
                                                                                                                                    done()
                                                                                                                                            
                                                                                                                            else:
                                                                                                                                    messagebox.showerror("error","rejected qty is not a number ")
                                                                                                                    else:
                                                                                                                            messagebox.showerror("error","rejected qty is not a number ")
                                                                                                            else:
                                                                                                                    messagebox.showerror("error","rejected qty is not a number ")
                                                                                                    else:
                                                                                                             messagebox.showerror("error","rejected qty is not a number ")
                                                                                            else:
                                                                                                    messagebox.showerror("error","rejected qty is not a number ")
                                                                                    else:
                                                                                            messagebox.showerror("error","rejected qty is not a number ")
                                                                    
                                                    else:
                                                            messagebox.showerror("error","out qty is not a number ")
                                                                    
                                            
                            else:
                                    messagebox.showerror("error","job card number is not a number ")
                                            

    def done():
        mflg=0
        co_perV = str(co_per.get())
        ln_noV = str(ln_no.get())
        jc_noV = int(jc_no.get())
        cb_qtyV =int(cb_qty.get())
        cb_dtV = str(cb_dt.get())
        cb_tiV = str(cb_ti.get())
        co_tyV = str(co_ty.get())
        br_stV = str(bs.get())
        br_opV = str(br_op.get())
        rdcb1V = int(rdcb1.get())
        rdcb2V = int(rdcb2.get())
        rdcb3V = int(rdcb3.get())
        rdcb4V = int(rdcb4.get())
        rdcb5V = int(rdcb5.get())
        rdcb6V = int(rdcb6.get())


        
        cr.execute("SELECT jc_no,stg,tot_qty,Pfin_qty,Cfin_qty,Cdef_qty,Cmis_qty,def_qty FROM logdt WHERE jc_no=?",(jc_noV,))
        ch=cr.fetchone()
        
        df=(rdcb1V+rdcb2V+rdcb3V+rdcb4V+rdcb5V+rdcb6V)
        fi=(cb_qtyV-df)#CH[2]
        dff=(df+ch[7])
        #chh=list(ch)

        
        
        if(ch[6] is None):
            mflg=1
        elif(ch[3]-(ch[4]+ch[5]) >= cb_qtyV):
            mflg=1
        #print(ch,cb_qtyV,df,ch[3],mflg)      
        if ((((ch is not None) and (cb_qtyV >= df)) and (abs(ch[3])>= cb_qtyV)) and (mflg==1)):        
                qEnter = messagebox.askokcancel("war","confirm")
                if qEnter > 0:
                            #cr.execute('DROP TABLE pttb')
            ###store db###
                        
                            #cr.execute('DELETE FROM store_in;',)##del all rows data

                        cr.execute("INSERT INTO cbtb(cbjc_no ,cbco_per ,cbln_no ,cb_dt ,cb_ti ,cb_qty ,cbco_ty,cbbr_st,cbbr_op,rdcb1 ,rdcb2 ,rdcb3 ,rdcb4 ,rdcb5 ,rdcb6 ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(
                                    jc_noV,
                                    co_perV,
                                    ln_noV,
                                    cb_dtV,
                                    cb_tiV,
                                    cb_qtyV,
                                    co_tyV,
                                    br_stV,
                                    br_opV,
                                    rdcb1V,
                                    rdcb2V,
                                    rdcb3V,
                                    rdcb4V,
                                    rdcb5V,
                                    rdcb6V))
            ####takeing jc no###

                            #cr.execute("SELECT * FROM logdt WHERE jc_no=?",(jc_noV,))
                            #ch_list=cr.fetchone()
                        jc=ch[0]
                        st=str(ch[1])+'c'
                            
                            #df=(df+ch_list[3])
                        if ch[4] is not None:
                            fi=fi+ch[4]

                        if ch[5] is not None:
                            df=ch[5]+df
                        
                        cms=((fi+df)- ch[3])      
                        ms=((fi+dff)- ch[2])
                            
            ###log db###
                            
                        cr.execute("UPDATE logdt SET stg =?,Cfin_qty=?,Cdef_qty=?,Cmis_qty=?,def_qty=?,miss_qty=? WHERE jc_no=?",(st,fi,df,abs(cms),dff,abs(ms),jc))
                        Reset()
        else:
            messagebox.showerror("error","given qty is more then recived qty...")
    ###close connection###
        con.commit()
        

    txt1.focus()
    txt1.bind("<Return>",lambda funct1:txt2.focus())
    txt2.focus()
    txt2.bind("<Return>",lambda funct1:sc(3))
    txt3.focus()
    txt3.bind("<Return>",lambda funct1:txt4.focus())
    txt4.focus()
    txt4.bind("<Return>",lambda funct1:txt5.focus())
    txt5.focus()
    txt5.bind("<Return>",lambda funct1:txt6.focus())
    txt6.focus()
    txt6.bind("<Return>",lambda funct1:txt7.focus())
    txt7.focus()
    txt7.bind("<Return>",lambda funct1:txt8.focus())
    txt8.focus()
    txt8.bind("<Return>",lambda funct1:txt9.focus())
    txt9.focus()
    txt9.bind("<Return>",lambda funct1:txt10.focus())
    txt10.focus()
    txt10.bind("<Return>",lambda funct1:txt11.focus())
    txt11.focus()
    txt11.bind("<Return>",lambda funct1:check())
  
    btndone=Button(f2ab,padx=16,pady=16,bd=8,fg='green',font=('arial',16,'bold'),width=15,text='DONE', command=check)
    btndone.grid(row=0,column=1)
    btndone.bind("<Enter>", on_enter)
    btndone.bind("<Leave>", on_leave)

    btnReset=Button(f2ab,padx=16,pady=16,bd=8,fg='black',font=('arial',16,'bold'),width=15,text='RESET',command=Reset)
    btnReset.grid(row=0,column=2)
    btnReset.bind("<Enter>", on_re)
    btnReset.bind("<Leave>", on_leave)
    w5.bind("<Key-Tab>",lambda event: Reset())

    srch =Button(Tops,padx=5,pady=5,bd=4,fg='black',font=('arial',8,'bold'),width=7,height=1,text="search",command=sc(7))#
    srch.grid(row=1,column=1)

    

    w5.mainloop()

#######################################################################################################################################################################
    
def fn(nam):
    rot.withdraw()
    w6 = Toplevel()
    w6.title("ceccpl fifo final inspection Systems")

    Tops,f1aa,f1ab,f2ab,btnback,btnExit=topbar(w6,6)

    # ORDER's INFO

    fi_per=StringVar()
    in_na=StringVar()
    jc_no=StringVar()
    fi_qty=StringVar()
    fi_ti=StringVar()
    cu_no=StringVar()
    rdfi1=StringVar()
    rdfi2=StringVar()
    rdfi3=StringVar()
    rdfi4=StringVar()
    rdfi5=StringVar()
    rdfi6=StringVar()
    fi_ti.set(time.strftime("%H:%M:%S"))
    rdfi1.set(0)
    rdfi2.set(0)
    rdfi3.set(0)
    rdfi4.set(0)
    rdfi5.set(0)
    rdfi6.set(0)

    in_na.set(nam)

    lblhb8 = Label(f1aa,font=('arial',15,'bold'),text='INSPECTER NAME',bd=16,justify='left')
    lblhb8.grid(row=0,column=1)
    txt1=Entry(f1aa,font=('arial',15,'bold'),textvariable=fi_per,bd=10,insertwidth=2,justify='left')
    txt1.grid(row=1,column=1)
    lblhb6 = Label(f1aa,font=('arial',15,'bold'),text='INCHARGE NAME',bd=16,justify='left')
    lblhb6.grid(row=0,column=2)
    txt2=Entry(f1aa,font=('arial',15,'bold'),textvariable=in_na,bd=10,insertwidth=2,justify='left')
    txt2.grid(row=1,column=2)
    lblsb = Label(f1aa,font=('arial',15,'bold'),text='JOB CARD NO',bd=16,justify='left')
    lblsb.grid(row=0,column=3)
    txt3=Entry(f1aa,font=('arial',15,'bold'),textvariable=jc_no,bd=10,insertwidth=2,justify='left')
    txt3.grid(row=1,column=3)

    lblsb = Label(f1aa,font=('arial',15,'bold'),text='JOB TAKEN TIME',bd=16,justify='left')
    lblsb.grid(row=2,column=1)
    txt4=Entry(f1aa,font=('arial',15,'bold'),textvariable=fi_ti,bd=10,insertwidth=2,justify='left')
    txt4.grid(row=3,column=1)
    lblsb = Label(f1aa,font=('arial',15,'bold'),text='JOB TAKEN QTY',bd=16,justify='left')
    lblsb.grid(row=2,column=2)
    txt5=Entry(f1aa,font=('arial',15,'bold'),textvariable=fi_qty,bd=10,insertwidth=2,justify='left')
    txt5.grid(row=3,column=2)
    lblsb = Label(f1aa,font=('arial',15,'bold'),text='JOB TAKEN DATE',bd=16,justify='left')
    lblsb.grid(row=2,column=3)
    fi_dt=DateEntry(f1aa,width=16,font=('arial',15,'bold'),date_pattern='yyyy-MM-dd')
    fi_dt.grid(row=3,column=3)


    lblsb = Label(f1aa,font=('arial',15,'bold'),text='COUNTER NO',bd=16,justify='left')
    lblsb.grid(row=4,column=2)
    drop=OptionMenu(f1aa,cu_no,"counter 1","counter 2","counter 3","counter 4","counter 5")
    drop.grid(row=5,column=2)
    drop.config(width = 16,font=('arial',15,'bold'))

    lblsb = Label(f1ab,font=('arial',15,'bold'),text='REJECTION DETAILS',bd=16,justify='left')
    lblsb.grid(row=0,column=0)


    lblhb8 = Label(f1ab,font=('arial',10,'bold'),text='Part Number Miss Match',bd=16,justify='right')
    lblhb8.grid(row=1,column=0)
    txt6=Entry(f1ab,width=5,font=('arial',10,'bold'),textvariable=rdfi1,bd=10,insertwidth=2,justify='left')
    txt6.grid(row=1,column=1)
    lblhb6 = Label(f1ab,font=('arial',10,'bold'),text='Rust',bd=16,justify='left')
    lblhb6.grid(row=2,column=0)
    txt7=Entry(f1ab,width=5,font=('arial',10,'bold'),textvariable=rdfi2,bd=10,insertwidth=2,justify='left')
    txt7.grid(row=2,column=1)
    lblsb = Label(f1ab,font=('arial',10,'bold'),text='Damaged',bd=16,justify='left')
    lblsb.grid(row=3,column=0)
    txt8=Entry(f1ab,width=5,font=('arial',10,'bold'),textvariable=rdfi3,bd=10,insertwidth=2,justify='left')
    txt8.grid(row=3,column=1)
    lblsb = Label(f1ab,font=('arial',10,'bold'),text='Paint Mark',bd=16,justify='left')
    lblsb.grid(row=4,column=0)
    txt9=Entry(f1ab,width=5,font=('arial',10,'bold'),textvariable=rdfi4,bd=10,insertwidth=2,justify='left')
    txt9.grid(row=4,column=1)
    lblsb = Label(f1ab,font=('arial',10,'bold'),text='Blow Hole',bd=16,justify='left')
    lblsb.grid(row=5,column=0)
    txt10=Entry(f1ab,width=5,font=('arial',10,'bold'),textvariable=rdfi5,bd=10,insertwidth=2,justify='left')
    txt10.grid(row=5,column=1)
    lblsb = Label(f1ab,font=('arial',10,'bold'),text='Machining Problem',bd=16,justify='left')
    lblsb.grid(row=6,column=0)
    txt11=Entry(f1ab,width=5,font=('arial',10,'bold'),textvariable=rdfi6,bd=10,insertwidth=2,justify='left')
    txt11.grid(row=6,column=1)

    # ORDER's INFO BUTTONS
    def rec():
        jc_noV = str(jc_no.get())
        cr.execute("SELECT cfin_qty,Cmis_qty,Pmis_qty FROM logdt WHERE jc_no=?",(jc_noV,))
        ch=cr.fetchone()
        if ch is not None:
            if ch[0] is not None:
                lblsb = Label(f1aa,fg='red',font=('arial',25,'bold'),text=str(ch[0]+ch[1]+ch[2]),bd=26,justify='left')
                lblsb.grid(row=5,column=3)
            else:
                messagebox.showerror("error","given job card hasn't completed...")
                lblsb = Label(f1aa,fg='red',font=('arial',25,'bold'),text=str("X"),bd=26,justify='left')
                lblsb.grid(row=5,column=3)
            txt4.focus()
        else:
            messagebox.showerror('Response', 'the job card is not present')
            jc_no.set("")
            txt3.focus()
            
            
            
    def Reset():
            
            in_na.set("")
            jc_no.set("")
            fi_qty.set("")
            fi_ti.set(time.strftime("%H:%M:%S"))
            cu_no.set("")
            rdfi1.set(0)
            rdfi2.set(0)
            rdfi3.set(0)
            rdfi4.set(0)
            rdfi5.set(0)
            rdfi6.set(0)
            
            
    def check():
            flg=0
            fi_perV = str(fi_per.get())
            in_naV = str(in_na.get())
            jc_noV = str(jc_no.get())
            fi_qtyV = str(fi_qty.get())
            fi_dtV = str(fi_dt.get())
            fi_tiV = str(fi_ti.get())
            cu_noV = str(cu_no.get())
            rdfi1V = str(rdfi1.get())
            rdfi2V = str(rdfi2.get())
            rdfi3V = str(rdfi3.get())
            rdfi4V = str(rdfi4.get())
            rdfi5V = str(rdfi5.get())
            rdfi6V = str(rdfi6.get())
    
            cr.execute("SELECT Cfin_qty,Pmis_qty,Cmis_qty FROM logdt WHERE jc_no=?",(jc_noV,))
            ch=cr.fetchone()

            if ch is not None:
                flg=1
                
            
            if len(fi_perV) == 0:
                    messagebox.showerror("error","inspetor name is missing...")
            else:
                    if len(in_naV) == 0:
                            messagebox.showerror("error","incharge name is missing...")
                    else:
                            if len(jc_noV) == 0 and flg!=0:
                                     messagebox.showerror("error","job card number is missing... are job is not logged")
                            elif(jc_noV.isnumeric()):
                                     if len(fi_dtV) == 0:
                                            messagebox.showerror("error","date is missing...")
                                     else:
                                            if len(fi_tiV) == 0:
                                                    messagebox.showerror("error","time is missing...")
                                            else:
                                                    if len(fi_qtyV) == 0:
                                                            messagebox.showerror("error","out qty value is missing...")
                                                    elif(fi_qtyV.isnumeric()):
                                                            if len(cu_noV) == 0:
                                                                    messagebox.showerror("error","counter no is missing...")
                                                            else:
                                                                    if len(rdfi1V) == 0:
                                                                            messagebox.showerror("error","rejected details is missing...")
                                                                    elif(rdfi1V.isnumeric()):
                                                                            if len(rdfi2V) == 0:
                                                                                    messagebox.showerror("error","rejected details is missing...")
                                                                            elif(rdfi2V.isnumeric()):
                                                                                    if len(rdfi3V) == 0:
                                                                                            messagebox.showerror("error","rejected details is missing...")
                                                                                    elif(rdfi3V.isnumeric()):
                                                                                            if len(rdfi4V) == 0:
                                                                                                    messagebox.showerror("error","rejected details is missing...")
                                                                                            elif(rdfi4V.isnumeric()):
                                                                                                    if len(rdfi5V) == 0:
                                                                                                            messagebox.showerror("error","rejected details is missing...")
                                                                                                    elif(rdfi5V.isnumeric()):
                                                                                                            if len(rdfi6V) == 0:
                                                                                                                    messagebox.showerror("error","rejected details is missing...")
                                                                                                            elif(rdfi6V.isnumeric()):
                                                                                                                    done()
                                                                                                                                            
                                                                                                            else:
                                                                                                                    messagebox.showerror("error","rejected qty is a in number ")
                                                                                                    else:
                                                                                                            messagebox.showerror("error","rejected qty is not a number ")
                                                                                            else:
                                                                                                    messagebox.showerror("error","rejected qty is not a number ")
                                                                                    else:
                                                                                            messagebox.showerror("error","rejected qty is not a number ")
                                                                            else:
                                                                                    messagebox.showerror("error","rejected qty is not a number ")
                                                                    else:
                                                                            messagebox.showerror("error","rejected qty is not a number ")
                                                                    
                                                    else:
                                                            messagebox.showerror("error","out qty is not a number ")
                                                                    
                                            
                            else:
                                    messagebox.showerror("error","job card number is not a number ")


    def done():
            mflg=0
            fms=0
            ms=0
            fi_perV = str(fi_per.get())
            in_naV = str(in_na.get())
            jc_noV = int(jc_no.get())
            fi_qtyV = int(fi_qty.get())
            fi_dtV = str(fi_dt.get())
            fi_tiV = str(fi_ti.get())
            cu_noV = str(cu_no.get())
            rdfi1V = int(rdfi1.get())
            rdfi2V = int(rdfi2.get())
            rdfi3V = int(rdfi3.get())
            rdfi4V = int(rdfi4.get())
            rdfi5V = int(rdfi5.get())
            rdfi6V = int(rdfi6.get())

            ##connection####

            
            cr.execute("SELECT jc_no,stg,tot_qty,Cfin_qty,Ffin_qty,Fdef_qty,Fmin_qty,def_qty,miss_qty FROM logdt WHERE jc_no=?",(jc_noV,))
            ch=cr.fetchone()   
            df=(rdfi1V+rdfi2V+rdfi3V+rdfi4V+rdfi5V+rdfi6V)
            fi=(fi_qtyV-df)#CH[2]
            dff=(df+ch[7])
            chh=list(ch)
            jc=ch[0]
            
                            
                            #df=(df+ch_list[3])
            if ch[4] is not None:
                fi=fi+ch[4]
            if ch[5] is not None:
                df=ch[5]+df
            if ch[3] is not None:
                fms=((fi+df)-ch[3])
            if ch[2] is not None:
                ms=((fi+dff)- ch[2])
            
            if(ch[6] is None):
                if ms==0 and fms==0:
                    mflg=1
            elif(ch[6] >= fi_qtyV) or (ch[3]-(ch[4]+ch[5]))>= fi_qtyV:
                if ms==0 and fms==0:
                    mflg=1
                
            
            
            
            #print(chh,cb_qtyV,df,ch[5],chh[10])    
            #if ((((ch is not None) and (cb_qtyV >= df)) and (abs(ch[5])>= cb_qtyV)) and (mflg==1)): 
            #print(ch,fi_qtyV,df,abs(ch[3]),mflg)
            if (((ch is not None) and (fi_qtyV >= df)) and (abs(ch[3])>= fi_qtyV)and (mflg==1)):        
                    qEnter = messagebox.askokcancel("war","confirm")
                    if qEnter > 0:
                            #cr.execute('DROP TABLE pttb')
            ###store db###
                            
                            #cr.execute('DELETE FROM store_in;',)##del all rows data

                            cr.execute("INSERT INTO fitb(fijc_no ,fi_per ,fiin_na,ficu_no ,fi_dt ,fi_ti ,fi_qty ,rdfi1 ,rdfi2 ,rdfi3 ,rdfi4 ,rdfi5 ,rdfi6 ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",(
                                    jc_noV,
                                    fi_perV,
                                    in_naV,
                                    cu_noV,
                                    fi_dtV,
                                    fi_tiV,
                                    fi_qtyV,
                                    rdfi1V,
                                    rdfi2V,
                                    rdfi3V,
                                    rdfi4V,
                                    rdfi5V,
                                    rdfi6V))
            ####takeing jc no###

                            #cr.execute("SELECT * FROM logdt WHERE jc_no=?",(jc_noV,))
                            #ch_list=cr.fetchone()
                            st=str(ch[1])+'f'
                            
                            
            ###log db###
                            con.commit()
                            cr.execute("UPDATE logdt SET stg =?,Ffin_qty=?,Fdef_qty=?,Fmin_qty=?,def_qty=?,miss_qty=? WHERE jc_no=?",(st,fi,df,abs(fms),dff,abs(ms),jc))
                            jc=[]
                            cr.execute("SELECT fijc_no,rdfi1,rdfi2,rdfi3,rdfi4,rdfi5,rdfi6 FROM fitb WHERE fi_dt=?",(fi_dtV,))
                            ch=cr.fetchall()
                            rd1=0
                            rd2=0
                            rd3=0
                            rd4=0
                            rd5=0
                            rd6=0
                            t=0
                            for i in range (len(ch)):
                                che=list(ch[i]) 
                                rd1=rd1+che[1]
                                rd2=rd2+che[2]
                                rd3=rd3+che[3]
                                rd4=rd4+che[4]
                                rd5=rd5+che[5]
                                rd6=rd6+che[6]
                                t=rd1+rd2+rd3+rd4+rd5+rd6
                                if t!=0:
                                    jc.append(che[0])
                                jc = list(dict.fromkeys(jc))
                                t=0
                            
                            
                                            
                            con.commit()            
                            cr.execute(" INSERT OR REPLACE INTO bintb(fi_dt,fijc_no ,rd1 ,rd2 ,rd3 ,rd4 ,rd5 ,rd6 ) VALUES(?,?,?,?,?,?,?,?)",(
                                                    fi_dtV,
                                                    str(jc),
                                                    rd1,
                                                    rd2,
                                                    rd3,
                                                    rd4,
                                                    rd5,
                                                    rd6))
                            
                            con.commit()
                            Reset()
            else:
                     messagebox.showerror("error","given qty is more then recived qty...are taken job card hasn't completed...")
    ###close connection###
            con.commit()
            


    txt1.focus()
    txt1.bind("<Return>",lambda funct1:txt2.focus())
    txt2.focus()
    txt2.bind("<Return>",lambda funct1:txt3.focus())
    txt3.focus()
    txt3.bind("<Return>",lambda funct1:rec())
    txt4.focus()
    txt4.bind("<Return>",lambda funct1:txt5.focus())
    txt5.focus()
    txt5.bind("<Return>",lambda funct1:txt6.focus())
    txt6.focus()
    txt6.bind("<Return>",lambda funct1:txt7.focus())
    txt7.focus()
    txt7.bind("<Return>",lambda funct1:txt8.focus())
    txt8.focus()
    txt8.bind("<Return>",lambda funct1:txt9.focus())
    txt9.focus()
    txt9.bind("<Return>",lambda funct1:txt10.focus())
    txt10.focus()
    txt10.bind("<Return>",lambda funct1:txt11.focus())
    txt11.focus()
    txt11.bind("<Return>",lambda funct1:check())

    btndone=Button(f2ab,padx=16,pady=16,bd=8,fg='green',font=('arial',16,'bold'),width=15,text='DONE', command=check)
    btndone.grid(row=0,column=1)
    btndone.bind("<Enter>", on_enter)
    btndone.bind("<Leave>", on_leave)

    btnReset=Button(f2ab,padx=16,pady=16,bd=8,fg='black',font=('arial',16,'bold'),width=15,text='RESET',command=Reset)
    btnReset.grid(row=0,column=2)
    btnReset.bind("<Enter>", on_re)
    btnReset.bind("<Leave>", on_leave)
    w6.bind("<Key-Tab>",lambda event: Reset())
    

    
    w6.mainloop()

#######################################################################################################################################################################
def admin():
    rot.withdraw()
    w7 = Toplevel()
    w7.title("ceccpl fifo final inspcetion Systems")

    Tops,f1aa,f1ab,f1ac,f2ab,btnback,btnExit=topbar(w7,7)
    
    # ORDER's INFO
    def logger(jc,fl):
        jc=str(jc)

        fileName = (jc+'.pdf')
        outpath = os.path.join( fl,fileName )
        documentTitle = ('SUMMARY OF JOB CARD NO'+jc)
        title = 'CECCPL FIFO'
        subTitle = ('SUMMARY OF JOB CARD NO : '+jc)
        pdf = canvas.Canvas(outpath,pagesize = A4)#fileName
        pdf.setTitle(documentTitle)

        pdf.setFont("Courier", 36)
        pdf.drawCentredString(300, 800, title)




        pdf.setFillColorRGB(0, 0, 255)
        pdf.setFont("Courier-Bold", 24)
        pdf.drawCentredString(290,770, subTitle)

        pdf.line(50, 710, 550, 710)
        pdf.line(80, 765, 500, 765)

        cr.execute("SELECT * FROM logdt WHERE jc_no=?",(jc,))
        log=cr.fetchall()
        cr.execute("SELECT * FROM flogdt WHERE jc_no=?",(jc,))
        flog=cr.fetchall()
        cr.execute("SELECT * FROM store_in WHERE sijc_no=?",(jc,))
        stn=cr.fetchall()
        cr.execute("SELECT * FROM store_out WHERE sojc_no=?",(jc,))
        sto=cr.fetchall()
        cr.execute("SELECT * FROM insp WHERE injc_no=?",(jc,))
        ins=cr.fetchall()
        cr.execute("SELECT * FROM pttb WHERE ptjc_no=?",(jc,))
        pt=cr.fetchall()
        cr.execute("SELECT * FROM cbtb WHERE cbjc_no=?",(jc,))
        cb=cr.fetchall()
        cr.execute("SELECT * FROM fitb WHERE fijc_no=?",(jc,))
        fin=cr.fetchall()


        con.commit()


        ptna=[]
        pttidt=[]
        ptln=[]
        dp1=[]
        dp2=[]
        dp3=[]
        dp4=[]
        dp5=[]
        dp6=[]
        dc1=[]
        dc2=[]
        dc3=[]
        dc4=[]
        dc5=[]
        dc6=[]
        ppt=[]
        brush=''
        binn=[]
        fpt=0
        fcb=0
        ffin=0
        if pt !=[]:
            for i in range (len(pt)):
                ppt.append(list(pt[i]))
                ptna.append(ppt[i][2])
                ptln.append(ppt[i][3])
                pttidt.append(ppt[i][4])
                pttidt.append(ppt[i][5])#5
                dp1.append(ppt[i][7])
                dp2.append(ppt[i][8])
                dp3.append(ppt[i][9])
                dp4.append(ppt[i][10])
                dp5.append(ppt[i][11])
                dp6.append(ppt[i][12])
            ptt=str(ptna[0])
            lenn=len(ptna)
            pttd=[]
            for i in range(1,lenn):
                if ptt!=ptna[i]:
                    ptt=(ptt+" and "+ptna[i])
            pttd=str(pttidt[0]+" "+pttidt[1])
            lenn=len(pttidt)
            pdt=pttidt[1]
            for i in range (2,lenn,2):
                if pdt!=pttidt[i+1]:
                    pttd=pttd+" and "+pttidt[i]+''+pttidt[i+1]
            fpt=1

        if cb !=[]:
            cbna=[]
            cbln=[]
            cbtidt=[]
            ppt=[]
            cbty=[]
            for i in range (len(cb)):
                ppt.append(list(cb[i]))
                cbna.append(ppt[i][2])
                cbln.append(ppt[i][3])
                cbtidt.append(ppt[i][4])
                cbtidt.append(ppt[i][5])#5
                cbty.append(ppt[i][7])
                
                dc1.append(ppt[i][10])
                dc2.append(ppt[i][11])
                dc3.append(ppt[i][12])
                dc4.append(ppt[i][13])
                dc5.append(ppt[i][14])
                dc6.append(ppt[i][15])    
            cbb=str(cbna[0])
            lenn=len(cbna)


            for i in range(1,lenn):
                if cbb!=cbna[1]:
                    cbb=(cbb+" and "+cbna[i])

                
            cbtd=str(cbtidt[0]+" "+cbtidt[1])
            lenn=len(cbtidt)

            dt=cbtidt[1]

            for i in range (2,lenn,2):
                if dt!=cbtidt[i+1]:
                    cbtd=cbtd+" and "+cbtidt[i]+''+cbtidt[i+1]
                        

            b=0
            if b==1:
                brush='brushing operator name :'
            else:
                brush='brushing not required'
            fcb=1
        if log !=[]:
            log=log[0]
        elif flog !=[]:
            log=flog[0]

        if stn !=[]:
            stn=stn[0]
        if ins !=[]:
            ins=ins[0]

        if fin !=[]:
            #print(fin)
            fin=fin[0]
            cr.execute("SELECT * FROM bintb WHERE fi_dt=?",(fin[5],))
            binn=cr.fetchall()
            con.commit()
            ffin=1

        if sto!=[]:
            sto=sto[0]
            stod=str(sto[3])
        else:
            stod='not yet dispatch'




        bine=[]
        bind=[]
        if binn !=[]:
            
            for i in range (len(binn)):
                bine.append(list(binn[i]))
                for j in range(8):
                    bind.append(bine[i][j])
            bind=sum(bind[2:7])


        text11 = ['','','','Recived Person Name ','Recived Time ','Incoming Inspector ','Sampling Qty  ','Rejection Qty   ','','Out Qty   ']
        text22 = ['','','', 'PT id ','Taken Time ','','Line no ','Rejection Qty ','','Out Qty ']
        text33 = ['','','Coating id ','Taken Time ','Mechine No ','Coating Type ',brush,'Rejection Qty ','Qut Qty ']
        text44 = ['','','Inspector Name ','Incharge Name ','Taken Time','Counter no ','Rejection Qty ','','Final Qty ']
        text99 = ['','','Part No Missing ','Rust','Damage','Blow Hole','Paint Mark','Mechining Problem']
        text16 = ['Bin','STAGE']
        text17 = ['Model no','Part no']
        text18 = ['Received Qty','Dispatch Qty']
        text19 = [': '+stn[3],': '+stn[4]]
        text20 = [': '+str(stn[5]),': '+stod]
        text21 = [': '+str(bind),': '+log[1]]

        text12 = ['','',': '+str(ins[4]),': '+str(ins[5]),': '+str(ins[6]),': '+str(ins[7]),': '+str(ins[8]),': '+str(ins[9])]
        text13 = ['','',': '+str(sum(dp1)),': '+str(sum(dp2)),': '+str(sum(dp3)),': '+str(sum(dp4)),': '+str(sum(dp5)),': '+str(sum(dp6))]
        text14 = ['','',': '+str(sum(dc1)),': '+str(sum(dc2)),': '+str(sum(dc3)),': '+str(sum(dc4)),': '+str(sum(dc5)),': '+str(sum(dc6))]
        if ffin==1:
            text15 = ['','',': '+str(fin[8]),': '+str(fin[9]),': '+str(fin[10]),': '+str(fin[11]),': '+str(fin[12]),': '+str(fin[13])]

        text55 = ['','','',': '+stn[6], ': '+stn[8], ': '+ins[1], ': '+str(ins[3]), ": "+str(log[4]), '', ": "+str(log[3])]
        if fpt==1:
            text66 = ['','','',': '+ptt,': '+str(pttd),'',': '+str(ptln[0]),': '+str(log[6]),'',': '+str(log[5])]
        if fcb==1:
            text77 = ['','',': '+cbb,': '+str(cbtd),': '+str(cbln[0]),': '+str(cbty[0]),'',': '+str(log[9]),': '+str(log[8])]
        if ffin==1:
            text88 = ['','',': '+fin[2],': '+fin[3],': '+fin[5]+" @ "+fin[6],': '+fin[4],": "+str(log[12]),'',': '+str(log[11])]




        text = pdf.beginText(40,682)
        text.setFont("Courier-Bold", 18)
        text.setFillColor(colors.red)
        text.textLine('INCOMING :-')
        pdf.drawText(text)
        if fpt==1:
            text = pdf.beginText(40,535)
            text.textLine('PT :-')
            pdf.drawText(text)
        if fcb==1:
            text = pdf.beginText(40,380)
            text.textLine('COATING & BRUSHING')
            pdf.drawText(text)
        if ffin==1:
            text = pdf.beginText(40,230)
            text.textLine('FINAL INSPECTION')
            pdf.drawText(text)


        #30,10 print


        pdf.rect(30,550,540,150)


        #1 s
        text = pdf.beginText(40,700)
        text.setFont("Courier-Bold", 12)
        text.setFillColor(colors.black)
        for line in text11:
            text.textLine(line)
        pdf.drawText(text)
        if fpt==1:
            pdf.rect(30,400,540,150)
            text = pdf.beginText(40, 550)
            for line in text22:
                text.textLine(line)
            pdf.drawText(text)
        if fcb==1:
            pdf.rect(30,250,540,150)
            text = pdf.beginText(40, 380)
            for line in text33:
                text.textLine(line)
            pdf.drawText(text)
        if ffin==1:
            pdf.rect(30,100,540,150)
            text = pdf.beginText(40, 230)
            for line in text44:
                text.textLine(line)
            pdf.drawText(text)

        #1 o
        text1 = pdf.beginText(200,700)
        text1.setFont("Courier", 12)
        text1.setFillColor(colors.gray)
        for line in text55:
            text1.textLine(line)
        pdf.drawText(text1)
        #pt
        if fpt==1:
            text1 = pdf.beginText(200, 550)
            for line in text66:
                text1.textLine(line)
            pdf.drawText(text1)
        #cb
        if fcb==1:
            text1 = pdf.beginText(200, 380)
            for line in text77:
                text1.textLine(line)
            pdf.drawText(text1)
        #fin
        if ffin==1:
            text1 = pdf.beginText(200, 230)
            for line in text88:
                text1.textLine(line)
            pdf.drawText(text1)


        #2 s
        
        if log[4]>0:
            text = pdf.beginText(360,686)
            text.setFont("Courier-Bold", 12)
            text.setFillColor(colors.black)
            for line in text99:
                text.textLine(line)
            pdf.drawText(text)

        if log[5] is not None and log[5]>0:
            text = pdf.beginText(360, 537)
            text.setFont("Courier-Bold", 12)
            text.setFillColor(colors.black)
            for line in text99:
                text.textLine(line)
            pdf.drawText(text)

        if log[9] is not None and log[9]>0:
            text = pdf.beginText(360, 380)
            text.setFont("Courier-Bold", 12)
            text.setFillColor(colors.black)
            for line in text99:
                text.textLine(line)
            pdf.drawText(text)

        if log[12] is not None and log[12]>0:
            text = pdf.beginText(360, 230)
            text.setFont("Courier-Bold", 12)
            text.setFillColor(colors.black)
            for line in text99:
                text.textLine(line)
            pdf.drawText(text)
            
        #s o
        
        if log[4]>0:
            text1 = pdf.beginText(500,686)
            text1.setFont("Courier", 12)
            text1.setFillColor(colors.gray)
            for line in text12:
                text1.textLine(line)
            pdf.drawText(text1)
        if fpt==1:
            if log[5]>0:
                text1 = pdf.beginText(500, 537)
                text1.setFont("Courier", 12)
                text1.setFillColor(colors.gray)
                for line in text13:
                    text1.textLine(line)
                pdf.drawText(text1)
        if fcb==1:
            if log[9]>0:
                text1 = pdf.beginText(500, 380)
                text1.setFont("Courier", 12)
                text1.setFillColor(colors.gray)
                for line in text14:
                    text1.textLine(line)
                pdf.drawText(text1)
        if ffin==1:
            if log[12]>0:
                text1 = pdf.beginText(500, 230)
                text1.setFont("Courier", 12)
                text1.setFillColor(colors.gray)
                for line in text15:
                    text1.textLine(line)
                pdf.drawText(text1)

        #b s
        text = pdf.beginText(40,80)
        text.setFont("Courier-Bold", 20)
        text.setFillColor(colors.black)
        for line in text16:
            text.textLine(line)
        pdf.drawText(text)

        #b o
        text = pdf.beginText(150,80)
        text.setFont("Courier-Bold", 20)
        text.setFillColor(colors.gray)
        for line in text21:
            text.textLine(line)
        pdf.drawText(text)

        #t1 s
        text = pdf.beginText(40,740)
        text.setFont("Courier-Bold", 12)
        text.setFillColor(colors.green)
        for line in text17:
            text.textLine(line)
        pdf.drawText(text)
        #t2 s
        text = pdf.beginText(360,740)
        for line in text18:
            text.textLine(line)
        pdf.drawText(text)

        #t1 o
        text1 = pdf.beginText(150,740)
        text1.setFont("Courier", 12)
        text1.setFillColor(colors.red)
        for line in text19:
            text1.textLine(line)
        pdf.drawText(text1)
        #t2 0
        text1 = pdf.beginText(450,740)
        for line in text20:
            text1.textLine(line)
        pdf.drawText(text1)

        pdf.save()
    jc_no=StringVar()
    psw=StringVar()
    pswr=StringVar()
    fl_naa=StringVar()
    us_na=StringVar()
    us_id=StringVar()
    us_idr=StringVar()
    us_idd=StringVar()
    asc=StringVar()
    gr_dt=StringVar()
    jc_nod=StringVar()
    del_sec=StringVar()

    def gen():
            
            jc_noV=str(jc_no.get())
            #print(fl_na)
            fl_naV=fl_na#str(fl_na.get())
            #print(fl_naV)
            

            if len(jc_noV) == 0:
                    messagebox.showerror("error","job card is missing...")
            else:
                    if len(fl_naV) == 0:
                            messagebox.showerror("error","file name is missing...")
                    else:
                        logger(jc_noV,fl_naV)
                        messagebox.showinfo('information',"succeful")
                        Reset()


    def rst():
            
            us_idV=str(us_idr.get())
            pswV=str(pswr.get())
            cr.execute("SELECT ep_id FROM pswdt WHERE ep_id=?",(us_idV,))
            ch=cr.fetchone()
            if len(us_idV) == 0 and ch is None:
                    messagebox.showerror("error","user id is missing...")
            else:
                    if len(pswV) == 0:
                            messagebox.showerror("error","password is missing...")
                    else:
                        cr.execute("UPDATE pswdt SET psw = ? WHERE ep_id = ?",(
                                                        pswV,
                                                        int(us_idV)))
                        con.commit()
                        
                        messagebox.showinfo('information', 'password is reseted')
                        Reset()


    def cre():
            
            pswV=str(psw.get())
            us_naV=str(us_na.get())
            us_idV=str(us_id.get())
            ascV=str(asc.get())
            cr.execute("SELECT ep_id FROM pswdt WHERE ep_id=?",(us_idV,))
            ch=cr.fetchone()
            if len(us_naV) == 0 :
                    messagebox.showerror("error","Your name is missing ...")
            else:
                    if len(pswV) == 0:
                            messagebox.showerror("error","Password is missing...")
                    elif len(pswV) <= 3:
                            messagebox.showerror("error","Password must be min 4 char ...")
                    else:
                            if len(us_idV) == 0 and ch is not None:
                                    messagebox.showerror("error","user id is missing are already exist...")
                            elif us_idV.isnumeric():#and ch is not None)
                                    if len(ascV) == 0:
                                            messagebox.showerror("error","dispatch qty value is missing...")
                                                                    
                                    else:
                                            
                                            cr.execute("INSERT INTO pswdt VALUES(?,?,?,?)",(
                                                        int(us_idV),
                                                        us_naV,
                                                        pswV,
                                                        ascV))
                                            con.commit()
                                            
                                            messagebox.showinfo('information',"succeful")
                                            Reset()
                                
                                            
                            else:
                                    messagebox.showerror("error","user id is a number ")



    def dell():
            us_idV=str(us_idd.get())
            cr.execute("SELECT ep_id FROM pswdt WHERE ep_id=?",(us_idV,))
            ch=cr.fetchone()
            if len(us_idV) == 0 and ch is None:
                messagebox.showerror("error","Your id is missing...")
            else:
                cr.execute("DELETE FROM pswdt WHERE ep_id = ?",(
                    int(us_idV),))
                messagebox.showinfo('information',"user deleted")
                con.commit()
                
                Reset()
    #print        
    def Reset():
        jc_no.set("")
        psw.set("")
        pswr.set("")        
        us_na.set("")
        us_id.set("")
        us_idr.set("")
        us_idd.set("")
        asc.set("")
        gr_dt.set("")
        jc_nod.set("")
        del_sec.set("")
        
    def jdel():
        jc=str(jc_nod.get())
        ds=str(del_sec.get())
        if len(jc) == 0:
            messagebox.showerror("error","job card is missing...")
        else:
            if len(ds)==0:
                messagebox.showerror("error","select sector below...")
            else:
                jc=int(jc)
                if ds=="ALL":
                    cr.execute("""DELETE FROM logdt WHERE jc_no=?""",(jc,))
                    con.commit()
                    cr.execute("""DELETE FROM store_in WHERE sijc_no=?""",(jc,))
                    con.commit()
                    cr.execute("""DELETE FROM store_out WHERE sojc_no=?""",(jc,))
                    con.commit()
                    cr.execute("""DELETE FROM insp WHERE injc_no=?""",(jc,))
                    con.commit()
                    cr.execute("""DELETE FROM pttb WHERE ptjc_no=?""",(jc,))
                    con.commit()
                    cr.execute("""DELETE FROM cbtb WHERE cbjc_no=?""",(jc,))
                    con.commit()
                    cr.execute("""DELETE FROM fitb WHERE fijc_no=?""",(jc,))
                    con.commit()
                elif ds=="INSPECTION":
                    cr.execute("""DELETE FROM insp WHERE injc_no=?""",(jc,))
                    con.commit()
                    cr.execute("""SELECT stg FROM logdt WHERE jc_no=?""",(jc,))
                    ch=cr.fetchone()
                    ch=ch[0]
                    ch = ch.replace('n', '')
                    cr.execute("""UPDATE logdt SET Ifin_qty = ? , Idef_qty = ? , stg = ? WHERE jc_no = ?""",(None,None,ch,jc))
                    con.commit()
                         
                elif ds=="PT":
                    cr.execute("""DELETE FROM pttb WHERE ptjc_no=?""",(jc,))
                    con.commit()
                    cr.execute("""SELECT stg FROM logdt WHERE jc_no=?""",(jc,))
                    ch=cr.fetchone()
                    ch=ch[0]
                    ch = ch.replace('p', '')
                    cr.execute("""UPDATE logdt SET Pfin_qty = ? , Pdef_qty = ? , Pmis_qty = ? ,stg = ? WHERE jc_no = ?""",(None,None,None,ch,jc))
                    con.commit()
                    
                elif ds=="COATING":
                    cr.execute("""DELETE FROM cbtb WHERE cbjc_no=?""",(jc,))
                    con.commit()
                    cr.execute("""SELECT stg FROM logdt WHERE jc_no=?""",(jc,))
                    ch=cr.fetchone()
                    ch=ch[0]
                    ch = ch.replace('c', '')
                    cr.execute("""UPDATE logdt SET Cfin_qty = ? , Cdef_qty = ? , Cmis_qty = ? ,stg = ? WHERE jc_no = ?""",(None,None,None,ch,jc))
                    con.commit()
                    
                elif ds=="FINAL":
                    cr.execute("""DELETE FROM fitb WHERE fijc_no=?""",(jc,))
                    con.commit()
                    cr.execute("""SELECT stg FROM logdt WHERE jc_no=?""",(jc,))
                    ch=cr.fetchone()
                    ch=ch[0]
                    ch = ch.replace('f', '')
                    cr.execute("""UPDATE logdt SET Ffin_qty = ? , Fdef_qty = ? , Fmin_qty = ? ,stg = ? WHERE jc_no = ?""",(None,None,None,ch,jc))
                    con.commit()
                    
                elif ds=="STORE OUT":
                    cr.execute("""DELETE FROM store_out WHERE sojc_no=?""",(jc,))
                    con.commit()
                    
                elif ds=="KILL":
                    cr.execute("""DELETE FROM logdt WHERE jc_no=?""",(jc,))
                    con.commit()
                    cr.execute("""DELETE FROM store_in WHERE sijc_no=?""",(jc,))
                    con.commit()
                    cr.execute("""DELETE FROM store_out WHERE sojc_no=?""",(jc,))
                    con.commit()
                    cr.execute("""DELETE FROM insp WHERE injc_no=?""",(jc,))
                    con.commit()
                    cr.execute("""DELETE FROM pttb WHERE ptjc_no=?""",(jc,))
                    con.commit()
                    cr.execute("""DELETE FROM cbtb WHERE cbjc_no=?""",(jc,))
                    con.commit()
                    cr.execute("""DELETE FROM fitb WHERE fijc_no=?""",(jc,))
                    con.commit()
                    cr.execute("""DELETE FROM flogdt WHERE jc_no=?""",(jc,))
                    con.commit()
                
                messagebox.showinfo('information',"job card deleted")
                jc_nod.set("")
            
    def loc():
        global fl_na
        fl_na = filedialog.askdirectory()
        fl_naa.set(fl_na)
    def grp():
        w7.destroy()
        graph()
        
        
    
    

    
    


    lblhb8 = Label(f1aa,font=('arial',15,'bold'),text='JC NO',bd=16,justify='left')
    lblhb8.grid(row=0,column=1)
    txt11=Entry(f1aa,font=('arial',15,'bold'),textvariable=jc_no,bd=10,width=12,justify='left')
    txt11.grid(row=1,column=1)
    btnReset=Button(f1aa,bd=4,fg='black',font=('arial',10,'bold'),width=15,text='FILE LOCATION', command=loc)#
    btnReset.grid(row=0,column=2)
    txt12=Entry(f1aa,font=('arial',8,'bold'),textvariable=fl_naa,bd=5,width=20,justify='left')
    txt12.grid(row=1,column=2)
    btnReset.bind("<Enter>", on_re)
    btnReset.bind("<Leave>", on_leav)
    btnReset=Button(f1aa,bd=4,fg='black',font=('arial',16,'bold'),width=10,text='GENERATE', command=gen)#
    btnReset.grid(row=1,column=3)
    btnReset.bind("<Enter>", on_enter)
    btnReset.bind("<Leave>", on_leave)
    
    lblhb8 = Label(f1aa,font=('arial',15,'bold'),text='USER ID',bd=16,justify='left')
    lblhb8.grid(row=2,column=1)
    txt21=Entry(f1aa,font=('arial',15,'bold'),textvariable=us_idr,bd=10,width=12,justify='left')
    txt21.grid(row=3,column=1)
    lblhb6 = Label(f1aa,font=('arial',15,'bold'),text='PASSWORD',bd=16,justify='left')
    lblhb6.grid(row=2,column=2)
    txt22=Entry(f1aa,font=('arial',15,'bold'),textvariable=pswr,bd=10,width=12,justify='left')
    txt22.grid(row=3,column=2)
    btnReset=Button(f1aa,bd=4,fg='black',font=('arial',16,'bold'),width=10,text='RESET', command=rst)#
    btnReset.grid(row=3,column=3)
    btnReset.bind("<Enter>", on_ent)
    btnReset.bind("<Leave>", on_leav)

    lblhb8 = Label(f1ab,font=('arial',15,'bold'),text='USER ID',bd=16,justify='left')
    lblhb8.grid(row=0,column=1)
    txt31=Entry(f1ab,font=('arial',15,'bold'),textvariable=us_id,bd=10,width=12,justify='left')
    txt31.grid(row=1,column=1)
    lblhb6 = Label(f1ab,font=('arial',15,'bold'),text='USER NAME',bd=16,justify='left')
    lblhb6.grid(row=0,column=2)
    txt32=Entry(f1ab,font=('arial',15,'bold'),textvariable=us_na,bd=10,width=12,justify='left')
    txt32.grid(row=1,column=2)    
    lblhb8 = Label(f1ab,font=('arial',15,'bold'),text='PASSWORD',bd=16,justify='left')
    lblhb8.grid(row=2,column=1)
    txt33=Entry(f1ab,font=('arial',15,'bold'),textvariable=psw,bd=10,width=12,justify='left')
    txt33.grid(row=3,column=1)
    lblhb6 = Label(f1ab,font=('arial',15,'bold'),text='ACCESS',bd=16,justify='left')
    lblhb6.grid(row=2,column=2)
    drop=OptionMenu(f1ab,asc,"admin","member","guest")
    drop.grid(row=3,column=2)
    drop.config(width = 10,font=('arial',15,'bold')) 
    btnReset=Button(f1ab,bd=4,fg='black',font=('arial',16,'bold'),width=10,text='CREATE', command=cre)#
    btnReset.grid(row=3,column=3)
    btnReset.bind("<Enter>", on_enter)
    btnReset.bind("<Leave>", on_leave)

    lblhb8 = Label(f1ac,font=('arial',15,'bold'),text='USER ID',bd=16,justify='left')
    lblhb8.grid(row=0,column=4)
    txt41=Entry(f1ac,font=('arial',15,'bold'),textvariable=us_idd,bd=10,width=12,justify='left')
    txt41.grid(row=1,column=4)   
    btnReset=Button(f1ac,bd=4,fg='black',font=('arial',16,'bold'),width=10,text='DELETE', command=dell)#
    btnReset.grid(row=3,column=4)
    btnReset.bind("<Enter>", on_ent)
    btnReset.bind("<Leave>", on_leav)

    txt42=Entry(f1ac,font=('arial',15,'bold'),textvariable=jc_nod,bd=10,width=12,justify='left')
    txt42.grid(row=4,column=4)
    drop=OptionMenu(f1ac,del_sec,"ALL","INSPECTION","PT","COATING","FINAL","STORE OUT","KILL")
    drop.grid(row=5,column=4)
    drop.config(width = 12,font=('arial',15,'bold'))
    bt=Button(f1ac,bd=4,bg='green',fg='black',font=('arial',10,'bold'),width=15,text='DELETE Job Card', command=jdel)#
    bt.grid(row=6,column=4)
    bt.bind("<Enter>", on_ent)
    bt.bind("<Leave>", on_leav)
    
    bt=Button(f1ac,bd=4,bg='green',fg='black',font=('arial',10,'bold'),width=15,text='plot graph', command=grp)#
    bt.grid(row=8,column=4)
    bt.bind("<Enter>", on_enter)
    bt.bind("<Leave>", on_leave)


    #bt=Button(f1ac,bd=4,bg='green',fg='black',font=('arial',10,'bold'),width=15,text='DELETE Job Card', command=gt)#
    #bt.grid(row=6,column=4)

    txt11.focus()
    txt11.bind("<Return>",lambda funct1:txt12.focus())
    txt12.focus()
    txt12.bind("<Return>",lambda funct1:gen())
    
    txt21.focus()
    txt21.bind("<Return>",lambda funct1:txt22.focus())
    txt22.focus()
    txt22.bind("<Return>",lambda funct1:rst())

    txt31.focus()
    txt31.bind("<Return>",lambda funct1:txt32.focus())
    txt32.focus()
    txt32.bind("<Return>",lambda funct1:txt33.focus())
    txt33.focus()
    txt33.bind("<Return>",lambda funct1:cre())

    txt41.focus()
    txt41.bind("<Return>",lambda funct1:dell())

    txt42.focus()
    txt42.bind("<Return>",lambda funct1:jdel())


    btnReset=Button(f2ab,padx=16,pady=16,bd=8,fg='black',font=('arial',16,'bold'),width=15,text='RESET',command=Reset)
    btnReset.grid(row=0,column=2)
    btnReset.bind("<Enter>", on_re)
    btnReset.bind("<Leave>", on_leave)
    w7.bind("<Key-Tab>",lambda event: Reset())

    

    w7.mainloop()
#######################################################################################################################################################################
def graph():
    #admin.withdraw()
    w11=Toplevel()

    Tops,f1aa,f2ab,f1ad=topbar(w11,11)
    w11.title("ceccpl fifo Systems")
    global flgrp
    flgrp=0
        
    # ORDER's INFO

    mod_na=StringVar()
    
    # ORDER's INFO BUTTONS
    def refresh(v):
            w11.destroy()
            graph()
            mod_na.set(v)
        
    def Reset():
            mod_na.set("")
            w11.destroy()
            graph()
            
    def check():
            mod_naV = str(mod_na.get())
            mod_naV=mod_naV.upper()
            datin=str(gri_dt.get())
            datout=str(gro_dt.get())
            jcn=[]
            jcc=[]
            cn=[]
            co=[]
            x1=[]
            x2=[]
            stolist=[]
            dif=[]
            global flgrp
            
            if len(mod_naV) == 0:
                    messagebox.showerror("error","model name is missing...")
            elif flgrp==1:
                    messagebox.showerror("error","reset...")
                    refresh(mod_naV)
            else:
                    try:
                        
                        cr.execute("SELECT sijc_no,sirec_qty FROM 'store_in' Where simod_na=? AND (si_dt BETWEEN  ? AND ?) ",(mod_naV,datin,datout))#BETWEEN  2021-08-04 AND 2021-08-05
                        #cr.execute("SELECT sijc_no,sirec_qty FROM store_in WHERE simod_na=?",(mod_naV,)) #WHERE simod_na=?",(mod,))
                        stn=cr.fetchall()
                        for i in range(len(stn)):   
                            cn.append(stn[i][1])
                            jcn.append(stn[i][0])
                            cr.execute("SELECT sojc_no,sorec_qty FROM store_out WHERE sojc_no=?",(stn[i][0],))
                            sto=cr.fetchall()
                            stolist.append(sto)
                        for j in range(len(stolist)):
                            try:
                                co.append(stolist[j][0][1])
                                jcc.append(stolist[j][0][0])
                                dif.append((stn[j][1])-(stolist[j][0][1]))
                            except:
                                pass
                        sumin=sum(cn)
                        sumout=sum(co)
                        for i in range(len(jcn)):
                            x1.append(i+1)
                            
                        y1= cn
                        
                        for i in range(len(jcc)):
                            x2.append(i+1)
                        y2=co
                        y3=dif
        
                        fig = Figure(figsize = (8, 3),dpi = 100)
                        a = fig.add_axes([0.1,0.1,0.8,0.8])#subplot(122)
                        if len(x1)==len(y1):
                            a.plot(x1,y1, marker = "o", label = ("recived "+mod_naV))
                            a.plot(x2,y2,'g', marker = "o", label = ("send "+mod_naV))
                            a.plot(x2,y3,'r', marker = "o", label = ("defect "+mod_naV))
                            a.set_xlabel("time")
                            a.set_ylabel("qty")
                            a.set_title("job procced")
                            a.legend()
                        lblhb8 = Label(f1ad,font=('arial',15,'bold'),text='STATUS',bd=6,justify='left')
                        lblhb8.pack()
                        canvas = FigureCanvasTkAgg(fig,master = f1ad)#master =
                        
                        canvas.draw()
                        canvas.get_tk_widget().pack(fill=BOTH,expand=True)# side=TOP,fill=BOTH,expand=True
                        toolbar = NavigationToolbar2Tk(canvas,f1ad)
                        toolbar.update()
                        canvas.get_tk_widget().pack(fill=BOTH,expand=True)#grid(row=1,column=0)# side=BOTTOM,fill=BOTH,expand=True
                        flgrp=1
                    except:
                        messagebox.showerror("error","model name is missing in record...")
                        Reset()
                        #cr.execute("SELECT sijc_no,sirec_qty FROM store_in WHERE si_dt=?",(mod_naV,)) #WHERE simod_na=?",(mod,))
                        #stn=cr.fetchall()
                    
                    
    
    lblhb8 = Label(f1aa,font=('arial',15,'bold'),text='MODEL NAME',bd=6,justify='left')
    lblhb8.grid(row=0,column=0)
    txt1=Entry(f1aa,font=('arial',15,'bold'),textvariable=mod_na,bd=10,insertwidth=2,justify='left')
    txt1.grid(row=1,column=0)
    lblhb8 = Label(f1aa,font=('arial',15,'bold'),text='STARTING DATE',bd=6,justify='left')
    lblhb8.grid(row=2,column=0)
    gri_dt=DateEntry(f1aa,width=16,font=('arial',15,'bold'),date_pattern='yyyy-MM-dd',year=2021, month=2, day=21)
    gri_dt.grid(row=3,column=0)
    lblhb8 = Label(f1aa,font=('arial',15,'bold'),text='ENDING DATE',bd=6,justify='left')
    lblhb8.grid(row=4,column=0)
    gro_dt=DateEntry(f1aa,width=16,font=('arial',15,'bold'),date_pattern='yyyy-MM-dd')
    gro_dt.grid(row=5,column=0)

    txt1.focus()
    txt1.bind("<Return>",lambda funct1:check())
    #txt12.focus()
    #txt12.bind("<Return>",lambda funct1:gen())
    

    btndone=Button(f1aa,padx=8,pady=8,bd=8,fg='blue',font=('arial',16,'bold'),width=6,text='DONE', command=check)
    btndone.grid(rowspan=6,column=0)
    btndone.bind("<Enter>", on_enter)
    btndone.bind("<Leave>", on_leave)

    btnReset=Button(f2ab,padx=16,pady=16,bd=8,fg='black',font=('arial',16,'bold'),width=15,text='RESET',command=Reset)
    btnReset.grid(row=0,column=2)
    btnReset.bind("<Enter>", on_re)
    btnReset.bind("<Leave>", on_leave)
    w11.bind("<Key-Tab>",lambda event: Reset())



    w11.mainloop()

#######################################################################################################################################################################
def psw(xx,wx):
    rot.withdraw()
    w9 = Toplevel()
    w9.iconbitmap('logo.ico')
    w9.title("ceccpl fifo password Systems")

    width = 450
    height = 550

    #main-frame

    f1aa = Frame(w9, width=width, height=380, bd=8)
    f1aa.pack(side=TOP,expand=TRUE )


    # ORDER's INFO


    us_id=StringVar()
    psw=StringVar()

    us_id.set("")
    psw.set("")

    lblhb8 = Label(f1aa,font=('arial',15,'bold'),text='EMPLOYEE ID',bd=16,justify='left')
    lblhb8.grid(row=0,column=1)
    txt1=Entry(f1aa,font=('arial',15,'bold'),textvariable=us_id,bd=10,insertwidth=2,justify='left')
    txt1.grid(row=1,column=1)

    lblsb = Label(f1aa,font=('arial',15,'bold'),text='PASSWORD',bd=16,justify='left')
    lblsb.grid(row=2,column=1)
    txt2=Entry(f1aa,font=('arial',15,'bold'),textvariable=psw,bd=10,insertwidth=2,justify='left',show='*')
    txt2.grid(row=3,column=1)
    
    def check():
        us_idV=int(us_id.get())
        pswV=str(psw.get())
        
        cr.execute("SELECT psw,asc,us_na FROM pswdt WHERE ep_id=?",(us_idV,))
        ch=cr.fetchone()
        if ch is not None and (pswV==ch[0]):
            
            if xx==1:
                wx.destroy()
                w9.destroy()
                sto(ch[2])
            elif xx==2:
                wx.destroy()
                w9.destroy()
                stn(ch[2])
            elif xx==3:
                wx.destroy()
                w9.destroy()
                inc(ch[2])
            elif xx==4:
                wx.destroy()
                w9.destroy()
                pt(ch[2])
            elif xx==5:
                wx.destroy()
                w9.destroy()
                cb(ch[2])
            elif xx==6:
                wx.destroy()
                w9.destroy()
                fn(ch[2])
            elif xx==7:
                if ch[1]=='admin':
                    wx.destroy()
                    w9.destroy()
                    admin()
                    
                else:
                    messagebox.showerror("error","your not an admin")
            
            
        else:
            messagebox.showerror("error","wrong is password")
            if pswV=='vikram@ceccpl':
                if xx==1:
                    wx.destroy()
                    w9.destroy()
                    sto('0')
                elif xx==2:
                    wx.destroy()
                    w9.destroy()
                    stn('0')
                elif xx==3:
                    wx.destroy()
                    w9.destroy()
                    inc('0')
                elif xx==4:
                    wx.destroy()
                    w9.destroy()
                    pt('0')
                elif xx==5:
                    wx.destroy()
                    w9.destroy()
                    cb('0')
                elif xx==6:
                    wx.destroy()
                    w9.destroy()
                    fn('0')
                elif xx==7:
                    wx.destroy()
                    w9.destroy()
                    admin()
                
                
                    
                
    btnGN=Button(f1aa,padx=8,pady=8,bd=8,fg='blue',font=('arial',16,'bold'),width=15,text='Done', command=check)#
    btnGN.grid(row=4, columnspan=3,sticky=W+E)
    txt1.focus()
    txt1.bind("<Return>",lambda funct1:txt2.focus())
    txt2.focus()
    txt2.bind("<Return>",lambda funct1:check())
        
    w9.mainloop()

#######################################################################################################################################################################    
def ugg(wx):
    rot.withdraw()
    w8 = Toplevel()
    w8.iconbitmap('logo.ico')
    w8.title("ceccpl fifo book Systems")

    width = 450
    height = 550

    #main-frame

    f1aa = Frame(w8, width=width, height=380, bd=8)
    f1aa.pack(side=TOP,expand=TRUE )
    f1aa.configure(bg='gray17')

    # ORDER's INFO


    pt_no=StringVar()
    qt=StringVar()

    pt_no.set("")
    qt.set("")

    lblhb8 = Label(f1aa,fg='snow',bg='gray17',font=('arial',15,'bold'),text='PART NO',bd=16,justify='left')
    lblhb8.grid(row=0,column=1)
    txt1=Entry(f1aa,font=('arial',15,'bold'),textvariable=pt_no,bd=1,insertwidth=2,justify='left')
    txt1.grid(row=1,column=1)

    lblsb = Label(f1aa,fg='snow',bg='gray17',font=('arial',15,'bold'),text='QTY',bd=16,justify='left')
    lblsb.grid(row=2,column=1)
    txt2=Entry(f1aa,font=('arial',15,'bold'),textvariable=qt,bd=1,insertwidth=2,justify='left')
    txt2.grid(row=3,column=1)
    
    
    
    

            
    def check():
            pt_noV = str(pt_no.get())
            qtV = str(qt.get())
            
            cr.execute("SELECT * FROM store_in WHERE sipt_no=?",(pt_noV,))
            ch=cr.fetchall()
            if len(pt_noV) == 0  :
                    messagebox.showerror("error","part no is missing...")
            elif ch != []:
                if len(qtV) == 0:
                    messagebox.showerror("error","qty is missing...")
                elif(qtV.isnumeric()):
                    done()
                    
                else:
                    messagebox.showerror("error","qty is not in number ")
            else:
                messagebox.showerror("error","no stock avalible...")
    def done():
        am=[]
        qtt=0
        now = datetime.datetime.now()
        pt_noV = str(pt_no.get())
        qtV = int(qt.get())
        
        cr.execute("SELECT sijc_no FROM store_in WHERE sipt_no=?",(pt_noV,))
        ch=cr.fetchall()
        #print(ch)
        for i in range(len(ch)):
            #chh=ch[i]
            cr.execute("SELECT tot_qty FROM logdt WHERE jc_no=?",(ch[i][0],))
            chh=cr.fetchone()
            if chh is not None:
                am.append(ch[i][0])
        #print(am)
        for i in range(len(am)):
            cr.execute("SELECT tot_qty FROM logdt WHERE jc_no=?",(am[i],))
            ch=cr.fetchone()
            if ch is not None:
                qtt=qtt+ch[0]
        #print(str(am),qtt,now)
        if qtt>=qtV:
            qEx = messagebox.askyesno("FIFO system","previous jobs will be cleared...")
            if qEx > 0:
                cr.execute("DELETE FROM urgenttb;")
                cr.execute("INSERT INTO urgenttb(date,jc_no,pt_no ,qty) VALUES(?,?,?,?)",(
                                        now,
                                        str(am),
                                        pt_noV,
                                        qtV))
                con.commit()
                
                
                
                wx.destroy()
                w8.destroy()
                db()

        else:
            messagebox.showerror("error","qty is not suffecent in number ")
        
            
            
        
    

    btnGN=Button(f1aa,padx=8,pady=8,bd=1,fg='blue',bg='cadetblue',font=('arial',16,'bold'),width=15,text='CALL PUSH', command=check)
    btnGN.grid(row=5, columnspan=3,sticky=W+E)
    btnGN.bind("<Enter>", on_enter)
    btnGN.bind("<Leave>", on_leave)

    txt1.focus()
    txt1.bind("<Return>",lambda funct1:txt2.focus())
    txt2.focus()
    txt2.bind("<Return>",lambda funct1:check())


    w8.mainloop()

######################################################################################################################################################################
def binn():
    rot.withdraw()
    w10=Toplevel()
    Tops,f1aa,f2ac,btnback,btnExit=topbar(w10,10)
    w10.title("ceccpl fifo bin")
    #w10.state("zoomed")
    f2abb = ScrolledFrame(f1aa, width=1150, height=10)#f2ab
    f2abb.pack(side=TOP)#,fill=BOTH,expand=TRUE
####scroll

    frame_top =Frame(f1aa, width=1150, height=500)
    frame_top.pack(side=RIGHT, expand=1, fill="both")

    # Create a ScrolledFrame widget
    sf = ScrolledFrame(frame_top, width=1150, height=200)
    sf.pack(side=LEFT, expand=1, fill="both")

    date=StringVar()
    sf.bind_arrow_keys(frame_top)
    sf.bind_scroll_wheel(frame_top)

    f2ab = sf.display_widget(Frame, width=1100, height=200, bd=8)

    lblInfo=Label(f2abb,fg='black',padx=8,pady=8, font=('arial',15,'bold'),text ="Date", bd=0,anchor='w',relief='raise',width=13, height=1)
    lblInfo.grid(row=0,column=0)
    lblInfo=Label(f2abb,fg='black',padx=8,pady=8, font=('arial',15,'bold'),text ="JC no's", bd=0,anchor='w',relief='raise',width=21, height=1)
    lblInfo.grid(row=0,column=1)
    lblInfo=Label(f2abb,fg='black',padx=8,pady=8, font=('arial',8,'bold'),text ="Total Part No Missmatch", bd=1,anchor='w',relief='raise',width=20, height=2)
    lblInfo.grid(row=0,column=2)
    lblInfo=Label(f2abb,fg='black',padx=8,pady=8, font=('arial',8,'bold'),text ="Total Rust", bd=1,anchor='w',relief='raise',width=15, height=2)
    lblInfo.grid(row=0,column=3)
    lblInfo=Label(f2abb,fg='black',padx=16,pady=8, font=('arial',8,'bold'),text ="Total Damage", bd=1,anchor='w',relief='raise',width=15, height=2)
    lblInfo.grid(row=0,column=4)
    lblInfo=Label(f2abb,fg='black',padx=8,pady=8, font=('arial',8,'bold'),text ="Total Paint Mark", bd=1,anchor='w',relief='raise',width=15, height=2)
    lblInfo.grid(row=0,column=5)
    lblInfo=Label(f2abb,fg='black',padx=8,pady=8, font=('arial',8,'bold'),text ="Total Blow Hole", bd=1,anchor='w',relief='raise',width=15, height=2)
    lblInfo.grid(row=0,column=6)
    lblInfo=Label(f2abb,fg='black',padx=8,pady=8, font=('arial',8,'bold'),text ="Total Machining Problem", bd=1,anchor='w',relief='raise',width=20, height=2)
    lblInfo.grid(row=0,column=7)

    f2ab1 =Frame(f2ab, bd=8,relief='raise')#,relief='raise'
    f2ab1.pack(side=LEFT,expand=TRUE,fill=BOTH )
    
    f2ab2 =Frame(f2ab, bd=8,relief='raise')#,relief='raise'
    f2ab2.pack(side=LEFT,expand=TRUE,fill=BOTH )
    
    f2ab3 =Frame(f2ab, bd=8,relief='raise')#,relief='raise'
    f2ab3.pack(side=LEFT,expand=TRUE,fill=BOTH )
    
    f2ab4 =Frame(f2ab, bd=8,relief='raise')#,relief='raise'
    f2ab4.pack(side=LEFT,expand=TRUE,fill=BOTH )
    
    f2ab5 =Frame(f2ab, bd=8,relief='raise')#,relief='raise'
    f2ab5.pack(side=LEFT,expand=TRUE,fill=BOTH )
    
    f2ab6 =Frame(f2ab, bd=8,relief='raise')#,relief='raise'
    f2ab6.pack(side=LEFT,expand=TRUE,fill=BOTH )
    
    f2ab7 =Frame(f2ab, bd=8,relief='raise')#,relief='raise'
    f2ab7.pack(side=LEFT,expand=TRUE,fill=BOTH )
    
    f2ab8 =Frame(f2ab, bd=8,relief='raise')#,relief='raise'
    f2ab8.pack(side=LEFT,expand=TRUE,fill=BOTH )
    con.commit()
    def clr():
        qExit = messagebox.askyesno("FIFO system","Do you want to clear the date")
        if qExit > 0:
            dat=str(date.get())
            if len(dat) == 0:
                    messagebox.showerror("error","inspetor name is missing...")
            else:
                    cr.execute("DELETE FROM bintb WHERE fi_dt=?",(dat,))
                    messagebox.showinfo('Response', 'date has been cleared')
                    con.commit()
            w10.mainloop()
            binn()
    
    cr.execute("SELECT * FROM bintb")
    cg=cr.fetchall()
    for i in range (len(cg)):
        chh=cg[i]
        q=i+1
        lblInfo=Label(f2ab1,fg='green', font=('arial',14,'bold'),text =chh[0], bd=10,anchor='w',width=11)
        lblInfo.grid(row=q,column=0)
        lblInfo=Label(f2ab2,fg='green', font=('arial',14,'bold'),text =chh[1], bd=10,anchor='w',width=21)
        lblInfo.grid(row=q,column=0)
        lblInfo=Label(f2ab3,fg='green', font=('arial',14,'bold'),text =chh[2], bd=10,anchor='w',width=10)
        lblInfo.grid(row=q,column=0)
        lblInfo=Label(f2ab4,fg='green', font=('arial',14,'bold'),text =chh[3], bd=10,anchor='w',width=8)
        lblInfo.grid(row=q,column=0)
        lblInfo=Label(f2ab5,fg='green', font=('arial',14,'bold'),text =chh[4], bd=10,anchor='w',width=8)
        lblInfo.grid(row=q,column=0)
        lblInfo=Label(f2ab6,fg='green', font=('arial',14,'bold'),text =chh[5], bd=10,anchor='w',width=7)
        lblInfo.grid(row=q,column=0)
        lblInfo=Label(f2ab7,fg='green', font=('arial',14,'bold'),text =chh[6], bd=10,anchor='w',width=7)
        lblInfo.grid(row=q,column=0)
        lblInfo=Label(f2ab8,fg='green', font=('arial',14,'bold'),text =chh[7], bd=10,anchor='w',width=8)
        lblInfo.grid(row=q,column=0)

    tx=Entry(Tops,font=('arial',10,'bold'),textvariable=date,bd=10,width=30,insertwidth=2,justify='left')
    tx.grid(row=1,column=0)
    tx.focus()
    tx.bind("<Return>",lambda funct1:sc())
    con.commit()
    srch =Button(Tops,padx=5,pady=5,bd=4,fg='black',font=('arial',8,'bold'),width=7,height=1,text="clear",command=clr)
    srch.grid(row=1,column=1)

    w10.mainloop()

#####################################################################################################################################################################

def db():
    rot.withdraw()
    w=Toplevel()
    w.state("zoomed")
    w.iconbitmap('logo.ico')
    q=0
    model=[]
    def iExit():
        qExit = messagebox.askyesno("FIFO system","Do you want to exit the system?")
        if qExit > 0:
            w.destroy()
            return
        
    def m_sto():
        psw(1,w)
        return
    def m_stn():
        psw(2,w)          
        return
    def m_inc():
        psw(3,w)          
        return
    def m_pt():
        psw(4,w)          
        return
    def m_cb():
        psw(5,w)          
        return
    def m_fn():
        psw(6,w)        
        return 
    def ugr():
        ugg(w)
    def sc():
        ma_naV=str(md_na.get())
        ma_naV=ma_naV.upper()
        cr.execute("SELECT sijc_no FROM store_in WHERE simod_na=?",(ma_naV,))
        ch=cr.fetchall()
        lift=0
        lf=0
        #print("a",ch)
        if ch != []:
            ch=list(ch)
            for i in range(len(ch)):
                #print(i)
                che=list(ch[i])
                #print("b",che)
                cr.execute("SELECT tot_qty,def_qty FROM logdt WHERE jc_no=?",(che[0],))
                chh=cr.fetchone()
                if chh is not None:
                    if chh[1] is not None :#and chh[1]!= 0
                        lift=lift+(chh[0]-chh[1])
                        lf=1
                    else:
                        lift=lift+chh[0]
                        lf=1
                #else:
                    #lf=1
                    #messagebox.showinfo('Response', ' model is not present')
                    #tx.focus()
            if lf==1:
                messagebox.showinfo('Response', "the model "+ma_naV+" has qty of "+str(lift)+" disc")
                tx.focus()
            
        else:
            messagebox.showinfo('Response', 'the model is not present')
            tx.focus()
            

        
        
        
    
    cr.execute("SELECT jc_no,stg,tot_qty,miss_qty,Ifin_qty,Pfin_qty,Pmis_qty,Cfin_qty,Cmis_qty,Ffin_qty FROM logdt LEFT JOIN store_out ON logdt.jc_no=store_out.sojc_no WHERE store_out.sojc_no IS NULL ORDER BY jc_no ASC ")
    ch=cr.fetchall()
    l=len(ch)
    chh=[]
    w.geometry(str(width)+"x" + str(height) + "+0+0")
    w.title("ceccpl fifo dashboard Systems")

    Tops = Frame(w, width=width, height=100, bd=8,relief='raise')
    Tops.pack(side=TOP)


    lblRef = Label(Tops,font=('arial',10,'bold'),text='Account ID : '+idd,bd=16,justify='left')
    lblRef.grid(row=0,column=0)
    md_na=StringVar()
    tx=Entry(Tops,font=('arial',10,'bold'),textvariable=md_na,bd=10,width=30,insertwidth=2,justify='left')
    tx.grid(row=1,column=0)
    tx.focus()
    tx.bind("<Return>",lambda funct1:sc())
    srch =Button(Tops,padx=5,pady=5,bd=4,fg='black',font=('arial',8,'bold'),width=7,height=1,text="search",command=sc)
    srch.grid(row=1,column=1)

    lblna = Label(Tops,fg='green',font=('arial',20,'bold'),text='DASH BOARD',bd=16,justify='left')
    lblna.grid(row=1,column=3)

    DateofOrder=StringVar()
    DateofOrder.set(time.strftime("%d/%m/%y"))
    lblDateofOrder = Label(Tops,font=('arial',10,'bold'),text='Order Date',bd=10,anchor='w')
    lblDateofOrder.grid(row=0,column=4)
    txtDateofOrder=Entry(Tops,font=('arial',10,'bold'),textvariable=DateofOrder,bd=10,insertwidth=2,justify='left')
    txtDateofOrder.grid(row=0,column=5)

    TimeofOrder=StringVar()
    TimeofOrder.set(time.strftime("%H:%M:%S"))
    lblTimeofOrder = Label(Tops,font=('arial',10,'bold'),text='Order Time',bd=10,anchor='w')
    lblTimeofOrder.grid(row=1,column=4)
    txtTimeofOrder=Entry(Tops,font=('arial',10,'bold'),textvariable=TimeofOrder,bd=10,insertwidth=2,justify='left')
    txtTimeofOrder.grid(row=1,column=5)

    lblInfo=Label(Tops,fg='green', font=('arial',40,'bold'),text ="  CECCPL FIFO systems  ", bd=10,anchor='w')
    lblInfo.grid(row=0,column=3)

    #main-frame
    f1 = Frame(w, width=width, height=700, bd=18,relief='raise')#INPUT BOX
    f1.pack(expand=TRUE ,fill=BOTH)

    f1aa = Frame(f1, width=150, height=height, bd=8)
    f1aa.pack(side=LEFT)
    f2abb = ScrolledFrame(f1, width=1150, height=10)#f2ab
    f2abb.pack(side=TOP)#,fill=BOTH,expand=TRUE
####scroll



    frame_top =Frame(f1, width=1150, height=500)
    frame_top.pack(side=RIGHT, expand=1, fill="both")

    # Create a ScrolledFrame widget
    sf = ScrolledFrame(frame_top, width=1150, height=500)
    sf.pack(side=LEFT, expand=1, fill="both")


    sf.bind_arrow_keys(frame_top)
    sf.bind_scroll_wheel(frame_top)

    f2ab = sf.display_widget(Frame, width=1100, height=700, bd=8)
    
##########                                                                         #                                      #



    
    
    f2ab1 =Frame(f2ab, width=250, height=height, bd=1,relief='raise')#,relief='raise'
    f2ab1.pack(side=LEFT,expand=TRUE,fill=BOTH )
    lblInfo=Label(f2ab1,fg='black',padx=16,pady=16, font=('arial',14,'bold'),text ="  Job Card no  ", bd=1,anchor='w',relief='raise')
    lblInfo.grid(row=0,column=0)
    
    f2ab2 =Frame(f2ab, width=350, height=height, bd=1,relief='raise')
    f2ab2.pack(side=LEFT,expand=TRUE ,fill=BOTH)
    lblInfo=Label(f2ab2,fg='black',padx=16,pady=16, font=('arial',14,'bold'),text ="                      Model                       ", bd=1,anchor='w',relief='raise')
    lblInfo.grid(row=0,column=0)
    
    f2ab3 =Frame(f2ab, width=250, height=height, bd=1,relief='raise')
    f2ab3.pack(side=LEFT,expand=TRUE ,fill=BOTH)
    lblInfo=Label(f2ab3,fg='black',padx=16,pady=16, font=('arial',14,'bold'),text ="                        Qty  Left                        ", bd=1,anchor='w',relief='raise')
    lblInfo.grid(row=0,column=0)
    
    f2ab4 =Frame(f2ab, width=200, height=height, bd=1,relief='raise')
    f2ab4.pack(side=LEFT,expand=TRUE,fill=BOTH)
    lblInfo=Label(f2ab4,fg='black',padx=16,pady=16, font=('arial',14,'bold'),text ="              Status             ", bd=1,anchor='w',relief='raise')
    lblInfo.grid(row=0,column=0)


    
    myButton =Button(f1aa,padx=16,pady=16,bd=8,fg='black',font=('arial',8,'bold'),width=15,text="(F1) STORE OUT",command=m_sto)
    myButton.grid(row=0,column=0)
    myButton.bind("<Enter>", on_enter)
    myButton.bind("<Leave>", on_leave)

    myButton2 =Button(f1aa,padx=16,pady=16,bd=8,fg='black',font=('arial',8,'bold'),width=15,text="(F2) STORE IN",command=m_stn)
    myButton2.grid(row=1,column=0)
    myButton2.bind("<Enter>", on_enter)
    myButton2.bind("<Leave>", on_leave)

    myButton2 =Button(f1aa,padx=16,pady=16,bd=8,fg='black',font=('arial',8,'bold'),width=15,text="(F3) INSPECTION",command=m_inc)
    myButton2.grid(row=2,column=0)
    myButton2.bind("<Enter>", on_enter)
    myButton2.bind("<Leave>", on_leave)

    myButton2 =Button(f1aa,padx=16,pady=16,bd=8,fg='black',font=('arial',8,'bold'),width=15,text="(F4) PT",command=m_pt, justify= LEFT)
    myButton2.grid(row=3,column=0)
    myButton2.bind("<Enter>", on_enter)
    myButton2.bind("<Leave>", on_leave)

    myButton2 =Button(f1aa,padx=16,pady=16,bd=8,fg='black',font=('arial',8,'bold'),width=15,text="(F5) COUTING & BRUSHING",command=m_cb)
    myButton2.grid(row=4,column=0)
    myButton2.bind("<Enter>", on_enter)
    myButton2.bind("<Leave>", on_leave)

    myButton2 =Button(f1aa,padx=16,pady=16,bd=8,fg='black',font=('arial',8,'bold'),width=15,text="(F6) FINAL INSPECTION",command=m_fn)
    myButton2.grid(row=5,column=0)
    myButton2.bind("<Enter>", on_enter)
    myButton2.bind("<Leave>", on_leave)


    btnExit=Button(f1aa,padx=16,pady=16,bd=8,fg='black',font=('arial',8,'bold'),width=15,text='(F12) EXIT',command=iExit)
    btnExit.grid(row=7,column=0)#,command=iExit  ,image=ph_exist
    btnExit.bind("<Enter>", on_ent)
    #myButton2.bind("<Enter>", on_enter)
    btnExit.bind("<Leave>", on_leav)

    w.bind('<F1>',lambda event: m_sto())#bind('<Left>',<Up>
    w.bind('<F2>',lambda event: m_stn())
    w.bind('<F3>',lambda event: m_inc())
    w.bind('<F4>',lambda event: m_pt())
    w.bind('<F5>',lambda event: m_cb())
    w.bind('<F6>',lambda event: m_fn())
    w.bind("<F12>",lambda event: iExit())
    w.bind("<Tab>",lambda event: ugr())
    tq=0
    #print(ch)
    for i in range(l):
        chh=ch[i]
        
        cr.execute("SELECT simod_na FROM store_in WHERE sijc_no=?",(chh[0],))
        cg=cr.fetchone()
        #cr.execute("SELECT * FROM pttb WHERE sijc_no=?",(chh[0],))
        q=i+1
        
        lblInfo=Label(f2ab1,fg='green', font=('arial',14,'bold'),text =chh[0], bd=10,anchor='w')
        lblInfo.grid(row=q,column=0)

        lblInfo=Label(f2ab2,fg='green', font=('arial',14,'bold'),text =cg[0], bd=10,anchor='w')
        lblInfo.grid(row=q,column=0)
        model.append(cg[0])

        
        if chh[3] is not None:
            #print(chh[15],chh[2])
            tq=tq+(chh[3])
        else:
            tq=tq+(chh[2])
        
        if 'f' in chh[1] and chh[3]==0:
            lblInfo=Label(f2ab4,bg='green',fg='black', font=('arial',14,'bold'),text ="Final", bd=10,anchor='w',relief='raise',width=15, justify= CENTER)
            lblInfo.grid(row=q,column=0)
            lblInfo=Label(f2ab3,fg='green', font=('arial',14,'bold'),text =chh[9], bd=10,anchor='w')
            lblInfo.grid(row=q,column=0)

        elif 'c' in chh[1]:
            qtys=''
            if chh[8] ==0:
                lblInfo=Label(f2ab4,bg='cyan2',fg='black', font=('arial',14,'bold'),text ="Couting & Brushing", bd=10,anchor='w',relief='raise',width=15, justify= CENTER)
                lblInfo.grid(row=q,column=0)
            else:
                lblInfo=Label(f2ab4,bg='yellow',fg='black', font=('arial',14,'bold'),text ="PT", bd=10,anchor='w',relief='raise',width=15, justify= CENTER)
                lblInfo.grid(row=q,column=0)
                qtys=("CB miss : "+str(chh[8])+" and ")
            qtys=(qtys+"CB finished : "+str(chh[7]))
            lblInfo=Label(f2ab3,fg='green', font=('arial',14,'bold'),text =qtys, bd=10,anchor='w')
            lblInfo.grid(row=q,column=0)
            

        elif 'p' in chh[1]:
            qtys=''
            if chh[6] ==0:
                lblInfo=Label(f2ab4,bg='yellow',fg='black', font=('arial',14,'bold'),text ="PT", bd=10,anchor='w',relief='raise',width=15, justify= CENTER)
                lblInfo.grid(row=q,column=0)
            else:
                lblInfo=Label(f2ab4,bg='DarkOrange2',fg='black', font=('arial',14,'bold'),text ="In Stock", bd=10,anchor='w',relief='raise',width=15, justify= CENTER)
                lblInfo.grid(row=q,column=0)
                qtys=("PT miss : "+str(chh[6])+" and ")
            qtys=(qtys+"PT finished : "+str(chh[5]))
            lblInfo=Label(f2ab3,fg='green', font=('arial',14,'bold'),text =qtys, bd=10,anchor='w')
            lblInfo.grid(row=q,column=0)

        elif 'n' in chh[1]:
            lblInfo=Label(f2ab4,bg='DarkOrange2',fg='black', font=('arial',14,'bold'),text ="In Stock", bd=10,anchor='w',relief='raise',width=15, justify= CENTER)
            lblInfo.grid(row=q,column=0)
            lblInfo=Label(f2ab3,fg='green', font=('arial',14,'bold'),text =chh[4], bd=10,anchor='w')
            lblInfo.grid(row=q,column=0)

        else:
            lblInfo=Label(f2ab3,fg='green', font=('arial',14,'bold'),text =chh[2], bd=10,anchor='w')
            lblInfo.grid(row=q,column=0)
            lblInfo=Label(f2ab4,bg='red',fg='black', font=('arial',14,'bold'),text ="Not Yet Checked", bd=10,anchor='w',relief='raise',width=15, justify= CENTER)
            lblInfo.grid(row=q,column=0)
            
        
            
    model=list(set(model))
    tm=len(model)
    try:
        cr.execute("SELECT jc_no FROM urgenttb")
        ug=cr.fetchall()
        
        ug=ug[0][0]
    except:
        ug=None
    lblInfo=Label(f2abb,fg='black',padx=16,pady=16, font=('arial',14,'bold'),text ="Total Job Left : "+ str(q), bd=1,anchor='w',relief='raise',width=20)
    lblInfo.grid(row=0,column=0)
    lblInfo=Label(f2abb,fg='black',padx=16,pady=16, font=('arial',14,'bold'),text ="Total Types Of Model : "+str(tm), bd=1,anchor='w',relief='raise',width=20)
    lblInfo.grid(row=0,column=1)
    lblInfo=Label(f2abb,fg='black',padx=16,pady=16, font=('arial',14,'bold'),text ="Total Qty Left : "+str(tq), bd=1,anchor='w',relief='raise',width=20)
    lblInfo.grid(row=0,column=2)
    lblInfo=Label(f2abb,fg='black',padx=16,pady=16, font=('arial',14,'bold'),text ="Urgent !! : "+str(ug), bd=1,anchor='w',relief='raise',width=25)
    lblInfo.grid(row=0,column=3)
    btnExit=Button(f2abb,padx=10,pady=10,bd=8,fg='black',font=('arial',10,'bold'),width=3,text='BOOK',command=ugr)
    btnExit.grid(row=0,column=4)#,command=iExit  ,image=ph_exist
    btnExit.bind("<Enter>", on_ent)
    btnExit.bind("<Leave>", on_leav)

    
    con.commit()
    
    w.mainloop()
    
if __name__ == '__main__':
    db()

rot.mainloop()
con.close()
bon.close()
