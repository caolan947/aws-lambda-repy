

import json

# TODO unit test, integration test, add logging
class EventFactory():
    def __init__(self, event):
        self.event = event

    def get_event_parser(self):
        if self.is_api_gw():
            return UnpackEvent(self.event)
        
        elif self.is_sqs():
            return UnpackSqsMessage(self.event)

            
    def is_api_gw(self):
        try:
            json.loads(self.event["body"])
            return True
        except (TypeError, KeyError):
            return False

    def is_sqs(self):
        try:
            json.loads(self.event["Records"][0]['body'])
            return True
        except Warning:
            return False

class UnpackEvent():
    def __init__(self, event):
        self.event = json.loads(event["body"])
    
class UnpackSqsMessage():
    def __init__(self, event):
        self.event = json.loads(event["Records"][0]['body'])



