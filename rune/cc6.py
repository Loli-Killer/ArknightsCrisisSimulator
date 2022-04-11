# Change this
# Comment or uncomment risks you want to take
# Run the file first to make sure you aren't taking conflicting risks
# Or check mitmdump console for errors

included_risks = [
    # "shield_croc_1", #[Tiacauh Brave] Max HP +40%, ATK +15%, RES +20 - (Risk 1)
    # "shield_croc_aspd_2", #[Tiacauh Brave] Max HP +60%, ATK +30%, ASPD +75, RES +40 - (Risk 2)
    "shield_croc_aspd_3", #[Tiacauh Brave] Max HP +90%, ATK +50%, ASPD +150, RES +60, gains Stealth - (Risk 3)
    # "shield_croc_def_2", #[Tiacauh Brave] Max HP +80%, ATK +30%, RES +40, when blocked self DEF only drops 40% - (Risk 2)
    "shield_croc_def_3", #[Tiacauh Brave] Max HP +130%, ATK +50%, RES +60, no longer lowers own DEF when blocked - (Risk 3)
    # "boxer_croc_1", #[Tiacauh Fanatic] Max HP +40%, ASPD +30, Movement Speed +50%, Weight Level +1 - (Risk 1)
    "boxer_croc_2", #[Tiacauh Fanatic] Max HP+90%, ASPD +70, Movement Speed +100%, Weight Level +1, DEF lowering effect +100% - (Risk 2)
    # "caster_croc_1", #[Tiacauh Ritualist] Max HP +30%, ATK +30%, DEF +50% - (Risk 1)
    "caster_croc_2", #[Tiacauh Ritualist] Max HP +70%, ATK +70%, DEF +100%, Attack Range +60% - (Risk 2)
    # "enemy_atk_up_1", #All enemies ATK +15% - (Risk 1)
    # "enemy_atk_up_2", #All enemies ATK +40% - (Risk 2)
    "enemy_atk_up_3", #All enemies ATK +80% - (Risk 3)
    # "enemy_hp_up_1", #Enemies Max HP +20% - (Risk 1)
    # "enemy_hp_up_2", #Enemies Max HP +60% - (Risk 2)
    "enemy_hp_up_3", #Enemies Max HP +110% - (Risk 3)
    # "ally_aspd_down_1", #Ally ASPD -20 - (Risk 1)
    "ally_aspd_down_2", #Ally ASPD -40 - (Risk 2)
    # "ally_hp_down_1", #All allies’ Max HP -15% - (Risk 1)
    # "ally_hp_down_2", #All allies’ Max HP -30% - (Risk 2)
    "ally_hp_down_3", #All allies’ Max HP -50% - (Risk 3)
    # "guard_specialist_1", #Guard and Specialist DP cost doubled - (Risk 1)
    "guard_specialist_2", #DP Costs of Guards and Specialists is tripled, and the redeployment time extended by 50%. - (Risk 2)
    # "supporter_caster_1", #Supporter and Caster DP Cost doubled - (Risk 1)
    # "supporter_caster_2", #Supporter and Caster DP Cost tripled, and the redeployment time extended by 50%. - (Risk 2)
    # "dp_down_1", #DP Regeneration reduced by -25% - (Risk 1)
    # "dp_down_2", #DP Regeneration reduced by -50% - (Risk 2)
    "dp_down_3", #DP Regeneration reduced by -75% - (Risk 3)
    # "max_squad_1", #Maximum 10 operators in squad - (Risk 1)
    "max_squad_2", #Maximum 7 operators in squad - (Risk 2)
    # "deploy_limit_1", #Deploy Limit reduced to 7 - (Risk 1)
    # "deploy_limit_2", #Deploy Limit reduced to 5 - (Risk 2)
    # "sandstorm_direction_1", #Sandstorm will switch to blowing from right to left - (Risk 1)
    "sandstorm_direction_2", #Sandstorm will switch to blowing from top to bottom - (Risk 2)
    "max_hp_1", #No enemies escape (Level HP set to 1) - (Risk 1)
    "ally_atk_down", #Allies ATK -20% - (Risk 1)
    "enemy_def_up", #Enemy DEF +200 - (Risk 1)
    "sand_noslow", #Sandstorm no longer reduces enemy movement speed. - (Risk 1)
    "sand_dmg_2" #Sandstom’s HP loss effect +20% - (Risk 2)
]

####### Don't touch below unless you know what you are doing

MAP_DATA = {
    "levelId": "Obt/Rune/level_rune_08-01",
    "mapId": "rune_08-01",
    "code": "Barrenlands",
    "name": "Howling Desert",
    "loadingPicId": "loading_OOD_03",
    "description": "On the desolate plains where sandstorms reign supreme, locals and mercenaries alike fall together in a deadly clash, each seeking to usurp the other's wealth. It's time to correct such thinking.\n<@lv.item><Sandstorm></> Allied units caught inside the sandstorm will have reduced ATK, continuously take damage over time, and have extended redeployment time; Enemy units will instead be slowed\n<@lv.item><Dirt Mound></> A reinforceable structure that can be used to resist sandstorms; Dirt Mounds are naturally more durable in this environment and have higher HP",
    "picId": "ccmap_howlingsand",
    "logoPicId": "logo_sargon",
}

RUNES = {
    "shield_croc_1": {
        "description": "[Tiacauh Brave] Max HP +40%, ATK +15%, RES +20",
        "points": 1,
        "group": "shield_croc",
        "runes": [{
            "key": "enemy_attribute_mul",
            "selector": {
                "professionMask": 0,
                "buildableMask": 0,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [{
                "key": "max_hp",
                "value": 1.4,
                "valueStr": None
            },
            {
                "key": "enemy",
                "value": 0,
                "valueStr": "enemy_1098_cchmpn"
            },
            {
                "key": "atk",
                "value": 1.15,
                "valueStr": None
            }]
        },
        {
            "key": "enemy_attribute_add",
            "selector": {
                "professionMask": 0,
                "buildableMask": 0,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [
                {
                    "key": "magic_resistance",
                    "value": 20,
                    "valueStr": None
                },
                {
                    "key": "enemy",
                    "value": 0,
                    "valueStr": "enemy_1098_cchmpn"
                }
            ]
        }]
    },
    "shield_croc_aspd_2": {
        "description": "[Tiacauh Brave] Max HP +60%, ATK +30%, ASPD +75, RES +40",
        "points": 2,
        "group": "shield_croc",
        "runes": [{
            "key": "enemy_attribute_mul",
            "selector": {
                "professionMask": 0,
                "buildableMask": 0,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [{
                "key": "max_hp",
                "value": 1.6,
                "valueStr": None
            },
            {
                "key": "enemy",
                "value": 0,
                "valueStr": "enemy_1098_cchmpn"
            },
            {
                "key": "atk",
                "value": 1.3,
                "valueStr": None
            },
            {
                "key": "attack_speed",
                "value": 1.75,
                "valueStr": None
            }]
        },
        {
            "key": "enemy_attribute_add",
            "selector": {
                "professionMask": 0,
                "buildableMask": 0,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [
                {
                    "key": "magic_resistance",
                    "value": 40,
                    "valueStr": None
                },
                {
                    "key": "enemy",
                    "value": 0,
                    "valueStr": "enemy_1098_cchmpn"
                }
            ]
        }]
    },
    "shield_croc_aspd_3": {
        "description": "[Tiacauh Brave] Max HP +90%, ATK +50%, ASPD +150, RES +60, gains Stealth",
        "points": 3,
        "group": "shield_croc",
        "runes": [{
            "key": "enemy_attribute_mul",
            "selector": {
                "professionMask": 0,
                "buildableMask": 0,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [{
                "key": "max_hp",
                "value": 1.9,
                "valueStr": None
            },
            {
                "key": "enemy",
                "value": 0,
                "valueStr": "enemy_1098_cchmpn"
            },
            {
                "key": "atk",
                "value": 1.5,
                "valueStr": None
            },
            {
                "key": "attack_speed",
                "value": 2.5,
                "valueStr": None
            }]
        },
        {
            "key": "enemy_attribute_add",
            "selector": {
                "professionMask": 0,
                "buildableMask": 0,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [
                {
                    "key": "magic_resistance",
                    "value": 60,
                    "valueStr": None
                },
                {
                    "key": "enemy",
                    "value": 0,
                    "valueStr": "enemy_1098_cchmpn"
                }
            ]
        },
        {
            "key": "enemy_dynamic_ability_new",
            "selector": {
                "professionMask": 0,
                "buildableMask": 0,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [
                {
                    "key": "enemy",
                    "value": 0,
                    "valueStr": "enemy_1098_cchmpn"
                },
                {
                    "key": "key",
                    "value": 0,
                    "valueStr": "invisible"
                }
            ]
        }]
    },
    "shield_croc_def_2": {
        "description": "[Tiacauh Brave] Max HP +80%, ATK +30%, RES +40, when blocked self DEF only drops 40%",
        "points": 2,
        "group": "shield_croc",
        "runes": [{
            "key": "enemy_attribute_mul",
            "selector": {
                "professionMask": 0,
                "buildableMask": 0,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [{
                "key": "max_hp",
                "value": 1.8,
                "valueStr": None
            },
            {
                "key": "enemy",
                "value": 0,
                "valueStr": "enemy_1098_cchmpn"
            },
            {
                "key": "atk",
                "value": 1.3,
                "valueStr": None
            }]
        },
        {
            "key": "enemy_attribute_add",
            "selector": {
                "professionMask": 0,
                "buildableMask": 0,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [
                {
                    "key": "magic_resistance",
                    "value": 40,
                    "valueStr": None
                },
                {
                    "key": "enemy",
                    "value": 0,
                    "valueStr": "enemy_1098_cchmpn"
                }
            ]
        },
        {
            "key": "enemy_talent_blackb_add",
            "selector": {
                "professionMask": 0,
                "buildableMask": 0,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [
                {
                    "key": "enemy",
                    "value": 0,
                    "valueStr": "enemy_1098_cchmpn"
                },
                {
                    "key": "duel.cchmpn_t_buff_self.def",
                    "value": 0.3,
                    "valueStr": None
                }
            ]
        }]
    },
    "shield_croc_def_3": {
        "description": "[Tiacauh Brave] Max HP +130%, ATK +50%, RES +60, no longer lowers own DEF when blocked",
        "points": 3,
        "group": "shield_croc",
        "runes": [{
            "key": "enemy_attribute_mul",
            "selector": {
                "professionMask": 0,
                "buildableMask": 0,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [{
                "key": "max_hp",
                "value": 2.3,
                "valueStr": None
            },
            {
                "key": "enemy",
                "value": 0,
                "valueStr": "enemy_1098_cchmpn"
            },
            {
                "key": "atk",
                "value": 1.5,
                "valueStr": None
            }]
        },
        {
            "key": "enemy_attribute_add",
            "selector": {
                "professionMask": 0,
                "buildableMask": 0,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [
                {
                    "key": "magic_resistance",
                    "value": 60,
                    "valueStr": None
                },
                {
                    "key": "enemy",
                    "value": 0,
                    "valueStr": "enemy_1098_cchmpn"
                }
            ]
        },
        {
            "key": "enemy_talent_blackb_add",
            "selector": {
                "professionMask": 0,
                "buildableMask": 0,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [
                {
                    "key": "enemy",
                    "value": 0,
                    "valueStr": "enemy_1098_cchmpn"
                },
                {
                    "key": "duel.cchmpn_t_buff_self.def",
                    "value": 0.7,
                    "valueStr": None
                }
            ]
        }]
    },
    "boxer_croc_1": {
        "description": "[Tiacauh Fanatic] Max HP +40%, ASPD +30, Movement Speed +50%, Weight Level +1",
        "points": 1,
        "group": "boxer_croc",
        "runes": [{
            "key": "enemy_attribute_mul",
            "selector": {
                "professionMask": 0,
                "buildableMask": 0,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [{
                "key": "max_hp",
                "value": 1.4,
                "valueStr": None
            },
            {
                "key": "enemy",
                "value": 0,
                "valueStr": "enemy_1095_ccripr"
            },
            {
                "key": "attack_speed",
                "value": 1.3,
                "valueStr": None
            },
            {
                "key": "move_speed",
                "value": 1.5,
                "valueStr": None
            },]
        },
        {
            "key": "enemy_attribute_add",
            "selector": {
                "professionMask": 0,
                "buildableMask": 0,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [
                {
                    "key": "enemy",
                    "value": 0,
                    "valueStr": "enemy_1095_ccripr"
                },
                {
                    "key": "mass_level",
                    "value": 1,
                    "valueStr": None
                }
            ]
        }]
    },
    "boxer_croc_2": {
        "description": "[Tiacauh Fanatic] Max HP+90%, ASPD +70, Movement Speed +100%, Weight Level +1, DEF lowering effect +100%",
        "points": 2,
        "group": "boxer_croc",
        "runes": [{
            "key": "enemy_attribute_mul",
            "selector": {
                "professionMask": 0,
                "buildableMask": 0,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [{
                "key": "max_hp",
                "value": 1.9,
                "valueStr": None
            },
            {
                "key": "enemy",
                "value": 0,
                "valueStr": "enemy_1095_ccripr"
            },
            {
                "key": "attack_speed",
                "value": 1.7,
                "valueStr": None
            },
            {
                "key": "move_speed",
                "value": 2,
                "valueStr": None
            }]
        },
        {
            "key": "enemy_attribute_add",
            "selector": {
                "professionMask": 0,
                "buildableMask": 0,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [
                {
                    "key": "enemy",
                    "value": 0,
                    "valueStr": "enemy_1095_ccripr"
                },
                {
                    "key": "mass_level",
                    "value": 1,
                    "valueStr": None
                }
            ]
        },
        {
            "key": "enemy_talent_blackb_mul",
            "selector": {
                "professionMask": 0,
                "buildableMask": 0,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [
                {
                    "key": "enemy",
                    "value": 0,
                    "valueStr": "enemy_1095_ccripr"
                },
                {
                    "key": "defdown.def",
                    "value": 2,
                    "valueStr": None
                }
            ]
        }]
    },
    "caster_croc_1": {
        "description": "[Tiacauh Ritualist] Max HP +30%, ATK +30%, DEF +50%",
        "points": 1,
        "group": "caster_croc",
        "runes": [{
            "key": "enemy_attribute_mul",
            "selector": {
                "professionMask": 0,
                "buildableMask": 0,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [{
                "key": "max_hp",
                "value": 1.3,
                "valueStr": None
            },
            {
                "key": "enemy",
                "value": 0,
                "valueStr": "enemy_1096_ccwitch"
            },
            {
                "key": "def",
                "value": 1.5,
                "valueStr": None
            },
            {
                "key": "atk",
                "value": 1.3,
                "valueStr": None
            }]
        }]
    },
    "caster_croc_2": {
        "description": "[Tiacauh Ritualist] Max HP +70%, ATK +70%, DEF +100%, Attack Range +60%",
        "points": 2,
        "group": "caster_croc",
        "runes": [{
            "key": "enemy_attribute_mul",
            "selector": {
                "professionMask": 0,
                "buildableMask": 0,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [{
                "key": "max_hp",
                "value": 1.7,
                "valueStr": None
            },
            {
                "key": "enemy",
                "value": 0,
                "valueStr": "enemy_1096_ccwitch"
            },
            {
                "key": "def",
                "value": 2,
                "valueStr": None
            },
            {
                "key": "atk",
                "value": 1.7,
                "valueStr": None
            }]
        },
        {
            "key": "enemy_attackradius_mul",
            "selector": {
                "professionMask": 0,
                "buildableMask": 0,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [
                {
                    "key": "scale",
                    "value": 1.6,
                    "valueStr": None
                },
                {
                    "key": "enemy",
                    "value": 0,
                    "valueStr": "enemy_1096_ccwitch"
                }
            ]
        }]
    },
    "enemy_atk_up_1": {
        "description": "All enemies ATK +15%",
        "points": 1,
        "group": "enemy_atk_up",
        "runes": [{
            "key": "enemy_attribute_mul",
            "selector": {
                "professionMask": 1023,
                "buildableMask": 3,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [
                {
                    "key": "atk",
                    "value": 1.15,
                    "valueStr": None
                }
            ]
        }]
    },
    "enemy_atk_up_2": {
        "description": "All enemies ATK +40%",
        "points": 2,
        "group": "enemy_atk_up",
        "runes": [{
            "key": "enemy_attribute_mul",
            "selector": {
                "professionMask": 1023,
                "buildableMask": 3,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [
                {
                    "key": "atk",
                    "value": 1.4,
                    "valueStr": None
                }
            ]
        }]
    },
    "enemy_atk_up_3": {
        "description": "All enemies ATK +80%",
        "points": 3,
        "group": "enemy_atk_up",
        "runes": [{
            "key": "enemy_attribute_mul",
            "selector": {
                "professionMask": 1023,
                "buildableMask": 3,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [
                {
                    "key": "atk",
                    "value": 1.8,
                    "valueStr": None
                }
            ]
        }]
    },
    "enemy_hp_up_1": {
        "description": "Enemies Max HP +20%",
        "points": 1,
        "group": "enemy_hp_up",
        "runes": [{
            "key": "enemy_attribute_mul",
            "selector": {
                "professionMask": 0,
                "buildableMask": 0,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [
                {
                    "key": "max_hp",
                    "value": 1.2,
                    "valueStr": None
                }
            ]
        }]
    },
    "enemy_hp_up_2": {
        "description": "Enemies Max HP +60%",
        "points": 2,
        "group": "enemy_hp_up",
        "runes": [{
            "key": "enemy_attribute_mul",
            "selector": {
                "professionMask": 0,
                "buildableMask": 0,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [
                {
                    "key": "max_hp",
                    "value": 1.6,
                    "valueStr": None
                }
            ]
        }]
    },
    "enemy_hp_up_3": {
        "description": "Enemies Max HP +110%",
        "points": 3,
        "group": "enemy_hp_up",
        "runes": [{
            "key": "enemy_attribute_mul",
            "selector": {
                "professionMask": 0,
                "buildableMask": 0,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [
                {
                    "key": "max_hp",
                    "value": 2.1,
                    "valueStr": None
                }
            ]
        }]
    },
    "ally_aspd_down_1": {
        "description": "Ally ASPD -20",
        "points": 1,
        "group": "ally_aspd_down",
        "runes": [{
            "key": "char_attribute_add",
            "selector": {
                "professionMask": 767,
                "buildableMask": 3,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [
                {
                    "key": "attack_speed",
                    "value": -20,
                    "valueStr": None
                }
            ]
        }]
    },
    "ally_aspd_down_2": {
        "description": "Ally ASPD -40",
        "points": 2,
        "group": "ally_aspd_down",
        "runes": [{
            "key": "char_attribute_add",
            "selector": {
                "professionMask": 767,
                "buildableMask": 3,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [
                {
                    "key": "attack_speed",
                    "value": -40,
                    "valueStr": None
                }
            ]
        }]
    },
    "ally_hp_down_1": {
        "description": "All allies’ Max HP -15%",
        "points": 1,
        "group": "ally_hp_down",
        "runes": [{
            "key": "char_attribute_mul",
            "selector": {
                "professionMask": 767,
                "buildableMask": 3,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [
                {
                    "key": "max_hp",
                    "value": 0.85,
                    "valueStr": None
                }
            ]
        }]
    },
    "ally_hp_down_2": {
        "description": "All allies’ Max HP -30%",
        "points": 2,
        "group": "ally_hp_down",
        "runes": [{
            "key": "char_attribute_mul",
            "selector": {
                "professionMask": 767,
                "buildableMask": 3,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [
                {
                    "key": "max_hp",
                    "value": 0.7,
                    "valueStr": None
                }
            ]
        }]
    },
    "ally_hp_down_3": {
        "description": "All allies’ Max HP -50%",
        "points": 3,
        "group": "ally_hp_down",
        "runes": [{
            "key": "char_attribute_mul",
            "selector": {
                "professionMask": 767,
                "buildableMask": 3,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [
                {
                    "key": "max_hp",
                    "value": 0.5,
                    "valueStr": None
                }
            ]
        }]
    },
    "guard_specialist_1": {
        "description": "Guard and Specialist DP cost doubled",
        "points": 1,
        "group": "class_limit",
        "runes": [{
            "key": "char_cost_mul",
            "selector": {
                "professionMask": 65,
                "buildableMask": 3,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [
                {
                    "key": "scale",
                    "value": 2,
                    "valueStr": None
                }
            ]
        }]
    },
    "guard_specialist_2": {
        "description": "DP Costs of Guards and Specialists is tripled, and the redeployment time extended by 50%.",
        "points": 2,
        "group": "class_limit",
        "runes": [{
            "key": "char_cost_mul",
            "selector": {
                "professionMask": 65,
                "buildableMask": 3,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [
                {
                    "key": "scale",
                    "value": 3,
                    "valueStr": None
                }
            ]
        },
        {
            "key": "char_respawntime_mul",
            "selector": {
                "professionMask": 65,
                "buildableMask": 3,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [
                {
                    "key": "scale",
                    "value": 1.5,
                    "valueStr": None
                }
            ]
        }]
    },
    "supporter_caster_1": {
        "description": "Supporter and Caster DP Cost doubled",
        "points": 1,
        "group": "class_limit",
        "runes": [{
            "key": "char_cost_mul",
            "selector": {
                "professionMask": 46,
                "buildableMask": 3,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [
                {
                    "key": "scale",
                    "value": 2,
                    "valueStr": None
                }
            ]
        }]
    },
    "supporter_caster_2": {
        "description": "Supporter and Caster DP Cost tripled, and the redeployment time extended by 50%.",
        "points": 2,
        "group": "class_limit",
        "runes": [{
            "key": "char_cost_mul",
            "selector": {
                "professionMask": 46,
                "buildableMask": 3,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [
                {
                    "key": "scale",
                    "value": 3,
                    "valueStr": None
                }
            ]
        },
        {
            "key": "char_respawntime_mul",
            "selector": {
                "professionMask": 65,
                "buildableMask": 3,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [
                {
                    "key": "scale",
                    "value": 1.5,
                    "valueStr": None
                }
            ]
        }]
    },
    "dp_down_1": {
        "description": "DP Regeneration reduced by -25%",
        "points": 1,
        "group": "dp_down",
        "runes": [{
            "key": "global_cost_recovery_mul",
            "selector": {
                "professionMask": 0,
                "buildableMask": 0,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None,
            },
            "blackboard": [
                {
                    "key": "scale",
                    "value": 1.333,
                    "valueStr": None
                }
            ]
        }]
    },
    "dp_down_2": {
        "description": "DP Regeneration reduced by -50%",
        "points": 2,
        "group": "dp_down",
        "runes": [{
            "key": "global_cost_recovery_mul",
            "selector": {
                "professionMask": 0,
                "buildableMask": 0,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None,
            },
            "blackboard": [
                {
                    "key": "scale",
                    "value": 2,
                    "valueStr": None
                }
            ]
        }]
    },
    "dp_down_3": {
        "description": "DP Regeneration reduced by -75%",
        "points": 3,
        "group": "dp_down",
        "runes": [{
            "key": "global_cost_recovery_mul",
            "selector": {
                "professionMask": 0,
                "buildableMask": 0,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None,
            },
            "blackboard": [
                {
                    "key": "scale",
                    "value": 4,
                    "valueStr": None
                }
            ]
        }]
    },
    "max_squad_1": {
        "description": "Maximum 10 operators in squad",
        "points": 1,
        "group": "max_squad_deploy_limit",
        "runes": [{
            "key": "global_squad_num_limit",
            "selector": {
                "professionMask": 0,
                "buildableMask": 0,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None,
            },
            "blackboard": [
                {
                    "key": "value",
                    "value": 10,
                    "valueStr": None
                }
            ]
        }]
    },
    "max_squad_2": {
        "description": "Maximum 7 operators in squad",
        "points": 2,
        "group": "max_squad_deploy_limit",
        "runes": [{
            "key": "global_squad_num_limit",
            "selector": {
                "professionMask": 0,
                "buildableMask": 0,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None,
            },
            "blackboard": [
                {
                    "key": "value",
                    "value": 7,
                    "valueStr": None
                }
            ]
        }]
    },
    "deploy_limit_1": {
        "description": "Deploy Limit reduced to 7",
        "points": 1,
        "group": "max_squad_deploy_limit",
        "runes": [{
            "key": "global_placable_char_num_add",
            "selector": {
                "professionMask": 0,
                "buildableMask": 0,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [
                {
                    "key": "value",
                    "value": -2,
                    "valueStr": None
                }
            ]
        }]
    },
    "deploy_limit_2": {
        "description": "Deploy Limit reduced to 5",
        "points": 2,
        "group": "max_squad_deploy_limit",
        "runes": [{
            "key": "global_placable_char_num_add",
            "selector": {
                "professionMask": 0,
                "buildableMask": 0,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [
                {
                    "key": "value",
                    "value": -4,
                    "valueStr": None
                }
            ]
        }]
    },
    "sandstorm_direction_1": {
        "description": "Sandstorm will switch to blowing from right to left",
        "points": 1,
        "group": "sandstorm_direction",
        "runes": [{
            "key": "level_predefines_enable",
            "selector": {
                "professionMask": 0,
                "buildableMask": 0,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [{
                "key": "trap_036_storm#1",
                "value": 0,
                "valueStr": None
            },
            {
                "key": "trap_036_storm#2",
                "value": 1,
                "valueStr": None
            }]
        }]
    },
    "sandstorm_direction_2": {
        "description": "Sandstorm will switch to blowing from top to bottom",
        "points": 2,
        "group": "sandstorm_direction",
        "runes": [{
            "key": "level_predefines_enable",
            "selector": {
                "professionMask": 0,
                "buildableMask": 0,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [{
                "key": "trap_036_storm#1",
                "value": 0,
                "valueStr": None
            },
            {
                "key": "trap_036_storm#3",
                "value": 1,
                "valueStr": None
            }]
        }]
    },
    "max_hp_1": {
        "description": "No enemies escape (Level HP set to 1)",
        "points": 1,
        "group": None,
        "runes": [{
            "key": "global_lifepoint",
            "selector": {
                "professionMask": 0,
                "buildableMask": 0,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [{
                "key": "value",
                "value": 1,
                "valueStr": None
            }]
        }]
    },
    "ally_atk_down": {
        "description": "Allies ATK -20%",
        "points": 1,
        "group": None,
        "runes": [{
            "key": "char_attribute_mul",
            "selector": {
                "professionMask": 1023,
                "buildableMask": 3,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [
                {
                    "key": "atk",
                    "value": 0.8,
                    "valueStr": None
                }
            ]
        }]
    },
    "enemy_def_up": {
        "description": "Enemy DEF +200",
        "points": 1,
        "group": None,
        "runes": [{
            "key": "enemy_attribute_add",
            "selector": {
                "professionMask": 0,
                "buildableMask": 0,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [
                {
                    "key": "def",
                    "value": 200,
                    "valueStr": None
                }
            ]
        }]
    },
    "sand_noslow": {
        "description": "Sandstorm no longer reduces enemy movement speed.",
        "points": 1,
        "group": "sandstorm_slow",
        "runes": [
        {
            "key": "char_skill_blackb_mul",
            "selector": {
                "professionMask": 1023,
                "buildableMask": 3,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [
                {
                    "key": "char",
                    "value": 0,
                    "valueStr": "trap_036_storm"
                },
                {
                    "key": "skill",
                    "value": 0,
                    "valueStr": "sktok_storm"
                },
                {
                    "key": "sand_storm[enemy].move_speed",
                    "value": 0,
                    "valueStr": None
                }
            ]
        }]
    },
    "sand_dmg_2": {
        "description": "Sandstom’s HP loss effect +20%",
        "points": 2,
        "group": "sandstorm_hp",
        "runes": [
        {
            "key": "char_skill_blackb_mul",
            "selector": {
                "professionMask": 1023,
                "buildableMask": 3,
                "charIdFilter": None,
                "enemyIdFilter": None,
                "skillIdFilter": None,
                "tileKeyFilter": None
            },
            "blackboard": [
                {
                    "key": "char",
                    "value": 0,
                    "valueStr": "trap_036_storm"
                },
                {
                    "key": "skill",
                    "value": 0,
                    "valueStr": "sktok_storm"
                },
                {
                    "key": "damage",
                    "value": 1.2,
                    "valueStr": None
                }
            ]
        }]
    }
}

import math

def list_runes():
    for i in RUNES:
        print(f"\"{i}\", #{RUNES[i]['description']} - (Risk {RUNES[i]['points']})")

def return_stage_data():
    return MAP_DATA

def calculate_risks():
    if check_runes():
        total_risks = 0
        for each_rune in included_risks:
            total_risks += RUNES[each_rune]["points"]
        print(total_risks)
    else:
        print("Selected Risks have conflicting groups. Please check and try again.")

def check_runes():
    included_groups = []
    for risk in included_risks:
        group = RUNES[risk]["group"]
        if group and group in included_groups:
            print(risk)
            return False
        included_groups.append(group)
    return True

def generate_risks(runes):
    checks_passed = check_runes()
    if checks_passed:
        org_runes_keys = [rune for rune in list(runes.keys()) if "buff" not in rune]
        if len(runes) - 1 < len(included_risks):
            risk_per_tag = math.ceil(len(included_risks)/len(runes))
            count = 0
            for i in range(0, len(included_risks), risk_per_tag):
                modified_rune = {}
                new_runes = []
                end_range = i+risk_per_tag if i+risk_per_tag < len(included_risks) else len(included_risks)
                for j in range(i, end_range):
                    new_runes.append(RUNES[included_risks[j]])
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
                runes.update({
                    org_runes_keys[count]: modified_rune
                })
                count += 1

        else:
            for index, risk in enumerate(included_risks):
                modified_rune = {
                    "id": org_runes_keys[index],
                    "points": RUNES[risk]["points"] if RUNES[risk]["points"] <= 3 else 3,
                    "mutexGroupKey": None,
                    "description": f'{RUNES[risk]["description"]} (Risk {RUNES[risk]["points"]})',
                    "runes": RUNES[risk]["runes"]
                }
                runes.update({
                    org_runes_keys[index]: modified_rune
                })
    else:
        print("Selected Risks have conflicting groups. Please check and try again.")

    return runes

# Uncomment to see all available risks
# list_runes()

# Uncomment to see calculate selected risks
# calculate_risks()

check_runes()
