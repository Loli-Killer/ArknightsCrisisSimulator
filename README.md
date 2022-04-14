# Note before continuing 

### This probably violates the TOS of hypergryph so use it at your own risk.

____________

# ArknightsCrisisSimulator
Proxy Arknights Contingency Contract info in order to replay past permanent maps with their respective risks
_____
## How To

1. Install [mitmproxy](https://mitmproxy.org/) and [python3](https://www.python.org/downloads/).
2. Configure your emulator to pass data through mitmproxy. [Link](https://docs.mitmproxy.org/stable/overview-getting-started/)
3. Clone the repo.
4. Run `start.bat` in the cloned folder.
5. Edit the info you want on the opened window.
6. Click `Update`.
7. Restart arknights in your emulator.

Restart arknights every time you update risks or cc map.

_____
## How it works (for those who care)

When you enter the "terminal", it will make a GET request to `https://gs.arknights.global:8443/crisis/getInfo` "once" only. This is the main reason why you need to restart the game every time you update the risks. (Another reason below)

After getting the info from `/crisis/getInfo`, the client will parse the data locally on client side and doesn't validate the CC data changes we make. So, we can intercept the response from the server, modify the data and then send the data back to the client.

When you actually modify and then try to select the risks, you will notice the risks either don't have the correct symbol, name, or description. Reasons are:

- Even though we can add more risk tag, when you start the CC map, the client sends a POST request to `https://gs.arknights.global:8443/crisis/battleStart` with the body which includes a list of the `runeId` which is the risk tag IDs you selected for battle. If you pass a `runeId` that isn't actually available in the original data, the server will response with an error which prevents us from entering the battle.
- The client doesn't support risk points greater than 3 so you can't get an accurate number of risks you've selected in the client directly.

To workaround this, I've combined multiple risks into one risk and then replace the original risk. This is the reason why in the descriptions, the descriptions of multiple risks are combined and prepended with (Risk `<count>`). The edited risks are also renamed as "Edited Risk"

For the symbol, I just thought it didn't matter so I didn't bother changing them since it will just be a combination of multiple risks.

After you finished/failed/exited the battle, the client does another POST request to `https://gs.arknights.global:8443/crisis/battleFinish`. Since we are playing with modified data, we obviously don't want to send the result back to the game server. Which is why whenever you are done with the battle, the script purposely redirects `https://gs.arknights.global:8443` to `http://localhost` which will make the client errors out causing you to restart the game.

Even though, all of the modifications so far doesn't seem to recieve any error from the server or trigger some "cheat" protection or whatever, do use the script at your own risk.
______
## TODO

CC Stages

- [x] CC#6
- [x] CC#5
- [ ] CC#4
- [ ] CC#3
- [ ] CC#2
- [ ] CC#1
- [ ] CC#0

UI
- [x] Add a UI for easy editing
- [ ] Maybe add correct symbol and make the UI similar to arknights original UI ?

Misc
- [ ] Allow adding custom risks