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
            {"question": "How often should you update your software?", "options": ["As soon as updates are available", "Only when you notice a problem", "Never, if it seems to be working fine"], "answer": 0}
        ]
        self.current_question = 0
        self.score = 0

        self.frame = tk.Frame(self.parent_frame, bg="#ECF0F1")
        self.frame.pack(expand=True, fill="both")

        self.question_label = tk.Label(self.frame, text="", font=("Arial", 24), bg="#ECF0F1", fg="#2C3E50")
        self.question_label.pack(pady=20)

        self.options_frame = tk.Frame(self.frame, bg="#ECF0F1")
        self.options_frame.pack(pady=20)

        self.restart_button = tk.Button(self.frame, text="Restart Quiz", font=("Arial", 18, "bold"), bg="#1ABC9C", fg="white", command=self.restart_quiz)
        self.restart_button.pack(pady=20)
        self.restart_button.pack_forget()  # Hide the button initially

    def start(self):
        """Start the quiz"""
        self.show_question()

    def show_question(self):
        """Display the current question and options"""
        question = self.questions[self.current_question]
        self.question_label.config(text=question["question"])

        for widget in self.options_frame.winfo_children():
            widget.destroy()

        for index, option in enumerate(question["options"]):
            tk.Button(self.options_frame, text=option, font=("Arial", 14), bg="#3498DB", fg="white", command=lambda idx=index: self.check_answer(idx)).pack(pady=5, fill="x")

    def check_answer(self, selected_option):
        """Check if the selected answer is correct"""
        correct_option = self.questions[self.current_question]["answer"]
        if selected_option == correct_option:
            self.score += 1

        self.current_question += 1
        if self.current_question < len(self.questions):
            self.show_question()
        else:
            self.show_result()

    def show_result(self):
        """Show the final score and a message"""
        score_message = f"Your score: {self.score} out of {len(self.questions)}"
        messagebox.showinfo("Quiz Completed", score_message)
        self.restart_button.pack(pady=20)  # Show the Restart Quiz button

    def restart_quiz(self):
        """Restart the quiz"""
        self.current_question = 0
        self.score = 0
        self.show_question()

class ProfilePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#ECF0F1")
        self.controller = controller

        # Title
        self.label = tk.Label(self, text="Profile", font=("Arial", 36, "bold"), bg="#ECF0F1", fg="#2C3E50")
        self.label.pack(pady=30)

        self.username_label = tk.Label(self, text="", font=("Arial", 18), bg="#ECF0F1", fg="#2C3E50")
        self.username_label.pack(pady=5)

        self.age_label = tk.Label(self, text="", font=("Arial", 18), bg="#ECF0F1", fg="#2C3E50")
        self.age_label.pack(pady=5)

        self.gender_label = tk.Label(self, text="", font=("Arial", 18), bg="#ECF0F1", fg="#2C3E50")
        self.gender_label.pack(pady=5)

        self.goals_label = tk.Label(self, text="", font=("Arial", 18), bg="#ECF0F1", fg="#2C3E50")
        self.goals_label.pack(pady=5)

    def update_info(self):
        """Update the profile information from user_info"""
        user_info = self.controller.user_info
        if user_info:
            self.username_label.config(text=f"Username: {user_info.get('username', 'Not Set')}")
            self.age_label.config(text=f"Age: {user_info.get('age', 'Not Set')}")
            self.gender_label.config(text=f"Gender: {user_info.get('gender', 'Not Set')}")
            self.goals_label.config(text=f"Goals: {user_info.get('goals', 'Not Set')}")

class ScamDetectorPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#ECF0F1")
        self.controller = controller

        # Title
        self.label = tk.Label(self, text="Scam Detector", font=("Arial", 36, "bold"), bg="#ECF0F1", fg="#2C3E50")
        self.label.pack(pady=30)

        # Email Detection
        self.email_label = tk.Label(self, text="Enter an email to check for scams:", bg="#ECF0F1", fg="#2C3E50")
        self.email_label.pack(pady=10)
        self.email_entry = tk.Entry(self, font=("Arial", 14))
        self.email_entry.pack(pady=5)
        self.email_check_button = tk.Button(self, text="Check Email", font=("Arial", 14), bg="#1ABC9C", fg="white", command=self.check_email)
        self.email_check_button.pack(pady=10)

        self.email_result = tk.Label(self, text="", bg="#ECF0F1", fg="#2C3E50")
        self.email_result.pack(pady=10)

        # Phone Number Detection
        self.phone_label = tk.Label(self, text="Enter a phone number to check for scams:", bg="#ECF0F1", fg="#2C3E50")
        self.phone_label.pack(pady=10)
        self.phone_entry = tk.Entry(self, font=("Arial", 14))
        self.phone_entry.pack(pady=5)
        self.phone_check_button = tk.Button(self, text="Check Phone Number", font=("Arial", 14), bg="#1ABC9C", fg="white", command=self.check_phone_number)
        self.phone_check_button.pack(pady=10)

        self.phone_result = tk.Label(self, text="", bg="#ECF0F1", fg="#2C3E50")
        self.phone_result.pack(pady=10)

    def check_email(self):
        email = self.email_entry.get()
        if self.is_scam_email(email):
            self.email_result.config(text="This email is likely a scam.", fg="#E74C3C")
        else:
            self.email_result.config(text="This email seems safe.", fg="#2ECC71")

    def check_phone_number(self):
        phone_number = self.phone_entry.get()
        if self.is_scam_phone_number(phone_number):
            self.phone_result.config(text="This phone number is likely a scam.", fg="#E74C3C")
        else:
            self.phone_result.config(text="This phone number seems safe.", fg="#2ECC71")

    def is_scam_email(self, email):
        # Basic email validation
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return not re.match(pattern, email)

    def is_scam_phone_number(self, phone_number):
        # Basic phone number validation
        pattern = r'^\+?[1-9]\d{1,14}$'
        return not re.match(pattern, phone_number)

if __name__ == "__main__":
    app = CyberSafetyApp()
    app.mainloop()
