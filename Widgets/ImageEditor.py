"""
Author: Kartikay Chiranjeev Gupta
"""

import tkinter as tk
from PIL import ImageTk, Image, ImageEnhance
from tkinter import messagebox as m_box

main_win = tk.Tk()
main_win.geometry("1000x600+150+30")
copy_img = None
ori_img = None
img_obj = None
copy_images = []
ori_images = []
back_count = -2
size_factor = 1


def Back_btn():
    global ori_img, copy_img, ori_images, copy_images, back_count
    try:
        ori_img = ori_images[back_count]
        copy_img = copy_images[back_count]
        copy_images.pop(back_count + 1)
        ori_images.pop(back_count + 1)
        Img_blit(copy_img)
    except:
        pass


def Save():
    global ori_img
    try:
        image_name = file_name.get()
        ori_img = ori_img.save(image_name)
        m_box.showinfo("Done", "Image saved successfully!")
    except:
        m_box.showerror("Error", "Error while saving")


def give_path(path_of_file):
    file_path = path_of_file.replace("\\", "/")
    return file_path


def Img_blit(copy):
    global copy_img, ori_img, img_obj
    img_obj = ImageTk.PhotoImage(copy)
    photo_blit = tk.Label(image_win, image=img_obj)
    photo_blit.grid(row=0, column=0)


def Image_search():
    global copy_img, ori_img, img_obj, size_factor
    path_file = path_.get()
    path = give_path(path_file)
    try:
        copy_img = Image.open(path)
        ori_img = Image.open(path)
    except:
        m_box.showerror("Error", "No such file in Directory")
    width, height = copy_img.size
    if width > 900 and height > 500:
        size_factor = 3
        copy_img = copy_img.resize((int(width / 3), int(height / 3)))
        copy_images.append(copy_img)
        ori_images.append(ori_img)
        Img_blit(copy_img)
    else:
        ori_images.append(ori_img)
        Img_blit(copy_img)
        Img_blit(copy_img)


def Brightness():
    bright_factor = bright_var.get()
    global ori_img, copy_img, copy_images, ori_images
    copy_img = ImageEnhance.Brightness(copy_img)
    copy_img = copy_img.enhance(bright_factor)
    ori_img = ImageEnhance.Brightness(ori_img)
    ori_img = ori_img.enhance(bright_factor)
    copy_images.append(copy_img)
    ori_images.append(ori_img)
    Img_blit(copy_img)


def Contrast():
    contrast_factor = contrast_var.get()
    global ori_img, copy_img, copy_images, ori_images
    copy_img = ImageEnhance.Contrast(copy_img)
    copy_img = copy_img.enhance(contrast_factor)
    ori_img = ImageEnhance.Contrast(ori_img)
    ori_img = ori_img.enhance(contrast_factor)
    copy_images.append(copy_img)
    ori_images.append(ori_img)
    Img_blit(copy_img)


def Sharpness():
    sharp_factor = sharp_var.get()
    global ori_img, copy_img, copy_images, ori_images
    copy_img = ImageEnhance.Sharpness(copy_img)
    copy_img = copy_img.enhance(sharp_factor)
    ori_img = ImageEnhance.Sharpness(ori_img)
    ori_img = ori_img.enhance(sharp_factor)
    copy_images.append(copy_img)
    ori_images.append(ori_img)
    Img_blit(copy_img)


def Colour():
    color_factor = color_var.get()
    global ori_img, copy_img, copy_images, ori_images
    copy_img = ImageEnhance.Color(copy_img)
    copy_img = copy_img.enhance(color_factor)
    ori_img = ImageEnhance.Color(ori_img)
    ori_img = ori_img.enhance(color_factor)
    copy_images.append(copy_img)
    ori_images.append(ori_img)
    Img_blit(copy_img)


def Crop_top():
    global copy_img, copy_images, ori_images, ori_img
    top = top_coor.get()
    below = 0
    right = 0
    left = 0
    c_width, c_height = copy_img.size
    o_width, o_height = ori_img.size
    copy_img = copy_img.crop((left, top, c_width - right, c_height - below))
    ori_img = ori_img.crop(
        (left * size_factor, top * size_factor, (o_width - right * size_factor), (o_height - below * size_factor)))
    copy_images.append(copy_img)
    ori_images.append(ori_img)
    Img_blit(copy_img)


def Crop_below():
    global copy_img, copy_images, ori_images, ori_img
    top = 0
    below = below_coor.get()
    right = 0
    left = 0
    c_width, c_height = copy_img.size
    o_width, o_height = ori_img.size
    copy_img = copy_img.crop((left, top, c_width - right, c_height - below))
    ori_img = ori_img.crop(
        (left * size_factor, top * size_factor, (o_width - right * size_factor), (o_height - below * size_factor)))
    copy_images.append(copy_img)
    ori_images.append(ori_img)
    Img_blit(copy_img)


def Crop_left():
    global copy_img, copy_images, ori_images, ori_img
    top = 0
    below = 0
    right = 0
    left = left_coor.get()
    c_width, c_height = copy_img.size
    o_width, o_height = ori_img.size
    copy_img = copy_img.crop((left, top, c_width - right, c_height - below))
    ori_img = ori_img.crop(
        (left * size_factor, top * size_factor, (o_width - right * size_factor), (o_height - below * size_factor)))
    copy_images.append(copy_img)
    ori_images.append(ori_img)
    Img_blit(copy_img)


def Crop_right():
    global copy_img, copy_images, ori_images, ori_img
    top = 0
    below = 0
    right = right_coor.get()
    left = 0
    c_width, c_height = copy_img.size
    o_width, o_height = ori_img.size
    copy_img = copy_img.crop((left, top, c_width - right, c_height - below))
    ori_img = ori_img.crop(
        (left * size_factor, top * size_factor, (o_width - right * size_factor), (o_height - below * size_factor)))
    copy_images.append(copy_img)
    ori_images.append(ori_img)
    Img_blit(copy_img)


option_win = tk.LabelFrame(main_win)
option_win.grid(row=0, column=0)

search_bar = tk.Label(option_win, text="Enter path Below:", font=("Copperplate Gothic Light", 12))
search_bar.grid(row=0, columnspan=4, padx=200)
path_ = tk.StringVar()
search_entry = tk.Entry(option_win, width=165, textvariable=path_)
search_entry.grid(row=1, columnspan=4)
search_btn = tk.Button(option_win, text="Search", command=Image_search, font=("Copperplate Gothic Light", 10))
search_btn.grid(row=2, columnspan=4, pady=2)

bright_label = tk.Button(option_win, text="Brightness :", font=("Copperplate Gothic Light", 10), command=Brightness)
bright_label.grid(row=3, column=0, pady=5)
bright_var = tk.IntVar()
bright_var.set(5)
bright_entry = tk.Entry(option_win, width=4, textvariable=bright_var)

bright_entry.grid(row=3, column=0, sticky=tk.E)
contrast_label = tk.Button(option_win, text="Contrast :", font=("Copperplate Gothic Light", 10), command=Contrast)
contrast_label.grid(row=3, column=1, padx=10, pady=5)
contrast_var = tk.IntVar()
contrast_var.set(5)
contrast_entry = tk.Entry(option_win, width=4, textvariable=contrast_var)
contrast_entry.grid(row=3, column=1, sticky=tk.E)

sharp_label = tk.Button(option_win, text="Sharpness :", font=("Copperplate Gothic Light", 10), command=Sharpness)
sharp_label.grid(row=3, column=2, pady=5)
sharp_var = tk.IntVar()
sharp_var.set(5)
sharp_entry = tk.Entry(option_win, width=4, textvariable=sharp_var)
sharp_entry.grid(row=3, column=2, sticky=tk.E)

color_label = tk.Button(option_win, text="Colour :", font=("Copperplate Gothic Light", 10), command=Colour)
color_label.grid(row=3, column=3, padx=10, pady=5)
color_var = tk.IntVar()
color_var.set(5)
color_entry = tk.Entry(option_win, width=4, textvariable=color_var)
color_entry.grid(row=3, column=3, sticky=tk.E)

undo_btn = tk.Button(option_win, text="Undo", font=("Copperplate Gothic light", 10), command=Back_btn)
undo_btn.grid(row=5, column=0, sticky=tk.W)

save_btn = tk.Button(option_win, text="Save", font=("Copperplate Gothic Light", 10), command=Save)
save_btn.grid(row=5, column=3, sticky=tk.E, pady=5)
file_name = tk.StringVar()
save_entry = tk.Entry(option_win, width=18, textvariable=file_name)
save_entry.grid(row=5, column=3)

top_coor = tk.IntVar()
top_label = tk.Button(option_win, text="TOP", font=("Copperplate Gothic Light", 10), command=Crop_top)
top_label.grid(row=4, column=0)
top_entry = tk.Entry(option_win, width=4, textvariable=top_coor)
top_entry.grid(row=4, column=0, sticky=tk.E)
below_coor = tk.IntVar()
below_label = tk.Button(option_win, text="Below", font=("Copperplate Gothic Light", 10), command=Crop_below)
below_label.grid(row=4, column=1)
below_entry = tk.Entry(option_win, width=4, textvariable=below_coor)
below_entry.grid(row=4, column=1, sticky=tk.E)
right_coor = tk.IntVar()
right_label = tk.Button(option_win, text="Right", font=("Copperplate Gothic Light", 10), command=Crop_right)
right_label.grid(row=4, column=2)
right_entry = tk.Entry(option_win, width=4, textvariable=right_coor)
right_entry.grid(row=4, column=2, sticky=tk.E)
left_coor = tk.IntVar()
left_label = tk.Button(option_win, text="Left", font=("Copperplate Gothic Light", 10), command=Crop_left)
left_label.grid(row=4, column=3)
left_entry = tk.Entry(option_win, width=4, textvariable=left_coor)
left_entry.grid(row=4, column=3, sticky=tk.E)

image_win = tk.LabelFrame(main_win)
image_win.grid(row=1, column=0)

main_win.mainloop()
