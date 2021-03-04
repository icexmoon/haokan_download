import platform
windowsHomePath = "d:\\download\\好看视频"
LinuxHomePath = "/home/pi/NewmanDisk/haokan"
config = {}
sysName = platform.system()
if sysName == "Windows":
    config["path"] = "\\"
    config["saveHome"] = windowsHomePath
elif sysName == "Linux":
    config["path"] = "/"
    config["saveHome"] = LinuxHomePath
else:
    print("本程序不支持当前操作系统")
    exit()
