#Setup stuff
import asyncio
import json
import discord
from discord.ext import commands
import random
import requests
import hashlib

#test

#Matrix specific
import subprocess
import simplematrixbotlib as botlib
from urllib.request import ssl, socket
import datetime, smtplib

#Pull from config
with open("config.json") as f:
    data = json.load(f)

MATRIX_URL = data["MATRIX_URL"]
MATRIX_USER = data["MATRIX_USER"]
MATRIX_PASS = data["MATRIX_PASS"]

#Pull from cards.json
with open("cards.json") as f:
    cardData = json.load(f)

#Pull from RockDB
with open("rockDB.json") as f:
    rockDB = json.load(f)

pokeLowerList = open("nameLower.txt", "r")
pokeLowerListDatat = pokeLowerList.read()
pokeLowerListData = pokeLowerListDatat.split(',')
pokeLowerList.close()

pokeList = open("name.txt", "r")
pokeListDatat = pokeList.read()
pokeListData = pokeListDatat.split(',')
pokeList.close()

pokeTypeList = open("type.txt", "r")
pokeTypeDatat = pokeTypeList.read()
pokeTypeData = pokeTypeDatat.split(',')
pokeTypeList.close()

creds = botlib.Creds(MATRIX_URL, MATRIX_USER, MATRIX_PASS)
bot = botlib.Bot(creds)

PREFIX = data["command-prefix"]

# Help
@bot.listener.on_message_event
async def help(room, message):
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("help"):
        help_message = """
        Command prefix: ~
        Help:
         - Displays help
        Crypto commands:
         - Usage: "~ticker"
         - Tickers: btc, xmr, eth, ethc, ltc, doge, xrp
         - Displays market data for selected coin
        Geoip:
         - Usage: "~geoip target"
         - Displays geoip info on a target URL or IP address
        Hashing:
         - ~md5 (input)
         - ~sha256 (input)
         - ~sha512 (input)
         - Hashes input with the selected algorithm
        Conversion:
         - ~dec2bin (input) - decimal to binary
         - ~bin2dec (input) - binary to decimal
         - ~dec2hex (input) - decimal to hexidecimal
         - ~hex2dec (input) - hexidecimal to decimal
         - Converts the input
        Echo:
         - Usage: "~echo your message"
         - Echos your message back to you
        """
        await bot.api.send_markdown_message(room.room_id, help_message)

# BTC
@bot.listener.on_message_event
async def btc(room, message):
    #Displays the current exchange rate of btc
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("btc"):
        apiURL = 'https://api.coinlore.net/api/ticker/?id=90'
        btcData = requests.get(apiURL)
        btcJson = btcData.json()
        btcData.close()
        ticker = btcJson[0]["symbol"]
        usd_price = btcJson[0]["price_usd"]
        day_change = btcJson[0]["percent_change_24h"] + "%"
        week_change = btcJson[0]["percent_change_7d"] + "%"
        
        btc_message = "~Price information for Bitcoin~\nTicker: %s\nUSD Price: %s\n24hr change: %s\n7d change: %s" % (ticker, usd_price, day_change, week_change)
        await bot.api.send_markdown_message(room.room_id, btc_message)
    
# Monero
@bot.listener.on_message_event
async def xmr(room, message):
    #Displays the current exchange rate of xmr    
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("xmr"):
        apiURL = 'https://api.coinlore.net/api/ticker/?id=28'
        btcData = requests.get(apiURL)
        btcJson = btcData.json()
        btcData.close()
        ticker = btcJson[0]["symbol"]
        usd_price = btcJson[0]["price_usd"]
        day_change = btcJson[0]["percent_change_24h"] + "%"
        week_change = btcJson[0]["percent_change_7d"] + "%"
        
        xmr_message = "~Price information for Monero~\nTicker: %s\nUSD Price: %s\n24hr change: %s\n7d change: %s" % (ticker, usd_price, day_change, week_change)
        await bot.api.send_markdown_message(room.room_id, xmr_message)

# Ethereum
@bot.listener.on_message_event
async def eth(room, message):
    #Displays the current exchange rate of eth
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("eth"):
        apiURL = 'https://api.coinlore.net/api/ticker/?id=80'
        btcData = requests.get(apiURL)
        btcJson = btcData.json()
        btcData.close()
        ticker = btcJson[0]["symbol"]
        usd_price = btcJson[0]["price_usd"]
        day_change = btcJson[0]["percent_change_24h"] + "%"
        week_change = btcJson[0]["percent_change_7d"] + "%"
        
        eth_message = "~Price information for Ethereum~\nTicker: %s\nUSD Price: %s\n24hr change: %s\n7d change: %s" % (ticker, usd_price, day_change, week_change)
        await bot.api.send_markdown_message(room.room_id, eth_message)

# Ethereum Classic
@bot.listener.on_message_event
async def ethc(room, message):
    #Displays the current exchange rate of ethc    
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("ethc"):
        apiURL = 'https://api.coinlore.net/api/ticker/?id=118'    #ip = temp[2]
        btcData = requests.get(apiURL)
        btcJson = btcData.json()
        btcData.close()
        ticker = btcJson[0]["symbol"]
        usd_price = btcJson[0]["price_usd"]
        day_change = btcJson[0]["percent_change_24h"] + "%"
        week_change = btcJson[0]["percent_change_7d"] + "%"

        ethc_message = "~Price information for Ethereum Classic~\nTicker: %s\nUSD Price: %s\n24hr change: %s\n7d change: %s" % (ticker, usd_price, day_change, week_change)
        await bot.api.send_markdown_message(room.room_id, ethc_message)

# LTC
@bot.listener.on_message_event
async def ltc(room, message):
    #Displays the current exchange rate of LTC
    
    
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("ltc"):
        apiURL = 'https://api.coinlore.net/api/ticker/?id=1'
        btcData = requests.get(apiURL)
        btcJson = btcData.json()
        btcData.close()
        ticker = btcJson[0]["symbol"]
        usd_price = btcJson[0]["price_usd"]
        day_change = btcJson[0]["percent_change_24h"] + "%"
        week_change = btcJson[0]["percent_change_7d"] + "%"

        ltc_message = "~Price information for Litecoin~\nTicker: %s\nUSD Price: %s\n24hr change: %s\n7d change: %s" % (ticker, usd_price, day_change, week_change)
        await bot.api.send_markdown_message(room.room_id, ltc_message)

# DogeCoin
@bot.listener.on_message_event
async def doge(room, message):
    #Displays the current exchange rate of DogeCoin
    
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("doge"):
        apiURL = 'https://api.coinlore.net/api/ticker/?id=2'
        btcData = requests.get(apiURL)
        btcJson = btcData.json()
        btcData.close()
        ticker = btcJson[0]["symbol"]
        usd_price = btcJson[0]["price_usd"]
        day_change = btcJson[0]["percent_change_24h"] + "%"
        week_change = btcJson[0]["percent_change_7d"] + "%"

        doge_message = "~Price information for Dogecoin~\nTicker: %s\nUSD Price: %s\n24hr change: %s\n7d change: %s" % (ticker, usd_price, day_change, week_change)
        await bot.api.send_markdown_message(room.room_id, doge_message)

# Ripple
@bot.listener.on_message_event
async def xrp(room, message):
    #Displays the current exchange rate of xrp
    
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("xrp"):
        apiURL = 'https://api.coinlore.net/api/ticker/?id=58'
        btcData = requests.get(apiURL)
        btcJson = btcData.json()
        btcData.close()
        ticker = btcJson[0]["symbol"]
        usd_price = btcJson[0]["price_usd"]
        day_change = btcJson[0]["percent_change_24h"] + "%"
        week_change = btcJson[0]["percent_change_7d"] + "%"

        ripple_message = "~Price information for Ripple~\nTicker: %s\nUSD Price: %s\n24hr change: %s\n7d change: %s" % (ticker, usd_price, day_change, week_change)
        await bot.api.send_markdown_message(room.room_id, ripple_message)


# Geoip
@bot.listener.on_message_event
async def geoip(room, message):

    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("geoip"):
        command = str(message)
        temp = command.split(" ")

        ip = temp[2]

        apiURL = 'http://ip-api.com/json/' + ip
        ipData = requests.get(apiURL)
        geoipJSON = ipData.json()
        ipData.close()

        country = str(geoipJSON["country"])
        countryCode = str(geoipJSON["countryCode"])
        region = str(geoipJSON["region"])
        regionName = str(geoipJSON["regionName"])
        city = str(geoipJSON["city"])
        zipCode = str(geoipJSON["zip"])
        latitude = str(geoipJSON["lat"])
        longitude = str(geoipJSON["lon"])
        timezone = str(geoipJSON["timezone"])
        isp = str(geoipJSON["isp"])

        geoip_message = "~Geoip information for: " + ip + "~" + "\n" + "Country: " + country + "\n" + "Country Code: " + countryCode + "\n" + "Region: " + region + "\n" + "Region Name: " + regionName +  "\n" + "City: " + city + "\n" + "Zip Code: " + zipCode + "\n" + "Latitude: " + latitude + "\n" + "Longitude: " + longitude + "\n" + "Timezone: " + timezone + "\n" + "ISP: " + isp
        await bot.api.send_markdown_message(room.room_id, geoip_message)
    

# BASE CONVERSION

# Binary
# Decimal to binary
@bot.listener.on_message_event
async def dec2bin(room, message):

    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("dec2bin"):
        command = str(message)
        temp = command.split(" ")

        uinput = temp[2]
        
        apiURL = ("https://networkcalc.com/api/binary/" + uinput + "?from=10&to=2")
        convData = requests.get(apiURL)
        convJson = convData.json()
        convData.close()

        converted = convJson["converted"]

        convertedVal = "~%s in binary~\n%s" % (uinput, converted)
        await bot.api.send_markdown_message(room.room_id, convertedVal)
# Binary to decimal
@bot.listener.on_message_event
async def bin2dec(room, message):

    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("bin2dec"):
        command = str(message)
        temp = command.split(" ")

        uinput = temp[2]
        
        apiURL = ("https://networkcalc.com/api/binary/" + uinput + "?from=2&to=10")
        convData = requests.get(apiURL)
        convJson = convData.json()
        convData.close()

        converted = convJson["converted"]

        convertedVal = "~%s in decimal~\n%s" % (uinput, converted)
        await bot.api.send_markdown_message(room.room_id, convertedVal)

# Hex
# Decimal to hex
@bot.listener.on_message_event
async def dec2hex(room, message):

    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("dec2hex"):
        command = str(message)
        temp = command.split(" ")

        uinput = temp[2]
        
        apiURL = ("https://networkcalc.com/api/binary/" + uinput + "?from=10&to=16")
        convData = requests.get(apiURL)
        convJson = convData.json()
        convData.close()

        converted = convJson["converted"]

        convertedVal = "~%s in hex~\n%s" % (uinput, converted)
        await bot.api.send_markdown_message(room.room_id, convertedVal)
# Hex to decimal
@bot.listener.on_message_event
async def hex2dec(room, message):

    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("hex2dec"):
        command = str(message)
        temp = command.split(" ")

        uinput = temp[2]
        
        apiURL = ("https://networkcalc.com/api/binary/" + uinput + "?from=16&to=10")
        convData = requests.get(apiURL)
        convJson = convData.json()
        convData.close()

        converted = convJson["converted"]

        convertedVal = "~%s in decimal~\n%s" % (uinput, converted)
        await bot.api.send_markdown_message(room.room_id, convertedVal)

#HASHING
#MD5 hash
@bot.listener.on_message_event
async def md5(room, message):

    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("md5"):
        command = str(message)
        rawinput = command.split(' ', 1)[1]
        toHash = rawinput[5:]
        encoded = hashlib.md5(toHash.encode("utf-8")).hexdigest()
        
        message = "~MD5 hash of %s~" % (toHash) + "\n" + encoded
        await bot.api.send_markdown_message(room.room_id, message)

#SHA256 hash
@bot.listener.on_message_event
async def sha256(room, message):pokeLowerList = open("nameLower.txt", "r")
    pokeLowerListDatat = pokeLowerList.read()
    pokeLowerListData = pokeLowerListDatat.split(',')
    pokeLowerList.close()

    pokeList = open("name.txt", "r")
    pokeListDatat = pokeList.read()
    pokeListData = pokeListDatat.split(',')
    pokeList.close()

    pokeTypeList = open("type.txt", "r")
    pokeTypeDatat = pokeTypeList.read()
    pokeTypeData = pokeTypeDatat.split(',')
    pokeTypeList.close()
        toHash = rawinput[8:]
        encoded = hashlib.sha256(toHash.encode("utf-8")).hexdigest()
        
        message = "~SHA256 hash of %s~" % (toHash) + "\n" + encoded
        await bot.api.send_markdown_message(room.room_id, message)

#SHA512 hash
@bot.listener.on_message_event
async def sha512(room, message):

    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("sha512"):
        command = str(message)
        rawinput = command.split(' ', 1)[1]
        toHash = rawinput[8:]
        encoded = hashlib.sha512(toHash.encode("utf-8")).hexdigest()
        
        message = "~SHA512 hash of %s~" % (toHash) + "\n" + encoded
        await bot.api.send_markdown_message(room.room_id, message)

#IMAGE EXAMPLE
@bot.listener.on_message_event
async def test(room, message):

    match = botlib.MessageMatch(room, message, bot, PREFIX)
    example_image = "./alfred.jpg"
    if match.is_not_from_this_bot() and match.prefix() and match.command("test"):
        await bot.api.send_image_message(
            room_id=room.room_id,
            image_filepath=example_image)
        message = "Alfred"
        await bot.api.send_markdown_message(room.room_id, message)

#Pokedex

# Echo
@bot.listener.on_message_event
async def echo(room, message):
    """
    Example function that "echoes" arguements.
    Usage:
    user:  !echo say something
    bot:   say something
    """
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("echo"):
        print("Room: {r}, User: {u}, Message: {m}".format(r=room.room_id, u=str(message).split(':')[0], m=str(message).split(':')[-1].strip()))
        await bot.api.send_text_message(room.room_id, " ".join(arg for arg in match.args()))


bot.run()
