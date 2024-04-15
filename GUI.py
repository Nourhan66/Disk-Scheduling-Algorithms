from pathlib import Path
from tkinter import Tk, Canvas, Entry, Label, Button, PhotoImage, StringVar, OptionMenu, Toplevel
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from SCAN import *
from CSCAN import *
from LOOK import *
from CLOOK import *
from SSTF import *
from FCFS import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"F:\Nourhan\LastTerm\Advanced OS\Labs\Disk Scheduling Algorithms\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def display_results():
    head = int(entry_2.get())
    direction=""
    requests_input = entry_1.get()
    selected_algorithm = selected_option.get()

    if selected_algorithm == "FCFS":
        seek_sequence, total_seek_time = FCFS(head, requests_input)
    elif selected_algorithm == "SSTF":
        seek_sequence, total_seek_time = SSTF(head, requests_input)
    elif selected_algorithm == "SCAN" :
        direction = entry_5.get()  # Read direction from text entry field
        max_tracks = entry_6.get()    # Read max_tracks from text entry field
        seek_sequence, total_seek_time = SCAN(head, requests_input, direction, max_tracks)
    elif selected_algorithm == "C-SCAN":
        direction = entry_5.get()  # Read direction from text entry field
        max_tracks = entry_6.get()    # Read max_tracks from text entry field
        seek_sequence, total_seek_time = CSCAN(requests_input,head,  direction, max_tracks)
    elif selected_algorithm == "LOOK":
        direction = entry_5.get()  # Read direction from text entry field
        seek_sequence, total_seek_time = LOOK(head, requests_input, direction)
    elif selected_algorithm == "C-LOOK":
        direction = entry_5.get()  # Read direction from text entry field
        seek_sequence, total_seek_time = CLOOK(requests_input,head,  direction)
    # Add other algorithms here as needed

    output_1.config(text=f'Seek Sequence: {" ".join(map(str, seek_sequence))}')
    output_2.config(text=f'Total Seek Time: {total_seek_time}')

    plot_request_list(seek_sequence,selected_algorithm,direction)

def plot_request_list(requests_input,s,d):
    # Parse request list
    requests_list = requests_input

    # Create a new window for plotting
    plot_window = Toplevel(window)
    if d=='rigth':
        d='right'
    elif d=='left':
        d='left'
    t = "Plot for "+d+" "+s
    plot_window.title("Request Plot")

    # Create a figure and plot
    fig = Figure(figsize=(6, 4))
    plot = fig.add_subplot(111)
    plot.plot(requests_list, marker='o', linestyle='-')

    # Customize plot
    plot.set_title(t)
    plot.set_xlabel("Request Index")
    plot.set_ylabel("Track Number")
    plot.grid(True)

    # Embed the plot into Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=plot_window)
    canvas.draw()
    canvas.get_tk_widget().pack()


window = Tk()

window.geometry("757x705")
window.configure(bg="#FFFFFF")

window.title("Disc Schedualing")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 732,
    width = 757,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    378.0,
    366.0,
    image=image_image_1
)

canvas.create_text(
    219.0,
    39.0,
    anchor="nw",
    text="Enter the requests (space-separated)",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
)

canvas.create_text(
    280.0,
    128.0,
    anchor="nw",
    text="Enter the head position",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    384.0,
    95.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=228.0,
    y=78.0,
    width=312.0,
    height=32.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    384.0,
    183.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=228.0,
    y=167.0,
    width=312.0,
    height=30.0
)

canvas.create_text(
    308.0,
    214.0,
    anchor="nw",
    text="Select Algorithm",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
)

entry_5 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)

entry_6 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)

entry_bg_5 = None
entry_bg_6 = None
def select_algorithm(*args):
    global entry_5, entry_6, entry_bg_5, entry_bg_6, text_label_5, text_label_6
    selected_option_value = selected_option.get()

    # Remove any previous instances of entry fields and text labels
    entry_5.place_forget()
    entry_6.place_forget()
    if entry_bg_5:
        canvas.delete(entry_bg_5)
    if entry_bg_6:
        canvas.delete(entry_bg_6)
    if 'text_label_5' in globals() or 'text_label_5' in locals():
        canvas.delete(text_label_5)
    if 'text_label_6' in globals() or 'text_label_6' in locals():
        canvas.delete(text_label_6)

    if selected_option_value in ["FCFS", "SSTF"]:
        entry_1.place(x=228.0, y=78.0, width=312.0, height=32.0)
        entry_2.place(x=228.0, y=167.0, width=312.0, height=30.0)
        button_1.config(command=display_results)
        output_1.place(x=138.0, y=417.0, width=482.0, height=38.0)
        output_2.place(x=138.0, y=482.0, width=482.0, height=38.0)
    elif selected_option_value in ["SCAN","C-SCAN"]:
        entry_1.place(x=228.0, y=78.0, width=312.0, height=32.0)
        entry_2.place(x=228.0, y=167.0, width=312.0, height=30.0)

        # Display entry fields and text for SCAN
        entry_5.place(x=296.0, y=570.0, width=166.0, height=38.0)
        entry_image_5 = PhotoImage(file=relative_to_assets("entry_5.png"))
        entry_bg_5 = canvas.create_image(379.0, 590.0, image=entry_image_5)

        text_label_5 = canvas.create_text(
            296.0,
            533.0,
            anchor="nw",
            text="Enter Direction (right/left)",
            fill="#FFFFFF",
            font=("Inter", 18 * -1)
        )

        entry_6.place(x=296.0, y=670.0, width=166.0, height=38.0)
        entry_image_6 = PhotoImage(file=relative_to_assets("entry_6.png"))
        entry_bg_6 = canvas.create_image(379.0, 690.0, image=entry_image_6)

        text_label_6 = canvas.create_text(
            259.0,
            636.0,
            anchor="nw",
            text="Enter total number of tracks",
            fill="#FFFFFF",
            font=("Inter", 18 * -1)
        )

        button_1.config(command=display_results)
        output_1.place(x=138.0, y=417.0, width=482.0, height=38.0)
        output_2.place(x=138.0, y=482.0, width=482.0, height=38.0)

    elif selected_option_value in ["LOOK","C-LOOK"]:
        entry_1.place(x=228.0, y=78.0, width=312.0, height=32.0)
        entry_2.place(x=228.0, y=167.0, width=312.0, height=30.0)

        # Display entry fields and text for LOOK
        entry_5.place(x=296.0, y=570.0, width=166.0, height=38.0)
        entry_image_5 = PhotoImage(file=relative_to_assets("entry_5.png"))
        entry_bg_5 = canvas.create_image(379.0, 590.0, image=entry_image_5)

        text_label_5 = canvas.create_text(
            296.0,
            533.0,
            anchor="nw",
            text="Enter Direction (right/left)",
            fill="#FFFFFF",
            font=("Inter", 18 * -1)
        )

        button_1.config(command=display_results)
        output_1.place(x=138.0, y=417.0, width=482.0, height=38.0)
        output_2.place(x=138.0, y=482.0, width=482.0, height=38.0)
    else:
        entry_1.place_forget()
        entry_2.place_forget()
        button_1.config(command=lambda: print("Button clicked"))
        output_1.place_forget()
        output_2.place_forget()

        if selected_option_value in ["C-SCAN", "SCAN"]:
            # Display entry fields and text for direction and total number of tracks
            canvas.create_text(
                296.0,
                533.0,
                anchor="nw",
                text="Enter Direction (right/left)",
                fill="#FFFFFF",
                font=("Inter", 18 * -1)
            )
            entry_5.place(
                x=296.0,
                y=570.0,
                width=166.0,
                height=38.0
            )

            canvas.create_text(
                259.0,
                636.0,
                anchor="nw",
                text="Enter total number of tracks",
                fill="#FFFFFF",
                font=("Inter", 18 * -1)
            )
            entry_6.place(
                x=296.0,
                y=670.0,
                width=166.0,
                height=38.0
            )
        elif selected_option_value in ["C-LOOK", "LOOK"]:
            # Display entry fields and text for direction and total number of tracks
            canvas.create_text(
                296.0,
                533.0,
                anchor="nw",
                text="Enter Direction (i/o)",
                fill="#FFFFFF",
                font=("Inter", 18 * -1)
            )
            entry_5.place(
                x=296.0,
                y=570.0,
                width=166.0,
                height=38.0
            )

canvas.create_text(
    308.0,
    214.0,
    anchor="nw",
    text="Select Algorithm",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
)

# Define the options for the dropdown
options = ["FCFS", "SSTF", "SCAN", "LOOK", "C-SCAN", "C-LOOK"]

# Create a tkinter variable to hold the selected option
selected_option = StringVar(window)

# Set default value for the dropdown
selected_option = StringVar(window, "")

# Create the dropdown menu
dropdown_menu = OptionMenu(window, selected_option, *options, command=select_algorithm)
dropdown_menu.configure(bg="#D9D9D9", fg="#000716", highlightthickness=0)
dropdown_menu.place(x=280, y=250, width=200, height=32)  # Adjusted y-coordinate and size


button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))

# Function to execute when the button is clicked
def button_click():
    print("button_1 clicked")

# Create a round button
button_1 = Button(
    window,
    text="Display results",
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=button_click,
    relief="flat",
    compound="center",  # Place the text at the center of the button
)

# Set the button size and position
button_1.place(
    x=308,  # Adjusted x-coordinate
    y=320,  # Adjusted y-coordinate
    width=120.0,
    height=54  # Adjust the height to match the width for a perfect circle
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    379.0,
    437.0,
    image=entry_image_3
)


output_1 = Label(
        window,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        bd=0,
        relief="flat",
        text="",
        wraplength=200,  # Adjust the width of the label
        justify="left",  # Align the text to the left
        font=("Inter", 12)
    )
output_1.place(
    x=138.0,
    y=417.0,
    width=482.0,
    height=38.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    379.0,
    502.0,
    image=entry_image_4
)
output_2 = Label(
        window,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        bd=0,
        relief="flat",
        text="",
        wraplength=200,  # Adjust the width of the label
        justify="left",  # Align the text to the left
        font=("Inter", 12)
    )
output_2.place(
    x=138.0,
    y=482.0,
    width=482.0,
    height=38.0
)


window.resizable(False, False)
window.mainloop()
