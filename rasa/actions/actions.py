# Custom actions for Rasa to query store state and perform transfers
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import os

STORE_API = os.environ.get('STORE_API', 'http://node-app:3000/stores')

class ActionCheckStore(Action):
    def name(self) -> Text:
        return "action_check_store"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        store_id = tracker.get_slot('store_id') or '1'
        try:
            r = requests.get(f"{STORE_API}/{store_id}")
            data = r.json()
            if data.get('isOpen'):
                dispatcher.utter_message(text="The store is open now. Would you like to be connected to an agent?")
            else:
                dispatcher.utter_message(text="Sorry, the store is currently closed. Our hours are 09:00 to 18:00.")
        except Exception as e:
            dispatcher.utter_message(text="Sorry, I couldn't check the store status right now.")
        return []

class ActionConnectAgent(Action):
    def name(self) -> Text:
        return "action_connect_agent"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # In a real deployment, set a flag or call the telephony API to bridge to agent
        dispatcher.utter_message(text="Okay, connecting you to an agent now.")
        return []
