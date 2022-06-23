import json

import PySimpleGUI as sg

with open("cc_entries.json") as f:
    cc_entries = json.load(f)

def generate_all_cc_risks():
    cc_layouts = []
    for each_cc in cc_entries:
        with open(f"rune\\{each_cc}\\riskdata.json") as f:
            all_risks = json.load(f)
        with open(f"rune\\{each_cc}\\selectedrisks.json") as f:
            selected_risks = json.load(f)
        risk_layout = []
        for each_risk in all_risks:
            enabled = False
            if each_risk in selected_risks:
                enabled = True
            new_risk = [sg.Checkbox(
                f'{all_risks[each_risk]["description"]} (Risk {all_risks[each_risk]["points"]})',
                default=enabled, key=f"{each_cc}_{each_risk}", enable_events=True
            )]
            risk_layout.append(new_risk)
        cc_layout = sg.Column(risk_layout, scrollable=True, visible=False, key=each_cc, expand_x=True)
        cc_layouts.append(cc_layout)
    return cc_layouts

def check_conflicts():
    keys = list(window.key_dict.keys())
    for cc_id in cc_entries:

        with open(f"rune\\{cc_id}\\riskdata.json") as f:
            all_risks = json.load(f)

        enabled_groups = []
        enabled_checkboxs = []
        for key in keys:
            if key.startswith(f"{cc_id}_"):
                if values[key] == True:
                    group = all_risks[key.split(f"{cc_id}_")[1]]["mutexGroupKey"]
                    if group:
                        enabled_checkboxs.append(key)
                        enabled_groups.append(group)

        for risk in all_risks:
            if all_risks[risk]["mutexGroupKey"] in enabled_groups:
                if f"{cc_id}_{risk}" not in enabled_checkboxs:
                    window[f"{cc_id}_{risk}"].Update(disabled=True)
            else:
                window[f"{cc_id}_{risk}"].Update(disabled=False)


def calculate_risks():
    total_risks = 0
    for cc_id in cc_entries:
        if cc_entries[cc_id] == values["cc_num"]:
            current_cc_num = cc_id
            with open(f"rune\\{current_cc_num}\\riskdata.json") as f:
                current_cc_data = json.load(f)
            break
    
    keys = list(window.key_dict.keys())
    for key in keys:
        if key.startswith(f"{current_cc_num}_"):
            if values[key] == True:
                total_risks += current_cc_data[key.split(f"{cc_id}_")[1]]["points"]

    return total_risks

def update_risks():
    for cc_id in cc_entries:
        if cc_entries[cc_id] == values["cc_num"]:
            current_cc_num = cc_id

    included_risks = []
    keys = list(window.key_dict.keys())
    for key in keys:
        if key.startswith(f"{current_cc_num}_"):
            if values[key] == True:
                included_risks.append(key.split(f"{current_cc_num}_")[1])

    with open(f"rune\\{current_cc_num}\\selectedrisks.json", "w") as f:
        json.dump(included_risks, f, indent=4)

    with open("current_cc.txt", "w") as f:
        f.write(current_cc_num)


layout = [
    [sg.Frame(
        layout=[[
            sg.DropDown(
                [cc_entries[cc_name] for cc_name in cc_entries],
                auto_size_text=True,
                readonly=True,
                enable_events=True,
                key="cc_num"
            ),
            sg.Push(), sg.Text("Total Risks Selected: 0", key="total_risks")
        ]],
        title="Select CC#",
        expand_x=True
    )],
    [sg.Frame(
        layout=[
            generate_all_cc_risks() + [sg.Text("Select CC#", key="default_cc_risk")]
        ],
        title='Select risks',
        expand_x=True,
        size=(1000, 500)
    )],
    [
        sg.Push(),
        sg.Button("Update", enable_events=True, key="update_risks")
    ]
]

window = sg.Window("Arknights Crisis Simulator", resizable=True, layout=layout)

while True:
    event, values = window.read()

    if event in (None, 'Exit'):
        break

    if values["cc_num"]:
        check_conflicts()
        total_risks = calculate_risks()
        window["total_risks"].Update(f"Total Risks Selected: {total_risks}")

    if event == 'cc_num':
        window["default_cc_risk"].Update(visible=False)
        for cc_id in cc_entries:
            if cc_entries[cc_id] == values[event]:
                window[cc_id].Update(visible=True)
            else:
                window[cc_id].Update(visible=False)

    if event == 'update_risks' and values["cc_num"]:
        update_risks()
        sg.Popup(
            "Risks Updated. Restart game to apply new risks.",
            title="Risks Updated", keep_on_top=True
        )

window.close()
