#! usr/bin/env python
# -*- coding: UTF-8 -*-
#http://askubuntu.com/questions/189231/where-are-the-stock-icon-names-defined-for-the-unity-panel-service-indicators-an
# sudo chmod +x to make the file executable
import pynotify

from datetime import date
import shutil
import os


class JnNotification:

	def sendmessage(self,title, message):
		try:
		    pynotify.init("Init")
		    notice = pynotify.Notification(title, message,"jn-notify")
		    notice.show()
		except pynotify.Error as e:
			print ('Error: %s' % e)

	def dailyProgram(self):

		week_pt = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')

		if(date.today().weekday() == 0):
			return ("NerdPlayer","<b>Lembrete:</b> Hoje tem NerdPlayer, confira https://goo.gl/PW15GH")

		elif(date.today().weekday() == 1):
			return ("Senhor K","<b>Lembrete:</b> Hoje tem Senhor K, confira https://goo.gl/PW15GH")

		elif(date.today().weekday() == 2):
			return ("NerdOffice","<b>Lembrete:</b> Hoje tem NerdOffice, confira https://goo.gl/PW15GH")

		elif(date.today().weekday() == 3):
			return ("Nerdologia","<b>Lembrete:</b> Hoje tem Nerdologia, confira https://goo.gl/EbddhZ")

		elif(date.today().weekday() == 6):
			return ("NerdCast","<b>Lembrete:</b> Hoje tem Nerdologia, confira https://goo.gl/M4SmW0")

		if(date.today().weekday() > 6):
			return "Error - JN-Notify"




class InstallNotify():

	#define the path that will contain the project icons;
	path_p = "/Projects/Python/JovemNerd/imgs/jn-notify.jpeg"

	#define the path of the system for icons;
	path_s = "/usr/share/icons/gnome/32x32/apps"

	def cpyIcon():
		try:
			shutil.copy(os.path.expanduser('~')+path_p, path_s)
		except shutil.Error as e:
			print ('Error: %s' % e)

		except IOError as e:
			print('Error: %s' % e.strerror)


if __name__ == '__main__':

	notify = JnNotification()
	notify.sendmessage(notify.dailyProgram()[0],notify.dailyProgram()[1])
	#print notify.dailyProgram()[0]
