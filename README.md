# TOBiNoS Server (Telegram Over-engineered Bill Notification Service)

To configure the notification service use the `bill_info.json` file under `data` or run the flask server via:

```bash
flask run
```

To run the notification service you can run the following command:

```bash
python tobinos_service.py
```

This server will send a notification to a specific telegram chat id, configured under `properties/config.py`, and send a follow up message after an 'X' number of minutes that can also be configured on the same file.
