import csv
import datetime

work_sessions = []
def start_work_session(task_name):
    start_time = datetime.datetime.now()
    session = {'task name': task_name, 'start time': start_time, 'end time': None}
    work_sessions.append(session)
    print(f"Started working on '{task_name}' at {start_time}")
    return session

def end_work_session(session):
    end_time = datetime.datetime.now()
    duration = end_time - session['start_time']

    session['end_time'] = end_time
    session['duration'] = duration
    print(f"Ended work on '{session['task_name']}' at {end_time}")
    print(f"Duration: {duration}")

def display_total_hours():
    total_duration = datetime.timedelta()
    for session in work_sessions:
        total_duration += session['duration']
    print(f"Total time worked: {total_duration}")

def save_sessions_to_cv():
    with open('work_hours.cv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Task', 'Start Time', 'End Time', 'Duration'])
        for session in work_sessions:
            writer.writerow([session['task name'], session['start time'], session['end time'], session['duration']])
    print("Work sessions saved to work_hours.csv")

if __name__ == "__main__":
    session1 = start_work_session('Project A')
    session2 = start_work_session('Project B')
    import time
    time.sleep(2)
    end_work_session(session1)
    time.sleep(3)
    end_work_session(session2)
    display_total_hours()
    save_sessions_to_cv()