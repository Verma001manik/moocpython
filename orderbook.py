class Task:
    current_id = 1

    def __init__(self, description, programmer, workload):
        self.id = Task.current_id
        Task.current_id += 1
        self.description = description
        self.programmer = programmer
        self.workload = int(workload)  # Convert workload to an integer
        self.finished = False

    def is_finished(self):
        if self.finished == False:
            print("NOT FINISHED")
        else: 
            print("FINISHED")

        return self.finished

    def mark_finished(self):
        self.finished = True

    def __str__(self):
        return f"{self.id}: {self.description} ({self.workload}), programmer {self.programmer}, {self.is_finished()}"


class OrderBook:
    def __init__(self):
        self.tasks = []

    def add_order(self):
        desc = input("description: ")
        programmer = input("programmer: ")
        workload = input("workload time: ")
        task = Task(desc, programmer, workload)
        self.tasks.append(task)

    def all_orders(self):
        return self.tasks

    def mark_finished(self):
        id = int(input("id: "))  # Convert input ID to an integer
        for task in self.tasks:
            if task.id == id:
                task.mark_finished()
                print(f"Task with ID {id} marked as finished.")
                return  # Exit the loop once the task is found and marked

        print(f"Task with ID {id} not found in the order book.")

    def finished_orders(self):
        r = [task for task in self.tasks if task.is_finished() == "FINISHED"]
        if len(r) == 0:
            print("No finished tasks found.")
        else:
            print("Finished Tasks:")
            for task in r:
                print(task)

    def unfinished_orders(self):
        r = [task for task in self.tasks if task.is_finished() == "NOT FINISHED"]
        if len(r) == 0:
            print("No unfinished tasks found.")
        else:
            print("Unfinished Tasks:")
            for task in r:
                print(task)

    def programmers(self):
        result = [task.programmer for task in self.tasks]
        print(set(result))

    def status_of_programmer(self):
        self.finished_tasks = 0
        self.unfinished_tasks = 0
        self.total_workload_finished = 0
        self.total_workload_unfinished = 0
        programmer = input("programmer: ")

        for task in self.tasks:
            if programmer == task.programmer:
                if task.is_finished() == "FINISHED":  # Modify the check here
                    self.finished_tasks += 1
                    self.total_workload_finished += task.workload
                elif task.is_finished() == "NOT FINISHED":  # Modify the check here
                    self.unfinished_tasks += 1
                    self.total_workload_unfinished += task.workload

        if self.finished_tasks == 0 and self.unfinished_tasks == 0:
            print('No tasks found for this programmer.')
        else:
            print(f"Total finished tasks: {self.finished_tasks}")
            print(f"Total unfinished tasks: {self.unfinished_tasks}")
            print(f"Total workload finished: {self.total_workload_finished}")
            print(f"Total workload unfinished: {self.total_workload_unfinished}")

    def help(self):
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def execute(self):
        self.help()
        while True:
            command = input("command: ")
            if command == '0':
                break
            elif command == '1':
                self.add_order()
            elif command == '2':
                self.finished_orders()
            elif command == '3':
                self.unfinished_orders()
            elif command == '4':
                self.mark_finished()
            elif command == '5':
                self.programmers()
            elif command == '6':
                self.status_of_programmer()
            else:
                print("Invalid command. Please try again.")

if __name__ == "__main__":
    orders = OrderBook()
    orders.execute()
