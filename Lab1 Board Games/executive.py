from boardgame import Boardgame
class Executive:
    def __init__(self, file_name):
        self.game_list = []
        self.file_name = file_name
    def file_reader(self):
        input_file = open(self.file_name, "r")
        for line in input_file:
            all_data = line.split()
            self.game_list.append(Boardgame(all_data[0],all_data[1],all_data[2],all_data[3],all_data[4],all_data[5]))
        input_file.close()
    def run(self):
        self.file_reader()
        self.menu()
    def menu(self):
#         present options
        user_selection = 0
        while user_selection != 6:
            print(""" 
            1. Games list sorted from highest to lowest Gibbons rating \n 
            2. Games by year \n 
            3. Games by their play time \n 
            4. People's rating vs Gibbons rating \n 
            5. Print based on ranking \n 
            6. Quit """)
            user_selection = input("Enter the number before the option you want: ")
            if user_selection == "1":
                print("All games highest to lowest Gibbons rating:")
                sorted = self.game_list
                sorted.sort(reverse = True)
                for game in sorted:
                    print(game)
            elif user_selection == "2":
                targ_year = input("Please input the year you want the games from:")
                print(f"Games from the year {targ_year}:")
                for game in self.game_list:
                    if game.year == int(targ_year):
                        print(game)
            elif user_selection == "3":
                print("Games by their play time:")
                targ_time = input("Please input the maximum play time you want the games from:")
                print(f"Games with the maximum play time {targ_time}:")
                for game in self.game_list:
                    if game.MT <= int(targ_time):
                        print(game)
            elif user_selection == "4":
                print("People's rating vs Gibbons rating:")
                targ_difference = input("Please input the difference between Gibbons rating and public rating:")
                print(f"Games with the {targ_difference} rating difference:")
                for game in self.game_list:
                    if abs(game.GR-game.PR) >= float(targ_difference):
                        print(game)
            elif user_selection == "5":
                print("All games based on their rankings:")
                targ_rating = input("Please the threshold rating you want the games from:")
                print(f"Games with the rating {targ_rating} or better:")
                for game in self.game_list:
                    if game.GR >= float(targ_rating):
                        print(game)

            elif user_selection == "6":
                print("We're quiting...")
                exit()
            else:
                print("Invalid input. Please make sure your input is a number between 1 and 6.")