import mysql.connector


try:
    apple = mysql.connector.connect(host="localhost",
                                    user="root",
                                    password="12345678")
    cur = apple.cursor()
    cur.execute("create database if not exists flight_booking")
    apple.commit()
except Exception as e:
    print("Database check complete.")


apple = mysql.connector.connect(host="localhost", user="root", password="12345678", database="flight_booking")
cur = apple.cursor()


try:
    cur.execute('''create table if not exists booking (
        passenger_name varchar(30) not null,
        passport_id int not null primary key,
        gender varchar(10) not null,
        seat_class varchar(15),
        arrival_airport varchar(40) not null,
        departure_airport varchar(40) not null,
        payment_method varchar(30) not null,
        seat_no int )''')
    apple.commit()
except Exception as e:
    print("Table check complete.")


def add_Record():
    p_name = input("Enter Passenger name: ")
    passport_id = int(input("Enter Passport id of the passinger (only numeric values allowed): "))
    gender = input("Gender: ")
    seat_class = input("Enter your seat preference class: ")
    arrival_airport = input("Enter arrival airport: ")
    departure_airport = input("Enter Departure airport: ")
    payment_method = input("Enter your payment method (card|Cash|UPI): ")
    seat_no = int(input("Enter Seat number: "))
    
    query = "insert into booking values('{}', {}, '{}', '{}', '{}', '{}', '{}', {})".format(
        p_name, passport_id, gender, seat_class, arrival_airport, departure_airport, payment_method, seat_no)
    cur.execute(query)
    apple.commit()
    print("Record added successfully")


def search_record():
    passport_id_search = int(input("Enter Passport id of person who's you want to search: "))
    query = "Select * from booking where passport_id = %s"
    cur.execute(query, (passport_id_search,))
    data = cur.fetchone()
    if data is not None:
        print(data)
    else:
        print("No record Found")


def delete_record():
    passport_id_delete = int(input("Enter Passport id of person: "))
    cur.execute("delete from booking where passport_id=%s", (passport_id_delete,))
    if cur.rowcount > 0:
        apple.commit()
        print("Deleted Successfully")
    else:
        print("Record not found")


def update_record():
    try:
        passport_id_update = int(input("Enter Passport ID to update: "))
        new_name = input("Enter new Name: ")
        new_gender = input("Enter new Gender: ")
        new_seat_class = input("Enter new Seat Class: ")
        query = "UPDATE booking SET passenger_name = %s, gender = %s, seat_class = %s WHERE passport_id = %s"
        cur.execute(query, (new_name, new_gender, new_seat_class, passport_id_update))
        if cur.rowcount > 0:
            apple.commit()
            print("Record Updated Successfully")
        else:
            print("Record not found (Check the Passport ID)")
    except Exception as e:
        print("Error updating record:", e)

def show_all():
    try:
        cur.execute("select * from booking")
        data = cur.fetchall()
        if data:
            print("--- All Booked Tickets ---")
            for row in data:
                print(row)
            print("--------------------------")
        else:
            print("No tickets booked yet.")
    except Exception as e:
        print("Error showing tickets:", e)


while True:
    print('''
    Welcome To Python & Mysql connectivity -> Flight Ticket Booking Program
    1. Book a Flight Ticket
    2. Search Your ticket
    3. Delete a Ticket
    4. Update a Record
    5. Show all Record
    6. Exit
    ''')
    cho = int(input("Enter Your Choice: "))
    if cho == 1:
        add_Record()
    elif cho == 2:
        search_record()
    elif cho == 3:
        delete_record()
    elif cho == 4:
        update_record()
    elif cho == 5:
        show_all()
    elif cho == 6:
        break
    else:
        print("Wrong option selected")
