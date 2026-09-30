import time

def get_valid_duration():
    while True:
        try:
            user_input = input("Enter duration in minutes (or 'q' to quit): ").lower()
            if user_input == 'q':
                return 'q'
            
            minutes = int(user_input)
            if minutes > 0:
                return minutes
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number or 'q'.")

def study_timer():
    print("--- Study Timer ---")
    
    while True:
        duration = get_valid_duration()
        if duration == 'q':
            break
            
        task_name = input("Enter task name (e.g., Math, History): ")
        
        print(f"\nGet ready to focus on '{task_name}' for {duration} minutes.")
        input("Press Enter to start...")
        
        total_seconds = duration * 60
        
        start_time = time.time()
        end_time = start_time + total_seconds
        
        while time.time() < end_time:
            remaining_seconds = int(end_time - time.time())
            
            minutes_left = remaining_seconds // 60
            seconds_left = remaining_seconds % 60
            
            timer_display = f"{minutes_left:02d}:{seconds_left:02d}"
            
            print(timer_display, end="\r")
            time.sleep(1)
            
        print("\n⏰ Time's up! Great job completing the session.")
        
        with open("study_log.txt", "a") as log_file:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            log_file.write(f"Task: {task_name} | Duration: {duration} mins | Completed: {timestamp}\n")
        print("Session logged to 'study_log.txt'.")
        
        play_again = input("Start another session? (y/n): ").lower()
        if play_again != 'y':
            break

    print("\nGoodbye!")

if __name__ == "__main__":
    study_timer()