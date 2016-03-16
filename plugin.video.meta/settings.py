#! /usr/bin/python
CACHE_TTL = 60
UPDATE_LIBRARY_INTERVAL = 4*60*60
    
if __name__ == "__main__":
    import xml.etree.ElementTree as ET
    tree = ET.parse('resources/settings.xml')
    ids = filter(None, [item.get('id') for item in tree.findall('.//setting')])
    
    content = []
    with open(__file__, "r") as me:
        content = me.readlines()
        content = content[:content.index("#GENERATED\n")+1]
    
    with open(__file__, 'w') as f:
        f.writelines(content)
        for _id in ids:
            line = "SETTING_{0} = \"{1}\"\n".format(_id.upper(), _id)
            f.write(line)    

#GENERATED
SETTING_PLAYERS_UPDATE_URL = "players_update_url"
SETTING_MOVIES_ENABLED_PLAYERS = "movies_enabled_players"
SETTING_MOVIES_DEFAULT_PLAYER = "movies_default_player"
SETTING_MOVIES_DEFAULT_PLAYER_FROM_LIBRARY = "movies_default_player_from_library"
SETTING_TV_ENABLED_PLAYERS = "tv_enabled_players"
SETTING_TV_DEFAULT_PLAYER = "tv_default_player"
SETTING_TV_DEFAULT_PLAYER_FROM_LIBRARY = "tv_default_player_from_library"
SETTING_LIBRARY_SET_DATE = "library_set_date"
SETTING_MOVIES_SERVER_URL = "movies_server_url"
SETTING_MOVIES_LIBRARY_FOLDER = "movies_library_folder"
SETTING_TV_LIBRARY_FOLDER = "tv_library_folder"
SETTING_USE_SIMPLE_SELECTOR = "use_simple_selector"
SETTING_ADVANCED_KEYBOARD_HACKS = "advanced_keyboard_hacks"
