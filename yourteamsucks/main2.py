	def join_fanclub(self, fb_uid, fanclub_id):
		"""Registers a user to a fanclub

		Args:
			fb_uid: Facebook ID of the user (`int`)
			fanclub_id: ID of the fanclub (`int`)
		"""

		# Retrieve the user
		alldata = session.query(model.User).all()
		for somedata in alldata:
		    print somedata

	def leave_fanclub(self, fb_uid, fanclub_id):
		"""Deregisters a user from a fanclub

		Args:
			fb_uid: Facebook ID of the user (`int`)
			fanclub_id: ID of the fanclub (`int`)
		"""

		pass

	def make_wager(self, from_fb_uid, to_fb_uid, type, message=None,
		prediction_team1=None, prediction_team2=None):
		"""Creates a new wager

		Args:
			from_fb_uid: Facebook ID of the user making the wager
			to_fb_uid: Facebook ID of the intended recipient
			type: type of the wager (`int`): 0 is message, 1 is color change,
				2 is score prediction
			message: message to send to the recipient; used only if type is 0
				(`str`)
			prediction_team1: prediction of team1's score (`int`)
			prediction_team2: prediction of team2's score (`int`)

		Team 1 and Team 2 are defined by the match
		"""

		team = model.Team(name)

		try:
		    self.session.add(team)
		    self.session.commit()
		except:
		    self.session.rollback()
		    raise
