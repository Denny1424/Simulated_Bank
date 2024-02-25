def xuandan(zhanghao):              #登入後作業

    loop=True
    while loop:
        DorZ = input('查詢餘額請按A，存款請按B，提款請按C，查詢帳戶資料請按D，登出請按E: ')
        
        if DorZ=='A' or DorZ=='a':
            print("帳戶餘額為%d元" %chayue(zhanghao))
            
        elif DorZ=='B' or DorZ=='b':
            try:
                cun=int(input("請輸入存款金額: "))
                numon=cunkuan(zhanghao,cun)
                print("已存入%d元,帳戶內餘額為%d" %(cun,numon))
            except ValueError :
                print('請輸入數字')
            except Exception as errXuandan1:
                print (errXuandan1)
        elif DorZ=='C' or DorZ=='c':
            try:
                tik=int(input("請輸入提款金額: "))
                numon=tikuan(zhanghao,tik)
                print("已提出%d元,帳戶內餘額為%d" %(tik,numon))
            except ValueError :
                print('請輸入數字')
            except Exception as errXuandan2:
                print (errXuandan2)
        elif DorZ=='D' or DorZ=='d':
            zi=ziliao(zhanghao)
            print("身分證字號: ",zi[0][0])
            print("密碼: ",zi[0][1])
            print("生日: ",zi[0][2])
            print("姓名: ",zi[0][3]+zi[0][4])
            print("教育程度: ",zi[0][5])
            print("地址: ",zi[0][6])
            print("電話: ",zi[0][7])
            print("國籍: ",zi[0][8])
            print("帳戶餘額: ",zi[0][9])
            print("電子信箱: ",zi[0][10])
            
        elif DorZ=='E' or DorZ=='e':
            print("登出成功")
            break
        
def ziliao(zhanghao):
    
    import sqlite3
    
    conn=sqlite3.connect('database.db')
    c=conn.cursor()
    
    SQL="SELECT * FROM BANK WHERE Email = %r" %(zhanghao)
    c.execute(SQL)
    
    zi=c.fetchall()
    
    return zi
        
def chayue(zhanghao):                   #輸入帳號
    
    import sqlite3
    
    conn=sqlite3.connect('database.db')
    c=conn.cursor()
    
    SQL="SELECT Money FROM BANK WHERE Email = %r" %(zhanghao)
    c.execute(SQL)
    
    
    #yue=int(cetcho.fne()[0])
    yue=c.fetchall()  
    
    conn.commit()
    
    conn.close()
    
    #return yue
    return yue[0][0]

def cunkuan(zhanghao,money):            #輸入存錢的帳號&錢
         
    if type(money)!=int:
        raise Exception ('請輸入數字')
        
    if money <= 0:
        raise Exception ('存款金額需大於零')
  
    
    yue=chayue(zhanghao)
    xinyue=yue+money
    
    gengxin(zhanghao,xinyue)
    
    return xinyue     

def tikuan(zhanghao,money):             #輸入提款帳號&錢

    if type(money)!=int:
        raise Exception ('請輸入數字')
    if money <= 0:
        raise Exception ('提款金額需大於零')
        
    yue=chayue(zhanghao)
    
    if money > yue:
        raise Exception ('餘額不足')
        
    xinyue=yue-money
    
    gengxin(zhanghao,xinyue)
    
    return xinyue

def gengxin(zhanghao,newmoney):         #輸入要更新的帳號&新的錢(由提款&存款函數產生)
    
    import sqlite3
    
    conn=sqlite3.connect('database.db')
    c=conn.cursor()
    
    SQL="UPDATE BANK set Money = %d WHERE Email = %r" %(newmoney,zhanghao)
    c.execute(SQL)
    
    conn.commit()
    
    conn.close()
    
def searchzhang(zhanghao):          #回傳True==>帳號存在
    
    import sqlite3
    
    conn=sqlite3.connect('database.db')
    c=conn.cursor()
    
    SQL="SELECT Money FROM BANK WHERE Email = %r" %(zhanghao)
    c.execute(SQL)
    templist=c.fetchall()
    
    if len(templist)==0:
        jodge=False
    else:
        jodge=True
    
    conn.commit()
    
    conn.close()

    return jodge

def searchmi(zhanghao,mima):            #回傳True==>登入成功
    
    import sqlite3
    
    conn=sqlite3.connect('database.db')
    c=conn.cursor()   
    
    SQL="SELECT Mima FROM BANK WHERE Email = %r" %(zhanghao)
    c.execute(SQL)
    temp=c.fetchone()[0]
    
    if temp==mima:
        jodge=True
    else:
        jodge=False
    
    conn.commit()
    
    conn.close()

    return jodge


class Panding:
    
    import sqlite3
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT Email,ID from BANK")
    templist = c.fetchall()
    conn.close

    
    def __init__(self, ID = '', Dianhua = ''):
        self.ID = ID
        self.Dianhua = Dianhua
    def pandingID(self):
        alphabet={'A':'10','B':'11','C':'12','D':'13','E':'14','F':'15','G':'16','H':'17','I':'34','J':'18',
                  'K':'19','M':'21','N':'22','O':'35','P':'23','Q':'24','T':'27','U':'28','V':'29','W':'32','X':'30','Z':'33'}
        try:
            IDlist = list(self.ID)
            n1n2 = list(alphabet[IDlist[0]])
            if (len(IDlist) != 10) or (IDlist[0] not in alphabet) or (int(int(n1n2[0])+int(n1n2[1])*9+int(IDlist[1])*8+int(IDlist[2])*7+int(IDlist[3])*6+int(IDlist[4])*5+int(IDlist[5])*4+int(IDlist[6])*3+int(IDlist[7])*2+int(IDlist[8])+int(IDlist[9]))%10 != 0) :
                raise Exception ("身分證不符合規則，請重新輸入")
        except:
            raise Exception ("身分證不符合規則，請重新輸入")
        for i in self.templist:
            if i[1] == self.ID:
                raise Exception("身分證重複")

    def pandingDianhua(self):
        Dianhualist = list(self.Dianhua)
        try:
            if len(self.Dianhua) != 10 or int(Dianhualist[2]+Dianhualist[3]) > 89 \
            or int(Dianhualist[2]+Dianhualist[3]) < 10 :
                raise Exception ('電話不符合規則，請重新輸入')
        except:
            raise Exception('電話不符合規則，請重新輸入')


def zhang(zhang):
    
    import sqlite3
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT Email,ID from BANK")
    templist = c.fetchall()
    conn.close
    
    zhanglist = list(zhang)
    ying = False
    su = False
    gmail = ""
    gmailpanding = False
    lentest = False
    
    if 5 < len(zhang) < 41:
        lentest = True
        for i in range(-10,0):
            gmail += zhang[i]
        if gmail == "@gmail.com":
            gmailpanding = True
    
    for i in zhanglist:
        if 64 < ord(i) < 91 or 96 < ord(i) <123:
            ying = True
        if 47 < ord(i) < 58:
            su = True          
        
    if ( lentest and ying and su and gmailpanding ) != True :
        raise Exception("帳號不符合規定請重新輸入\n(帳號需為正規gmail信箱)")
        
    for i in templist:
        if i[0] == zhang:
            raise Exception("帳號重複")
        
    return zhang
    
def mi(mi):
    milist = list(mi)   
    ying = False
    su = False
    fuhao = False
    mitest = False
    lentest = False
    
    if 5 < len(mi) < 13:
        lentest = True
    else:
        raise Exception('密碼長度不符\n(長度需在6~12字)')
    
    for i in milist:
        if 64 < ord(i) < 91 or 96 < ord(i) <123:
            ying = True
        if 47 < ord(i) < 58:
            su = True
        if 32 < ord(i) < 48:
            fuhao = True
    if (lentest and ying and su and fuhao) == True :
        mitest = True
    if mitest == False:
        raise Exception("密碼強度不足\n(密碼需包含英文、數字、特殊符號(ASCII碼32~48))")

    return mi