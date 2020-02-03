import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf
import data
import datetime
import vlc
import time

fajr_img = GdkPixbuf.Pixbuf.new_from_file_at_scale(
    filename="fajr.png",
    width=200,
    height=100,
    preserve_aspect_ratio=True)

sunrise_img = GdkPixbuf.Pixbuf.new_from_file_at_scale(
    filename="sunrise.png",
    width=200,
    height=100,
    preserve_aspect_ratio=True)

dhuhr_img = GdkPixbuf.Pixbuf.new_from_file_at_scale(
    filename="dhuhr.png",
    width=200,
    height=100,
    preserve_aspect_ratio=True)

asr_img = GdkPixbuf.Pixbuf.new_from_file_at_scale(
    filename="asr.png",
    width=200,
    height=100,
    preserve_aspect_ratio=True)

magrib_img = GdkPixbuf.Pixbuf.new_from_file_at_scale(
    filename="magrib.png",
    width=200,
    height=100,
    preserve_aspect_ratio=True)

isha_img = GdkPixbuf.Pixbuf.new_from_file_at_scale(
    filename="isha.png",
    width=200,
    height=100,
    preserve_aspect_ratio=True)

image1 = Gtk.Image.new_from_pixbuf(fajr_img)
image2 = Gtk.Image.new_from_pixbuf(sunrise_img)
image3 = Gtk.Image.new_from_pixbuf(dhuhr_img)
image4 = Gtk.Image.new_from_pixbuf(asr_img)
image5 = Gtk.Image.new_from_pixbuf(magrib_img)
image6 = Gtk.Image.new_from_pixbuf(isha_img)


def incpection(widget, lang, layout):
    flag = True
    i = 0
    time_now = datetime.datetime.time(datetime.datetime.today())
    while flag:
        if i == 0 or i == 1:
            if time_now.hour < int(data.times[i][0]):
                if i == 0:
                    if lang == "en":
                        widget.set_text("Next - Fajr")
                        layout.attach(image6, 0, 0, 1, 1)
                        flag = False
                    elif lang == "ru":
                        widget.set_text("Следующий - Утренний")
                        flag = False

                elif i == 1:
                    if lang == "en":
                        widget.set_text("Next - Sunrise")
                        layout.attach(image1, 0, 0, 1, 1)
                        flag = False
                    elif lang == "ru":
                        widget.set_text("Следующий - Восход")
                        flag = False

            elif time_now.hour == int(data.times[i][0]):
                if time_now.minute < int(data.times[i][2:]):
                    if i == 0:
                        if lang == "en":
                            widget.set_text("Next - Fajr")
                            layout.attach(image6, 0, 0, 1, 1)
                            flag = False
                        elif lang == "ru":
                            widget.set_text("Следующий - Утренний")
                            flag = False
                    elif i == 1:
                        if lang == "en":
                            widget.set_text("Next - Sunrise")
                            layout.attach(image1, 0, 0, 1, 1)
                            flag = False
                        elif lang == "ru":
                            widget.set_text("Следующий - Восход")
                            flag = False
                if time_now.minute == int(data.times[i][2:]) or time_now.minute > int(data.times[i][2:]):
                    if i == 0:
                        if lang == "en":
                            widget.set_text("Next - Sunrise")
                            layout.attach(image1, 0, 0, 1, 1)
                            flag = False
                        elif lang == "ru":
                            widget.set_text("Следующий - Восход")
                            flag = False
                    elif i == 1:
                        if lang == "en":
                            widget.set_text("Next - Dhuhr")
                            layout.attach(image2, 0, 0, 1, 1)
                            flag = False
                        elif lang == "ru":
                            widget.set_text("Следующий - Обеденный")
                            flag = False
            else:
                i += 1
        elif i == 2:
            if time_now.hour < int(data.times[i][0:2]):
                if lang == "en":
                    widget.set_text("Next - Dhuhr")
                    layout.attach(image2, 0, 0, 1, 1)
                    flag = False
                elif lang == "ru":
                    widget.set_text("Следующий - Обеденный")
                    flag = False
            elif time_now.hour == int(data.times[i][0:2]):
                if time_now.minute < int(data.times[i][3:]):
                    if lang == "en":
                        widget.set_text("Next - Dhuhr")
                        layout.attach(image2, 0, 0, 1, 1)
                        flag = False
                    elif lang == "ru":
                        widget.set_text("Следующий - Обеденный")
                        flag = False
                elif time_now.minute == int(data.times[i][3:]) or time_now.minute > int(data.times[i][3:]):
                    if lang == "en":
                        widget.set_text("Next - Asr")
                        layout.attach(image3, 0, 0, 1, 1)
                        flag = False
                    elif lang == "ru":
                        widget.set_text("Следующий - Послеобеденный")
                        flag = False
            else:
                i += 1
        elif i == 3:
            if time_now.hour < int(data.times[i][0:2]):
                if lang == "en":
                    widget.set_text("Next - Asr")
                    layout.attach(image3, 0, 0, 1, 1)
                    flag = False
                elif lang == "ru":
                    widget.set_text("Следующий - Послеобеденный")
                    flag = False
            elif time_now.hour == int(data.times[i][0:2]):
                if time_now.minute < int(data.times[i][3:]):
                    if lang == "en":
                        widget.set_text("Next - Asr")
                        layout.attach(image3, 0, 0, 1, 1)
                        flag = False
                    elif lang == "ru":
                        widget.set_text("Следующий - Послеобеденный")
                        flag = False
                elif time_now.minute == int(data.times[i][3:]) or time_now.minute > int(data.times[i][3:]):
                    if lang == "en":
                        widget.set_text("Next - Magrib")
                        layout.attach(image4, 0, 0, 1, 1)
                        flag = False
                    elif lang == "ru":
                        widget.set_text("Следующий - Вечерний")
                        flag = False
            else:
                i += 1
        elif i == 4:
            if time_now.hour < int(data.times[i][0:2]):
                if lang == "en":
                    widget.set_text("Next - Magrib")
                    layout.attach(image4, 0, 0, 1, 1)
                    flag = False
                elif lang == "ru":
                    widget.set_text("Следующий - Вечерний")
                    flag = False
            elif time_now.hour == int(data.times[i][0:2]):
                if time_now.minute < int(data.times[i][3:]):
                    if lang == "en":
                        widget.set_text("Next - Magrib")
                        layout.attach(image4, 0, 0, 1, 1)
                        flag = False
                    elif lang == "ru":
                        widget.set_text("Следующий - Вечерний")
                        flag = False
                elif time_now.minute == int(data.times[i][3:]) or time_now.minute > int(data.times[i][3:]):
                    if lang == "en":
                        widget.set_text("Next - Isha")
                        layout.attach(image5, 0, 0, 1, 1)
                        flag = False
                    elif lang == "ru":
                        widget.set_text("Следующий - Ночной")
                        flag = False
            else:
                i += 1
        elif i == 5:
            if time_now.hour < int(data.times[i][0:2]):
                if lang == "en":
                    widget.set_text("Next - Isha")
                    layout.attach(image5, 0, 0, 1, 1)
                    flag = False
                elif lang == "ru":
                    widget.set_text("Следующий - Ночной")
                    flag = False
            elif time_now.hour == int(data.times[i][0:2]):
                if time_now.minute < int(data.times[i][3:]):
                    if lang == "en":
                        widget.set_text("Next - Isha")
                        layout.attach(image5, 0, 0, 1, 1)
                        flag = False
                    elif lang == "ru":
                        widget.set_text("Следующий - Ночной")
                        flag = False
                elif time_now.minute == int(data.times[i][3:]) or time_now.minute > int(data.times[i][3:]):
                    if lang == "en":
                        widget.set_text("Next - Fajr")
                        layout.attach(image6, 0, 0, 1, 1)
                        flag = False
                    elif lang == "ru":
                        widget.set_text("Следующий - Утренний")
                        flag = False
            elif time_now.hour > int(data.times[i][0:2]):
                if lang == "en":
                    widget.set_text("Next - Fajr")
                    layout.attach(image6, 0, 0, 1, 1)
                    flag = False
                elif lang == "ru":
                    widget.set_text("Следующий - Утренний")
                    flag = False
            else:
                i += 1
        else:
            i += 1


fajr = Gtk.Label(label="Fajr - " + data.times[0])
sunrise = Gtk.Label(label="Sunrise - " + data.times[1])
dhuhr = Gtk.Label(label="Dhuhr - " + data.times[2])
asr = Gtk.Label(label="Asr - " + data.times[3])
magrib = Gtk.Label(label="Magrib - " + data.times[4])
isha = Gtk.Label(label="Isha - " + data.times[5])
line = Gtk.Label(label="--------------------------------")
following = Gtk.Label(label="Next - ")


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Namaz times")
        # self.resize(160, 203)
        grid = Gtk.Grid()
        grid.set_row_spacing(5)
        self.add(grid)

        fajr.set_text("Fajr - " + data.times[0])
        sunrise.set_text("Sunrise - " + data.times[1])
        dhuhr.set_text("Dhuhr - " + data.times[2])
        asr.set_text("Asr - " + data.times[3])
        magrib.set_text("Magrib - " + data.times[4])
        isha.set_text("Isha - " + data.times[5])
        line.set_text("--------------------------------")
        following.set_text("Next - ")

        grid.attach(fajr, 0, 1, 1, 1)
        grid.attach(sunrise, 0, 2, 1, 1)
        grid.attach(dhuhr, 0, 3, 1, 1)
        grid.attach(asr, 0, 4, 1, 1)
        grid.attach(magrib, 0, 5, 1, 1)
        grid.attach(isha, 0, 6, 1, 1)
        grid.attach(line, 0, 7, 1, 1)
        grid.attach(following, 0, 8, 1, 1)
        incpection(following, "en", grid)


window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
