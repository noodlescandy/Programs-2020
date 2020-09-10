import requests
import time
discord_webhook_url = 'https://discordapp.com/api/webhooks/735389499328167968/bOJSAnIdWsW2ATprfLMtOtYibU_0OZpq4PtiEEFqatHtBrMVv5SWcYPP-NyAwPdjPcBr'
Message = {
    "content": "hey",
    "avatar_url": "https://www.jennstrends.com/wp-content/uploads/2013/10/bad-profile-pic-2-768x768.jpeg",  #"/home/timothy/Pictures/test/'test 1.jpg'",
    "username": "Man 1",
    # "tts": true # line does not work, error is : "tts": true NameError: name 'true' is not defined

}
requests.post(discord_webhook_url, data=Message)
time.sleep(1)
Message = {
    "content": "hi",
    "username": "Man 2",
    "avatar_url": "https://www.whatsappprofiledpimages.com/wp-content/uploads/2018/07/cool-profile-pictures47-300x300.jpg", 
    # "tts": true # line does not work, error is : "tts": true NameError: name 'true' is not defined

}
requests.post(discord_webhook_url, data=Message)

