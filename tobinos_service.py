########################################################################
## TOBiNoS Server (Telegram Over-engineered Bill Notification Service)
########################################################################
import time
from src.json_utils import get_json_file
from src.notification import send_bill_notifications, send_bill_follow_ups
from properties.config import FOLLOW_UP_MINUTES

BILLS_PATH = './data/bills_info.json'

def start_service():
  """
  Starts the Notification Service
  """
  try:
    print('(*) The notification service is running...')
    while True:
      # Get the bills from a JSON file
      bills = get_json_file(path=BILLS_PATH)

      # Send notification for every bill
      send_bill_notifications(bills)

      # Send follow up notification
      send_bill_follow_ups(bills, minutes=FOLLOW_UP_MINUTES)

      time.sleep(1)
  except:
    pass

if __name__ == '__main__':
  start_service()