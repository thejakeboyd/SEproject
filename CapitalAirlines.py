from tkinter import *
import random


totalcustomers = 0
seats = []
seatstaken = []
bonly = [109, 110, 111, 112, 113, 114, 115,116, 117, 119, 119, 120]
for x in range(1, 121):
    seats.append(x)
alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
customers = []
satisfaction = []

def family():
    familywin = Tk()
    familywin.configure(bg='grey')
    familywin.title('Capital Flights')
    Label(familywin, text='Family', bg='grey', font=('Arial', 65)).grid(row=0, column=0)
    Label(familywin, text='How many people are in your group?: ', bg='grey', font=('Arial', 35)).grid(row=1, column=0)
    Label(familywin, text='Enter First Passenger Name: ', bg='grey', font=('Arial', 35)).grid(row=2, column=0)
    Label(familywin, text='Enter Second Passenger Name: ', bg='grey', font=('Arial', 35)).grid(row=3, column=0)
    Label(familywin, text='Enter Third Passenger Name: ', bg='grey', font=('Arial', 35)).grid(row=4, column=0)
    Label(familywin, text='Enter Fourth Passenger Name: ', bg='grey', font=('Arial', 35)).grid(row=5, column=0)
    Label(familywin, text='Enter Fifth Passenger Name: ', bg='grey', font=('Arial', 35)).grid(row=6, column=0)
    numgroup = Entry(familywin)
    numgroup.grid(row=1, column=1)
    familyname1 = Entry(familywin)
    familyname1.grid(row=2, column=1)
    familyname2 = Entry(familywin)
    familyname2.grid(row=3, column=1)
    familyname3 = Entry(familywin)
    familyname3.grid(row=4, column=1)
    familyname4 = Entry(familywin)
    familyname4.grid(row=5, column=1)
    familyname5 = Entry(familywin)
    familyname5.grid(row=6, column=1)
    Label(familywin, text="Leave Name blank if N/A", bg='white', font=('Arial', 20)).grid(row=7, column=0)
    Button(familywin, text='SUBMIT', command=lambda: ticket3(numgroup, familyname1, familyname2, familyname3, familyname4, familyname5, familywin)).grid(row=8,
                                                                                                            column=1)

def tourist():
    touristwin = Tk()
    touristwin.configure(bg='grey')
    touristwin.title('Capital Flights')
    Label(touristwin, text='Tourists', bg='grey', font=('Arial', 65)).grid(row=0, column=0)
    Label(touristwin, text='Enter First Passenger Name: ', bg='grey', font=('Arial', 35)).grid(row=2, column=0)
    Label(touristwin, text='Enter Second Passenger Name: ', bg='grey', font=('Arial', 35)).grid(row=3, column=0)
    touristname1 = Entry(touristwin)
    touristname1.grid(row=2, column=1)
    touristname2 = Entry(touristwin)
    touristname2.grid(row=3, column=1)
    Button(touristwin, text='SUBMIT', command=lambda: ticket2(touristname1, touristname2, touristwin)).grid(row=4, column=1)

def business():
    businesswin = Tk()
    businesswin.configure(bg='grey')
    businesswin.title('Capital Flights')
    Label(businesswin, text='Business Customer', bg='grey', font=('Arial', 65)).grid(row=0, column=0)
    Label(businesswin, text='Enter your Name: ', bg='grey', font=('Arial', 35)).grid(row=2, column=0)
    bussinessname = Entry(businesswin)
    bussinessname.grid(row=2, column=1)
    Button(businesswin, text='SUBMIT', command=lambda : ticket(bussinessname, businesswin)).grid(row=3, column=1)

def manager3(manwin2):
    manwin2.destroy()
    manwin3 = Tk()
    manwin3.title("FLIGHT REPORT")
    Label(manwin3, text='TOTAL CUSTOMERS: ', bg='grey').grid(row=0, column=0)
    Label(manwin3, text=len(seatstaken)).grid(row=1, column=0)
    Label(manwin3, text='AVG SATISFACTION: ', bg='grey').grid(row=2, column=0)
    final = sum(satisfaction) / len(satisfaction)
    Label(manwin3, text=final).grid(row=3, column=0)

def manager2(manwin):
    manwin.destroy()
    manwin2 = Tk()
    manwin2.configure(bg='grey')
    manwin2.title('MANAGER SCREEN')
    x=0
    y=6
    i=1
    j=0
    Label(manwin2, text='ROW', bg='grey').grid(row=0, column=0)
    while i <= 20:
        Label(manwin2, text=alph[j]).grid(row=i, column=0)
        i += 1
        j += 1
    i=1
    while y <= 120:
        Label(manwin2, text=seats[x:y]).grid(row=i, column=1)
        x += 6
        y += 6
        i += 1
    Label(manwin2, text='SEATS TAKEN: ', bg='grey').grid(row=0, column=3)
    Label(manwin2, text='ROW', bg='grey').grid(row=0, column=0)
    Label(manwin2, text=seatstaken).grid(row=2, column=3)
    Label(manwin2, text='TOTAL CUSTOMERS: ', bg='grey').grid(row=4, column=3)
    Label(manwin2, text=len(seatstaken)).grid(row=6, column=3)
    Button(manwin2, text='FINISH FLIGHT // GENERATE REPORT', command=lambda : manager3(manwin2)).grid(row=8, column=3)


def manager():
    manwin = Tk()
    manwin.title("MANAGER LOGIN")
    Label(manwin, text='User Name').grid(row=0, column=0)
    username = StringVar()
    usernameEntry = Entry(manwin, textvariable=username).grid(row=0, column=1)
    Label(manwin, text='Password'). grid(row=1, column=0)
    password = StringVar()
    passwordEntry = Entry(manwin, textvariable=password, show='*').grid(row=1, column=1)
    Button(manwin, text='LOGIN', command=lambda : manager2(manwin)).grid(row=2, column=1)


def customer():
    customerwin = Tk()
    customerwin.configure(bg='grey')
    customerwin.title("Capital Flights")
    Label(customerwin, text='Customer Login', bg='grey', font=('Arial', 65)).grid(row=2, column=0)
    Button(customerwin, text='Business', command=lambda : business()).grid(row=3, column=0)
    Button(customerwin, text='Tourist', command=lambda : tourist()).grid(row=4, column=0)
    Button(customerwin, text='Family', command=lambda : family()).grid(row=5, column=0)

def ticket(businessname, businesswin):
    ticketwin = Tk()
    ticketwin.configure(bg='grey')
    ticketwin.title("TICKET")
    Label(ticketwin, text='PLANE TICKET', bg='grey', font=('Arial', 65)).grid(row=0, column=0)
    Label(ticketwin, text='Name: ', bg='grey', font=('Arial', 35)).grid(row=1, column=0)
    Label(ticketwin, text='Row: ', bg='grey', font=('Arial', 35)).grid(row=2, column=0)
    Label(ticketwin, text='Seat Number: ', bg='grey', font=('Arial', 35)).grid(row=3, column=0)
    customers.append(1)
    name = businessname.get()
    businesswin.destroy()
    Label(ticketwin, text=name, bg='grey', font=('Arial', 35)).grid(row=1, column=1)
    try:
        var = 108
        SI = 0
        while SI == 0:
            if seats[var] not in seatstaken:
                seatstaken.append(seats[var])
                SI = 1
            else:
                var += 1
        alphI = (var) // 6
        row = alph[alphI]
        print(row, seats[var])
        Label(ticketwin, text=row, bg='grey', font=('Arial', 35)).grid(row=2, column=1)
        Label(ticketwin, text=seats[var], bg='grey', font=('Arial', 35)).grid(row=3, column=1)
        satisfaction.append(0)
    except IndexError:
        var = 0
        SI = 0
        while SI == 0:
            if seats[var] not in seatstaken:
                seatstaken.append(seats[var])
                SI = 1
            else:
                var += 1
        alphI = (var) // 6
        row = alph[alphI]
        print(row, seats[var])
        Label(ticketwin, text=row, bg='grey', font=('Arial', 35)).grid(row=2, column=1)
        Label(ticketwin, text=seats[var], bg='grey', font=('Arial', 35)).grid(row=3, column=1)
        satisfaction.append(-5)

def ticket2(touristname1, touristname2, touristwin):
    ticketwin2 = Tk()
    ticketwin2.configure(bg='grey')
    ticketwin2.title("TICKET")
    Label(ticketwin2, text='PLANE TICKET', bg='grey', font=('Arial', 65)).grid(row=0, column=0)
    Label(ticketwin2, text='Name: ', bg='grey', font=('Arial', 35)).grid(row=1, column=0)
    Label(ticketwin2, text='Row: ', bg='grey', font=('Arial', 35)).grid(row=2, column=0)
    Label(ticketwin2, text='Seat Number: ', bg='grey', font=('Arial', 35)).grid(row=3, column=0)
    customers.append(1)
    name = touristname1.get()
    Label(ticketwin2, text=name, bg='grey', font=('Arial', 35)).grid(row=1, column=1)
    try:
        var = 0
        SI = 0
        while SI == 0:
            if seats[var] not in seatstaken and seats[var] not in bonly:
                seatstaken.append(seats[var])
                SI = 1
            else:
                var += 6
        alphI = (var) // 6
        row = alph[alphI]
        print(row, seats[var])
        Label(ticketwin2, text=row, bg='grey', font=('Arial', 35)).grid(row=2, column=1)
        Label(ticketwin2, text=seats[var], bg='grey', font=('Arial', 35)).grid(row=3, column=1)
        satisfaction.append(5)
    except IndexError:
        var = 5
        SI = 0
        while SI == 0:
            if seats[var] not in seatstaken:
                seatstaken.append(seats[var])
                SI = 1
            else:
                var += 1
        alphI = (var) // 6
        row = alph[alphI]
        print(row, seats[var])
        Label(ticketwin2, text=row, bg='grey', font=('Arial', 35)).grid(row=2, column=1)
        Label(ticketwin2, text=seats[var], bg='grey', font=('Arial', 35)).grid(row=3, column=1)
        satisfaction.append(5)
    ticketwin3 = Tk()
    ticketwin3.configure(bg='grey')
    ticketwin3.title("TICKET")
    Label(ticketwin3, text='PLANE TICKET', bg='grey', font=('Arial', 65)).grid(row=0, column=0)
    Label(ticketwin3, text='Name: ', bg='grey', font=('Arial', 35)).grid(row=1, column=0)
    Label(ticketwin3, text='Row: ', bg='grey', font=('Arial', 35)).grid(row=2, column=0)
    Label(ticketwin3, text='Seat Number: ', bg='grey', font=('Arial', 35)).grid(row=3, column=0)
    customers.append(1)
    name = touristname2.get()
    touristwin.destroy()
    Label(ticketwin3, text=name, bg='grey', font=('Arial', 35)).grid(row=1, column=1)
    try:
        var = 1
        SI = 0
        while SI == 0:
            if seats[var] not in seatstaken and seats[var] not in bonly:
                seatstaken.append(seats[var])
                SI = 1
            else:
                var += 6
        alphI = (var) // 6
        row = alph[alphI]
        print(row, seats[var])
        Label(ticketwin3, text=row, bg='grey', font=('Arial', 35)).grid(row=2, column=1)
        Label(ticketwin3, text=seats[var], bg='grey', font=('Arial', 35)).grid(row=3, column=1)
        satisfaction.append(10)
    except IndexError:
        var = 4
        SI = 0
        while SI == 0:
            if seats[var] not in seatstaken:
                seatstaken.append(seats[var])
                SI = 1
            else:
                var += 1
        alphI = (var) // 6
        row = alph[alphI]
        print(row, seats[var])
        Label(ticketwin3, text=row, bg='grey', font=('Arial', 35)).grid(row=2, column=1)
        Label(ticketwin3, text=seats[var], bg='grey', font=('Arial', 35)).grid(row=3, column=1)
        satisfaction.append(10)

def ticket3(numgroup, familyname1, familyname2, familyname3, familyname4, familyname5, familywin):
    numgroup = numgroup.get()
    if numgroup == '3':
        ticketwin4 = Tk()
        ticketwin4.configure(bg='grey')
        ticketwin4.title("TICKET")
        Label(ticketwin4, text='PLANE TICKET', bg='grey', font=('Arial', 65)).grid(row=0, column=0)
        Label(ticketwin4, text='Name: ', bg='grey', font=('Arial', 35)).grid(row=1, column=0)
        Label(ticketwin4, text='Row: ', bg='grey', font=('Arial', 35)).grid(row=2, column=0)
        Label(ticketwin4, text='Seat Number: ', bg='grey', font=('Arial', 35)).grid(row=3, column=0)
        customers.append(1)
        name = familyname1.get()
        Label(ticketwin4, text=name, bg='grey', font=('Arial', 35)).grid(row=1, column=1)
        try:
            var = 2
            SI = 0
            while SI == 0:
                if seats[var] not in seatstaken and seats[var] not in bonly:
                    seatstaken.append(seats[var])
                    SI = 1
                else:
                    var += 6
            alphI = (var) // 6
            row = alph[alphI]
            print(row, seats[var])
            Label(ticketwin4, text=row, bg='grey', font=('Arial', 35)).grid(row=2, column=1)
            Label(ticketwin4, text=seats[var], bg='grey', font=('Arial', 35)).grid(row=3, column=1)
            satisfaction.append(5)
        except IndexError:
            var = 3
            SI = 0
            while SI == 0:
                if seats[var] not in seatstaken:
                    seatstaken.append(seats[var])
                    SI = 1
                else:
                    var += 1
            alphI = (var) // 6
            row = alph[alphI]
            print(row, seats[var])
            Label(ticketwin4, text=row, bg='grey', font=('Arial', 35)).grid(row=2, column=1)
            Label(ticketwin4, text=seats[var], bg='grey', font=('Arial', 35)).grid(row=3, column=1)
            satisfaction.append(5)
        ticketwin5 = Tk()
        ticketwin5.configure(bg='grey')
        ticketwin5.title("TICKET")
        Label(ticketwin5, text='PLANE TICKET', bg='grey', font=('Arial', 65)).grid(row=0, column=0)
        Label(ticketwin5, text='Name: ', bg='grey', font=('Arial', 35)).grid(row=1, column=0)
        Label(ticketwin5, text='Row: ', bg='grey', font=('Arial', 35)).grid(row=2, column=0)
        Label(ticketwin5, text='Seat Number: ', bg='grey', font=('Arial', 35)).grid(row=3, column=0)
        customers.append(1)
        name2 = familyname2.get()
        Label(ticketwin5, text=name2, bg='grey', font=('Arial', 35)).grid(row=1, column=1)
        try:
            var = 3
            SI = 0
            while SI == 0:
                if seats[var] not in seatstaken and seats[var] not in bonly:
                    seatstaken.append(seats[var])
                    SI = 1
                else:
                    var += 6
            alphI = (var) // 6
            row = alph[alphI]
            print(row, seats[var])
            Label(ticketwin5, text=row, bg='grey', font=('Arial', 35)).grid(row=2, column=1)
            Label(ticketwin5, text=seats[var], bg='grey', font=('Arial', 35)).grid(row=3, column=1)
            satisfaction.append(5)
        except IndexError:
            var = 8
            SI = 0
            while SI == 0:
                if seats[var] not in seatstaken:
                    seatstaken.append(seats[var])
                    SI = 1
                else:
                    var += 1
            alphI = (var) // 6
            row = alph[alphI]
            print(row, seats[var])
            Label(ticketwin5, text=row, bg='grey', font=('Arial', 35)).grid(row=2, column=1)
            Label(ticketwin5, text=seats[var], bg='grey', font=('Arial', 35)).grid(row=3, column=1)
            satisfaction.append(5)
        ticketwin6 = Tk()
        ticketwin6.configure(bg='grey')
        ticketwin6.title("TICKET")
        Label(ticketwin6, text='PLANE TICKET', bg='grey', font=('Arial', 65)).grid(row=0, column=0)
        Label(ticketwin6, text='Name: ', bg='grey', font=('Arial', 35)).grid(row=1, column=0)
        Label(ticketwin6, text='Row: ', bg='grey', font=('Arial', 35)).grid(row=2, column=0)
        Label(ticketwin6, text='Seat Number: ', bg='grey', font=('Arial', 35)).grid(row=3, column=0)
        customers.append(1)
        name3 = familyname3.get()
        familywin.destroy()
        Label(ticketwin6, text=name3, bg='grey', font=('Arial', 35)).grid(row=1, column=1)
        try:
            var = 8
            SI = 0
            while SI == 0:
                if seats[var] not in seatstaken and seats[var] not in bonly:
                    seatstaken.append(seats[var])
                    SI = 1
                else:
                    var += 6
            alphI = (var) // 6
            row = alph[alphI]
            print(row, seats[var])
            Label(ticketwin6, text=row, bg='grey', font=('Arial', 35)).grid(row=2, column=1)
            Label(ticketwin6, text=seats[var], bg='grey', font=('Arial', 35)).grid(row=3, column=1)
        except IndexError:
            var = 9
            SI = 0
            while SI == 0:
                if seats[var] not in seatstaken:
                    seatstaken.append(seats[var])
                    SI = 1
                else:
                    var += 1
            alphI = (var) // 6
            row = alph[alphI]
            print(row, seats[var])
            Label(ticketwin6, text=row, bg='grey', font=('Arial', 35)).grid(row=2, column=1)
            Label(ticketwin6, text=seats[var], bg='grey', font=('Arial', 35)).grid(row=3, column=1)
            satisfaction.append(10)
    if numgroup == '4':
        ticketwin4 = Tk()
        ticketwin4.configure(bg='grey')
        ticketwin4.title("TICKET")
        Label(ticketwin4, text='PLANE TICKET', bg='grey', font=('Arial', 65)).grid(row=0, column=0)
        Label(ticketwin4, text='Name: ', bg='grey', font=('Arial', 35)).grid(row=1, column=0)
        Label(ticketwin4, text='Row: ', bg='grey', font=('Arial', 35)).grid(row=2, column=0)
        Label(ticketwin4, text='Seat Number: ', bg='grey', font=('Arial', 35)).grid(row=3, column=0)
        customers.append(1)
        name = familyname1.get()
        Label(ticketwin4, text=name, bg='grey', font=('Arial', 35)).grid(row=1, column=1)
        try:
            var = 2
            SI = 0
            while SI == 0:
                if seats[var] not in seatstaken and seats[var] not in bonly:
                    seatstaken.append(seats[var])
                    SI = 1
                else:
                    var += 6
            alphI = (var) // 6
            row = alph[alphI]
            print(row, seats[var])
            Label(ticketwin4, text=row, bg='grey', font=('Arial', 35)).grid(row=2, column=1)
            Label(ticketwin4, text=seats[var], bg='grey', font=('Arial', 35)).grid(row=3, column=1)
            satisfaction.append(5)
        except IndexError:
            var = 3
            SI = 0
            while SI == 0:
                if seats[var] not in seatstaken:
                    seatstaken.append(seats[var])
                    SI = 1
                else:
                    var += 1
            alphI = (var) // 6
            row = alph[alphI]
            print(row, seats[var])
            Label(ticketwin4, text=row, bg='grey', font=('Arial', 35)).grid(row=2, column=1)
            Label(ticketwin4, text=seats[var], bg='grey', font=('Arial', 35)).grid(row=3, column=1)
            satisfaction.append(5)
        ticketwin5 = Tk()
        ticketwin5.configure(bg='grey')
        ticketwin5.title("TICKET")
        Label(ticketwin5, text='PLANE TICKET', bg='grey', font=('Arial', 65)).grid(row=0, column=0)
        Label(ticketwin5, text='Name: ', bg='grey', font=('Arial', 35)).grid(row=1, column=0)
        Label(ticketwin5, text='Row: ', bg='grey', font=('Arial', 35)).grid(row=2, column=0)
        Label(ticketwin5, text='Seat Number: ', bg='grey', font=('Arial', 35)).grid(row=3, column=0)
        customers.append(1)
        name2 = familyname2.get()
        Label(ticketwin5, text=name2, bg='grey', font=('Arial', 35)).grid(row=1, column=1)
        try:
            var = 3
            SI = 0
            while SI == 0:
                if seats[var] not in seatstaken and seats[var] not in bonly:
                    seatstaken.append(seats[var])
                    SI = 1
                else:
                    var += 6
            alphI = (var) // 6
            row = alph[alphI]
            print(row, seats[var])
            Label(ticketwin5, text=row, bg='grey', font=('Arial', 35)).grid(row=2, column=1)
            Label(ticketwin5, text=seats[var], bg='grey', font=('Arial', 35)).grid(row=3, column=1)
            satisfaction.append(5)
        except IndexError:
            var = 8
            SI = 0
            while SI == 0:
                if seats[var] not in seatstaken:
                    seatstaken.append(seats[var])
                    SI = 1
                else:
                    var += 1
            alphI = (var) // 6
            row = alph[alphI]
            print(row, seats[var])
            Label(ticketwin5, text=row, bg='grey', font=('Arial', 35)).grid(row=2, column=1)
            Label(ticketwin5, text=seats[var], bg='grey', font=('Arial', 35)).grid(row=3, column=1)
            satisfaction.append(5)
        ticketwin6 = Tk()
        ticketwin6.configure(bg='grey')
        ticketwin6.title("TICKET")
        Label(ticketwin6, text='PLANE TICKET', bg='grey', font=('Arial', 65)).grid(row=0, column=0)
        Label(ticketwin6, text='Name: ', bg='grey', font=('Arial', 35)).grid(row=1, column=0)
        Label(ticketwin6, text='Row: ', bg='grey', font=('Arial', 35)).grid(row=2, column=0)
        Label(ticketwin6, text='Seat Number: ', bg='grey', font=('Arial', 35)).grid(row=3, column=0)
        customers.append(1)
        name3 = familyname3.get()
        Label(ticketwin6, text=name3, bg='grey', font=('Arial', 35)).grid(row=1, column=1)
        try:
            var = 8
            SI = 0
            while SI == 0:
                if seats[var] not in seatstaken and seats[var] not in bonly:
                    seatstaken.append(seats[var])
                    SI = 1
                else:
                    var += 6
            alphI = (var) // 6
            row = alph[alphI]
            print(row, seats[var])
            Label(ticketwin6, text=row, bg='grey', font=('Arial', 35)).grid(row=2, column=1)
            Label(ticketwin6, text=seats[var], bg='grey', font=('Arial', 35)).grid(row=3, column=1)
            satisfaction.append(5)
        except IndexError:
            var = 9
            SI = 0
            while SI == 0:
                if seats[var] not in seatstaken:
                    seatstaken.append(seats[var])
                    SI = 1
                else:
                    var += 1
            alphI = (var) // 6
            row = alph[alphI]
            print(row, seats[var])
            Label(ticketwin6, text=row, bg='grey', font=('Arial', 35)).grid(row=2, column=1)
            Label(ticketwin6, text=seats[var], bg='grey', font=('Arial', 35)).grid(row=3, column=1)
            satisfaction.append(5)
        ticketwin7 = Tk()
        ticketwin7.configure(bg='grey')
        ticketwin7.title("TICKET")
        Label(ticketwin7, text='PLANE TICKET', bg='grey', font=('Arial', 65)).grid(row=0, column=0)
        Label(ticketwin7, text='Name: ', bg='grey', font=('Arial', 35)).grid(row=1, column=0)
        Label(ticketwin7, text='Row: ', bg='grey', font=('Arial', 35)).grid(row=2, column=0)
        Label(ticketwin7, text='Seat Number: ', bg='grey', font=('Arial', 35)).grid(row=3, column=0)
        customers.append(1)
        name4 = familyname4.get()
        familywin.destroy()
        Label(ticketwin7, text=name4, bg='grey', font=('Arial', 35)).grid(row=1, column=1)
        try:
            var = 9
            SI = 0
            while SI == 0:
                if seats[var] not in seatstaken and seats[var] not in bonly:
                    seatstaken.append(seats[var])
                    SI = 1
                else:
                    var += 6
            alphI = (var) // 6
            row = alph[alphI]
            print(row, seats[var])
            Label(ticketwin7, text=row, bg='grey', font=('Arial', 35)).grid(row=2, column=1)
            Label(ticketwin7, text=seats[var], bg='grey', font=('Arial', 35)).grid(row=3, column=1)
            satisfaction.append(5)
        except IndexError:
            var = 14
            SI = 0
            while SI == 0:
                if seats[var] not in seatstaken:
                    seatstaken.append(seats[var])
                    SI = 1
                else:
                    var += 1
            alphI = (var) // 6
            row = alph[alphI]
            print(row, seats[var])
            Label(ticketwin7, text=row, bg='grey', font=('Arial', 35)).grid(row=2, column=1)
            Label(ticketwin7, text=seats[var], bg='grey', font=('Arial', 35)).grid(row=3, column=1)
            satisfaction.append(5)
            satisfaction.append(10)
    if numgroup == '5':
        ticketwin4 = Tk()
        ticketwin4.configure(bg='grey')
        ticketwin4.title("TICKET")
        Label(ticketwin4, text='PLANE TICKET', bg='grey', font=('Arial', 65)).grid(row=0, column=0)
        Label(ticketwin4, text='Name: ', bg='grey', font=('Arial', 35)).grid(row=1, column=0)
        Label(ticketwin4, text='Row: ', bg='grey', font=('Arial', 35)).grid(row=2, column=0)
        Label(ticketwin4, text='Seat Number: ', bg='grey', font=('Arial', 35)).grid(row=3, column=0)
        customers.append(1)
        name = familyname1.get()
        Label(ticketwin4, text=name, bg='grey', font=('Arial', 35)).grid(row=1, column=1)
        try:
            var = 2
            SI = 0
            while SI == 0:
                if seats[var] not in seatstaken and seats[var] not in bonly:
                    seatstaken.append(seats[var])
                    SI = 1
                else:
                    var += 6
            alphI = (var) // 6
            row = alph[alphI]
            print(row, seats[var])
            Label(ticketwin4, text=row, bg='grey', font=('Arial', 35)).grid(row=2, column=1)
            Label(ticketwin4, text=seats[var], bg='grey', font=('Arial', 35)).grid(row=3, column=1)
            satisfaction.append(5)
        except IndexError:
            var = 3
            SI = 0
            while SI == 0:
                if seats[var] not in seatstaken:
                    seatstaken.append(seats[var])
                    SI = 1
                else:
                    var += 1
            alphI = (var) // 6
            row = alph[alphI]
            print(row, seats[var])
            Label(ticketwin4, text=row, bg='grey', font=('Arial', 35)).grid(row=2, column=1)
            Label(ticketwin4, text=seats[var], bg='grey', font=('Arial', 35)).grid(row=3, column=1)
            satisfaction.append(5)
        ticketwin5 = Tk()
        ticketwin5.configure(bg='grey')
        ticketwin5.title("TICKET")
        Label(ticketwin5, text='PLANE TICKET', bg='grey', font=('Arial', 65)).grid(row=0, column=0)
        Label(ticketwin5, text='Name: ', bg='grey', font=('Arial', 35)).grid(row=1, column=0)
        Label(ticketwin5, text='Row: ', bg='grey', font=('Arial', 35)).grid(row=2, column=0)
        Label(ticketwin5, text='Seat Number: ', bg='grey', font=('Arial', 35)).grid(row=3, column=0)
        customers.append(1)
        name2 = familyname2.get()
        Label(ticketwin5, text=name2, bg='grey', font=('Arial', 35)).grid(row=1, column=1)
        try:
            var = 3
            SI = 0
            while SI == 0:
                if seats[var] not in seatstaken and seats[var] not in bonly:
                    seatstaken.append(seats[var])
                    SI = 1
                else:
                    var += 6
            alphI = (var) // 6
            row = alph[alphI]
            print(row, seats[var])
            Label(ticketwin5, text=row, bg='grey', font=('Arial', 35)).grid(row=2, column=1)
            Label(ticketwin5, text=seats[var], bg='grey', font=('Arial', 35)).grid(row=3, column=1)
            satisfaction.append(5)
        except IndexError:
            var = 8
            SI = 0
            while SI == 0:
                if seats[var] not in seatstaken:
                    seatstaken.append(seats[var])
                    SI = 1
                else:
                    var += 1
            alphI = (var) // 6
            row = alph[alphI]
            print(row, seats[var])
            Label(ticketwin5, text=row, bg='grey', font=('Arial', 35)).grid(row=2, column=1)
            Label(ticketwin5, text=seats[var], bg='grey', font=('Arial', 35)).grid(row=3, column=1)
            satisfaction.append(5)
        ticketwin6 = Tk()
        ticketwin6.configure(bg='grey')
        ticketwin6.title("TICKET")
        Label(ticketwin6, text='PLANE TICKET', bg='grey', font=('Arial', 65)).grid(row=0, column=0)
        Label(ticketwin6, text='Name: ', bg='grey', font=('Arial', 35)).grid(row=1, column=0)
        Label(ticketwin6, text='Row: ', bg='grey', font=('Arial', 35)).grid(row=2, column=0)
        Label(ticketwin6, text='Seat Number: ', bg='grey', font=('Arial', 35)).grid(row=3, column=0)
        customers.append(1)
        name3 = familyname3.get()
        Label(ticketwin6, text=name3, bg='grey', font=('Arial', 35)).grid(row=1, column=1)
        try:
            var = 8
            SI = 0
            while SI == 0:
                if seats[var] not in seatstaken and seats[var] not in bonly:
                    seatstaken.append(seats[var])
                    SI = 1
                else:
                    var += 6
            alphI = (var) // 6
            row = alph[alphI]
            print(row, seats[var])
            Label(ticketwin6, text=row, bg='grey', font=('Arial', 35)).grid(row=2, column=1)
            Label(ticketwin6, text=seats[var], bg='grey', font=('Arial', 35)).grid(row=3, column=1)
            satisfaction.append(5)
        except IndexError:
            var = 9
            SI = 0
            while SI == 0:
                if seats[var] not in seatstaken:
                    seatstaken.append(seats[var])
                    SI = 1
                else:
                    var += 1
            alphI = (var) // 6
            row = alph[alphI]
            print(row, seats[var])
            Label(ticketwin6, text=row, bg='grey', font=('Arial', 35)).grid(row=2, column=1)
            Label(ticketwin6, text=seats[var], bg='grey', font=('Arial', 35)).grid(row=3, column=1)
            satisfaction.append(5)
        ticketwin7 = Tk()
        ticketwin7.configure(bg='grey')
        ticketwin7.title("TICKET")
        Label(ticketwin7, text='PLANE TICKET', bg='grey', font=('Arial', 65)).grid(row=0, column=0)
        Label(ticketwin7, text='Name: ', bg='grey', font=('Arial', 35)).grid(row=1, column=0)
        Label(ticketwin7, text='Row: ', bg='grey', font=('Arial', 35)).grid(row=2, column=0)
        Label(ticketwin7, text='Seat Number: ', bg='grey', font=('Arial', 35)).grid(row=3, column=0)
        customers.append(1)
        name4 = familyname4.get()
        Label(ticketwin7, text=name4, bg='grey', font=('Arial', 35)).grid(row=1, column=1)
        try:
            var = 9
            SI = 0
            while SI == 0:
                if seats[var] not in seatstaken and seats[var] not in bonly:
                    seatstaken.append(seats[var])
                    SI = 1
                else:
                    var += 6
            alphI = (var) // 6
            row = alph[alphI]
            print(row, seats[var])
            Label(ticketwin7, text=row, bg='grey', font=('Arial', 35)).grid(row=2, column=1)
            Label(ticketwin7, text=seats[var], bg='grey', font=('Arial', 35)).grid(row=3, column=1)
            satisfaction.append(5)
        except IndexError:
            var = 14
            SI = 0
            while SI == 0:
                if seats[var] not in seatstaken:
                    seatstaken.append(seats[var])
                    SI = 1
                else:
                    var += 1
            alphI = (var) // 6
            row = alph[alphI]
            print(row, seats[var])
            Label(ticketwin7, text=row, bg='grey', font=('Arial', 35)).grid(row=2, column=1)
            Label(ticketwin7, text=seats[var], bg='grey', font=('Arial', 35)).grid(row=3, column=1)
            satisfaction.append(5)
        ticketwin8 = Tk()
        ticketwin8.configure(bg='grey')
        ticketwin8.title("TICKET")
        Label(ticketwin8, text='PLANE TICKET', bg='grey', font=('Arial', 65)).grid(row=0, column=0)
        Label(ticketwin8, text='Name: ', bg='grey', font=('Arial', 35)).grid(row=1, column=0)
        Label(ticketwin8, text='Row: ', bg='grey', font=('Arial', 35)).grid(row=2, column=0)
        Label(ticketwin8, text='Seat Number: ', bg='grey', font=('Arial', 35)).grid(row=3, column=0)
        customers.append(1)
        name5 = familyname5.get()
        familywin.destroy()
        Label(ticketwin8, text=name5, bg='grey', font=('Arial', 35)).grid(row=1, column=1)
        try:
            var = 13
            SI = 0
            while SI == 0:
                if seats[var] not in seatstaken and seats[var] not in bonly:
                    seatstaken.append(seats[var])
                    SI = 1
                else:
                    var += 6
            alphI = (var) // 6
            row = alph[alphI]
            print(row, seats[var])
            Label(ticketwin8, text=row, bg='grey', font=('Arial', 35)).grid(row=2, column=1)
            Label(ticketwin8, text=seats[var], bg='grey', font=('Arial', 35)).grid(row=3, column=1)
        except IndexError:
            var = 14
            SI = 0
            while SI == 0:
                if seats[var] not in seatstaken:
                    seatstaken.append(seats[var])
                    SI = 1
                else:
                    var += 1
            alphI = (var) // 6
            row = alph[alphI]
            print(row, seats[var])
            Label(ticketwin8, text=row, bg='grey', font=('Arial', 35)).grid(row=2, column=1)
            Label(ticketwin8, text=seats[var], bg='grey', font=('Arial', 35)).grid(row=3, column=1)
            satisfaction.append(10)




mainroot = Tk()
mainroot.configure(bg='grey')
mainroot.title("Capital Flights")
Label(mainroot, text='Capital Flights', bg='grey', font=('Arial', 80)).grid(row=2, column=0)
Button(mainroot, text='Customer', command=lambda : customer()).grid(row=3, column=0)
Button(mainroot, text='Manager', command=lambda : manager()).grid(row=6, column=0)

mainroot.mainloop()