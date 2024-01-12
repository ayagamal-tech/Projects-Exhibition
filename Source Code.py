from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from tkinter import messagebox
import webbrowser

#menu1 : main menu for level selection
#menu2 : projects selection


#A:heart sensor
#B:RC car
#C:home security
#D:laser tripwire alarm
#E:glasses for the blind

class Project: #to prevent repetetion
    def __init__(self, description=None, members=None):
        self.description = description if description is not None else []
        self.members = members if members is not None else []

    def set_description(self, description):
        self.description = description

    def set_members(self, members):
        self.members = members

## File handling ##
projects = [Project()] * 6

current_project_number = 0

with open("Description for all projects.txt", "r", encoding="utf-8") as description_file, \
        open("Members for all projects.txt", "r", encoding="utf-8") as members_file:

    for num in range(6):
        projects[current_project_number] = Project()
        current_project_description = []

        # Read details for the current project
        for line in description_file:
            current_project_description.append(line.rstrip(f"#{chr(ord('A')+current_project_number)})"))
            if line.startswith("#") :
                projects[current_project_number].set_description(current_project_description)
                current_project_number += 1
                break
    projects[current_project_number].set_description(current_project_description)


    current_project_number = 0
    for num in range(6):
        current_project_members = []

        # Read members for the current project
        for line in members_file:
            current_project_members.append(line.rstrip(f"#{chr(ord('A')+current_project_number)}"))
            if line.startswith("#"):
                projects[current_project_number].set_members(current_project_members)
                current_project_number += 1
                break
        projects[current_project_number].set_members(current_project_members)
### End of file handling ###


# List for Repo links
repo_links = [
    "https://github.com/ProjectExhibition1/Heart_rate_sensor",
    "https://github.com/ProjectExhibition1/Bluetooth_Car",
    "https://github.com/ProjectExhibition1/Arduino-Home-Security-project",
    "https://github.com/ProjectExhibition1/Owner-avatar-Laser_Tripwire_Alarm-",
    "https://github.com/ProjectExhibition1/Glasses_for_blind_people",
]

def fun(repo_link):
    webbrowser.open(repo_link)

#Level 2 message
def level2():
    messagebox.showinfo(title="Level 2", message="Coming Soon!")


#open menu 2
def open_menu2(previous_window):
    previous_window.withdraw()  # Withdraw the current window
    global menu2
    menu2 = Toplevel(previous_window)
    menu2.title("Exhibition - Level Two")
    menu2.geometry("1000x600")

    button_width=0.3
    button_height=0.15


    project1 = tb.Button(menu2, text="Heart rate sensor", bootstyle="primary,outline", command=lambda: open_project_details(1, menu2))
    project1.place(relx=0.25,rely=0.1,relheight=button_height,relwidth=button_width,anchor="center")

    project2 = tb.Button(menu2, text="RC Car", bootstyle="primary,outline", command=lambda: open_project_details(2, menu2))
    project2.place(relx=0.75,rely=0.1,relheight=button_height,relwidth=button_width,anchor="center")

    project3 = tb.Button(menu2, text="Home Security", bootstyle="primary,outline",command=lambda: open_project_details(3, menu2))
    project3.place(relx=0.25,rely=0.4,relheight=button_height,relwidth=button_width,anchor="center")

    project4 = tb.Button(menu2, text="Laser Tripwire Alarm", bootstyle="primary,outline",command=lambda: open_project_details(4, menu2))
    project4.place(relx=0.75,rely=0.4,relheight=button_height,relwidth=button_width,anchor="center")

    project5 = tb.Button(menu2, text="Glasses for the bilnd", bootstyle="primary,outline",command=lambda: open_project_details(5, menu2))
    project5.place(relx=0.25,rely=0.7,relheight=button_height,relwidth=button_width,anchor="center")

    project6 = tb.Button(menu2, text="Project 6", bootstyle="primary,outline",command=lambda: open_project_details(6, menu2))
    project6.place(relx=0.75,rely=0.7,relheight=button_height,relwidth=button_width,anchor="center")

    back_to_menu1 = tb.Button(menu2, text="Back", bootstyle="dark,outline", command=lambda: back_to_menu(menu2, menu1))
    back_to_menu1.place(relx=0.4, rely=0.85, relheight=0.07, relwidth=0.1, anchor="center")

    exit_menu2 = tb.Button(menu2, text="Exit", bootstyle="danger,outline", command=menu1.destroy)
    exit_menu2.place(relx=0.6, rely=0.85, relheight=0.07, relwidth=0.1, anchor="center")


def open_project_details(project_number, previous_window):
    previous_window.withdraw()  # Withdraw the current window
    project_details = Toplevel(previous_window)
    project_details.title("Project Details")
    project_details.geometry("1000x600")

    title_frame_height = 0.15
    title_frame = tb.Frame(project_details)
    title_frame.place(relx=0, rely=0, relwidth=1, relheight=title_frame_height, anchor="nw")

    title_label = tb.Label(title_frame, text="Project Details", font=("Helvetica", 20), foreground="#378dfc")
    title_label.place(relx=0.5, rely=0.5, anchor="center")

    main_frame = tb.Frame(project_details)
    main_frame.place(relx=0, rely=title_frame_height, relwidth=1, relheight=1-title_frame_height)

    scroll = tb.Scrollbar(main_frame, orient="vertical", bootstyle="primary,round")
    scroll.pack(side=RIGHT, fill=Y)

    project_info_text = tb.Text(main_frame, wrap="word", yscrollcommand=scroll.set, font=("Helvetica", 16))
    project_info_text.pack(side=TOP, fill=BOTH, expand=True)

    project_info_text.insert(END, "Description :\n\n" + "\n".join(projects[project_number].description))
    project_info_text.insert(END, "\n\n")

    # Adding image
    global image
    image = PhotoImage(file=f"Project{project_number}.png")
    project_info_text.image_create(END, image=image)
    project_info_text.insert(END, "\n\n")  # Add some space after the image

    project_info_text.insert(END, "\n\nMembers:\n\n" + "\n".join(projects[project_number].members))
    project_info_text.insert(END, "\n\n")

    # Configure the scrollbar to work with the Text widget
    scroll.config(command=project_info_text.yview)

    # button frame
    button_frame_height = 0.1
    button_frame = tb.Frame(project_details)
    button_frame.place(relx=0, rely=1-button_frame_height, relwidth=1, relheight=button_frame_height)

    button_width = 0.2
    button_height = 0.8
    button_padding = 0.1

    back_to_menu2 = tb.Button(button_frame, text="Back", bootstyle="dark,outline",command=lambda: back_to_menu(project_details, menu2))
    back_to_menu2.place(relx=button_padding, rely=0.1, relwidth=button_width, relheight=button_height)

    repo_button = tb.Button(button_frame, text="Project repository", bootstyle="success,outline",command=lambda: fun(repo_links[project_number-1]))
    repo_button.place(relx=0.5 - button_width / 2, rely=0.1, relwidth=button_width, relheight=button_height)

    exit_project_details = tb.Button(button_frame, text="Exit", bootstyle="danger,outline",command=project_details.destroy)
    exit_project_details.place(relx=1 - button_width - button_padding, rely=0.1, relwidth=button_width,relheight=button_height)

    project_info_text.config(state=DISABLED)  # Disable text editing
    title_frame.lift()


#back buttons
def back_to_menu(current_window, previous_window):
    current_window.withdraw()  # Withdraw the current window
    previous_window.deiconify()  # Deiconify the previous window


# main menu
menu1 = tb.Window(themename="morph")
menu1.title("Projects Exhibition")
menu1.geometry("1000x600")

style=tb.Style()  #style for button font
style.configure("primary.Outline.TButton",font=("Franklin Gothic Demi",17))

lvl1 = tb.Button(menu1, text="Level One", bootstyle="primary,outline",style="primary.Outline.TButton", command=lambda: open_menu2(menu1))
lvl1.place(relx=0.5, rely=0.5, relheight=0.1, relwidth=0.3, y=-200, anchor="center")

level2 = tb.Button(menu1, text="Level Two", bootstyle="primary,outline", command=level2)
level2.place(relx=0.5, rely=0.5, relheight=0.1, relwidth=0.3, y=0, anchor="center")

exit1 = tb.Button(menu1, text="Exit", bootstyle="danger,outline", command=menu1.destroy)
exit1.place(relx=0.5, rely=0.5, relheight=0.07, relwidth=0.1, y=200, anchor="center")

menu1.mainloop()



