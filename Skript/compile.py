import re
from datetime import datetime, timedelta
import locale
import os
import glob
import sys

locale.setlocale(locale.LC_TIME, "de_DE")


class Compiler:

    def __init__(self):
        self.reps = 3
        with open('skript.tex', encoding="UTF-8") as file:
            self.entrypoint = file.read()

        self.filename = "Test"
        self.output = self.entrypoint

    def start(self, filename):
        self.filename = filename
        self.output = self.entrypoint
        return self

    def handout(self):
        self.output = re.sub(r"^\s*%\s*handout\s*$", "handout", self.output, flags=re.M)
        return self

    def slides(self):
        self.output = re.sub(r"^\s*handout\s*$", "%handout", self.output, flags=re.M)
        return self

    def light(self):
        self.output = re.sub(r"^\s*colortheme=dark[, ]*$", "colortheme=light", self.output, flags=re.M)
        return self

    def dark(self):
        self.output = re.sub(r"^\s*colortheme=light[, ]*$", "colortheme=dark", self.output, flags=re.M)
        return self

    def day_replace(self, day, match):
        current_day = int(match.group(1))
        result = r"\input{skript_tag_" + str(current_day) + "}"
        if current_day > day:
            result = "%" + result
        return result

    def until_day(self, day):
        self.output = re.sub(r"^\s*[%]*\\input{skript_tag_(\d+)}\s*$",
                             lambda match: self.day_replace(day, match),
                             self.output,
                             flags=re.M)
        return self

    def only_day(self, day):
        self.output = re.sub(r"^\s*(\\input{skript_tag_\d+})\s*$", r'%\1', self.output, flags=re.M)
        self.output = re.sub(r"^%(\\input{skript_tag_" + str(day) + "})", r'\1', self.output, flags=re.M)
        return self

    def add_days(self, days):
        date = self.getDate()
        date = date + timedelta(days)
        return self.setDate(date)

    def sub_days(self, days):
        date = self.getDate()
        date = date - timedelta(days)
        return self.setDate(date)

    def getDate(self):
        date = re.search(r"^\s*\\date{(.*)}", self.output, re.M).group(1)
        return datetime.strptime(date, '%d. %B %Y')

    def setDate(self, date):
        date = datetime.strftime(date, "%d. %B %Y")
        replace = r"\\date{" + date + "}"
        self.output = re.sub(r"^\s*\\date{(.*)}", replace, self.output, flags=re.M)
        return self

    def day_title(self, day):
        self.remove_subtitles()
        self.output = re.sub(r"^%(\\subtitle{Teil " + str(day) + ")", r'\1', self.output, flags=re.M)
        return self

    def general_title(self):
        self.remove_subtitles()
        self.output = re.sub(r"^%\\subtitle{(?!Teil \d)", '\\\\subtitle{', self.output, flags=re.M)
        return self

    def remove_subtitles(self):
        self.output = re.sub(r"^\s*\\subtitle{", '%\\\\subtitle{', self.output, 50, flags=re.M)
        return self

    def compile(self):
        with open(self.filename + ".tex", "w", encoding="UTF-8") as file:
            file.write(self.output)

        for k in range(1, self.reps + 1):
            print("\n\n\n")
            print("************************************")
            print(f"Compiling {self.filename} the {k}. time")
            print("************************************")
            print("\n\n")
            status = os.system(f"pdflatex -synctex=1 -interaction=batchmode -shell-escape \"{self.filename}.tex\"")
            if status != 0:
                raise Exception(f"Compiling for file {self.filename} went wrong")

        cwd = os.getcwd()

        # remove Tex Files
        files = glob.glob(f"{cwd}/{self.filename}.*[!pdf]")
        for file in files:
            print(file)
            os.remove(file)

        # remove minted files
        path = '_minted-' + self.filename.replace(' ', '_')
        files = glob.glob(f"{cwd}/{path}/*")
        for file in files:
            os.remove(file)
        os.removedirs(path)

    def run(self, day):
        self.start("Lehrskript dunkel").slides().dark().until_day(day + 1).general_title().compile()
        self.start("Lehrskript hell").slides().light().until_day(day + 1).general_title().compile()
        self.start("Präsentation").slides().dark().until_day(day).general_title().compile()
        self.start("Handout Gesamt").handout().dark().until_day(day).general_title().compile()
        self.start(f"Tag-{str(day).zfill(2)}-Entwurf").handout().dark().only_day(day).day_title(day).compile()
        if day > 1:
            day -= 1
            self.start(f"Tag-{str(day).zfill(2)}").sub_days(7).handout().dark().only_day(day).day_title(day).compile()
        print("\n\n\n\n")
        print("*******************")
        print("Everything went fine")


day = int(sys.argv[1])
Compiler().run(day)
