import smtplib
import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime, timedelta
import smtpd
from email.mime.text import MIMEText
import matplotlib.pyplot as plt
from threading import Timer

from matplotlib.backend_tools import cursors

conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS tasks
               (id INTEGER PRIMARY KEY, title TEXT, description TEXT, deadline TEXT, priority TEXT, status TEXT)''')
conn.commit()

def add_task(title, description, deadline, priority):
    cursor.execute("INSERT INTO tasks (title, description, deadline, priority, status) VALUES (?, ?, ?, ?, ?)",
                   (title, description, deadline, priority, 'Pending'))
    conn.commit()

def get_today_tasks():
    today = datetime.now().strftime('%Y-%m-%d')
    cursor.execute("SELECT * FROM tasks WHERE deadline=?", (today,))
    return cursor.fetchall()
def send_email_reminder(task):
    sender = "ak1287@g.rit.edu"
    reciever = "akhliddinqoziboyev@gmail.com"
    msg = MIMEText(f"Reminder: You have a task '{task[1]}' due on {task[3]}. ")
    msg['Subject'] = 'Task Reminder'
    msg['From'] = sender
    msg['To'] = reciever

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender, "ak1287")
            server.send_message(sender, reciever, msg.as_string())
        print('Email sent successfully !')
    except Exception as e:
        print(f"Error sending email: {e}")

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Task Manager")

        self.title_label = tk.Label(root, text="Task Title")
        self.title_label.pack()
        self.title_entry = tk.Entry(root)
        self.title_entry.pack()


        self.desc_label = tk.Label(root, text="Task Description")
        self.desc_label.pack()
        self.desc_entry = tk.Entry(root)
        self.desc_entry.pack()


        self.date_label = tk.Label(root, text="Deadline (YYYY-MM-DD)")
        self.date_label.pack()
        self.date_entry = tk.Entry(root)
        self.date_entry.pack()

        self.priority_label = tk.Label(root, text="Priority (Low, Medium, High)")
        self.priority_label.pack()
        self.priority_entry = tk.Entry(root)
        self.priority_entry.pack()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_tasks)
        self.add_button.pack()

        self.show_task_button = tk.Button(root, text="Show Today's Tasks", command=self.show_task)
        self.show_task_button.pack()

def add_task(self):
    title = self.title_entry.get()
    description = self.desc_entry.get()
    deadline = self.date_entry.get()
    priority = self.priority_entry.get()

    if title and description and deadline and priority:
        add_task(title, description, deadline, priority)
        messagebox.showinfo("Success", "Task added successfully !")
        self.clear_entries()
    else:
        messagebox.showwarning("Error", "All fields are required !")

def show_tasks(self):
    tasks = get_today_tasks()
    if tasks:
        tasks_str = "\n".join([f"{task[1]} (Due: {task[3]}, Priority: {task[4]})" for task in tasks])
        messagebox.showinfo("Today's Tasks", tasks_str)
    else:
        messagebox.showinfo("No Tasks", "No tasks for today !")

def clear_entries(self):
    self.title_entry.delete(0, tk.END)
    self.desc_entry.delete(0, tk.END)
    self.date_entry.delete(0, tk.END)
    self.priority_entry.delete(0, tk.END)

def plot_progress():
    cursor.execute("SELECT status, COUNT(*) FROM tasks GROUP BY status")
    data = cursor.fetchall()
    labels = [row[0] for row in data]
    sizes = [row[1] for row in data]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title("Task Completion Progress")
    plt.show()

def setup_reminders():
    cursor.execute("SELECT * FROM tasks WHERE deadline = ?", ((datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d'),))
    tasks = cursor.fetchall()
    for task in tasks:
        Timer(5, send_email_reminder, args=(task,)).start()


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)

    setup_reminders()
    root.mainloop()
    conn.close()