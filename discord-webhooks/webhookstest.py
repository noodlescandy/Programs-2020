import requests
discord_webhook_url = 'https://discordapp.com/api/webhooks/735389499328167968/bOJSAnIdWsW2ATprfLMtOtYibU_0OZpq4PtiEEFqatHtBrMVv5SWcYPP-NyAwPdjPcBr'
Message = {
    "content": "@everyone hello world"
}
requests.post(discord_webhook_url, data=Message)
# tested and it works!
