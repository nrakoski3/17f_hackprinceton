

#### Get Emergency Service for location ####
    #

# Dial number (Would be emergency service)
# Get pickup status

    # Twilio will submit a request to the action URL with the parameter 'DialCallStatus'.
    # If nobody picks up, 'DialCallStatus' will be 'no-answer'.
    # If the line is busy, 'DialCallStatus' will be 'busy'.
    # If the called party picks up, 'DialCallStatus' will be 'completed'.
    # If a conference is successfully dialed, 'DialCallStatus' will be 'answered'.
    # If an invalid phone number was provided, 'DialCallStatus' will be 'failed'.

# Get information from Smart911Connect Account
# http://www.smart911connect.com/get-access/
# Development Block :(
# no free APIs that send medical info to Emergency Services, however they all return JSON
# Use Mongoose, JSON -> DB -> JSON

# Get information
    # Function that returns JSON

    ##### Save pre-built JSON and AUDIO files in database for faster I/0 ###
    ##### Rebuild with each push to the database #####
    ##### Time build & output VS output only ####


# JSON -> Python NamedTuple

# Use Python named tuple for Text to Speach

# Use IBM Text to Speech
# Credentials:
{
  "text_to_speech": [
    {
      "name": "json-to-speech-text-to-sp-1510448059170",
      "plan": "lite",
      "credentials": {
        "url": "https://stream.watsonplatform.net/text-to-speech/api",
        "username": "728659a3-2a8c-4df6-8d3a-e951cd8cc0ca",
        "password": "p7uNJT0BueoP"
      }
    }
  ]
# Synthesizes Text to Speech
curl -X POST -u {username}:{password} \
--header "Content-Type: application/json" \
--header "Accept: audio/wav" \
--data "{\"text\":\"hello world\"}" \
--output hello_world.wav \
"https://stream.watsonplatform.net/text-to-speech/api/v1/synthesize"

# Synthesize Text in Spanish
curl -X GET -u {username}:{password} \
--output hola_mundo.wav \
"https://stream.watsonplatform.net/text-to-speech/api/v1/synthesize?


# Twilio - Operator Interface:
    # ask operator if they recieved database information via "APIs"
        # if no - ask for fax number so database information can be faxed to 911 and then to hospital
            DB/ JSON ----> txt file API ??
        # if yes - ask if they would like to repeat initial message
            # if yes - repeat
            # if no - ask if they would like to end call