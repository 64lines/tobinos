def format_datetime(date):
  return "{}-{}-{} {}:{}:{}".format(
    str(date.day).zfill(2), 
    str(date.month).zfill(2),
    str(date.year).zfill(2),
    str(date.hour).zfill(2), 
    str(date.minute).zfill(2),
    str(date.second).zfill(2)
  )