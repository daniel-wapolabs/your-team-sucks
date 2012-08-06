"""Game engine for Your Team Sucks game

Author: Daniel Li <daniel@wapolabs.com>

Copyright 2012 WaPo Labs, The Washington Post Company
"""

import sqlalchemy.orm

import connection
import model


class Engine(object):
	"""Game engine
	"""

	def __init__(self):
		Session = sqlalchemy.orm.sessionmaker(bind=connection.engine)
		self.session = Session()

	def create_team(self, name):
		"""Creates a new team

		Args:
			name: name of the team (`str`)

		Returns:
			The new team object (`Team`)
		"""

		team = model.Team(name)

		try:
		    self.session.add(team)
		    self.session.commit()
		except:
		    self.session.rollback()
		    print('Error in creating team')

	    return team

	def delete_team(self, team_id):
		"""Deletes an existing team

		Args:
			team_id: ID of the team to destroy
		"""

		pass

	def create_match(self, team1_id, team2_id):
		"""Creates a new match

		Args:
			team1_id: ID of one of the two teams participating (`int`)
			team2_id: ID of the other team (`int`)

		Returns:
			The new match object (`Match`)
		"""

		match = model.Match(team1_id, team2_id)

		try:
		    self.session.add(match)
		    self.session.commit()
		except:
		    self.session.rollback()
		    print('Error in creating match')

	    return match

	def delete_match(self, match_id):
		"""Deletes an existing match

		Args:
			match_id: ID of the match to destroy
		"""

		pass

	def create_user(self, fb_uid, name, default_team_id=None, fanclub_id=None):
		"""Creates a new user

		This method creates a new user in our system.  This user is tied to a
		Facebook ID.

		Args:
			fb_uid: Facebook ID of the user (`int`)
			name: user's name (`str`)
			default_team_id: ID of user's default team (`int`)

		Returns:
			The new user object (`User`)
		"""

		user = model.User(fb_uid, name, default_team_id, fanclub_id)

		try:
		    self.session.add(user)
		    self.session.commit()
		except:
		    self.session.rollback()
		    print('Error in creating user')

	    return user

	def delete_user(self, fb_uid):
		"""Deletes an existing user

		Args:
			fb_uid: ID of the user to destroy
		"""

		pass

	def create_fanclub(self, name, team_id):
		"""Creates a new fanclub

		Args:
			name: name of the fanclub (`str`)
			team_id: ID of the team for which this fanclub roots (`int`)

		Returns:
			The new fanclub object (`Fanclub`)
		"""

		fanclub = model.Fanclub(name, team_id)

		try:
		    self.session.add(fanclub)
		    self.session.commit()
		except:
		    self.session.rollback()
		    print('Error in creating fanclub')

	    return fanclub

	def delete_fanclub(self, fanclub_id):
		"""Deletes an existing fanclub

		Args:
			fanclub_id: ID of the fanclub to destroy
		"""

		pass
