# alfred-psychopathy

Alfred bot on matrix

Python libraries used:
  -json
  -random
  -requests
  -hashlib
  -urllib.request
  -simplematrixbotlib
  -os

config.json:
{
    "MATRIX_URL": "https://home.server.url",
    "MATRIX_USER": "@USER:home.server.url",
    "MATRIX_PASS": "YOUR PASSWORD",
    "command-prefix": "~"
}

Set MATRIX_URL to your server url, MATRIX_USER to the bot user (you will need to create one on your server), MATRIX_PASS to that bot users password, and command-prefix to whatever you want to use to call your commands.

Commands included:

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

Run this on any pc with python3 and an internet connection. If you have any issues feel free to reach out I'll try to help but I'm still learning myself. Some of the code probably isn't the most efficent, I know the list of crystals is not implimented well it's something I will fix eventually as everything works right now. If you have advice also feel free to reach out. Enjoy the bot though, this is the documentation for the library I used to make this: https://simple-matrix-bot-lib.readthedocs.io/en/latest/quickstart.html
