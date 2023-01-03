import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])

try:
    # Call the chat.postMessage method using the WebClient
    response = client.chat_postMessage(
        channel="#mychannel",
        text="Hello, World!"
    )
    print(response)
except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    # (caused by an error returned by the Slack API)
    print("Error: {}".format(e))
