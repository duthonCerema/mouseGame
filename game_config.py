# ---------------- levels configuration ----------------

level_config = """
{   
    "players_stats": {
        "file": "player.gif",
        "hp": 20,
        "gold": 0,
        "alive": true
    },
    "level2": {
        "level_csv": "level2.csv",
        "player_xy": {
            "x":8,
            "y":21
            },
        "exit":{
            "x":41,
            "y":41
        },
        "monsters": {
            "monster1":{"x":4,"y":28,"file":"monster.gif","hp":10,"gold":0,"alive":true},
            "monster2":{"x":17,"y":13,"file":"monster.gif","hp":5,"gold":0,"alive":true},
            "monster3":{"x":22,"y":21,"file":"imp.gif","hp":5,"gold":0,"alive":true},
            "monster4":{"x":24,"y":27,"file":"monster.gif","hp":5,"gold":0,"alive":true}
            },
        "voids": {
            "void1":{"text":"DR", "x":47, "y":47, "z":49}
            },
        "boxes": {
        },
        "torches": {
            "torch1":{"text":"T", "x":3, "y":19},
            "torch2":{"text":"T", "x":21, "y":10},
            "torch3":{"text":"T", "x":15, "y":10},
            "torch4":{"text":"T", "x":3, "y":26},
            "torch5":{"text":"T", "x":15, "y":31},
            "torch6":{"text":"T", "x":26, "y":31},
            "torch7":{"text":"T", "x":31, "y":6},
            "torch8":{"text":"T", "x":3, "y":6}
        }, 
        "bubbles": {
            "bubble1":{"text":"What? A puzzle is hidden here, just under the armchair?", "x":15, "y":19},
            "bubble2":{"text":"Oh, what's that bracelet on the cabinet?", "x":12, "y":9},
            "bubble3":{"text":"There are probably clues in every room, I'll have to have a look.", "x":6, "y":13},
            "bubble4":{"text":"What? The mirror talks?", "x":18, "y":9},
            "bubble5":{"text":"There's an inscription on the wall: 'begins with the green bird.'", "x":22, "y":9},
            "bubble6":{"text":"What do I see on the terrace, a wooden chest?", "x":30, "y":9},
            "bubble7":{"text":"In the dark, a clue appears.", "x":30, "y":21}
        },
        "chests": {
            "chest2":{"x":14, "y":30, "file":"chest_golden_open_full.png", "visible":true, "text":"gaga", "img":"tresor1.png"},
            "chest3":{"x":28, "y":8, "file":"chest_golden_open_full.png", "visible":true, "text":"gaga", "img":"tresor2.png"},
            "chest4":{"x":30, "y":18, "file":"chest_golden_open_full.png", "visible":true, "text":"gaga", "img":"tresor3.png"},
            "chest5":{"x":4, "y":8, "file":"chest_golden_open_full.png", "visible":true, "text":"gaga", "img":"tresor4.png"}
        } 

    }
}
"""

# ---------------- tilset dictionary ----------------

tileset = {
    "@": "https://oshi.at/ZMUu/avRY.gif",
    "W": "https://thumbs2.imgbox.com/10/db/7zaxbIP8_t.png",  # wall
    "FP": "https://thumbs2.imgbox.com/29/22/5rTLr6WH_t.png",  # floor_plain
    "FPB": "https://raw.githubusercontent.com/duthonCerema/mouseGame/main/graphics/tileset/cuisine.png",  # floor_plain
    "FPC": "https://raw.githubusercontent.com/duthonCerema/mouseGame/main/graphics/tileset/couloir.png",  # floor_plain
    "FPD": "https://raw.githubusercontent.com/duthonCerema/mouseGame/main/graphics/tileset/salon.png",  # floor_plain
    "FPE": "https://raw.githubusercontent.com/duthonCerema/mouseGame/main/graphics/tileset/chambre.png",  # floor_plain
    "FPF": "https://raw.githubusercontent.com/duthonCerema/mouseGame/main/graphics/tileset/escalier.png",  # floor_plain
    "FPG": "https://raw.githubusercontent.com/duthonCerema/mouseGame/main/graphics/tileset/ext.png",  # floor_plain
    "FPH": "https://raw.githubusercontent.com/duthonCerema/mouseGame/main/graphics/tileset/noir.png",  # floor_plain
    "MU": "https://raw.githubusercontent.com/duthonCerema/mouseGame/main/graphics/tileset/mur2.png",  # floor_plain
    # "FP": "https://oshi.at/PQkn/ExtR.png",  # floor 1 tilset 2
    "CAT": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/other/cat.gif",  # cat
    "M": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/other/monster.gif",  # monster, skeleton
    "FS": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/tileset/floor_stain_1.png",
    "E": "data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==",
    "FE3": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/tileset/floor_edge_3.png",  # floor_edge_3
    "WON": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/tileset/Wall_outer_n.png",  # Wall_outer_n
    "WOE": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/tileset/Wall_outer_e.png",  # Wall_outer_e
    "WONE": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/tileset/Wall_outer_ne.png",  # Wall_outer_ne
    "WOW": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/tileset/Wall_outer_w.png",  # Wall_outer_w
    "WONW": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/tileset/Wall_outer_nw.png",  # wall_outer_nw
    "WFR": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/tileset/Wall_front_right.png",  # wall front right
    "WTR": "https://oshi.at/QpWg/Mfxv.png",  # wall top right
    # "DK": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/tileset/wall_missing_brick_2.png",  # darkness
    "WMB": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/tileset/wall_missing_brick_2.png",  # wall missing brick 1
    "BOX": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/tileset/box.png",  # box
    "DR": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/tileset/darkness_right.png",  # darkenss right
    "DB": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/tileset/darkness_bottom.png",  # darkness bottom
    "T": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/other/torch.gif",  # torch
    "FMN1": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/tileset/floor_mud_n_1.png",  # floor_mud_n_1
    "FMN2": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/tileset/floor_mud_n_2.png",  # floor_mud_n_2
    "FMNE": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/tileset/floor_mud_ne.png",  # floor_mud_ne
    "CGOF": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/tileset/chest_golden_open_full.png",  # chest_golden_open_full
    "CGOO": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/tileset/chest_open_empty.png",  # chest_open_empty
    "FL": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/tileset/Floor_ladder.png",  # Floor_ladder
}

tileset_movable = {
    "@": True,
    "W": False,
    "FP": True,  # floor_plain
    "FPB": True,  # floor_plain
    "FPC": True,  # floor_plain
    "FPD": True,  # floor_plain
    "FPE": True,  # floor_plain
    "FPF": True,  # floor_plain
    "FPG": True,  # floor_plain
    "FPH": True,  # floor_plain
    "MU": False,  # floor_plain
    # "FP": "https://oshi.at/PQkn/ExtR.png",  # floor 1 tilset 2
    "CAT": True,
    "M": True,  # monster, skeleton
    "FS": True,
    "E": False,
    "FE3": False,  # floor_edge_3
    "WON": False,  # wall outer n
    "WOE": False,  # wall outer e
    "WONE": False,  # wall outer ne
    "WOW": False,  # wall outer w
    "WONW": False,  # wall_outer_nw
    "WFR": False,  # wall front right
    "WTR": False,  # wall top right
    "DK": False,  # darkness
    "WMB": False,  # wall missing brick
    "BOX": False,  # box
    "DR": False,  # darkenss right
    "DB": False,  # darkness bottom
    "T": False,  # torch
    "FMN1": True,  # floor mud n1
    "FMN2": True,
    "FMNE": True,  # floor mud ne
    "FL": True,
}

player_img = "https://raw.githubusercontent.com/duthonCerema/mouseGame/main/graphics/other/player.gif"
