#Setup stuff
import json
import random
import requests
import hashlib
import urllib.request

#Matrix specific
import simplematrixbotlib as botlib
from urllib.request import ssl, socket
import os

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
        Pokedex:
         - ~poke (name or number) - returns a specific pokemon
         - ~poke rand - returns a random pokemon
        Tarot:
         - Usage: "~tarot (deck) (amount)"
         - Decks: 1: default, 2: crows
         - Returns a set amount of cards randomly selected from a chosen deck
        Eight ball:
         - Usage: "~eight"
         - Returns a fortune
        GIFs:
         - ~getrotated
         - ~goldfish
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
        try:
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
        except:
            message = "Invalid input"
            await bot.api.send_markdown_message(room.room_id, message)

# Monero
@bot.listener.on_message_event
async def xmr(room, message):
    #Displays the current exchange rate of xmr    
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("xmr"):
        try:
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
        except:
            message = "Invalid input"
            await bot.api.send_markdown_message(room.room_id, message)

# Ethereum
@bot.listener.on_message_event
async def eth(room, message):
    #Displays the current exchange rate of eth
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("eth"):
        try:
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
        except:
            message = "Invalid input"
            await bot.api.send_markdown_message(room.room_id, message)

# Ethereum Classic
@bot.listener.on_message_event
async def ethc(room, message):
    #Displays the current exchange rate of ethc    
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("ethc"):
        try:
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
        except:
            message = "Invalid input"
            await bot.api.send_markdown_message(room.room_id, message)

# LTC
@bot.listener.on_message_event
async def ltc(room, message):
    #Displays the current exchange rate of LTC
    
    
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("ltc"):
        try:
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
        except:
            message = "Invalid input"
            await bot.api.send_markdown_message(room.room_id, message)

# DogeCoin
@bot.listener.on_message_event
async def doge(room, message):
    #Displays the current exchange rate of DogeCoin
    
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("doge"):
        try:
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
        except:
            message = "Invalid input"
            await bot.api.send_markdown_message(room.room_id, message)

# Ripple
@bot.listener.on_message_event
async def xrp(room, message):
    #Displays the current exchange rate of xrp
    
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("xrp"):
        try:
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
        except:
            message = "Invalid input"
            await bot.api.send_markdown_message(room.room_id, message)


# Geoip
@bot.listener.on_message_event
async def geoip(room, message):

    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("geoip"):
        try:
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
        except:
            message = "Invalid input"
            await bot.api.send_markdown_message(room.room_id, message)

# Binary
# Decimal to binary
@bot.listener.on_message_event
async def dec2bin(room, message):

    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("dec2bin"):
        try:
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

        except:
            message = "Invalid input"
            await bot.api.send_markdown_message(room.room_id, message)
# Binary to decimal
@bot.listener.on_message_event
async def bin2dec(room, message):

    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("bin2dec"):
        try:
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
        except:
            message = "Invalid input"
            await bot.api.send_markdown_message(room.room_id, message)

# Hex
# Decimal to hex
@bot.listener.on_message_event
async def dec2hex(room, message):

    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("dec2hex"):
        try:
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
        except:
            message = "Invalid input"
            await bot.api.send_markdown_message(room.room_id, message)

# Hex to decimal
@bot.listener.on_message_event
async def hex2dec(room, message):

    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("hex2dec"):
        try:
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
        except:
            message = "Invalid input"
            await bot.api.send_markdown_message(room.room_id, message)

#HASHING
#MD5 hash
@bot.listener.on_message_event
async def md5(room, message):

    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("md5"):
        try:
            command = str(message)
            rawinput = command.split(' ', 1)[1]
            toHash = rawinput[5:]
            encoded = hashlib.md5(toHash.encode("utf-8")).hexdigest()
            message = "~MD5 hash of %s~" % (toHash) + "\n" + encoded
            await bot.api.send_markdown_message(room.room_id, message)
        except:
            message = "Invalid input"
            await bot.api.send_markdown_message(room.room_id, message)

#SHA512 hash
@bot.listener.on_message_event
async def sha512(room, message):

    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("sha512"):
        try:
            command = str(message)
            rawinput = command.split(' ', 1)[1]
            toHash = rawinput[8:]
            encoded = hashlib.sha512(toHash.encode("utf-8")).hexdigest()
            message = "~SHA512 hash of %s~" % (toHash) + "\n" + encoded
            await bot.api.send_markdown_message(room.room_id, message)
        except:
            message = "Invalid input"
            await bot.api.send_markdown_message(room.room_id, message)
'''
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
'''

#Pokedex
@bot.listener.on_message_event
async def poke(room, message):

    match = botlib.MessageMatch(room, message, bot, PREFIX)

    if match.is_not_from_this_bot() and match.prefix() and match.command("poke"):
        try:
            command = str(message)
            rawinput = command.split(' ', 1)[1]
            uInput = rawinput[6:]

            if uInput.isnumeric():
                pokeNumberData = str(uInput).zfill(3)

                query = (int(pokeNumberData) - 1)

                image = 'https://www.serebii.net/pokemon/art/' + pokeNumberData + '.png'
                name=pokeListData[query]
                pokeType=pokeTypeData[query]
                number=pokeNumberData
        
            elif uInput.lower() == "rand":

                randNum = random.randint(1, 1025)

                pokeNumberData = str(randNum).zfill(3)

                query = (int(pokeNumberData) - 1)

                image = 'https://www.serebii.net/pokemon/art/' + pokeNumberData + '.png'
                name=pokeListData[query]
                pokeType=pokeTypeData[query]
                number=pokeNumberData

            else:
                inLower = uInput.lower()
                pokeNum = (pokeLowerListData.index(inLower) + 1)
                pokeNumberData = str(pokeNum).zfill(3)

                query = (int(pokeNumberData) - 1)

                image = 'https://www.serebii.net/pokemon/art/' + str(pokeNumberData) + '.png'
                name = pokeListData[query]
                pokeType = pokeTypeData[query]
                number = pokeNumberData
        
            imgURL = image

            urllib.request.urlretrieve(imgURL, "temp.png")
        
            message = "Name: %s\nNumber: %s\nType: %s\n" % (name, number, pokeType)

            await bot.api.send_markdown_message(room.room_id, message)
            await bot.api.send_image_message(
                room_id=room.room_id,
                image_filepath="temp.png")
            file_path = "temp.png"

            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"File '{file_path}' deleted successfully.")
            else:
                print(f"File '{file_path}' does not exist.")
        except:
            message = "Invalid input"
            await bot.api.send_markdown_message(room.room_id, message)

#Tarot
@bot.listener.on_message_event
async def tarot(room, message):

    match = botlib.MessageMatch(room, message, bot, PREFIX)

    if match.is_not_from_this_bot() and match.prefix() and match.command("tarot"):
        try:
            command = str(message)
            rawinput = command.split(' ', 1)[1]
            argsList = rawinput[7:].split(' ')
            deck = argsList[0]
            amount = int(argsList[1])

            pathPart = "Tarot/%s/" % (deck)

            for i in range(amount):

                num = random.randint(0,77)

                card = cardData[str(num + 1)]

                pos = random.randint(0,1)

                cardParts = card.split("|")

                name = cardParts[1]

                poseDescs = cardParts[2].split(";")

                if pos == 0:
                    description = poseDescs[0]
                    #position = "regular"
                    fileName = str(num+1) + ".jpg"
                    print(fileName)
                else:
                    description = poseDescs[1]
                    name = name + " Reversed"
                    #position = "reversed"
                    fileName = "r" + str(num+1) + ".jpg"
                    print(fileName)

                capitalized_description = description[0].upper() + description[1:]

                file = (pathPart + fileName)

                message = "%s\n%s" % (name, capitalized_description)

                await bot.api.send_markdown_message(room.room_id, message)
                await bot.api.send_image_message(
                    room_id=room.room_id,
                    image_filepath=file)
        except:
            message = "Invalid input"

            await bot.api.send_markdown_message(room.room_id, message)

#Rocks
@bot.listener.on_message_event
async def rock(room, message):

    match = botlib.MessageMatch(room, message, bot, PREFIX)

    if match.is_not_from_this_bot() and match.prefix() and match.command("rock"):
        command = str(message).split(' ', 1)[1]
        uInput = command[6:].lower()

        try:
            if uInput == "rand":
                num = random.randint(0,58)
                rockstring="flourite,pyrite,fuchsite,quartzcrystal,agate,garnet,rhodochrosite,amazonite,hematite,ruby,amber,herkimerdiamond,rutilatedquartz,amethyst,howlite,sapphire,aquamarine,kunzite,selenite,aventurine,kyanite,silver,azurite,labradorite,smokyquartz,calcite,lapislazuli,sodalite,celestite,lepidolite,staurolite,chrysocolla,lingamstone,stromatolite,chrysoprase,malachite,tanzanite,citrine,moldavite,tigereye,cobaltiancalcite,moonstone,topaz,copal,obsidian,tourmalinatedquartz,danburite,onyx,tourmaline,emerald,opal,vanadinite,epidote,peridot,zircon,faitystone,petrifiedwood,fireagate,prehnite"
                rocklist = rockstring.split(",")
                uInput = rocklist[num]

            title=uInput.capitalize()
            metaphysical = rockDB[uInput]["metaphysical"]
        
            fileName = uInput.replace(' ', '') + ".jpg"
            file = "Rocks/" + fileName

            message = "Crystal name: %s\nMetaphysical effects: %s" % (title, metaphysical)

            await bot.api.send_markdown_message(room.room_id, message)
            await bot.api.send_image_message(
                room_id=room.room_id,
                image_filepath=file)
        except:
            message = "Invalid rock"

            await bot.api.send_markdown_message(room.room_id, message)
#List rocks
@bot.listener.on_message_event
async def rocklist(room, message):

    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("rocklist"):

        message = "Agate, Amber, Amethyst, Aventurine, Aquamarine, Azurite, Amazonite, Calcite, Celestite, Chrysocolla, Chrysoprase, Citrine, Cobaltian Calcite, Copal, Danburite, Emerald, Epidote, Fairy Stone, Fire Agate, Fluorite, Fuchsite, Garnet, Hematite, Herkimer Diamond, Howlite, Kunzite, Kyanite, Labradorite, Lapis Lazuli, Lepidolite, Lingam Stone, Malachite, Moldavite, Moonstone, Obsidian, Onyx, Opal, Peridot, Petrified Wood, Prehnite, Pyrite, Quartz Crystal, Rhodochrosite, Ruby, Rutilated Quartz, Sapphire, Selenite, Silver, Smoky Quartz, Sodalite, Staurolite, Stromatolite, Tanzanite, Tigereye, Topaz, Tourmaline, Tourmalinated Quartz, Vanadinite, Zircon"
        await bot.api.send_markdown_message(room.room_id, message)

#Goldfish
@bot.listener.on_message_event
async def goldfish(room, message):
    
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("goldfish"):
        try:
            imgURL = "https://i.kym-cdn.com/photos/images/newsfeed/002/486/154/c06.gif"
            urllib.request.urlretrieve(imgURL, "temp.gif")
            await bot.api.send_image_message(
                room_id=room.room_id,
                image_filepath="temp.gif")
            file_path = "temp.gif"

            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"File '{file_path}' deleted successfully.")
            else:
                print(f"File '{file_path}' does not exist.")
        except:
            message = "Error :("
            await bot.api.send_markdown_message(room.room_id, message)

#Get rotated idiot
@bot.listener.on_message_event
async def getrotated(room, message):
    
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("getrotated"):
        try:
            imgURL = "https://media.tenor.com/JNvOKP5bX6kAAAAM/rotate.gif"
            urllib.request.urlretrieve(imgURL, "temp.gif")
            await bot.api.send_image_message(
                room_id=room.room_id,
                image_filepath="temp.gif")
            file_path = "temp.gif"

            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"File '{file_path}' deleted successfully.")
            else:
                print(f"File '{file_path}' does not exist.")
        except:
            message = "Error :("
            await bot.api.send_markdown_message(room.room_id, message)

# Robohash
@bot.listener.on_message_event
async def robohash(room, message):

    match = botlib.MessageMatch(room, message, bot, PREFIX)

    if match.is_not_from_this_bot() and match.prefix() and match.command("robohash"):
        try:
            command = str(message)
            rawinput = command.split(' ', 1)[1]
            toHash = rawinput[10:]
            imgURL = "https://robohash.org/%s.png" % toHash
            
            urllib.request.urlretrieve(imgURL, "temp.png")
            await bot.api.send_image_message(
                room_id=room.room_id,
                image_filepath="temp.png")
            file_path = "temp.png"

            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"File '{file_path}' deleted successfully.")
            else:
                print(f"File '{file_path}' does not exist.")
        except:
            message = "Error :("
            await bot.api.send_markdown_message(room.room_id, message)

# Eight ball
@bot.listener.on_message_event
async def eight(room, message):
    
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("eight"):
        try:
            num = random.randint(1,11)
            imgURL = "8ball/" + str(num) + ".png"
            await bot.api.send_image_message(
                room_id=room.room_id,
                image_filepath=imgURL)
        except:
            message = "Error :("
            await bot.api.send_markdown_message(room.room_id, message)

# Coin flip
@bot.listener.on_message_event
async def coin(room, message):

    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("coin"):
        try:
            command = str(message)
            rawinput = command.split(' ')
            amount = int(rawinput[2])
            
            for i in range(amount):
                num = random.randint(0,1)
                if num == 1:
                    coin="Heads"
                    imgURL = "Coins/heads.png"
                    await bot.api.send_image_message(
                        room_id=room.room_id,
                        image_filepath=imgURL)
                    await bot.api.send_markdown_message(room.room_id, coin)
                else:
                    coin="Tails"
                    imgURL = "Coins/tails.png"
                    await bot.api.send_image_message(
                        room_id=room.room_id,
                        image_filepath=imgURL)
                    await bot.api.send_markdown_message(room.room_id, coin)

        except:
            message = "Error :("
            await bot.api.send_markdown_message(room.room_id, message)

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
