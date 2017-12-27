#!/usr/bin/python3

with open('f3.csv', 'r') as infile, open ('output.out','w') as outfile:
    outfile.write('The following is the parsed info')
    for line in infile:
        row=line.strip()
        col=row.split(',')
        if col[1] == "Lease Summary":
            print(col[1]+': '+col[9]+'\n')
        if col[7]== "Lease Number":
            print("Lease Number: "+col[8]+"\n")
        if col[0] == "BRANCH":
            print(col[0] +': '+col[1]+','+col[3]+'\n')
            print(col[7] +': '+col[8]+'\n')
        if col[0] == "Commencement Date":
            print(col[0] +': '+col[3]+'\n')
            print(col[4] +': '+ col[5]+'\n')
        if col[0] == "Expiration Date":            
            print(col[0] +': '+col[3]+'\n')
        if col[0] == "Free Rent":
            print(col[0] +'\n')
        if col[0]=="Escalating Payments":
            print(col[0]+'\n')
        if col[4]=='Escalation Info':
            print('Escalation info: '+col[5] + '\n')
        if col[0] == "Security Deposit":
            print(col[0] +': '+col[3] + col[4]+'\n')
        if col[0] =="Lessor":
            print(col[0] +': '+col[1] + '\n')
        if col[0] == 'Address':
            print('Phone: '+col[7] + "\n")#phone
            print('Address: '+col[1] + "\n")#start of address
        if col[6] == 'Fax':
            print('\t'+col[1]+'\n')
            fax=('Fax: '+col[7]+'\n')
        if col[6] == 'Email':
            print('\t'+col[1]+'\n')
        if col[6] == 'Email':
            print('Email: '+col[7]+'\n')
            print(fax)
        if col[6] == 'Contact':
            print('Contact: '+col[7]+'\n')
        if col[7] == 'Building Leases':
            print("Leased Property Location: "+col[1]+' '+col[2]+' '+col[3]+'\n')
        if col[6] == 'Space':
            print('\t'+'\t'+col[1]+'\n')
            print('Space: '+col[7])
        if (col[8] == 'Base yr') or (col[7]=='Base yr') or (col[6]=='Base yr'):
            print(col[1]+'\n')
            print('Base yr'+col[7]+'\n')
print("\nYOUR FILE PARSED SUCCESSFULLY")
