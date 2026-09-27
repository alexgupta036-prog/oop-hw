class DailyHelper:
    def __init__(self, name):
        self.my_name = name
        self.todo_list = []
        print("Helper started! Hello " + self.my_name)

    def add_item(self, item):
        self.todo_list.append(item)
        print("Added: " + item)

    def show_all(self):
        print("\n--- My Reminders ---")
        for number, item in enumerate(self.todo_list, start=1):
            print(str(number) + ". " + item)
        print("--------------------\n")

    def find_item(self, word):
        print("Looking for: " + word)
        for number, item in enumerate(self.todo_list, start=1):
            if word in item:
                print("Found it at number " + str(number) + ": " + item)

    def close(self):
        print("Goodbye! Helper for " + self.my_name + " is closing down.")


my_helper = DailyHelper("Sam")
my_helper.add_item("Do homework math lesson")
my_helper.add_item("Finish Codingal python assignment")
my_helper.add_item("Clean up my room")
my_helper.show_all()
my_helper.find_item("python")
print("\nEnding the program now...")
my_helper.close()