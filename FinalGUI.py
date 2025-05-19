from tkinter import *
from tkinter import messagebox
import os

EVENT_OPTIONS = ["Maths", "Sports", "Science", "Literature"]
MAX_TEAMS = 4
MAX_INDIVIDUALS = 20
MAX_TIME = 60  # Benchmark time in minutes

class MainApp:
    def __init__(self):
        self.main_window = None
        self.team_name_var = None
        self.user_vars = None
        self.individual_user_var = None
        self.team_points_var = None
        self.individual_points_var = None
        self.team_time_var = None
        self.individual_time_var = None
        self.team_event_type_var = None
        self.individual_event_type_var = None
        self.create_main_menu()

    def create_main_menu(self):
        self.main_window = Tk()
        self.main_window.title("Main Menu")
        self.main_window.geometry("960x500")

        self.team_event_type_var = StringVar(value=EVENT_OPTIONS[0])
        self.individual_event_type_var = StringVar(value=EVENT_OPTIONS[0])
        self.team_name_var = StringVar()
        self.user_vars = [StringVar() for _ in range(5)]
        self.individual_user_var = StringVar()
        self.team_points_var = StringVar()
        self.individual_points_var = StringVar()
        self.team_time_var = StringVar()
        self.individual_time_var = StringVar()

        Button(self.main_window, width=30, height=2, text="Leaderboard", command=self.open_ldbrdwin,
               bg='black', fg='white', font=('helvetica')).place(x=340, y=200)

        Button(self.main_window, width=30, height=2, text="Team", command=self.open_team_window,
               bg='black', fg='white', font=('helvetica')).place(x=110, y=100)

        Button(self.main_window, width=30, height=2, text="Individual", command=self.open_individual_window,
               bg='black', fg='white', font=('helvetica')).place(x=570, y=100)

        Label(self.main_window, width=30, height=2, text='Main Menu', bg='blue', fg='white',
              font=('helvetica')).place(x=340, y=25)

        Button(self.main_window, width=10, text="Exit", command=self.exit_app,
               bg='red', fg='white', font=('helvetica')).place(x=10, y=20)

        self.main_window.mainloop()

    def calculate_adjusted_points(self, raw_points, time_taken):
        try:
            raw = float(raw_points)
            time = float(time_taken)
            multiplier = max(0, 2 - (time / MAX_TIME))
            return round(min(raw * multiplier, raw * 2), 2)
        except ValueError:
            return None

    def Team_event_enter(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        doc_path = os.path.join(script_dir, "teams.txt")

        team_name = self.team_name_var.get().strip()
        members = [var.get().strip() for var in self.user_vars if var.get().strip()]
        event_type = self.team_event_type_var.get()
        raw_points = self.team_points_var.get().strip()
        time_taken = self.team_time_var.get().strip()

        if not team_name:
            messagebox.showwarning("Warning", "Please enter a team name.")
            return

        if os.path.exists(doc_path):
            with open(doc_path, "r") as f:
                team_lines = f.readlines()
            if len(team_lines) >= MAX_TEAMS:
                messagebox.showerror("Limit Reached", "Maximum number of teams (4) has been reached.")
                return

        adjusted = self.calculate_adjusted_points(raw_points, time_taken)
        if adjusted is None:
            messagebox.showerror("Invalid Input", "Please enter valid points and time.")
            return

        with open(doc_path, "a") as f:
            f.write(f"Team Name: {team_name}, Members: {', '.join(members)}, Event: {event_type}, Raw Points: {raw_points}, Time: {time_taken}, Adjusted Points: {adjusted}\n")
        messagebox.showinfo("Success", f"Team {team_name} entered.")

    def individual_event_enter(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        doc_path = os.path.join(script_dir, "indiv.txt")

        name = self.individual_user_var.get().strip()
        event_type = self.individual_event_type_var.get()
        raw_points = self.individual_points_var.get().strip()
        time_taken = self.individual_time_var.get().strip()

        if not name:
            messagebox.showwarning("Warning", "Please enter a name.")
            return

        if os.path.exists(doc_path):
            with open(doc_path, "r") as f:
                indiv_lines = f.readlines()
            if len(indiv_lines) >= MAX_INDIVIDUALS:
                messagebox.showerror("Limit Reached", "Maximum number of individuals (20) has been reached.")
                return

        adjusted = self.calculate_adjusted_points(raw_points, time_taken)
        if adjusted is None:
            messagebox.showerror("Invalid Input", "Please enter valid points and time.")
            return

        with open(doc_path, "a") as f:
            f.write(f"Name: {name}, Event: {event_type}, Raw Points: {raw_points}, Time: {time_taken}, Adjusted Points: {adjusted}\n")
        messagebox.showinfo("Success", f"Individual {name} entered.")

    def open_team_window(self):
        self.main_window.withdraw()
        win = Toplevel()
        win.title("Team Entry")
        win.geometry("500x500")

        Label(win, text="Team Name").place(x=30, y=20)
        Entry(win, textvariable=self.team_name_var).place(x=150, y=20)

        for i in range(5):
            Label(win, text=f"Member {i + 1}").place(x=30, y=60 + i * 30)
            Entry(win, textvariable=self.user_vars[i]).place(x=150, y=60 + i * 30)

        Label(win, text="Event").place(x=30, y=230)
        OptionMenu(win, self.team_event_type_var, *EVENT_OPTIONS).place(x=150, y=225)

        Label(win, text="Raw Points").place(x=30, y=270)
        Entry(win, textvariable=self.team_points_var).place(x=150, y=270)

        Label(win, text="Time Taken (min)").place(x=30, y=310)
        Entry(win, textvariable=self.team_time_var).place(x=150, y=310)

        Button(win, text="Enter", command=self.Team_event_enter).place(x=200, y=350)
        Button(win, text="Back", command=lambda: [win.destroy(), self.main_window.deiconify()]).place(x=30, y=350)

    def open_individual_window(self):
        self.main_window.withdraw()
        win = Toplevel()
        win.title("Individual Entry")
        win.geometry("400x400")

        Label(win, text="Name").place(x=30, y=20)
        Entry(win, textvariable=self.individual_user_var).place(x=120, y=20)

        Label(win, text="Event").place(x=30, y=60)
        OptionMenu(win, self.individual_event_type_var, *EVENT_OPTIONS).place(x=120, y=55)

        Label(win, text="Raw Points").place(x=30, y=100)
        Entry(win, textvariable=self.individual_points_var).place(x=120, y=100)

        Label(win, text="Time Taken (min)").place(x=30, y=140)
        Entry(win, textvariable=self.individual_time_var).place(x=160, y=140)

        Button(win, text="Enter", command=self.individual_event_enter).place(x=150, y=180)
        Button(win, text="Back", command=lambda: [win.destroy(), self.main_window.deiconify()]).place(x=30, y=180)

    def parse_adjusted_points(self, line):
        try:
            parts = line.strip().split(",")
            for part in parts:
                if "Adjusted Points" in part:
                    return float(part.strip().split(":")[-1])
        except Exception:
            return 0.0
        return 0.0

    def open_ldbrdwin(self):
        self.main_window.withdraw()
        win = Toplevel()
        win.title("Leaderboard")
        win.geometry("600x600")

        Label(win, text="Team Leaderboard").pack()
        team_box = Listbox(win, width=80)
        team_box.pack()
        team_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "teams.txt")
        if os.path.exists(team_path):
            with open(team_path, "r") as f:
                lines = f.readlines()
            lines.sort(key=self.parse_adjusted_points, reverse=True)
            for line in lines:
                team_box.insert(END, line.strip())

        Label(win, text="Individual Leaderboard").pack()
        indiv_box = Listbox(win, width=80)
        indiv_box.pack()
        indiv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "indiv.txt")
        if os.path.exists(indiv_path):
            with open(indiv_path, "r") as f:
                lines = f.readlines()
            lines.sort(key=self.parse_adjusted_points, reverse=True)
            for line in lines:
                indiv_box.insert(END, line.strip())

        Button(win, text="Back", command=lambda: [win.destroy(), self.main_window.deiconify()]).pack()

    def exit_app(self):
        if self.main_window:
            self.main_window.destroy()

if __name__ == "__main__":
    MainApp()
