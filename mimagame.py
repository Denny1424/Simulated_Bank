anslist=['#','#','#','#']
times=5
lanjiao = False
def mg():
    import tkinter as tk
    import random
    from tkinter import messagebox
    
    win=tk.Toplevel()
    
    global times
    times = 5

    

    ansvar=tk.StringVar()
    ansvar.set("####")
    
    
    
    #隨機產生密碼
    alb="0123456789"
    mima=""
    for i in random.sample(alb,4):
        mima+=i
    
    #print(mima)     #顯示密碼(測試用)

    def confirm():
        global times,anslist,lanjiao
        jodging=[0,0]
        if mima==str(zuhe()):
            messagebox.showinfo('Congratulation!','你猜得沒錯')
            lanjiao = True
            win.quit()
            win.destroy()
        else:
            for i in range(4):
                if zuhe().find(mima[i])>-1:
                    if zuhe()[i]==mima[i]:
                        jodging[0]+=1
                    else:
                        jodging[1]+=1
            times-=1
            tempstr="%sA%sB"%(jodging[0],jodging[1])
            cfbut.config(state = 'disabled')
            messagebox.showwarning("Wrong","答題次數剩餘%d次\n"%(times)+tempstr)
            cfbut.config(state = 'normal')
            numtext.insert("end","第%d次：%s  %s\n"%(5-times,zuhe(),tempstr))
            if times==0:
                win.quit()
                win.destroy()
            #按鈕&數字初始化
            button_0.config(state='normal')
            button_1.config(state='normal')
            button_2.config(state='normal')
            button_3.config(state='normal')
            button_4.config(state='normal')
            button_5.config(state='normal')
            button_6.config(state='normal')
            button_7.config(state='normal')
            button_8.config(state='normal')
            button_9.config(state='normal')
            anslist=['#','#','#','#']
            ansvar.set("####")
            
    def zuhe():
        global anslist
        ans=""
        for i in anslist:
            ans+=i
        return ans
    
    def plus(num):
        global anslist
        
        if(anslist[0]=='#'):
            for i in range(3):
                anslist[i]=anslist[i+1]
            anslist[3]=str(num)
            return 1
        else:
            return 0
    
    def minus():
        global anslist
        lastn=anslist[3]
        
        for i in range(1,4):
            anslist[4-i]=anslist[3-i]
            
        anslist[0]='#'
        ansvar.set(zuhe())
        
        if(lastn=='0'):
            button_0.config(state='normal')
        elif(lastn=='1'):
            button_1.config(state='normal')
        elif(lastn=='2'):
            button_2.config(state='normal')
        elif(lastn=='3'):
            button_3.config(state='normal')
        elif(lastn=='4'):
            button_4.config(state='normal')
        elif(lastn=='5'):
            button_5.config(state='normal')
        elif(lastn=='6'):
            button_6.config(state='normal')
        elif(lastn=='7'):
            button_7.config(state='normal')
        elif(lastn=='8'):
            button_8.config(state='normal')
        elif(lastn=='9'):
            button_9.config(state='normal')
        
    def but_0(): 
        if(plus(0)):
            button_0.config(state='disabled')  
            ansvar.set(zuhe())
    
    def but_1():
        if(plus(1)):
            button_1.config(state='disabled')  
            ansvar.set(zuhe())
    
    def but_2():
        if(plus(2)):
            button_2.config(state='disabled')  
            ansvar.set(zuhe())
        
    def but_3():
        if(plus(3)):
            button_3.config(state='disabled')  
            ansvar.set(zuhe())
        
    def but_4():
        if(plus(4)):
            button_4.config(state='disabled')  
            ansvar.set(zuhe())
        
    def but_5():
        if(plus(5)):
            button_5.config(state='disabled')  
            ansvar.set(zuhe())
        
    def but_6():
        if(plus(6)):
            button_6.config(state='disabled')  
            ansvar.set(zuhe())
        
    def but_7():
        if(plus(7)):
            button_7.config(state='disabled') 
            ansvar.set(zuhe())
        
    def but_8():
        if(plus(8)):
            button_8.config(state='disabled') 
            ansvar.set(zuhe())
        
    def but_9():
        if(plus(9)):
            button_9.config(state='disabled')  
            ansvar.set(zuhe())
    
    #視窗初始化設定
    win.title("minigame")  
    win.geometry("1024x768+400+150")   #(+400+150) 為初始視窗位置
    win.iconbitmap("image\\shaizi.ico")
    mainframe=tk.Frame(win)
    mainframe.pack()
    
    #上框架
    topfrm=tk.Frame(mainframe)
    topfrm.pack()
    
    #下框架
    underfrm=tk.Frame(mainframe)
    underfrm.pack()
    
    #TEXT
    numtext=tk.Text(topfrm,height=5,width=43)
    numtext.pack()
    
    #數字顯示Lable
    numlb=tk.Label(topfrm,textvariable=ansvar, fg="black", bg="skyblue")
    numlb.config(font=("Arial",64),padx=40,pady=10,bd=20,relief="groove")  #relief=邊框 
    numlb.pack()
    
    #數字按鍵
    img1=tk.PhotoImage(file="image\\1.png")
    button_1=tk.Button(underfrm,image=img1,command=but_1)
    button_1.grid(row=0,column=0)
    
    img2=tk.PhotoImage(file="image\\2.png")
    button_2=tk.Button(underfrm,image=img2,command=but_2)
    button_2.grid(row=0,column=1)
    
    img3=tk.PhotoImage(file="image\\3.png")
    button_3=tk.Button(underfrm,image=img3,command=but_3)
    button_3.grid(row=0,column=2)
    
    img4=tk.PhotoImage(file="image\\4.png")
    button_4=tk.Button(underfrm,image=img4,command=but_4)
    button_4.grid(row=1,column=0)
    
    img5=tk.PhotoImage(file="image\\5.png")
    button_5=tk.Button(underfrm,image=img5,command=but_5)
    button_5.grid(row=1,column=1)
    
    img6=tk.PhotoImage(file="image\\6.png")
    button_6=tk.Button(underfrm,image=img6,command=but_6)
    button_6.grid(row=1,column=2)
    
    img7=tk.PhotoImage(file="image\\7.png")
    button_7=tk.Button(underfrm,image=img7,command=but_7)
    button_7.grid(row=2,column=0)
    
    img8=tk.PhotoImage(file="image\\8.png")
    button_8=tk.Button(underfrm,image=img8,command=but_8)
    button_8.grid(row=2,column=1)
    
    img9=tk.PhotoImage(file="image\\9.png")
    button_9=tk.Button(underfrm,image=img9,command=but_9)
    button_9.grid(row=2,column=2)
    
    img0=tk.PhotoImage(file="image\\0.png")
    button_0=tk.Button(underfrm,image=img0,command=but_0)
    button_0.grid(row=3,column=1)
    
    #確認鍵&倒退&取消
    
    imgconfirm=tk.PhotoImage(file="image\\confirm.png")
    cfbut=tk.Button(underfrm,image=imgconfirm,command=confirm)
    cfbut.grid(row=3,column=2)
    
    imgcancel=tk.PhotoImage(file="image\\cancel.png")
    cabut=tk.Button(underfrm,image=imgcancel,command=minus)
    cabut.grid(row=3,column=0)
    
    
    win.mainloop()

    return lanjiao