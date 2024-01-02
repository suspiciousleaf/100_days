from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
running = False

# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    global reps, running
    running = False
    reps = 0
    canvas.itemconfig(timer_text, text="Begin!")
    label_ticks.config(text="")
    label_timer.config(text="Timer", fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps, running
    running = True
    if reps > 8:
        reset()
    elif reps == 8:
        label_timer.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN)  # * 60)
    elif reps % 2 == 1:
        label_timer.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN)  # * 60)
    else:
        label_timer.config(text="Work", fg=GREEN)
        count_down(WORK_MIN)  # * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global reps, running
    check_mark = "✔"

    if running:
        convert = time.strftime("%M:%S", time.gmtime(count))
        canvas.itemconfig(timer_text, text=convert)

        if count >= 0:
            window.after(1000, count_down, count - 1)
        else:
            reps += 1
            if reps % 2 == 1:
                label_ticks.config(text=((reps // 2) + 1) * check_mark)
            start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="day_28/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="Begin!", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)


label_timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
label_timer.grid(column=1, row=0)

label_ticks = Label(
    text="", fg=GREEN, bg=YELLOW, highlightthickness=0, font=("Arial", 12)
)
label_ticks.grid(column=1, row=3)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)


window.mainloop()
