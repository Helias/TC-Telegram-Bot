import telegram
import telnetlib

HOST = "127.0.0.1"	#IP of the server
port = 3443		#Port of the server
username = ""		#Username telnet access 
password = ""		#Password telnet access
logs = 1		#Enable/Disable logs (1/0)

TOKEN = ""		#Token of your telegram bot that you created from @BotFather

def command(command, output=0):
	tn = telnetlib.Telnet(HOST, port)

	#tn.set_debuglevel(5) #this is to print the logs of the connection via telnet

	tn.read_until("Username: ")
	tn.write(username + "\r\n")
	tn.read_until("Password: ")
	tn.write(password + "\r\n")
	tn.read_until("TC")
	tn.write(str(command) + "\r\n")
	tn.write("exit" + "\r\n")

	read = tn.read_all()

	if command == ".ticket list" or ".ticket viewid " in command or ".ticket onlinelist" in command:
		read = read.replace("|cffaaffaa","")
		read = read.replace("|r","")
		read = read.replace("|cffaaccff","")
		read = read.replace("|cff00ff00","")
		read = read.replace("|cff00ccff","")

	tn.close()

	print (command) #print command log in the console

	if logs == 1:
		fo = open("logs.txt", "a+")
		fo.write(command + "\n");

	if output == 1:
		read = read.replace("TC>exit\r\n", "")
		read = read.replace("TC>", "")
		read = read.replace("Bye\r\n", "")
		fo.write(read + "\n")
		fo.close()
		print (read) #print log in the console
		return read

	if logs == 1:
		fo.close()


bot = telegram.Bot(TOKEN)

try:
	LAST_UPDATE_ID = bot.getUpdates()[-1].update_id
except IndexError:
	LAST_UPDATE_ID = 0


text = ""

while True:
	messageText = ""
	for update in bot.getUpdates(offset=LAST_UPDATE_ID, timeout=2):
	    text = update.message.text
	    chat_id = update.message.chat.id
	    update_id = update.update_id

	if text != "":
		text = text.lower()
		if text.startswith('/'):
			if text == '/help':
				messageText = ('/saveall \n/serverinfo - show server info\n/ticket list - show ticket list\n/ticket onlinelist - show ticket onlinelist\n/ticket viewid {ID}\n/ticket complete {ID} {Reason}\n/mute {PlayerName} {minutes} {reason}\n/mutehistory {accountName}\n/unmute {PlayerName}\n/gmannounce {testo}\n/announce {testo}\n/tele {PlayerName} {Area}\n/reload {table}\n/revive {PlayerName}\n/pinfo {PlayerName}\n/kick {PlayerName}\n/unstuck {PlayerName}\n/baninfo ip/account/character {ip/accountName/playerName}')
			elif text == "/saveall":
				messageText = command(".saveall", 1) 
			elif text == "/serverinfo":
				messageText = command(".server info", 1)
			elif text == '/ticket list':
				messageText = command(".ticket list", 1)
			elif text == "/ticket onlinelist":
				messageText = command(".ticket onlinelist", 1)
			elif "/ticket viewid " in text:
				ticketid = text.replace("/ticket viewid", "")
				messageText = command(".ticket viewid " + ticketid, 1)
			elif "/ticket complete " in text:
				params = text.replace("/ticket complete ", "")
				command(".ticket complete " + params)
				messageText  = "Ticket closed"
			elif "/mute " in text:
				conditions = text.replace("/mute ", "")
				messageText = command(".mute " + conditions, 1)
			elif "/mutehistory " in text:
				accountName = text.replace("/mutehistory ", "")
				messageText = command(".mutehistory " + accountName, 1)
			elif "/unmute " in text:
				playername = text.replace("/unmute ", "")
				messageText = command(".unmute " + playername, 1)
			elif "/gmannounce " in text:
				testo = text.replace("/gmannounce ", "")
				command(".gmannounce "+ testo)
				messageText = ("[GM Announcements]: " + testo)
			elif "/announce " in text:
				testo = text.replace("/announce ", "")
				command(".announce "+ testo)
				messageText = ("[Server Announce]: " + testo)
			elif "/tele " in text:
				tele = text.replace("/tele ", "")
				messageText  = command(".tele name " + tele, 1)
			elif "/reload "  in text:
				table = text.replace("/reload ", "")
				command(".reload "+ table)
				messageText = table +" reloaded."
			elif "/revive " in text:
				playername = text.replace("/revive ", "")
				messageText = command("revive "+ playername, 1)
				if not "Player not found!" in messageText:
					messageText = playername+" resurrected"
			elif "/pinfo " in text:
				playername = text.replace("/pinfo ","")
				messageText = command(".pinfo "+ playername, 1)
			elif "/kick " in text:
				playername = text.replace("/kick ","")
				messageText = command(".kick "+ playername, 1)
			elif "/unstuck " in text:
				playername = text.replace("/unstuck ","")
				command("unstuck "+playername, 1)
				if not 'Player not found!' in messageText:
					messageText = "Unstuck on "+ playername +" successfully executed!"
			elif "/baninfo " in text:
				params = text.replace("/baninfo ","")
				messageText = command(".baninfo "+ params, 1)

			if messageText != "":
				bot.sendMessage(chat_id=chat_id, text=messageText)
				LAST_UPDATE_ID = update_id + 1
				text = ""
