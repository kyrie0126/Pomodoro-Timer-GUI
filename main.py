import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#F8C4B4"
GREEN = "#A1C298"
LIGHT_GREEN = "#C6EBC5"
YELLOW = "#FBF2CF"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    # stop the countdown
    window.after_cancel(timer)
    # timer_text 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # title_label "Timer"
    title_label.config(text="Timer")
    # reset checkmarks
    check_label.config(text="")
    # reset reps
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps
    reps += 1
    print(reps)

    if reps % 8 == 0:
        countdown(int(LONG_BREAK_MIN * 60))
        title_label.config(text="Long Break", font=(FONT_NAME, 30, "bold"), fg=PINK, bg=YELLOW)
    elif reps % 2 == 0:
        countdown(int(SHORT_BREAK_MIN * 60))
        title_label.config(text="Short Break", font=(FONT_NAME, 30, "bold"), fg=PINK, bg=YELLOW)
    else:
        countdown(int(WORK_MIN * 60))
        title_label.config(text="Work Period", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    # count is entered as minute
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    for i in range(1, 10):
        if count_sec == i:
            count_sec = f"0{i}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start()
        marks = ""
        for i in range(math.floor(reps/2)):
            marks += "✔"
        check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
# window setup
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# background image and timer
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # about same height as image
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# label
title_label = tk.Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

check_label = tk.Label(text="", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)


# buttons
start_button = tk.Button(text="Start", command=start, bg=LIGHT_GREEN, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", command=reset, bg=PINK, highlightthickness=0)
reset_button.grid(column=2, row=2)


window.mainloop()
