import math
import json

import mitmproxy.http

def generate_risks(org_runes, included_risks, new_risks_data):
    org_runes_keys = [rune for rune in list(org_runes.keys()) if "buff" not in rune]
    if len(org_runes_keys) < len(included_risks):
        risk_per_tag = math.ceil(len(included_risks)/len(org_runes_keys))
        count = 0
        for i in range(0, len(included_risks), risk_per_tag):
            modified_rune = {}
            new_runes = []
            end_range = i+risk_per_tag if i+risk_per_tag < len(included_risks) else len(included_risks)
            for j in range(i, end_range):
                new_runes.append(new_risks_data[included_risks[j]])
            new_descrption = []
            new_points = 0
            new_rune_data = []
            for each_rune in new_runes:
                new_descrption.append(each_rune["description"])
                new_points += each_rune["points"]
                new_rune_data += each_rune["runes"]
            modified_rune = {
                "id": org_runes_keys[count],
                "points": new_points if new_points <= 3 else 3,
                "mutexGroupKey": None,
                "description": " + ".join(new_descrption) + f" (Risk {new_points})",
                "runes": new_rune_data
            }
            org_runes.update({
                org_runes_keys[count]: modified_rune
            })
            count += 1

    else:
        for index, risk in enumerate(included_risks):
            modified_rune = {
                "id": org_runes_keys[index],
                "points": new_risks_data[risk]["points"] if new_risks_data[risk]["points"] <= 3 else 3,
                "mutexGroupKey": None,
                "description": f'{new_risks_data[risk]["description"]} (Risk {new_risks_data[risk]["points"]})',
                "runes": new_risks_data[risk]["runes"]
            }
            org_runes.update({
                org_runes_keys[index]: modified_rune
            })

    return org_runes


class AKRedirect:

  def __init__(self):
    print('Addon for Redirecting Arknight [EN] Loaded !')

  def request(self, flow: mitmproxy.http.HTTPFlow):
    # Manually making the client errors out to prevent sending modified data back to server
    if 'crisis/battleFinish' in flow.request.path:
      if 'gs.arknights.global' in flow.request.pretty_host:
        flow.request.host = "localhost"
        flow.request.scheme = 'http'
        
    if 'android.bugly.qq.com' in flow.request.pretty_host:
        flow.request.host = "localhost"
        flow.request.scheme = 'http'

  def response(self, flow: mitmproxy.http.HTTPFlow):
    # Modify cc info before sending response back to client
    if 'crisis/getInfo' in flow.request.path:
        info = json.loads(flow.response.get_text())

        with open('current_cc.txt') as f:
            cc_num = f.read().strip()

        with open(f'rune\\{cc_num}\\riskdata.json') as f:
            cc_risks = json.load(f)

        with open(f'rune\\{cc_num}\\selectedrisks.json') as f:
            included_risks = json.load(f)

        with open(f'rune\\{cc_num}\\mapdata.json') as f:
            cc_stage_data = json.load(f)

        currentStage = info["playerDataDelta"]["modified"]["crisis"]["training"]["currentStage"][0]
        info["data"]["trainingInfo"]["stages"][currentStage].update(cc_stage_data)
        rune_keys = [rune for rune in list(info["data"]["stageRune"][currentStage].keys()) if "buff" not in rune]
        selected_risk_count = len(included_risks)
        rune_count_can_change = len(rune_keys)
        risk_range = math.ceil(selected_risk_count/math.ceil(selected_risk_count/rune_count_can_change))

        for i in range(risk_range):
            for eachRuneIndex in range(len(info["data"]["runeInfoList"][currentStage])):
                if info["data"]["runeInfoList"][currentStage][eachRuneIndex]["runeId"] == rune_keys[i]:
                    info["data"]["runeInfoList"][currentStage][eachRuneIndex]["runeName"] = "Edited Risk"
                    break

        info["data"]["stageRune"][currentStage] = generate_risks(info["data"]["stageRune"][currentStage], included_risks, cc_risks)
        flow.response.text = json.dumps(info)


addons = [
  AKRedirect()
]
