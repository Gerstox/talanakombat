from app.manage_json import ManageJson
from app.utils import Utils
from app.fighter import Fighter

manageJson = ManageJson()

peleas = manageJson.read_json(Utils.fights_file)

fighters = Utils.fighters

p1 = "player1"
fighter_obj = Fighter(p1)

fighter_obj.get_player_info()
