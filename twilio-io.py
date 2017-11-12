from twilio.twiml.voice_response import Dial, Number, VoiceResponse


def main():
    auto_call()

    return


def auto_call():

    # Get Emergency Service for location


    # Dial number (Would be emergency service)
    response = VoiceResponse()
    dial = Dial()
    dial.number('470-705-7212')
    response.append(dial)
    print(response)

    # Get pickup status
    response = VoiceResponse()
    response.dial('415-123-4567', action='/handleDialCallStatus', method='GET')
    response.say('I am unreachable')
    # Twilio will submit a request to the action URL with the parameter 'DialCallStatus'.
    # If nobody picks up, 'DialCallStatus' will be 'no-answer'.
    # If the line is busy, 'DialCallStatus' will be 'busy'.
    # If the called party picks up, 'DialCallStatus' will be 'completed'.
    # If a conference is successfully dialed, 'DialCallStatus' will be 'answered'.
    # If an invalid phone number was provided, 'DialCallStatus' will be 'failed'.

    print(response)

    # Automated Voice Intro = "(person's name)"

    # Get information from Smart911Connect Account
    # http://www.smart911connect.com/get-access/
    # Development Block :(
    # no free APIs that send medical info to Emergency Services, however they all return JSON
    # Use Mongoose, JSON -> DB -> JSON

    # Get information as JSON - Python NamedTuple -> String

    # Feed into IBM Watson
    import json
    from watson_developer_cloud import DialogV1 as Dialog

    dialog = Dialog(username='YOUR_USERNAME', password='YOUR_PASSWORD')
    dialog_id = 'YOUR_DIALOGID'
    conversation = dialog.conversation(dialog_id)
    client_id = conversation['client_id']
    print dialog.update_profile(dialog_id=dialog_id, client_id=client_id,
                                name_values={"name_values": [{"name": "Product_Name", "value": "Sunglasses"}]})
    print dialog.update_profile(dialog_id=dialog_id, client_id=client_id,
                                name_values=[{"name": "Product_Name", "value": "Sunglasses"}])


    # Operator Interface with Twilio





    return


if __name__ == '__main__':
    main()
