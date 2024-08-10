import tkinter as tk
from tkinter import messagebox
import re

class CyberSafetyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cyber Security: World Behind The Screen")
        self.geometry("900x600")
        self.configure(bg="#F0F4F8")  # Light grey background

        self.user_info = {}  # Initialize user_info attribute

        # Create and initialize the sidebar and pages
        self.sidebar = tk.Frame(self, bg="#2C3E50", width=200, height=600, relief="raised", borderwidth=2)
        self.sidebar.pack(side="left", fill="y")

        self.container = tk.Frame(self, bg="#ECF0F1")
        self.container.pack(side="right", fill="both", expand=True)

        # Initialize the sidebar buttons
        self.create_sidebar_button("Login", "LoginPage")
        self.create_sidebar_button("Home", "HomePage")
        self.create_sidebar_button("Daily Sessions", "DailySessionsPage")
        self.create_sidebar_button("Profile", "ProfilePage")
        self.create_sidebar_button("Scam Detector", "ScamDetectorPage")

        # Dictionary to hold the different pages
        self.frames = {}

        # Create and initialize all pages
        for F in (LoginPage, HomePage, DailySessionsPage, ProfilePage, ScamDetectorPage):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Configure grid layout for the container
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Show the login page first
        self.show_frame("LoginPage")

    def create_sidebar_button(self, text, frame_name):
        button = tk.Button(self.sidebar, text=text, font=("Arial", 14), bg="#34495E", fg="white",
                           command=lambda: self.show_frame(frame_name), relief="flat", padx=10, pady=10)
        button.pack(fill="x", padx=5, pady=5)

    def show_frame(self, page_name):
        """Show a frame for the given page name"""
        frame = self.frames[page_name]
        if page_name == "ProfilePage":
            frame.update_info()  # Update profile info when showing the Profile page
        frame.tkraise()

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#ECF0F1")
        self.controller = controller

        # Title
        self.label = tk.Label(self, text="Create Profile", font=("Arial", 36, "bold"), bg="#ECF0F1", fg="#2C3E50")
        self.label.pack(pady=30)

        # User Info
        self.username_label = tk.Label(self, text="Username:", bg="#ECF0F1", fg="#2C3E50")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(self, font=("Arial", 14))
        self.username_entry.pack(pady=5)

        self.age_label = tk.Label(self, text="Age:", bg="#ECF0F1", fg="#2C3E50")
        self.age_label.pack(pady=5)
        self.age_entry = tk.Entry(self, font=("Arial", 14))
        self.age_entry.pack(pady=5)

        self.gender_label = tk.Label(self, text="Gender (M/F):", bg="#ECF0F1", fg="#2C3E50")
        self.gender_label.pack(pady=5)
        self.gender_entry = tk.Entry(self, font=("Arial", 14))
        self.gender_entry.pack(pady=5)

        self.goals_label = tk.Label(self, text="Goals:", bg="#ECF0F1", fg="#2C3E50")
        self.goals_label.pack(pady=5)
        self.goals_entry = tk.Entry(self, font=("Arial", 14))
        self.goals_entry.pack(pady=5)

        self.login_button = tk.Button(self, text="Create Profile", font=("Arial", 18, "bold"), bg="#1ABC9C", fg="white", command=self.create_profile)
        self.login_button.pack(pady=20)

    def create_profile(self):
        """Handle profile creation logic"""
        username = self.username_entry.get()
        age = self.age_entry.get()
        gender = self.gender_entry.get()
        goals = self.goals_entry.get()

        if not username or not age or not gender or not goals:
            messagebox.showerror("Error", "All fields must be filled out.")
        elif not age.isdigit() or int(age) <= 0:
            messagebox.showerror("Error", "Please enter a valid age.")
        elif gender not in ["M", "F"]:
            messagebox.showerror("Error", "Please enter a valid gender (M/F).")
        else:
            messagebox.showinfo("Profile Created", f"Profile created successfully for {username}!")
            self.controller.user_info = {'username': username, 'age': age, 'gender': gender, 'goals': goals}
            self.controller.show_frame("HomePage")

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#ECF0F1")
        self.controller = controller

        # Centered App Name in Cyber Shield
        self.shield_frame = tk.Frame(self, bg="#ECF0F1")
        self.shield_frame.pack(pady=30, expand=True)

        # Cyber Shield Design
        self.shield_label = tk.Label(self.shield_frame, text="🛡️", font=("Arial", 100), bg="#ECF0F1", fg="#2C3E50")
        self.shield_label.pack(pady=10)

        self.app_name_label = tk.Label(self.shield_frame, text="Cyber Safety App", font=("Arial", 36, "bold"), bg="#ECF0F1", fg="#2C3E50")
        self.app_name_label.pack(pady=10)

class DailySessionsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#ECF0F1")
        self.controller = controller

        # Title
        self.label = tk.Label(self, text="Daily Cyber Safety Quiz", font=("Arial", 36, "bold"), bg="#ECF0F1", fg="#2C3E50")
        self.label.pack(pady=30)

        # Start Quiz Button
        self.start_quiz_button = tk.Button(self, text="Start Quiz", font=("Arial", 18, "bold"), bg="#1ABC9C", fg="white", command=self.start_quiz)
        self.start_quiz_button.pack(pady=20)

    def start_quiz(self):
        """Start the quiz and show the first question"""
        self.start_quiz_button.pack_forget()
        self.quiz = Quiz(self)
        self.quiz.start()

class Quiz:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.questions = [
            {"question": "What does HTTPS stand for?", "options": ["HyperText Transfer Protocol Secure", "HyperText Transfer Protocol Standard", "HyperText Transfer Protocol Site"], "answer": 0},
            {"question": "What is phishing?", "options": ["A type of fishing", "A technique used to trick people into giving sensitive information", "A method to catch fish"], "answer": 1},
            {"question": "What should you do if you receive an unexpected email asking for personal information?", "options": ["Respond with your details", "Ignore and delete the email", "Forward it to a friend"], "answer": 1},
            {"question": "What is a strong password?", "options": ["A password with at least 6 characters", "A password with a mix of letters, numbers, and symbols", "A password with your name and birthdate"], "answer": 1},
            {"question": "What is two-factor authentication?", "options": ["A method of verifying your identity with a password and a code", "A way to protect your phone from being stolen", "A technique to secure your Wi-Fi network"], "answer": 0},
            {"question": "What should you do if you think your account has been hacked?", "options": ["Change your password immediately", "Continue using it", "Contact the hacker"], "answer": 0},
            {"question": "What is a firewall?", "options": ["A type of antivirus software", "A system designed to prevent unauthorized access to your network", "A tool to clean your computer"], "answer": 1},
            {"question": "Why should you avoid using public Wi-Fi for banking?", "options": ["It is often unsecured and can be intercepted by attackers", "Public Wi-Fi is always secure", "It makes your phone run slower"], "answer": 0},
            {"question": "What is ransomware?", "options": ["Software that encrypts your files and demands payment to unlock them", "A type of antivirus program", "A technique used to steal your personal data"], "answer": 0},
            {"question": "How often should you update your software?", "options": ["As soon as updates are available", "Once a year", "Never"], "answer": 0},
        ]
        self.current_question = 0
        self.score = 0

    def start(self):
        """Display the first question"""
        self.display_question()

    def display_question(self):
        """Display the current question and options"""
        question_data = self.questions[self.current_question]
        question_text = question_data["question"]
        options = question_data["options"]

        # Clear previous question widgets if any
        for widget in self.parent_frame.winfo_children():
            widget.pack_forget()

        # Show the current question
        self.question_label = tk.Label(self.parent_frame, text=question_text, font=("Arial", 18, "bold"), bg="#ECF0F1", fg="#2C3E50")
        self.question_label.pack(pady=20)

        # Show the options
        self.option_buttons = []
        for index, option in enumerate(options):
            option_button = tk.Button(self.parent_frame, text=option, font=("Arial", 14), bg="white", fg="#2C3E50",
                                      command=lambda idx=index: self.check_answer(idx))
            option_button.pack(pady=5)
            self.option_buttons.append(option_button)

    def check_answer(self, selected_index):
        """Check if the selected answer is correct and update score"""
        correct_index = self.questions[self.current_question]["answer"]

        if selected_index == correct_index:
            self.score += 1
            self.option_buttons[selected_index].configure(bg="green", fg="white")
        else:
            self.option_buttons[selected_index].configure(bg="red", fg="white")
            self.option_buttons[correct_index].configure(bg="green", fg="white")

        # Move to the next question after a short delay
        self.parent_frame.after(1000, self.next_question)

    def next_question(self):
        """Move to the next question or show the final score"""
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.display_question()
        else:
            self.show_score()

    def show_score(self):
        """Display the final score after the quiz ends"""
        for widget in self.parent_frame.winfo_children():
            widget.pack_forget()

        score_text = f"Your final score is {self.score}/{len(self.questions)}"
        score_label = tk.Label(self.parent_frame, text=score_text, font=("Arial", 24, "bold"), bg="#ECF0F1", fg="#2C3E50")
        score_label.pack(pady=20)

        # Add a restart quiz button
        restart_button = tk.Button(self.parent_frame, text="Restart Quiz", font=("Arial", 18, "bold"), bg="#1ABC9C", fg="white", command=self.restart_quiz)
        restart_button.pack(pady=20)

    def restart_quiz(self):
        """Restart the quiz"""
        self.current_question = 0
        self.score = 0
        self.start()

class ProfilePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#ECF0F1")
        self.controller = controller

        # Title
        self.label = tk.Label(self, text="Profile", font=("Arial", 36, "bold"), bg="#ECF0F1", fg="#2C3E50")
        self.label.pack(pady=30)

        # User Information Labels
        self.username_label = tk.Label(self, text="Username: ", font=("Arial", 18), bg="#ECF0F1", fg="#2C3E50")
        self.username_label.pack(pady=5)

        self.age_label = tk.Label(self, text="Age: ", font=("Arial", 18), bg="#ECF0F1", fg="#2C3E50")
        self.age_label.pack(pady=5)

        self.gender_label = tk.Label(self, text="Gender: ", font=("Arial", 18), bg="#ECF0F1", fg="#2C3E50")
        self.gender_label.pack(pady=5)

        self.goals_label = tk.Label(self, text="Goals: ", font=("Arial", 18), bg="#ECF0F1", fg="#2C3E50")
        self.goals_label.pack(pady=5)

    def update_info(self):
        """Update the profile page with the user's information"""
        user_info = self.controller.user_info
        self.username_label.config(text=f"Username: {user_info.get('username', '')}")
        self.age_label.config(text=f"Age: {user_info.get('age', '')}")
        self.gender_label.config(text=f"Gender: {user_info.get('gender', '')}")
        self.goals_label.config(text=f"Goals: {user_info.get('goals', '')}")

class ScamDetectorPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#ECF0F1")
        self.controller = controller

        # Title
        self.label = tk.Label(self, text="Scam Detector", font=("Arial", 36, "bold"), bg="#ECF0F1", fg="#2C3E50")
        self.label.pack(pady=30)

        # Instruction
        self.instruction_label = tk.Label(self, text="Enter phone number or email to check for scams", font=("Arial", 18), bg="#ECF0F1", fg="#2C3E50")
        self.instruction_label.pack(pady=20)

        # Entry for phone number or email
        self.input_entry = tk.Entry(self, font=("Arial", 18), width=40)
        self.input_entry.pack(pady=10)

        # Detect button
        self.detect_button = tk.Button(self, text="Detect", font=("Arial", 18, "bold"), bg="#1ABC9C", fg="white", command=self.detect_scam)
        self.detect_button.pack(pady=20)

        # Result Label
        self.result_label = tk.Label(self, text="", font=("Arial", 18), bg="#ECF0F1", fg="#2C3E50")
        self.result_label.pack(pady=20)

    def detect_scam(self):
        input_value = self.input_entry.get()
        phone_pattern = r"^\+?[1-9]\d{1,14}$"
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        if re.match(phone_pattern, input_value):
            self.result_label.config(text=f"Phone number '{input_value}' is not detected as a scam.")
        elif re.match(email_pattern, input_value):
            self.result_label.config(text=f"Email '{input_value}' is not detected as a scam.")
        else:
            self.result_label.config(text="Invalid input. Please enter a valid phone number or email.")

if __name__ == "__main__":
    app = CyberSafetyApp()
    app.mainloop()



