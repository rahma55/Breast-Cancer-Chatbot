from typing import Dict, Text, List, Optional, Any

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.executor import CollectingDispatcher, Action
from rasa_sdk.events import AllSlotsReset, SlotSet
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.types import DomainDict

# show projects
class ActionService(Action):

    def name(self) -> Text:
        return "action_service"

    def run(self,dispatcher: CollectingDispatcher,
            tracker:Tracker,
            domain: Dict[Text ,Any]) -> List[Dict[Text, Any]]:
        buttons=[
            {"payload":'/docs{"content_type":"blogs"}',"title":"Documentation"},
            {"payload":'/video{"content_type":"video"}',"title":"Video content"},
           
        ]
        dispatcher.utter_message(Text="How would you like to recieve the information?",buttons=buttons)

        return []

class ActionService_fr(Action):

    def name(self) -> Text:
        return "action_service_fr"

    def run(self,dispatcher: CollectingDispatcher,
            tracker:Tracker,
            domain: Dict[Text ,Any]) -> List[Dict[Text, Any]]:
        buttons=[
            {"payload":'/docs_fr{"content_type":"blogs"}',"title":"Documentation"},
            {"payload":'/video_fr{"content_type":"video"}',"title":"Video content"},
           
        ]
        dispatcher.utter_message(Text="Comment voudriez-vous recevoir les informations?",buttons=buttons)

        return []

