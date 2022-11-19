from datetime import datetime, timedelta
from src.bot_utils import send_telegram_message
from src.date_utils import format_datetime
from properties.messages import NOTIFICATION_MESSAGE, FOLLOW_UP_MESSAGE

def send_notification(notification_date, message):
  """
  Sends a notification using a notification date.
  """
  if format_datetime(datetime.now()) == notification_date:
    return send_telegram_message(text=message)

def add_minutes(bill_date, minutes):
  bill_datetime = datetime.strptime(bill_date, '%d-%m-%Y %H:%M:%S')
  return format_datetime(bill_datetime + timedelta(minutes=minutes))

def create_notification_message(bill_name):
  return NOTIFICATION_MESSAGE.format(bill_name)

def create_follow_up_message(bill_name):
  return FOLLOW_UP_MESSAGE.format(bill_name)

def send_bill_notifications(bills):
  return [
    send_notification(
      notification_date=bill['date'],
      message=create_notification_message(bill_name=bill['name'])
    ) for bill in bills
  ]

def send_bill_follow_ups(bills, minutes):
  return [
    send_notification(
      notification_date=add_minutes(
        bill_date=bill['date'], 
        minutes=minutes
      ), 
      message=create_follow_up_message(bill_name=bill['name'])
    ) for bill in bills
  ]
