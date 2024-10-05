import json

# TODO unit test, integration test, add logging, organise into modules, docstring
class EventFactory():
    def __init__(self, event):
        self.event = event

    def get_event_parser(self):
        if self.is_api_gw():
            return ParseApiGatewayEvent(self.event)
        
        elif self.is_sqs():
            return ParseSqsMessage(self.event)
            
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
        except (TypeError, KeyError):
            return False

class ParseApiGatewayEvent():
    def __init__(self, event):
        self.event = json.loads(event["body"])
        print(f"Parsed API Gateway event {self.event}")
    
class ParseSqsMessage():
    def __init__(self, event):
        self.event = json.loads(event["Records"][0]['body'])
        print(f"Parsed SQS message {self.event}")