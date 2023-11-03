from tkinter import *
from tkinter import messagebox
import random,os,tempfile
#fuctionality part
def clear():
    
    S23ultraEntry.delete(0,END)
    S22ultraEntry.delete(0,END)
    S21ultraEntry.delete(0,END)
    S23Entry.delete(0,END)
    S22Entry.delete(0,END)
    S21Entry.delete(0,END)
    
    budsFEEntry.delete(0,END)
    buds2proEntry.delete(0,END)
    buds2Entry.delete(0,END)
    budsliveEntry.delete(0,END)
    budsproEntry.delete(0,END)
    budsplusEntry.delete(0,END)
    
    watch6proEntry.delete(0,END)
    watch6Entry.delete(0,END)
    watch5proEntry.delete(0,END)
    watch5Entry.delete(0,END)
    watch4proEntry.delete(0,END)
    watch4Entry.delete(0,END)
    
    S23ultraEntry.insert(0,0)
    S22ultraEntry.insert(0,0)
    S21ultraEntry.insert(0,0)
    S23Entry.insert(0,0)
    S22Entry.insert(0,0)
    S21Entry.insert(0,0)
    
    budsFEEntry.insert(0,0)
    buds2proEntry.insert(0,0)
    buds2Entry.insert(0,0)
    budsliveEntry.insert(0,0)
    budsproEntry.insert(0,0)
    budsplusEntry.insert(0,0)
    
    watch6proEntry.insert(0,0)
    watch6Entry.insert(0,0)
    watch5proEntry.insert(0,0)
    watch5Entry.insert(0,0)
    watch4proEntry.insert(0,0)
    watch4Entry.insert(0,0)
    
    mobilepriceEntry.delete(0, END)
    earbudspriceEntry.delete(0, END)
    watchpriceEntry.delete(0, END)
    
    watchtaxEntry.delete(0, END) 
    mobiletaxEntry.delete(0, END) 
    earbudstaxEntry.delete(0, END) 
    
    nameEntry.delete(0,END)
    PhoneEntry.delete(0,END)
    billnumberEntry.delete(0,END)
    
    textarea.delete(1.0,END)
    
def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')

if not os.path.exists('bills'):
    os.mkdir('bills')

def search_bill():
   file_path=r"./bills"
   bill_number=billnumberEntry.get()
   file_path=os.path.join(file_path,f"{bill_number}.txt")
   if os.path.exists(file_path):
       with open(file_path,'r') as file:
           bill_contents=file.read()
           textarea.delete('1.0','end')
           textarea.insert('1.0',bill_contents)    
   else:
        messagebox.showerror('Error','Invaid Bill Number')    

def save_bill():
    global billnumber
    result=messagebox.askyesno('confirm','Do you want to save this bill?')
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'bills/{billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('success',f'Bill number {billnumber} is saved successfully')
        billnumber=random.randint(500,1000)

billnumber=random.randint(500,1000)


def bill_area() :
    if nameEntry.get=='' or PhoneEntry.get()=='':
        messagebox.showerror('Error','Customer Detail Required')
    elif mobilepriceEntry.get()=='' and earbudspriceEntry.get()=='' and watchpriceEntry()=='':
        messagebox.showerror('Error','No Products Are Selected')    
    elif mobilepriceEntry.get()=='0 Rs' and earbudspriceEntry.get()=='0 Rs' and watchpriceEntry.get()=='0 Rs':
        messagebox.showerror('Error','No Products Are Selected') 
   
    
    else :
       textarea.delete(1.0,END) 
       textarea.insert(END,'\t\t**WELCOME CUSTOMER**\n')
       textarea.insert(END,f'\nBILL NUMBER: {billnumber}\n')
       textarea.insert(END,f'\nCUSTOMER NAME: {nameEntry.get()}\n')
       textarea.insert(END,f'\nPHONE NUMBER: {PhoneEntry.get()}\n')
       textarea.insert(END,'\n*********************************************')
       textarea.insert(END,'PRODUCT\t\tQUANTITY\t\tPRICE')
       textarea.insert(END,'\n*********************************************')
       if S23ultraEntry.get()!='0':
        textarea.insert(END,f'\nS23 ULTRA\t\t{S23ultraEntry.get()}\t\t{S23ultraprice} Rs')
       if S22ultraEntry.get()!='0':
        textarea.insert(END,f'\nS22 ULTRA\t\t{S22ultraEntry.get()}\t\t{S22ultraprice} Rs')
       if S21ultraEntry.get()!='0':
        textarea.insert(END,f'\nS21 ULTRA\t\t{S21ultraEntry.get()}\t\t{s21ultraprice} Rs')
       if S23Entry.get()!='0':
        textarea.insert(END,f'\nS23\t\t{S23Entry.get()}\t\t{s23price} Rs')
       if S22Entry.get()!='0':
        textarea.insert(END,f'\nS22\t\t{S22Entry.get()}\t\t{s22price} Rs')
       if S21Entry.get()!='0':
        textarea.insert(END,f'\nS21\t\t{S21Entry.get()}\t\t{s21price} Rs')
       
       if budsFEEntry.get()!='0':
        textarea.insert(END,f'\nbuds FE\t\t{budsFEEntry.get()}\t\t{budsfeprice} Rs')
       if buds2proEntry.get()!='0':
        textarea.insert(END,f'\nbuds2 pro\t\t{buds2proEntry.get()}\t\t{buds2proprice} Rs')
       if budsplusEntry.get()!='0':
        textarea.insert(END,f'\nbuds plus\t\t{budsplusEntry.get()}\t\t{budplusprice} Rs')
       if buds2Entry.get()!='0':
        textarea.insert(END,f'\nbuds2\t\t{buds2Entry.get()}\t\t{bud2price} Rs')
       if budsliveEntry.get()!='0':
        textarea.insert(END,f'\nbudslive\t\t{budsliveEntry.get()}\t\t{budsliveprice} Rs')
       if budsproEntry.get()!='0':
        textarea.insert(END,f'\nbuds pro\t\t{budsproEntry.get()}\t\t{ budsproprice} Rs')
         
       if watch6proEntry.get()!='0':
        textarea.insert(END,f'\nWatch6 pro\t\t{watch6proEntry.get()}\t\t{watch6proprice} Rs')
       if watch6Entry.get()!='0':
        textarea.insert(END,f'\nWatch6\t\t{watch6Entry.get()}\t\t{watch6price} Rs')
       if watch5proEntry.get()!='0':
        textarea.insert(END,f'\nWatch5 pro\t\t{watch5proEntry.get()}\t\t{watch5proprice} Rs')
       if watch5Entry.get()!='0':
        textarea.insert(END,f'\nWatch5 \t\t{watch5Entry.get()}\t\t{watch5price} Rs')
       if watch4proEntry.get()!='0':
        textarea.insert(END,f'\nWatch4 pro\t\t{watch4proEntry.get()}\t\t{watch4proprice} Rs')
       if watch4Entry.get()!='0':
        textarea.insert(END,f'\nWatch4\t\t{watch4Entry.get()}\t\t{watch4price} Rs')
       textarea.insert(END,'\n*********************************************')
        
       if mobiletaxEntry.get()!='0,0 Rs':
        textarea.insert(END,f'\n mobile tax\t\t{mobiletaxEntry.get()}')
       if earbudstaxEntry.get()!='0,0 Rs':
        textarea.insert(END,f'\n Buds tax\t\t{earbudstaxEntry.get()}')
       if watchtaxEntry.get()!='0,0 Rs':
        textarea.insert(END,f'\n Watch tax\t\t{watchtaxEntry.get()}')
       textarea.insert(END,f'\n\nTotal bill\t\t {totalbill}')                             
       textarea.insert(END,'\n*********************************************')
       save_bill()
       
       
       
def total():
    global totalbill
    global S23ultraprice
    global S22ultraprice
    global s21ultraprice
    global s23price
    global s22price
    global s21price
    S23ultraprice=int(S23ultraEntry.get())*154999
    S22ultraprice=int(S22ultraEntry.get())*110799
    s21ultraprice=int(S21ultraEntry.get())*95999
    s23price=int(S23Entry.get())*74999
    s22price=int(S22Entry.get())*64999
    s21price=int(S21Entry.get())*45280
    
    totalsseriseprice=S23ultraprice+S22ultraprice+s21ultraprice+s23price+s22price+s21price
    mobilepriceEntry.delete(0, END)
    mobilepriceEntry.insert(0, str(totalsseriseprice) +' Rs')
    mobiletax=totalsseriseprice*1.2
    mobiletaxEntry.delete(0, END) 
    mobiletaxEntry.insert(0, str(mobiletax) +' Rs')
    
    global budsfeprice
    global buds2proprice
    global budplusprice
    global bud2price
    global budsliveprice
    global budsproprice
    budsfeprice=int(budsFEEntry.get())*7999
    buds2proprice=int(buds2proEntry.get())*14999
    budplusprice=int(budsplusEntry.get())*8999
    bud2price=int(buds2Entry.get())*5490
    budsliveprice=int(budsliveEntry.get())*4299
    budsproprice=int(budsproEntry.get())*6599
    
    totalbudprice=budsfeprice+buds2proprice+budplusprice+bud2price+budsliveprice+budsproprice
    earbudspriceEntry.delete(0, END)
    earbudspriceEntry.insert(0, str(totalbudprice) +' Rs')    
    earbudstax=totalbudprice*2
    earbudstaxEntry.delete(0, END) 
    earbudstaxEntry.insert(0, str(earbudstax) +' Rs')
    
    global watch6proprice
    global watch6price
    global watch5proprice
    global watch5price
    global watch4proprice
    global watch4price
    
    watch6proprice=int(watch6proEntry.get())*21999
    watch6price=int(watch6Entry.get())*29999
    watch5proprice=int(watch5proEntry.get())*30998
    watch5price=int(watch5Entry.get())*25499
    watch4proprice=int(watch4proEntry.get())*30599
    watch4price=int(watch4Entry.get())*28899
    
    totalwatchprice=watch6proprice+watch6price+watch5proprice+watch5price+watch4proprice+watch4price
    watchpriceEntry.delete(0, END)
    watchpriceEntry.insert(0, str(totalwatchprice) +' Rs')
    watchtax=totalwatchprice*0.23
    watchtaxEntry.delete(0, END) 
    watchtaxEntry.insert(0, str(watchtax) +' Rs')
    
    totalbill=totalsseriseprice+totalbudprice+totalwatchprice+mobiletax+earbudstax+watchtax
    
    
    
    
    
#GUI part
root=Tk()
root.title('Galaxy Tax Invoice')
root.geometry('1270x685')
#root.iconbitmap('finance_dollar_money_payment_receipt_bill_invoice_icon_251678.ico')
headinglabel=Label(root,text='Galaxy Tax Invoice',font=('times new roman',30,'bold'),bg='gray44',fg='gray99',bd=12,relief=GROOVE)
headinglabel.pack(fill=X)

customer_details_frame=LabelFrame(root,text='Cutomer Details',font=('times new roman',15,'bold'),fg='gray99',bd='8',relief=GROOVE,bg='gray44')
customer_details_frame.pack(fill=X)

nameLabel=Label(customer_details_frame,text='Name',font=('times new roman',15,'bold'),bg='gray44',fg='gray99')
nameLabel.grid(row=0,column=0,padx=20,pady=2)

nameEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel=Label(customer_details_frame,text='Phone Number',font=('times new roman',15,'bold'),bg='gray44',fg='gray99')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)

PhoneEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
PhoneEntry.grid(row=0,column=3,padx=8)

billnumberLabel=Label(customer_details_frame,text='BillNumber',font=('times new roman',15,'bold'),bg='gray44',fg='gray99')
billnumberLabel.grid(row=0,column=4,padx=20,pady=2)

billnumberEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
billnumberEntry.grid(row=0,column=5,padx=8)

searchbutton=Button(customer_details_frame,text='SEARCH',font=('arial',12,'bold'),bd=7,width=16, command=search_bill)
searchbutton.grid(row=0,column=6,padx=20,pady=8)

productsFrame=Frame(root)
productsFrame.pack()

mobileFrame=LabelFrame(productsFrame,text='Galaxy S Series',font=('times new roman',15,'bold'),fg='gray99',bd='8',relief=GROOVE,bg='gray44')
mobileFrame.grid(row=0,column=0)

S23ultraLable=Label(mobileFrame,text='S23 ULTRA',font=('times new roman',15,'bold'),bg='gray44',fg='gray99')
S23ultraLable.grid(row=0,column=0,pady=9,padx=10,sticky='W')

S23ultraEntry=Entry(mobileFrame,font=('times new roman',15,'bold'),width=10,bd=5)
S23ultraEntry.grid(row=0,column=1,pady=9,padx=10)
S23ultraEntry.insert(0,0)

S22ultraLable=Label(mobileFrame,text='S22 ULTRA',font=('times new roman',15,'bold'),bg='gray44',fg='gray99')
S22ultraLable.grid(row=1,column=0,pady=9,padx=10,sticky='w')

S22ultraEntry=Entry(mobileFrame,font=('times new roman',15,'bold'),width=10,bd=5)
S22ultraEntry.grid(row=1,column=1,pady=9,padx=10)
S22ultraEntry.insert(0,0)

S21ultraLable=Label(mobileFrame,text='S21 ULTRA',font=('times new roman',15,'bold'),bg='gray44',fg='gray99')
S21ultraLable.grid(row=2,column=0,pady=9,padx=10,sticky='w')

S21ultraEntry=Entry(mobileFrame,font=('times new roman',15,'bold'),width=10,bd=5)
S21ultraEntry.grid(row=2,column=1,pady=9,padx=10)
S21ultraEntry.insert(0,0)

S23Lable=Label(mobileFrame,text='S23',font=('times new roman',15,'bold'),bg='gray44',fg='gray99')
S23Lable.grid(row=3,column=0,pady=9,padx=10,sticky='w')

S23Entry=Entry(mobileFrame,font=('times new roman',15,'bold'),width=10,bd=5)
S23Entry.grid(row=3,column=1,pady=9,padx=10)
S23Entry.insert(0,0)

S22Lable=Label(mobileFrame,text='S22',font=('times new roman',15,'bold'),bg='gray44',fg='gray99')
S22Lable.grid(row=4,column=0,pady=9,padx=10,sticky='w')

S22Entry=Entry(mobileFrame,font=('times new roman',15,'bold'),width=10,bd=5)
S22Entry.grid(row=4,column=1,pady=9,padx=10)
S22Entry.insert(0,0)

S21Lable=Label(mobileFrame,text='S21',font=('times new roman',15,'bold'),bg='gray44',fg='gray99')
S21Lable.grid(row=5,column=0,pady=9,padx=10,sticky='w')

S21Entry=Entry(mobileFrame,font=('times new roman',15,'bold'),width=10,bd=5)
S21Entry.grid(row=5,column=1,pady=9,padx=10)
S21Entry.insert(0,0)

earbudsFrame=LabelFrame(productsFrame,text='Ear Buds',font=('times new roman',15,'bold'),fg='gray99',bd='8',relief=GROOVE,bg='gray44')
earbudsFrame.grid(row=0,column=1)

budsFELable=Label(earbudsFrame,text='Galaxy Buds FE',font=('times new roman',15,'bold'),bg='gray44',fg='gray99')
budsFELable.grid(row=0,column=0,pady=9,padx=10,sticky='w')

budsFEEntry=Entry(earbudsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
budsFEEntry.grid(row=0,column=1,pady=9,padx=10)
budsFEEntry.insert(0,0)

buds2proLabale=Label(earbudsFrame,text='Galaxy Buds2 pro',font=('times new roman',15,'bold'),bg='gray44',fg='gray99')
buds2proLabale.grid(row=1,column=0,pady=9,padx=10,sticky='w')

buds2proEntry=Entry(earbudsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
buds2proEntry.grid(row=1,column=1,pady=9,padx=10)
buds2proEntry.insert(0,0)

buds2Lable=Label(earbudsFrame,text='Galaxy Buds2',font=('times new roman',15,'bold'),bg='gray44',fg='gray99')
buds2Lable.grid(row=2,column=0,pady=9,padx=10,sticky='w')

buds2Entry=Entry(earbudsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
buds2Entry.grid(row=2,column=1,pady=9,padx=10)
buds2Entry.insert(0,0)

budsliveLable=Label(earbudsFrame,text='Galaxy Buds Live',font=('times new roman',15,'bold'),bg='gray44',fg='gray99')
budsliveLable.grid(row=3,column=0,pady=9,padx=10,sticky='w')

budsliveEntry=Entry(earbudsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
budsliveEntry.grid(row=3,column=1,pady=9,padx=10)
budsliveEntry.insert(0,0)

budsproLable=Label(earbudsFrame,text='Galaxy Buds Pro',font=('times new roman',15,'bold'),bg='gray44',fg='gray99')
budsproLable.grid(row=4,column=0,pady=9,padx=10,sticky='w')

budsproEntry=Entry(earbudsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
budsproEntry.grid(row=4,column=1,pady=9,padx=10)
budsproEntry.insert(0,0)

budsplusLable=Label(earbudsFrame,text='Galaxy Buds',font=('times new roman',15,'bold'),bg='gray44',fg='gray99')
budsplusLable.grid(row=5,column=0,pady=9,padx=10,sticky='w')

budsplusEntry=Entry(earbudsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
budsplusEntry.grid(row=5,column=1,pady=9,padx=10)
budsplusEntry.insert(0,0)

watchFrame=LabelFrame(productsFrame,text='Galaxy Watches',font=('times new roman',15,'bold'),fg='gray99',bd='8',relief=GROOVE,bg='gray44')
watchFrame.grid(row=0,column=2)

watch6proLable=Label(watchFrame,text='Galaxy Wtach6 pro',font=('times new roman',15,'bold'),bg='gray44',fg='gray99')
watch6proLable.grid(row=0,column=0,pady=9,padx=10,sticky='w')

watch6proEntry=Entry(watchFrame,font=('times new roman',15,'bold'),width=10,bd=5)
watch6proEntry.grid(row=0,column=1,pady=9,padx=10)
watch6proEntry.insert(0,0)

watch6Labale=Label(watchFrame,text='Galaxy Watch6',font=('times new roman',15,'bold'),bg='gray44',fg='gray99')
watch6Labale.grid(row=1,column=0,pady=9,padx=10,sticky='w')

watch6Entry=Entry(watchFrame,font=('times new roman',15,'bold'),width=10,bd=5)
watch6Entry.grid(row=1,column=1,pady=9,padx=10)
watch6Entry.insert(0,0)

watch5proLable=Label(watchFrame,text='Galaxy Watch5 pro',font=('times new roman',15,'bold'),bg='gray44',fg='gray99')
watch5proLable.grid(row=2,column=0,pady=9,padx=10,sticky='w')

watch5proEntry=Entry(watchFrame,font=('times new roman',15,'bold'),width=10,bd=5)
watch5proEntry.grid(row=2,column=1,pady=9,padx=10)
watch5proEntry.insert(0,0)

watch5Lable=Label(watchFrame,text='Galaxy Watch5',font=('times new roman',15,'bold'),bg='gray44',fg='gray99')
watch5Lable.grid(row=3,column=0,pady=9,padx=10,sticky='w')

watch5Entry=Entry(watchFrame,font=('times new roman',15,'bold'),width=10,bd=5)
watch5Entry.grid(row=3,column=1,pady=9,padx=10)
watch5Entry.insert(0,0)

watch4proLable=Label(watchFrame,text='Galaxy Watch4 pro',font=('times new roman',15,'bold'),bg='gray44',fg='gray99')
watch4proLable.grid(row=4,column=0,pady=9,padx=10,sticky='w')

watch4proEntry=Entry(watchFrame,font=('times new roman',15,'bold'),width=10,bd=5)
watch4proEntry.grid(row=4,column=1,pady=9,padx=10)
watch4proEntry.insert(0,0)

watch4Lable=Label(watchFrame,text='Galaxy Watch4',font=('times new roman',15,'bold'),bg='gray44',fg='gray99')
watch4Lable.grid(row=5,column=0,pady=9,padx=10,sticky='w')

watch4Entry=Entry(watchFrame,font=('times new roman',15,'bold'),width=10,bd=5)
watch4Entry.grid(row=5,column=1,pady=9,padx=10)
watch4Entry.insert(0,0)

billframe=Frame(productsFrame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3,padx=10,pady=10)

billareaLabel=Label(billframe,text='INVOICE',font=('times new roman',15,'bold'),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)

scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billframe,height=18,width=45,yscrollcommand=Scrollbar.set(self=scrollbar, first=0,last=0))
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenuFrame=LabelFrame(root,text='Bill Menu',font=('times new roman',12,'bold'),fg='gray99',bd='8',relief=GROOVE,bg='gray44')
billmenuFrame.pack(fill=X)

mobilepriceLable=Label(billmenuFrame,text='Mobile Price',font=('times new roman',12,'bold'),bg='gray44',fg='gray99')
mobilepriceLable.grid(row=0,column=0,pady=9,padx=10,sticky='w')

mobilepriceEntry=Entry(billmenuFrame,font=('times new roman',12,'bold'),width=10,bd=5)
mobilepriceEntry.grid(row=0,column=1,pady=9,padx=10)

earbudspriceLable=Label(billmenuFrame,text='Earbuds Price',font=('times new roman',12,'bold'),bg='gray44',fg='gray99')
earbudspriceLable.grid(row=1,column=0,pady=9,padx=10,sticky='w')

earbudspriceEntry=Entry(billmenuFrame,font=('times new roman',12,'bold'),width=10,bd=5)
earbudspriceEntry.grid(row=1,column=1,pady=9,padx=10)

watchpriceLable=Label(billmenuFrame,text='Watch Price',font=('times new roman',12,'bold'),bg='gray44',fg='gray99')
watchpriceLable.grid(row=2,column=0,pady=9,padx=10,sticky='w')

watchpriceEntry=Entry(billmenuFrame,font=('times new roman',12,'bold'),width=10,bd=5)
watchpriceEntry.grid(row=2,column=1,pady=9,padx=10)

mobiletaxLable=Label(billmenuFrame,text='Mobile Tax',font=('times new roman',12,'bold'),bg='gray44',fg='gray99')
mobiletaxLable.grid(row=0,column=2,pady=9,padx=10,sticky='w')

mobiletaxEntry=Entry(billmenuFrame,font=('times new roman',12,'bold'),width=10,bd=5)
mobiletaxEntry.grid(row=0,column=3,pady=9,padx=10)

earbudstaxLable=Label(billmenuFrame,text='Earbuds Tax',font=('times new roman',12,'bold'),bg='gray44',fg='gray99')
earbudstaxLable.grid(row=1,column=2,pady=9,padx=10,sticky='w')

earbudstaxEntry=Entry(billmenuFrame,font=('times new roman',12,'bold'),width=10,bd=5)
earbudstaxEntry.grid(row=1,column=3,pady=9,padx=10)

watchtaxLable=Label(billmenuFrame,text='Watch Tax',font=('times new roman',12,'bold'),bg='gray44',fg='gray99')
watchtaxLable.grid(row=2,column=2,pady=9,padx=10,sticky='w')

watchtaxEntry=Entry(billmenuFrame,font=('times new roman',12,'bold'),width=10,bd=5)
watchtaxEntry.grid(row=2,column=3,pady=9,padx=10)

buttonFrame=Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

totalButton=Button(buttonFrame,text='Total',font=('arial',16,'bold'), bg='gray44', fg='gray99', bd=5, width=8, pady=10, command=total)
totalButton.grid(row=0,column=0,pady=25,padx=20)

billButton=Button(buttonFrame,text='Bill',font=('arial',16,'bold'),bg='gray44',fg='gray99',bd=5,width=8,pady=10, command=bill_area)
billButton.grid(row=0,column=1,pady=25,padx=20)

printButton=Button(buttonFrame,text='Print',font=('arial',16,'bold'),bg='gray44',fg='gray99',bd=5,width=8,pady=10, command=print_bill)
printButton.grid(row=0,column=2,pady=25,padx=20)

clearButton=Button(buttonFrame,text='Clear',font=('arial',16,'bold'),bg='gray44',fg='gray99',bd=5,width=8,pady=10,command=clear)
clearButton.grid(row=0,column=3,pady=25,padx=20)

root.mainloop() 
