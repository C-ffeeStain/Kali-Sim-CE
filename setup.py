import os
import logger

install_dir = f"{os.getenv('APPDATA')}\\Kali Sim - CE\\"

logger.updater("Installing...")
os.system("python -m pip install requests")
exe_data = []
with open("main.exe", "rb") as f:
   exe_data = f.readlines()
os.remove("main.exe")
os.system(f"mkdir \"{install_dir}\"")
new_pos = open(f"{install_dir}KaliSim_ConsoleEditon.exe", "wb")
new_pos.writelines(exe_data)
new_pos.close()
logger.updater(f"Finished installing to \"{install_dir}!\"")