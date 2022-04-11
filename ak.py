import math
import json
from importlib import import_module

import mitmproxy.http

# Change the cc num you want to play
# Currently only cc#6 available
cc_num = 6

class AKRedirect:

  def __init__(self):
    print('Addon for Redirecting Arknight [EN] Loaded !')

  def request(self, flow: mitmproxy.http.HTTPFlow):
    # Manually making the client errors out to prevent sending modified data back to server
    if 'crisis/battleFinish' in flow.request.path:
      if 'gs.arknights.global' in flow.request.pretty_host:
        flow.request.host = "localhost"
        flow.request.scheme = 'http'

  def response(self, flow: mitmproxy.http.HTTPFlow):
    # Modify cc info before sending response back to client
    if 'crisis/getInfo' in flow.request.path:
      info = json.loads(flow.response.get_text())
      cc_module = import_module(f'rune.cc{cc_num}')
      currentStage = info["playerDataDelta"]["modified"]["crisis"]["training"]["currentStage"][0]
      cc_stage_data = cc_module.return_stage_data()
      info["data"]["trainingInfo"]["stages"][currentStage].update(cc_stage_data)
      rune_keys = list(info["data"]["stageRune"][currentStage].keys())
      risk_range = math.ceil(len(cc_module.included_risks)/math.ceil(len(cc_module.included_risks)/len(info["data"]["runeInfoList"][currentStage])))
      for i in range(risk_range):
        for eachRuneIndex in range(len(info["data"]["runeInfoList"][currentStage])):
          if info["data"]["runeInfoList"][currentStage][eachRuneIndex]["runeId"] == rune_keys[i]:
            info["data"]["runeInfoList"][currentStage][eachRuneIndex]["runeName"] = "Edited Risk"
            break
      info["data"]["stageRune"][currentStage] = cc_module.generate_risks(info["data"]["stageRune"][currentStage])
      flow.response.text = json.dumps(info)


addons = [
  AKRedirect()
]
