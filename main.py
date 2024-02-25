'''
Frame為框架 LabelFrame為框架的延伸 可圍住其子元件 
LabelFrame(父框架,屬性)

'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import function as fn
import tkinter as tk
from tkinter import messagebox
from mimagame import mg
#import ttk



root = tk.Tk()
root.title('TKU Bank')
root.geometry('800x600')
mainframe = tk.Frame(root).pack()


  

longstr="密碼是由4個不重複數字組合而成\n玩家每次猜題會得到提示\nA的代表猜中數字且數字在正確位置        \
            \nB代表猜中數字但數字不在正確位置\nEX:答案為1234 若玩家猜1248 則得到1A2B"
anslist=['#','#','#','#']                     
times=5
loginfail=dict()

##############
def button3tikuan():
    loginframe.grid_remove() #grid_remove()為隱藏 destroy為直接刪除
    cunkuanframe.grid_remove()
    yueframe.grid_remove()
    tikuanframe.grid()
    
    tikuanmoney.set(0)
    


def button4cunkuan():
    tikuanframe.grid_remove()
    loginframe.grid_remove() #grid_remove()為隱藏 destroy為直接刪除
    yueframe.grid_remove()
    cunkuanframe.grid()
    
    cunkuanmoney.set(0)
    
def button5yue():
    tikuanframe.grid_remove()
    loginframe.grid_remove() #grid_remove()為隱藏 destroy為直接刪除
    cunkuanframe.grid_remove()
    yueframe.grid()
    
    zhangstr = account_string.get()
    try:
        yuenow.set(fn.chayue(zhangstr))
    except:
        pass
    
    
def button6xingzhang():
    functionbutton6.config(state='disabled')
    functionbutton7.config(state='active')
    accountentry.config(state='disabled')
    passwdentry.config(state='disabled')
    loginbutton.config(state='disabled')
    label1_entry.config(state='normal')
    label2_entry.config(state='normal')
    label3_entry.config(state='normal')
    label4_entry.config(state='normal')
    label5_entry.config(state='normal')
    label6_entry.config(state='normal')
    label7_entry.config(state='normal')
    label8_entry.config(state='normal')
    label9_entry.config(state='normal')
    message_cheak.config(state='normal')
    
def button7back():  
    if messagebox.askokcancel('Message','確定返回登入?\n(右邊輸入內容將重製)') == True:
        functionbutton6.config(state='active')
        functionbutton7.config(state='disabled')
        accountentry.config(state='normal')
        passwdentry.config(state='normal')
        loginbutton.config(state='active')
        label1_var.set("")
        label2_var.set("")
        label3_var.set("")
        label4_var.set("")
        label5_var.set("")
        label6_var.set("")
        label7_var.set("")
        label8_var.set("")
        label9_var.set("")
        label1_entry.config(state='disabled')
        label2_entry.config(state='disabled')
        label3_entry.config(state='disabled')
        label4_entry.config(state='disabled')
        label5_entry.config(state='disabled')
        label6_entry.config(state='disabled')
        label7_entry.config(state='disabled')
        label8_entry.config(state='disabled')
        label9_entry.config(state='disabled')
        message_cheak.config(state='disabled')
    else:
        pass

def button8dengchu():
    if messagebox.askokcancel('Message','確定要登出嗎?\n(將返回登入介面)') == True:
        account_string.set("")
        passwd_string.set("")
        functionbutton2.config(state='disabled')
        functionbutton3.config(state='disabled')
        functionbutton4.config(state='disabled')
        functionbutton5.config(state='disabled')
        functionbutton6.config(state='active')
        functionbutton7.config(state='disabled')
        functionbutton8.config(state='disabled')
        yueframe.grid_remove()
        tikuanframe.grid_remove()
        cunkuanframe.grid_remove()
        loginframe.grid()
    else:
        pass
def minigame():
    yon=messagebox.askyesno("Warning","參加此遊戲需支付%d元\n五次內成功猜出答案可獲得獎金%d元"%(1000,10000))  #參加費&獎金
    if yon:
        root.state("icon")
        
        zhang = account_string.get()
        try:
            fn.tikuan(zhang,1000)
            button5yue()
            messagebox.showinfo("遊戲說明",longstr) 
            a = mg()
            if a == True:
                fn.cunkuan(zhang,10000)
                button5yue()
        except Exception as err:
            messagebox.showinfo('Message',err)
            
def test():
    root.destroy()

def check_login():
    
    import sqlite3

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    zhang = account_string.get()
    mi = passwd_string.get()
    SQL="SELECT Suoding from BANK WHERE Email = %r" %(zhang)
    c.execute(SQL)
    suo = c.fetchone()
    global loginfail
    print(suo)
    if fn.searchzhang(zhang) == True:
        
        templg=fn.searchmi(zhang,mi)
        
        if type(suo) == tuple:
            if suo[0] == 1:
                messagebox.showinfo('Message','此帳號已被鎖定,必須本人親自到銀行辦理解鎖')
                templg=False
        

        
        if templg == True:
            functionbutton2.config(state='active')
            functionbutton3.config(state='active')
            functionbutton4.config(state='active')
            functionbutton5.config(state='active')
            functionbutton6.config(state='disabled')
            functionbutton7.config(state='disabled')
            functionbutton8.config(state='active')
            #showimg.destroy()
            messagebox.showinfo('Message', '登入成功')
            
            button5yue()
        else:
            if loginfail.__contains__(zhang):
                loginfail[zhang]+=1
            else:
                loginfail[zhang]=1
            
            if suo[0]!=1 and loginfail[zhang]==5:
                messagebox.showinfo('Message','aa此帳號已被鎖定,必須本人親自到銀行辦理解鎖')
                SQL="UPDATE BANK set Suoding = 1 WHERE Email = %r" %(zhang)
                c.execute(SQL)

            
            if suo[0]!=1 and loginfail[zhang]<5:
                messagebox.showinfo('Message',
                                    "密碼錯誤，剩餘%d次機會"%(5-loginfail[zhang]))
            
            #loginfail exist ==> loginfail key+1  if not exist create loginfail default=1
            #if loginfail key=5 suoding=1
    

    else:
        messagebox.showinfo('Message',
            "帳號錯誤或無此帳號")
        
    conn.commit()
    conn.close()

def check_tikuan():
    zhang = account_string.get()
    money = tikuanmoney.get()
    try:
        newmoney = fn.tikuan(zhang,money)
        messagebox.showinfo('Message',"成功提出%d元，帳戶餘額:%d"%(money,newmoney))
    except Exception as err:
        messagebox.showinfo('Message',err)

def cheak_cunkuan():
    zhang = account_string.get()
    money = cunkuanmoney.get()
    try:
        newmoney = fn.cunkuan(zhang,money)
        messagebox.showinfo('Message',"成功存入%d元，帳戶餘額:%d"%(money,newmoney))
    except Exception as err:
        messagebox.showinfo('Message',err)

def message_cheak_button():
    
    var1=label1_var.get()
    var2=label2_var.get()
    var3=label3_var.get()
    var4=label4_var.get()
    var5=label5_var.get()
    var6=label6_var.get()
    var7=label7_var.get()
    var8=label8_var.get()
    var9=label9_var.get()

    errstr = ''
    errlist = []
    if (var1 and var2 and var3 and var4 and var5 and var6 and var7 and var8 and var9) =="":
        messagebox.showinfo('Message','請填寫完所有資料')
    else:
        v1v8panding = fn.Panding(var1,var8)
        
        try:
            v1v8panding.pandingID()
        except Exception as err1:
            errlist.append(err1)
            
        try:
            v1v8panding.pandingDianhua()
        except Exception as err2:
            errlist.append(err2)
        
        try:
            fn.zhang(var9)
        except Exception as err3:
            errlist.append(err3)
        
        try:
            fn.mi(var2)
        except Exception as err4:
            errlist.append(err4)

        if len(errlist) != 0:
            for i in range(len(errlist)):
                errstr += str(errlist[i])+'\n'
            messagebox.showinfo('Message',errstr)
        else:
            import sqlite3
            conn = sqlite3.connect('database.db') #連接or創立一個資料庫
            c = conn.cursor()
            
            
            tempstr="INSERT INTO BANK VALUES(%r,%r,%r,%r,%r,%r,%r,%r,'臺灣',0,%r,0)"%(var1,var2,var3,var4,var5,var6,var7,var8,var9)
            c.execute(tempstr)
            
            messagebox.showinfo('Message','註冊成功')
            
            conn.commit()
            
            conn.close()
            
            functionbutton6.config(state='active')
            functionbutton7.config(state='disabled')
            accountentry.config(state='normal')
            passwdentry.config(state='normal')
            loginbutton.config(state='active')
            label1_var.set("")
            label2_var.set("")
            label3_var.set("")
            label4_var.set("")
            label5_var.set("")
            label6_var.set("")
            label7_var.set("")
            label8_var.set("")
            label9_var.set("")
            label1_entry.config(state='disabled')
            label2_entry.config(state='disabled')
            label3_entry.config(state='disabled')
            label4_entry.config(state='disabled')
            label5_entry.config(state='disabled')
            label6_entry.config(state='disabled')
            label7_entry.config(state='disabled')
            label8_entry.config(state='disabled')
            label9_entry.config(state='disabled')
            message_cheak.config(state='disabled')
    
    
    
    
    
    
##############
leftframe = tk.LabelFrame(mainframe,text="Left")#.grid(row=0, column=1)
leftframe.pack(side='left',
    padx=10, ipadx=0, pady=10, ipady=10, 
    fill="y", anchor=tk.E)
#############
loginframe = tk.LabelFrame(leftframe, 
            text="Login")#.grid(row=0, column=1)
loginframe.grid(row=0, column=0, #side='left',
    padx=10, ipadx=5, pady=10, ipady=10)
functionframe = tk.LabelFrame(leftframe, 
            text="Functions")#.grid(row=0, column=1)
functionframe.grid(row=1, column=0,columnspan=1,
    padx=10, ipadx=1, pady=10, ipady=10)#, sticky=tk.E+tk.W)
##  #########
messageframe = tk.LabelFrame(mainframe, 
            text="Message")#.grid(row=0, column=1)
messageframe.pack(side='right',
    padx=10, ipadx=10, pady=10, ipady=10, expand='yes', fill='both')
    #sticky=tk.W+tk.E+tk.N+tk.S)
    #fill="both", expand="yes")

###########################################################
tikuanmoney = tk.IntVar()
tikuanframe = tk.LabelFrame(leftframe, text ="提款視窗")
tikuanframe.grid(row=0, column=0, #side='left',
                 padx=10, ipadx=0, pady=10, ipady=10)

tikuanlabel = tk.Label(tikuanframe, 
                  text="請在下方輸入提款金額").grid(row=0, column=0, 
padx=10, ipadx=0, pady=10, ipady=10)
tikuanentry = tk.Entry(tikuanframe, textvariable=tikuanmoney,
                        font=("Helvetica",20),
                       width=10).grid(row=1, column=0, 
                      padx=11, ipadx=13, pady=6, ipady=6)


tikuanbutton= tk.Button(tikuanframe, command=check_tikuan,
                  text="確認取出").grid(row=2, column=0,
                           padx=10, ipadx=10, pady=10, ipady=10, sticky=tk.E+tk.W)
    
tikuanframe.grid_remove()
    
"""-----------------上面是button3按下後會顯現的東西---------------------"""
cunkuanmoney = tk.IntVar()
cunkuanframe = tk.LabelFrame(leftframe, text ="存款視窗")
cunkuanframe.grid(row=0, column=0, #side='left',
                 padx=10, ipadx=0, pady=10, ipady=10)

cunkuanlabel = tk.Label(cunkuanframe, 
                  text="請在下方輸入存款金額").grid(row=0, column=0, 
                                   padx=10, ipadx=0, pady=10, ipady=10)
cunkuanentry = tk.Entry(cunkuanframe, textvariable=cunkuanmoney,font=("Helvetica",20),
                       width=10).grid(row=1, column=0, 
                      padx=11, ipadx=13, pady=6, ipady=6)

cunkuanbutton= tk.Button(cunkuanframe, command=cheak_cunkuan,
                  text="確定存入").grid(row=2, column=0,
                           padx=10, ipadx=10, pady=10, ipady=10, sticky=tk.E+tk.W)
    
cunkuanframe.grid_remove()

"""-----------------上面是button4按下後會顯現的東西---------------------"""
yuenow = tk.IntVar()
yuenow.set(0)
yueframe = tk.LabelFrame(leftframe, text ="餘額視窗")
yueframe.grid(row=0, column=0, #side='left',
                 padx=10, ipadx=5, pady=10, ipady=10)


yuelabel = tk.Label(yueframe, 
                  text="下方為您的餘額").grid(row=0, column=0, 
                                padx=10, ipadx=10, pady=10, ipady=10)
yuemoney = tk.Label(yueframe, textvariable = yuenow ,wraplength = 162,
                    font=("Helvetica",25),width = 8, height = 2).grid(row = 1,column = 0, 
                   padx=11, ipadx=6, pady=11, ipady=11)

yueframe.grid_remove()

"""-----------------上面是button5按下後會顯現的東西---------------------"""




account_string = tk.StringVar()
passwd_string = tk.StringVar()


accountlabel = tk.Label(loginframe, 
                      text="帳號").grid(row=0, column=0, 
    padx=10, ipadx=10, pady=10, ipady=10)
accountentry = tk.Entry(loginframe, textvariable=account_string,
                  width=10)
accountentry.grid(row=0, column=1, 
    padx=10, ipadx=10, pady=10, ipady=10)


passwdlabel = tk.Label(loginframe, 
                      text="密碼").grid(row=1, column=0, 
    padx=10, ipadx=12, pady=10, ipady=10)
passwdentry = tk.Entry(loginframe, width=10, textvariable=passwd_string,
          show='*')
passwdentry.grid(row=1, column=1, 
    padx=10, ipadx=12, pady=10, ipady=10)



loginbutton= tk.Button(loginframe, command=check_login,
                      text="登入",font=("Terminal",11))
loginbutton.grid(row=2, column=0, columnspan=2,
    padx=10, ipadx=10, pady=11, ipady=11, sticky=tk.E+tk.W)


"""----------------------------------------------------------"""
    


# ###############
functionbutton1 = tk.Button(functionframe, state='normal',
                      text="離開", command=test, height = 0 , width = 6)
functionbutton1.grid(row=0, column=0,
    padx=13, ipadx=10, pady=10, ipady=10, sticky=tk.E+tk.W)
functionbutton2 = tk.Button(functionframe, state='disabled',
                      text="1A2B", command =minigame , height = 0 , width = 6)
functionbutton2.grid(row=1, column=0,
    padx=13, ipadx=10, pady=10, ipady=10)
functionbutton3 = tk.Button(functionframe, state='disabled',
                      text="提款" , height = 0 , width = 6 ,command = button3tikuan)
functionbutton3.grid(row=2, column=0,
    padx=13, ipadx=10, pady=10, ipady=10, )
functionbutton4 = tk.Button(functionframe, state='disabled',
                      text="存款", height = 0 , width = 6, command = button4cunkuan)
functionbutton4.grid(row=3, column=0,
    padx=13, ipadx=10, pady=10, ipady=10)

functionbutton5 = tk.Button(functionframe, state='disabled',
                      text="查詢餘額", height = 0 , width = 6,command = button5yue)
functionbutton5.grid(row=0, column=1,
    padx=13, ipadx=10, pady=10, ipady=10)


functionbutton6 = tk.Button(functionframe, state='active',
                      text="新建帳號", height = 0 , width = 6,command = button6xingzhang)
functionbutton6.grid(row=1, column=1,
    padx=13, ipadx=10, pady=10, ipady=10)


functionbutton7 = tk.Button(functionframe, state='disabled',command = button7back,
                      text="返回登入",height = 0 , width = 6)
functionbutton7.grid(row=2, column=1,
    padx=13, ipadx=10, pady=10, ipady=10)


functionbutton8 = tk.Button(functionframe, state='disabled',
                      text="登出", height = 0 , width = 6 , command = button8dengchu )
functionbutton8.grid(row=3, column=1,
    padx=13, ipadx=10, pady=10, ipady=10)
# functionbutton5 = tk.Button(functionframe, state='disabled',
#                       text="Button5").grid(row=4, column=0,
#     padx=10, ipadx=10, pady=10, ipady=10, sticky=tk.E)
###########                           
#img = tk.PhotoImage(file='tku_logo.gif')
#showimg = tk.Label(messageframe, image=img)
#showimg.pack()
################

label1_var = tk.StringVar()
label2_var = tk.StringVar()
label3_var = tk.StringVar()
label4_var = tk.StringVar()
label5_var = tk.StringVar()
label6_var = tk.StringVar()
label7_var = tk.StringVar()
label8_var = tk.StringVar()
label9_var = tk.StringVar()


label1 = tk.Label(messageframe,
                      text="身分證").grid(row=0, column=0, 
    padx=10, ipadx=10, pady=10, ipady=10)
label1_entry = tk.Entry(messageframe, textvariable=label1_var,
                  width=30,state = 'disabled')
label1_entry.grid(row=0, column=1, 
    padx=10, ipadx=10, pady=10, ipady=10)

label2 = tk.Label(messageframe, 
                      text="密碼").grid(row=1, column=0, 
    padx=10, ipadx=10, pady=10, ipady=10)
label2_entry = tk.Entry(messageframe, textvariable=label2_var,
                  width=30,state = 'disabled')
label2_entry.grid(row=1, column=1, 
    padx=10, ipadx=10, pady=10, ipady=10)


label3 = tk.Label(messageframe, 
                      text="生日").grid(row=2, column=0, 
    padx=10, ipadx=10, pady=10, ipady=10)
label3_entry = tk.Entry(messageframe, textvariable=label3_var,
                  width=30,state = 'disabled')
label3_entry.grid(row=2, column=1, 
    padx=10, ipadx=10, pady=10, ipady=10)


label4 = tk.Label(messageframe, 
                      text="姓氏").grid(row=3, column=0, 
    padx=10, ipadx=10, pady=10, ipady=10)
label4_entry = tk.Entry(messageframe, textvariable=label4_var,
                  width=30,state = 'disabled')
label4_entry.grid(row=3, column=1, 
    padx=10, ipadx=10, pady=10, ipady=10)


label5 = tk.Label(messageframe, 
                      text="名字").grid(row=4, column=0, 
    padx=10, ipadx=10, pady=10, ipady=10)
label5_entry = tk.Entry(messageframe, textvariable=label5_var,
                  width=30,state = 'disabled')
label5_entry.grid(row=4, column=1, 
    padx=10, ipadx=10, pady=10, ipady=10)

label6 = tk.Label(messageframe, 
                      text="學歷").grid(row=5, column=0, 
    padx=10, ipadx=10, pady=10, ipady=10)
label6_entry = tk.Entry(messageframe, textvariable=label6_var,
                  width=30,state = 'disabled')
label6_entry.grid(row=5, column=1, 
    padx=10, ipadx=10, pady=10, ipady=10)

label7 = tk.Label(messageframe, 
                      text="地址").grid(row=6, column=0, 
    padx=10, ipadx=10, pady=10, ipady=10)
label7_entry = tk.Entry(messageframe, textvariable=label7_var,
                  width=30,state = 'disabled')
label7_entry.grid(row=6, column=1, 
    padx=10, ipadx=10, pady=10, ipady=10)


label8 = tk.Label(messageframe, 
                      text="電話").grid(row=7, column=0, 
    padx=10, ipadx=10, pady=10, ipady=10)
label8_entry = tk.Entry(messageframe, textvariable=label8_var,
                  width=30,state = 'disabled')
label8_entry.grid(row=7, column=1, 
    padx=10, ipadx=10, pady=10, ipady=10)

label9 = tk.Label(messageframe, 
                      text="帳號").grid(row=8, column=0, 
    padx=10, ipadx=10, pady=10, ipady=10)
label9_entry = tk.Entry(messageframe, textvariable=label9_var,
                  width=30,state = 'disabled')
label9_entry.grid(row=8, column=1, 
    padx=10, ipadx=10, pady=10, ipady=10)



message_cheak = tk.Button(messageframe, state='disabled', command=message_cheak_button,
                      text="確\n認", font = ("Helvetica",60) ,height = 5 , width = 0)
message_cheak.grid(row=0, column=2,rowspan = 9,
    padx=13, ipadx=10, pady=10, ipady=10)


                             
root.mainloop()
