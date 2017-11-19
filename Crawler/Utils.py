import os
import webbrowser
from gtts import gTTS

# ����static method and class method �ѦҤ�:
# http://www.wklken.me/posts/2013/12/22/difference-between-staticmethod-and-classmethod-in-python.html


class FileUtils:  # create FileUtils class
    # ==== Defined Constructor Code (For test) ====
    # <<Description:>>
    #   Python �u��s�b�@�ӫغc�l�A�]�i�H���Ωw�q�غc�l
    #   self: ��ܦ�Class������A�ҥH�p�G���ݨD�Oclass method call another method in the same class ==> self.methodName()
    #
    # <<Code:>>
    # def __init__(self):
    #     print(self)
    #
    # # constructor with parameter
    # def __init__(self, test1, test2):
    #     self.test1 = test1
    #     self.test2 = test2

    # �ˬd�÷s�W��Ƨ� (�ѩ󤣻ݭninstance�����ܼ�or����A�ҥH�Ҽ{�@��static function)
    def check_and_create(self, folder_name):
        check_dir = folder_name

        if os.path.exists(check_dir):  # Checks if the dir exists
            print("The directory exists")
        else:
            print("No directory found for " + check_dir)  # Output if no directory
            print()
            os.makedirs(check_dir)  # Creates a new dir for the given name
            print("Directory created for " + check_dir)

    # �����n����(�t�ˬd�@�~�t��) => ���]�i�H�@��static method�A���b���m��class method
    def generate_sound(self, report):
        folder = "Sound"

        self.check_and_create(folder)

        # get path
        print(os.getcwd())
        tts = gTTS(text=report, lang='zh')
        tts.save("{}/{}/NBAReporter.mp3".format(os.getcwd(), folder))

        # �P�_��e�@�~�t��
        sys_nm = os.name
        if sys_nm == "nt":  # os: windows
            webbrowser.open("NBAReporter.mp3")
        elif sys_nm == "posix":  # os: linus or maxos
            chrome_path = 'open -a /Applications/Google\ Chrome.app %s'  # ���wwebbrower�ϥ�Chrome�}���ɮ�
            webbrowser.get(chrome_path).open("{}/NBAReporter.mp3".format(folder))

# ========= Test class code =========
# fileUtil = FileUtils(1,2)
# print(fileUtil.test1)
# print(fileUtil.test2)
# fileUtil.checkAndCreate("sound")
# fileUtil2 = FileUtils()
# fileUtil2.checkAndCreate("sound")
