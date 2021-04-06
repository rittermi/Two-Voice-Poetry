import json
import random

def getGround():
  floors = ["field","earth","dirt","gold", "grass", "mud"]
  floor = random.choice(floors)
  return floor

def lambda_handler(event, context):
    # TODO implement
    result = {
        "dialogAction":
        {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText"
            }
        }
    }
    if event["currentIntent"]["name"] == "testDrive":
        # Do the intent 1
        upper = int(event["currentIntent"]["slots"]["upperNumber"])
        lower = int(event["currentIntent"]["slots"]["lowerNumber"])
        result["dialogAction"]["message"]["content"] = "Your random number is " + \
            str(random.randint(lower, upper))
    elif event["currentIntent"]["name"] == "iwalk":
        place = event["currentIntent"]["slots"]["place"]
        if place == "below a setting sun":
           fancy = "its warmth"
        elif place == "beside a raging sea":
            fancy = "its roar"
        elif place == "among a grove of oak":
            fancy = "its life"
        result["dialogAction"]["message"]["content"] = "Surrounded by "+fancy+""
    elif event["currentIntent"]["name"] == "bigStretch":
        choices = ["A storm above.", "The waves below."]
        choice = random.choice(choices)
        result["dialogAction"]["message"]["content"] = choice
    elif event["currentIntent"]["name"] == "smile":
        looks = ["a sardonic smile.", "a pensive stare."]
        look = random.choice(looks)
        result["dialogAction"]["message"]["content"] = "And me, " +look+""
    elif event["currentIntent"]["name"] == "overUnder":
        floor = getGround()
        result["dialogAction"]["message"]["content"] = "The " +floor+" below."
    elif event["currentIntent"]["name"] == "times":
        whens = ["Until the sky clears and seasons numbering ", "Before the setting sun and seasons numbering "]
        when = random.choice(whens)
        result["dialogAction"]["message"]["content"] =  when + str(random.randint(21, 99))
    return result