import tkinter as tk
from tkinter import messagebox, filedialog
import datetime
import time
import threading
from playsound import playsound
import os

# --- Global Variables ---
alarm_thread = None # To store the alarm checking thread
alarm_active = False # Flag to indicate if an alarm is currently ringing
alarm_sound_path = "alarm.mp3" # Default sound file
snooze_duration_minutes = 5

# --- Helper Functions ---

def play_alarm_sound():
    """Plays the alarm sound repeatedly until stopped."""
    global alarm_active
    alarm_active = True
    print(f"Playing alarm sound: {alarm_sound_path}")
    while alarm_active:
        try:
            playsound(alarm_sound_path)
            # Short pause to prevent replaying too quickly if playsound finishes fast
            time.sleep(1) 
        except Exception as e:
            print(f"Error playing sound: {e}")
            messagebox.showerror("Sound Error", f"Could not play sound: {e}\nPlease check the file path.")
            break # Stop trying to play if there's an error

def stop_alarm_sound():
    """Stops the alarm sound and resets the active flag."""
    global alarm_active
    alarm_active = False
    print("Alarm sound stopped.")
    # You might need to kill the playsound process if it's blocking
    # playsound doesn't offer a clean stop for ongoing playback.
    # For more control, consider pygame.mixer or pydub.

def alarm_check_loop(target_hour, target_minute):
    """The thread function that continuously checks the time."""
    global alarm_active
    print(f"Alarm check thread started for {target_hour:02d}:{target_minute:02d}")
    
    while True:
        now = datetime.datetime.now()
        current_hour = now.hour
        current_minute = now.minute

        # If the alarm has passed for today, but we are still checking,
        # and it's not set for tomorrow, we might need a better way to handle
        # one-time vs. recurring. For simplicity, this is a one-time alarm.
        
        if current_hour == target_hour and current_minute == target_minute:
            print("Alarm triggered!")
            # Stop any previous alarm sounds if active
            stop_alarm_sound() 
            
            # Start playing sound in a new thread to keep GUI responsive
            threading.Thread(target=play_alarm_sound, daemon=True).start()
            
            # Show the dismiss/snooze pop-up
            show_alarm_popup(target_hour, target_minute)
            break # Exit this alarm's check loop

        # Check every few seconds
        time.sleep(5) 

def set_new_alarm():
    """Reads input and sets a new alarm."""
    global alarm_thread

    try:
        hour = int(hour_entry.get())
        minute = int(minute_entry.get())

        if not (0 <= hour <= 23 and 0 <= minute <= 59):
            messagebox.showerror("Invalid Time", "Please enter valid hour (0-23) and minute (0-59).")
            return

        # Stop any existing alarm thread before starting a new one for simplicity
        # For multiple alarms, you'd manage a list of threads
        if alarm_thread and alarm_thread.is_alive():
            # In a real app, you'd manage multiple alarms, not just replace
            # For this simple example, we'll just stop the previous one if it exists.
            # However, playsound might block the thread, making it hard to stop gracefully.
            # A more robust solution involves a queue of alarms and one controlling thread.
            pass # We'll just let the old thread run its course if it's not the alarm time yet.

        # Start the alarm checking in a new daemon thread
        # A daemon thread will exit automatically when the main program exits.
        alarm_thread = threading.Thread(target=alarm_check_loop, args=(hour, minute), daemon=True)
        alarm_thread.start()
        
        status_label.config(text=f"Alarm set for: {hour:02d}:{minute:02d}")
        messagebox.showinfo("Alarm Set", f"Alarm successfully set for {hour:02d}:{minute:02d}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for hour and minute.")

def choose_sound_file():
    """Opens a file dialog to choose an alarm sound."""
    global alarm_sound_path
    filename = filedialog.askopenfilename(
        title="Select Alarm Sound",
        filetypes=(("MP3 files", "*.mp3"), ("WAV files", "*.wav"), ("All files", "*.*"))
    )
    if filename:
        alarm_sound_path = filename
        sound_label.config(text=f"Sound: {os.path.basename(filename)}")
        messagebox.showinfo("Sound Chosen", f"Alarm sound set to: {os.path.basename(filename)}")

# --- Alarm Pop-up Window ---
def show_alarm_popup(alarm_hour, alarm_minute):
    """Creates and displays the alarm dismissal/snooze popup."""
    popup_window = tk.Toplevel(root)
    popup_window.title("ALARM!")
    popup_window.geometry("400x200")
    popup_window.attributes('-topmost', True) # Keep on top of other windows
    
    # Optionally make it full screen or bring to front more aggressively
    # popup_window.attributes('-fullscreen', True) # Use with caution!
    popup_window.lift()
    popup_window.focus_force() # Force focus to this window

    tk.Label(popup_window, text=f"It's {alarm_hour:02d}:{alarm_minute:02d}!", font=("Arial", 24, "bold"), fg="red").pack(pady=10)

    def dismiss_alarm():
        stop_alarm_sound()
        popup_window.destroy()

    def snooze_alarm():
        stop_alarm_sound()
        popup_window.destroy()
        
        now = datetime.datetime.now()
        snooze_time = now + datetime.timedelta(minutes=snooze_duration_minutes)
        snooze_hour = snooze_time.hour
        snooze_minute = snooze_time.minute
        
        # Start a new alarm check thread for the snoozed time
        threading.Thread(target=alarm_check_loop, args=(snooze_hour, snooze_minute), daemon=True).start()
        status_label.config(text=f"Snoozed! Next alarm: {snooze_hour:02d}:{snooze_minute:02d}")
        messagebox.showinfo("Snoozed", f"Alarm snoozed for {snooze_duration_minutes} minutes. Next alarm at {snooze_hour:02d}:{snooze_minute:02d}")


    tk.Button(popup_window, text="Dismiss", command=dismiss_alarm, font=("Arial", 16), bg="green", fg="white", padx=20, pady=10).pack(side=tk.LEFT, padx=20)
    tk.Button(popup_window, text=f"Snooze ({snooze_duration_minutes} min)", command=snooze_alarm, font=("Arial", 16), bg="blue", fg="white", padx=20, pady=10).pack(side=tk.RIGHT, padx=20)

    # Make sure the popup closes if the user closes it manually
    popup_window.protocol("WM_DELETE_WINDOW", dismiss_alarm)


# --- Main GUI Setup ---
root = tk.Tk()
root.title("Python PC Alarm")
root.geometry("400x300")

# Input Frame
input_frame = tk.Frame(root, padx=10, pady=10)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Set Alarm Time:").grid(row=0, column=0, columnspan=2, pady=5)

tk.Label(input_frame, text="Hour (0-23):").grid(row=1, column=0, sticky="w")
hour_entry = tk.Entry(input_frame, width=5)
hour_entry.grid(row=1, column=1, sticky="ew")

tk.Label(input_frame, text="Minute (0-59):").grid(row=2, column=0, sticky="w")
minute_entry = tk.Entry(input_frame, width=5)
minute_entry.grid(row=2, column=1, sticky="ew")

set_button = tk.Button(input_frame, text="Set Alarm", command=set_new_alarm)
set_button.grid(row=3, column=0, columnspan=2, pady=10)

# Sound Selection
sound_frame = tk.Frame(root, padx=10, pady=5)
sound_frame.pack(pady=5)

sound_label = tk.Label(sound_frame, text=f"Sound: {os.path.basename(alarm_sound_path)}")
sound_label.pack(side=tk.LEFT)
sound_button = tk.Button(sound_frame, text="Change Sound", command=choose_sound_file)
sound_button.pack(side=tk.RIGHT, padx=10)

# Status Label
status_label = tk.Label(root, text="No alarm set.", font=("Arial", 12))
status_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()