# from pykeyboard import PyKeyboard
# import time
# kb = PyKeyboard()
#
# kb.tab_key(kb.enter_key)
# time.sleep(2)
# kb.type_string('yz666', interval=0.2)
# time.sleep(1)
# kb.tab_key(kb.enter_key)


# default_audio = 'Windows Media Player'
# time.sleep(5)
# uiautomation.ButtonControl(AutomationId="SystemSettings_DefaultApps_Audio_Button").Click()
# audio_list = uiautomation.PaneControl(AutomationId="DefaultAppsFlyoutPresenter").GetChildren()[0].GetChildren()
# audio_lis = []
# for i in audio_list[1: -1]:
#     audio_lis.append(i.Name)
# print(audio_lis)
# audio_lis.remove(default_audio)
# print(audio_lis)
# random_audio = random.choice(audio_lis)
# print(random_audio)
# uiautomation.ButtonControl(Name=random_audio).Click()


# time.sleep(5)
# current_time_zone = uiautomation.ComboBoxControl(
#     AutomationId="SystemSettings_DateTime_TimezoneInfo_ComboBox").AccessibleGetCurrentSelection()[0].Name
# print(current_time_zone)
# uiautomation.ComboBoxControl(
#     AutomationId="SystemSettings_DateTime_TimezoneInfo_ComboBox").Click()
# sele_list = uiautomation.ComboBoxControl(
#     AutomationId="SystemSettings_DateTime_TimezoneInfo_ComboBox").GetChildren()
# s_lis = []
# for i in sele_list:
#     s_lis.append(i.Name)
# print(s_lis)
# s_lis.remove("(UTC+08:00) 北京，重庆，香港特别行政区，乌鲁木齐")
# random_time_zone = random.choice(s_lis)
# print(random_time_zone)
# uiautomation.ComboBoxControl(AutomationId="SystemSettings_DateTime_TimezoneInfo_ComboBox").Select(random_time_zone)

# path = os.path.join(os.getcwd(), "test.yaml")
# data = dict()
# data["key"] = "value"
#
# with open(path, "w") as w:
#     # yaml.safe_dump(data, w)
#     yaml.dump(data, w)
# with open(path, 'r') as w:
#     # print(yaml.safe_load(w))
#     print(yaml.load(w, Loader=yaml.Loader))

#
# def get_current_path():
#     current_path = os.path.join(os.getcwd(), os.path.realpath(sys.argv[0]))
#     print(current_path)
#
#
# get_current_path()

import pyautogui
from common.picture_operate import start

loc, size = start("templete")
pyautogui.click(loc)

