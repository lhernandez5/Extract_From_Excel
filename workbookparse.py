#!/usr/bin/python3 
#This script parses 
#


import xlrd, datetime, xlwt
from numbers import Number
from decimal import Decimal

wb=xlrd.open_workbook('/Users/hdz/Leases file.xlsx')
wS=xlwt.Workbook()
ws=wS.add_sheet("Sheet1")

for s in wb.sheets():
   print ('Sheet: ', s.name)
print("\nYour file parsing was successful!")
print("The number of worksheets in Leases: {0}\n".format(wb.nsheets))
ws.write(0,0,'Branch Code')
ws.write(0,1,'Branch Name')
ws.write(0,2,'Lease Code')
ws.write(0,3,'Commencement Date')
ws.write(0,4,'Expiration Date')
ws.write(0,5,'Renewal Option')
ws.write(0,6,'Escalation Info')
ws.write(0,7,'Security Deposit')
ws.write(0,8,'Lessor')
ws.write(0,9,'Address')
ws.write(0,10,'Lease Property Location')
ws.write(0,11,'Phone')
ws.write(0,12,'Fax')
ws.write(0,13,'Email')
ws.write(0,14,'Contact')
ws.write(0,15,'Space')
ws.write(0,16,'Base Yr')
counter=0
for s in wb.sheets():
    counter+=1
    branchCode="{0}".format(s.cell_value(rowx=3, colx=1))
    ws.write(counter,0,branchCode)
    branchName="{0}".format(s.cell_value(rowx=3, colx=3))
    ws.write(counter,1,branchName)
    leaseCode="{0}".format(s.cell_value(rowx=1, colx=8))
    ws.write(counter,2,leaseCode)
    commencement=s.cell_value(rowx=6, colx=3)
    if (type(commencement)==float):
        commencement_as_date=datetime.datetime(*xlrd.xldate_as_tuple(commencement, wb.datemode))
        commencementDate= " %s" % commencement_as_date
        ws.write(counter,3,commencementDate)
    elif (type(commencement)==str):
        commencementDate=" %s" % (commencement)
        ws.write(counter,3,commencementDate)
    
    expired=s.cell_value(rowx=7, colx=3)
    if (type(expired)==float):
        expired_as_date=datetime.datetime(*xlrd.xldate_as_tuple(expired, wb.datemode))
        expirationDate= " %s" % expired_as_date
        ws.write(counter,4,expirationDate)
    elif (type(expired)== str):
        expired=s.cell_value(rowx=7, colx=3)
        expirationDate=" %s" % expired
        ws.write(counter,4,expirationDate)
    
    renewalOption= "{0}".format(s.cell_value(rowx=6, colx=5))+' {0}'.format(s.cell_value(rowx=7, colx=5))+' {0}'.format(s.cell_value(rowx=8, colx=5))
    ws.write(counter,5,renewalOption)
    escalationInfo= "{0}".format(s.cell_value(rowx=10, colx=5))+' {0}'.format(s.cell_value(rowx=11, colx=5))+' {0}'.format(s.cell_value(rowx=12, colx=5))+' {0}'.format(s.cell_value(rowx=13, colx=5))
    ws.write(counter,6,escalationInfo)
    securityDeposit=" {0}".format(s.cell_value(rowx=13, colx=3))
    ws.write(counter,7,securityDeposit)
    lessor= "{0}".format(s.cell_value(rowx=15, colx=1))
    ws.write(counter,8,lessor)
    address="{0}".format(s.cell_value(rowx=17, colx=1))+ '\n\t'+ '{0}'.format(s.cell_value(rowx=18, colx=1))+'\n\t'+'{0}'.format(s.cell_value(rowx=19, colx=1))+'\n\t'+'{0}'.format(s.cell_value(rowx=20, colx=1))+'\n\t'+'{0}'.format(s.cell_value(rowx=21, colx=1))
    ws.write(counter,9,address)
    leasedPropertyLocation="{0}".format(s.cell_value(rowx=24, colx=1))+ '\n\t\t\t'+ '{0}'.format(s.cell_value(rowx=25, colx=1))+'\n\t\t\t'+'{0}'.format(s.cell_value(rowx=26, colx=1))+'\n\t\t\t'+'{0}'.format(s.cell_value(rowx=27, colx=1))
    ws.write(counter,10,leasedPropertyLocation)
    phone="{0}".format(s.cell_value(rowx=17, colx=7))
    ws.write(counter,11,phone)
    fax= "{0}".format(s.cell_value(rowx=18, colx=7)) 
    ws.write(counter,12,fax)
    email="{0}".format(s.cell_value(rowx=19, colx=7))
    ws.write(counter,13,email)
    contact="{0}".format(s.cell_value(rowx=20, colx=7))
    ws.write(counter,14,contact)
    space="{0}".format(s.cell_value(rowx=25, colx=7))
    ws.write(counter,15,space)
    baseYr="{0}".format(s.cell_value(rowx=26, colx=7))
    ws.write(counter,16,baseYr)
wS.save("example.xls")
