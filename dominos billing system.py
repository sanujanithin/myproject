print('                                            welcome to dominos pizza|||we wish u to make u a day yummy|||                                             ');
print('')
print('')
from datetime import datetime
n=datetime.now()
print('date:%s-%s-%s                                                                                                                         time:%s-%s-%s'%(n.day,n.month,n.year,n.hour,n.minute,n.second));
from datetime import date
import calendar
m=date.today()
n1=calendar.day_name[m.weekday()]
print('                                                       welcome to '+n1+' dhamakaaaaaaaaaa                                                                   ');
print('')
print('')
print('                                                                  menu                                                                                     ');
print('')
print('')
print('')
print('')
print('')
bill=0;
count=0;
a=True
c=True
v=True
while(a):
    l=[[1,'DELUXE VEGGIE',235,450,695],[2,'VEG EXTRAVAGZENA',235,450,695],[3,'5pepper',235,450,695],[4,'double cheese',235,450,695]]
    for i in l:
        print('%s                 %s'%(i[0],i[1]))
        print('size             S     M      L')
        print('                 %s  %s    %s'%(i[2],i[3],i[4]))
        print('')
    while(v):
        order=input('tell me your pizza sir/mam?choose the num:');
        order=str(order)
        if order=='1' or order=='2' or order=='3' or order=='4':
            order=order;
            v=False
        else:
            print('invalid number')
            v=True
            
            
        size=raw_input('which size would like to have S/M/L?')
        size=size.upper();
        b=True
        while(b):
            if order=='1' and size=='S':
                bill=bill+l[0][2]
                b=False
                c=True
            elif order=='1' and size=='M':
                bill=bill+l[0][3]
                b=False
                c=True
            elif order=='1' and size=='L':
                bill=bill+l[0][4]
                b=False
                c=True
            elif order=='2' and size=='S':
                bill=bill+l[1][2]
                b=False
                c=True
            elif order=='2' and size=='M':
                bill=bill+l[1][3]
                b=False
                c=True
            elif order=='2' and size=='L':
                bill=bill+l[1][4]
                b=False
                c=True
            elif order=='3' and size=='S':
                bill=bill+l[2][2]
                b=False
                c=True
            elif order=='3' and size=='M':
                bill=bill+l[2][3]
                b=False
                c=True
            elif order=='3' and size=='L':
                bill=bill+l[2][4]
                b=False
                c=True
            elif order=='4' and size=='S':
                bill=bill+l[3][2]
                b=False
                c=True
            elif order=='4' and size=='M':
                bill=bill+l[3][3]
                b=False
                C=True
            elif order=='4' and size=='L':
                bill=bill+l[3][4]
                b=False
                c=True
            else:
                print('invalid input')
                b=False
        while(c):
            count=count+1
            print('')
            print('added to cart......... current bill is:Rs',bill,'only.total number of pizzas=',count)
            print('')
            extra=raw_input('anything else do u wantY/N?');
            extra=extra.upper();
            if(extra=='Y'):
                a=True
                c=False
                v=True
            elif(extra=='N'):
                a=False
                c=False
            else:
                print('invalid number')
                c=True
print('total bill withouttaxes is  %s'%(bill))
GST=bill*12/100;
VAT=bill*6/100;
total_bill=GST+VAT+bill;
print('GST %s'%(GST));
print('VAT %s'%(VAT));
print('total bill with taxes is %s'%(total_bill))
print('thank u for visting us have a nice day|||Come again');


    
    



    





        



