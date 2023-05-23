#  Star Cinema Hall Project
#  Abdullah AL Adib Akhand




class Star_Cinema:
    _hall_list =[]

    def entry_hall(self, hallname):
        Star_Cinema._hall_list.append(hallname)



class Hall:
    def __init__(self, rows, cols, hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = {}
        self.show_list = []
        Star_Cinema._hall_list.append(self)

    def entry_show(self, id , movie_name, time):
        show_info = (movie_name , id, time)
        self.show_list.append(show_info)
        seat_view = [[chr(ord('@')+j+1)+str(i) for i in range(self.cols)] for j in range(self.rows)]
        self.seats[id] = seat_view


    def book_seats(self, customer_name, mobile_number , show_id, seatNo):
        for info in self.show_list:
            check = False
            if show_id in info:
                check = True
                tickets = []
                for seat in seatNo:
                    try:
                        if self.seats[show_id][seat[0]][seat[1]] != 'X':
                            tickets.append(self.seats[show_id][seat[0]][seat[1]])
                            self.seats[show_id][seat[0]][seat[1]] = 'X'
                        else:
                                print("Sorry Sir! This seat is already booked. Look for another option")
                                return
                                
                    except:
                        print("Sorry Sir. The Seat No is invalid") 
                        return 
                if len(seatNo) == len(tickets):
                    print("\n\n")
                    print("              ### Ticket booked successfully ### ")
                    print("_______________________________________________________________________________")
                    print(f"Name: {customer_name}\nMobile Number: {mobile_number}")
                    print(f"\nMovie Name: { info[0]}                 Movie Time: { [info[2]]}")
                    print("Tickets: ", *tickets)
                    print(f"Hall: {self.hall_no}\n")
                    print("________________________________________________________________________________")
                    return
        if check == False:
            print("Sorry. This Show ID is not valid")


        

                     
                    







    def view_show_list(self):
        print("\n")
        print("___________________________________________________________________________\n")
        for show in self.show_list:

            print(f"Movie Name: {show[0]}      Show Id: {show[1]}      Time: {show[2]}")

        print("____________________________________________________________________________")    
        print("\n")
            
    def view_available_seat(self, showID):
        for show in self.show_list:
            if showID in show:
                print("\n")
                print(f"Movie Name: {show[0]}                Time: {show[2]}")
                print("X for already booked seats")
                print("___________________________________________________________________________")
                for row in self.seats[showID]:
                    print(*row , sep = "        " )
                print("____________________________________________________________________________")
                return
        print("This Show ID is not valid")    






StarCinema = Star_Cinema()
hall1 = Hall(5,5, "Mirpur001")
hall1.entry_show("XYZ123", "Kurulus Osman", "Dec 01 2022 04:00 PM")
hall1.entry_show("ABC123", "Malazgirt 1071", "Dec 01 2022 08:00 PM")




while True:
    print("1. View All Show Today")
    print("2. View All Available Seats")
    print("3. Book Seat")
    option = int(input("Choose Your Option: "))
    if option == 1:
        hall1.view_show_list()
        
    elif option == 2:
        movie_id = input("Movie Id: ")
        hall1.view_available_seat(movie_id)
    elif option == 3:
        customerName = input("Enter Customer Name: ")
        phoneNo = input("Enter Phone Number: ")    
        showId = input("Enter Show Id: ")
        ticket_num = int(input("How many tickets: ")) 
        seat_info = ()
        seat_list = []

        for x in range(ticket_num ):
            ticket = input("Enter Seat No: ")
            seat_info = (int(ord(ticket[0]))-65, int(ticket[1]))
            seat_list.append(seat_info)
        hall1.book_seats(customerName, phoneNo, showId, seat_list)
            
            
        
        



