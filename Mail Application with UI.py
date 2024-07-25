import sqlite3

def init_db():
    conn = sqlite3.connect('mail_app.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS smtp_settings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            smtp_server TEXT NOT NULL,
            smtp_port INTEGER NOT NULL,
            smtp_user TEXT NOT NULL,
            smtp_password TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')
    conn.commit()
    conn.close()
import tkinter as tk
from tkinter import messagebox

class MailApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mail Application")

        self.username_label = tk.Label(root, text="Username")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(root)
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(root, text="Password")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(root, show='*')
        self.password_entry.pack(pady=5)

        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # For simplicity, skipping actual user authentication
        if username and password:
            self.show_smtp_config()
        else:
            messagebox.showerror("Error", "Please enter username and password")

    def show_smtp_config(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.smtp_server_label = tk.Label(self.root, text="SMTP Server")
        self.smtp_server_label.pack(pady=5)
        self.smtp_server_entry = tk.Entry(self.root)
        self.smtp_server_entry.pack(pady=5)

        self.smtp_port_label = tk.Label(self.root, text="SMTP Port")
        self.smtp_port_label.pack(pady=5)
        self.smtp_port_entry = tk.Entry(self.root)
        self.smtp_port_entry.pack(pady=5)

        self.smtp_user_label = tk.Label(self.root, text="SMTP User")
        self.smtp_user_label.pack(pady=5)
        self.smtp_user_entry = tk.Entry(self.root)
        self.smtp_user_entry.pack(pady=5)

        self.smtp_password_label = tk.Label(self.root, text="SMTP Password")
        self.smtp_password_label.pack(pady=5)
        self.smtp_password_entry = tk.Entry(self.root, show='*')
        self.smtp_password_entry.pack(pady=5)

        self.save_button = tk.Button(self.root, text="Save and Send Email", command=self.save_smtp_config)
        self.save_button.pack(pady=20)

    def save_smtp_config(self):
        smtp_server = self.smtp_server_entry.get()
        smtp_port = self.smtp_port_entry.get()
        smtp_user = self.smtp_user_entry.get()
        smtp_password = self.smtp_password_entry.get()

        if smtp_server and smtp_port and smtp_user and smtp_password:
            self.send_email(smtp_server, smtp_port, smtp_user, smtp_password)
        else:
            messagebox.showerror("Error", "Please fill all SMTP settings")

    def send_email(self, smtp_server, smtp_port, smtp_user, smtp_password):
        import smtplib
        from email.mime.text import MIMEText

        msg = MIMEText("This is a test email")
        msg['Subject'] = 'Test Email'
        msg['From'] = smtp_user
        msg['To'] = smtp_user

        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_user, smtp_password)
                server.sendmail(smtp_user, [smtp_user], msg.as_string())
                messagebox.showinfo("Success", "Email sent successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = MailApp(root)
    root.mainloop()

