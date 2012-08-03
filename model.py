class RealWorldGame(object):

	def __init__(self):
		self._real_world_teams = (None, None)
		self._fantasy_games = set()


class RealWorldTeam(object):

	def __init__(self):
		self._real_world_game = None
		self._fanclubs = set()


class Fan(object):

	def __init__(self):
		self._fanclubs = set()
		self._created_wager = None
		self._accepted_wager = None
		self._predictions = {}		# RealWorldGame : value


class Fanclub(object):

	def __init__(self):
		self._real_world_team = None
		self._fans = set()


class Wager(object):

	def __init__(self):
		self._value = None
		self._creator = None
		self._acceptor = None


class FantasyGame(object):

	def __init__(self):
		self._real_world_game = None
