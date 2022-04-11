# Note before continuing 

### This probably violates the TOS of hypergryph so use it at your own risk.

____________

# ArknightsCrisisSimulator
Proxy Arknights Contingency Contract info in order to replay past permanent maps with their respective risks

## How To

1. Install [mitmproxy](https://mitmproxy.org/) and [python3](https://www.python.org/downloads/).
2. Configure your emulator to pass data through mitmproxy. [Link](https://docs.mitmproxy.org/stable/overview-getting-started/)
3. Clone the repo
4. Run `pip install -r requirements.txt` in the cloned folder
5. Edit the cc number in `ak.py` to what you want.
6. Edit the risks in `rune\<your_chosen_cc>.py` to your liking
7. Run `mitmdump.exe -s ak.py` in the cloned folder
8. Restart arknights in your emulator.

Close the console you ran in step `7` and repeat steps `5-8` if you want to edit risks or cc maps
