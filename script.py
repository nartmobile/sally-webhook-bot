from discord_webhook import DiscordWebhook
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
import os

print('Started successfully!\n')

def cron_process():
	x = datetime.datetime.utcnow()
	print('Function fired successfully!\n')
	if (x.hour == 3 or x.hour == 9 or x.hour == 23) and x.minute == 0:
		webhook = DiscordWebhook(url=str(os.environ.get("serverurl")), content=str(os.environ.get("message")))
		response = webhook.execute()
		print('Message printed!\n')


scheduler = BlockingScheduler()
scheduler.add_job(cron_process, 'cron', month = '3', minute = '*')
scheduler.start()