from azure.communication.email import EmailClient
import os
def main():
    try:
        connection_string = "endpoint=https://vivianforokccommservice.unitedstates.communication.azure.com/;accesskey="+os.environ['AccessKey']
        client = EmailClient.from_connection_string(connection_string)

        message = {
            "senderAddress": "DoNotReply@vivianforokc.com",
            "recipients":  {
                "to": [{"address": "andrewjwv@yahoo.com" }],
            },
            "content": {
                "subject": "Test Email",
                "plainText": "Hello world via email.",
            }
        }

        poller = client.begin_send(message)
        result = poller.result()

    except Exception as ex:
        print(ex)
main()