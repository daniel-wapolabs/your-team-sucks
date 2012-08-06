"""Model for Your Team Sucks game

Author: Daniel Li <daniel@wapolabs.com>

Copyright 2012 WaPo Labs, The Washington Post Company
"""

import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

import connection


Base = sqlalchemy.ext.declarative.declarative_base()


class Team(Base):
	__tablename__ = 'teams'

	id = sqlalchemy.Column(
		sqlalchemy.Integer,
		primary_key=True,
		nullable=False
	)

	name = sqlalchemy.Column(
		sqlalchemy.String(255),
		nullable=False
	)

	users = sqlalchemy.orm.relationship(
		'User',
		backref='default_team'
	)

	fanclubs = sqlalchemy.orm.relationship(
		'Fanclub',
		backref='team'
	)

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return '{cls}({id}, {name})'.format(
			cls=self.__class__.__name__,
			id=self.id,
			name=self.name
		)


class Match(Base):
	__tablename__ = 'matches'

	id = sqlalchemy.Column(
		sqlalchemy.Integer,
		primary_key=True,
		nullable=False
	)

	team1_id = sqlalchemy.Column(
		sqlalchemy.Integer,
		sqlalchemy.ForeignKey('teams.id'),
		nullable=False
	)

	team2_id = sqlalchemy.Column(
		sqlalchemy.Integer,
		sqlalchemy.ForeignKey('teams.id'),
		nullable=False
	)

	faceoffs = sqlalchemy.orm.relationship(
		'Faceoff',
		backref='match'
	)

	def __init__(self, team1_id, team2_id):
		self.team1_id = team1_id
		self.team2_id = team2_id

	def __repr__(self):
		return '{cls}({id}, {team1}, {team2})'.format(
			cls=self.__class__.__name__,
			id=self.id,
			team1=self.team1,
			team2=self.team2
		)


#class User(Base):
#	__tablename__ = 'users'
#
#	id = sqlalchemy.Column(
#		sqlalchemy.Integer,
#		primary_key=True,
#		nullable=False
#	)
#
#	name = sqlalchemy.Column(
#		sqlalchemy.String(255),
#		nullable=False
#	)
#
#	default_team_id = sqlalchemy.Column(
#		sqlalchemy.Integer,
#		sqlalchemy.ForeignKey('teams.id')
#	)
#
#	def __init__(self, id, name, default_team_id=None):
#		self.id = id
#		self.name = name
#		self.default_team_id = default_team_id
#
#	def __repr__(self):
#		return '{cls}({id}, {name}, {default_team_id})'.format(
#			cls=self.__class__.__name__,
#			id=self.id,
#			name=self.name,
#			default_team_id=self.default_team_id
#		)


class Fanclub(Base):
	__tablename__ = 'fanclubs'

	id = sqlalchemy.Column(
		sqlalchemy.Integer,
		primary_key=True,
		nullable=False
	)

	name = sqlalchemy.Column(
		sqlalchemy.String(255),
		nullable=False
	)

	team_id = sqlalchemy.Column(
		sqlalchemy.Integer,
		sqlalchemy.ForeignKey('teams.id'),
		nullable=False
	)

	users = sqlalchemy.orm.relationship(
		'User',
		backref='fanclubs'
	)

#	users = sqlalchemy.orm.relationship(
#		'User',
#		secondary='fanclub_memberships',
#		backref='fanclubs'
#	)

	def __init__(self, name, team_id):
		self.name = name
		self.team_id = team_id

	def __repr__(self):
		return '{cls}({id}, {name}, {team_id})'.format(
			cls=self.__class__.__name__,
			id=self.id,
			name=self.name,
			team_id=self.team_id
		)


class User(Base):
	__tablename__ = 'users'

	id = sqlalchemy.Column(
		sqlalchemy.Integer,
		primary_key=True,
		nullable=False
	)

	name = sqlalchemy.Column(
		sqlalchemy.String(255),
		nullable=False
	)

	default_team_id = sqlalchemy.Column(
		sqlalchemy.Integer,
		sqlalchemy.ForeignKey('teams.id')
	)

	fanclub_id = sqlalchemy.Column(
		sqlalchemy.Integer,
		sqlalchemy.ForeignKey('fanclubs.id')
	)

	def __init__(self, id, name, default_team_id=None, fanclub_id=None):
		self.id = id
		self.name = name
		self.default_team_id = default_team_id
		self.fanclub_id = fanclub_id

	def __repr__(self):
		return '{cls}({id}, {name}, {default_team_id}, {fanclub_id})'.format(
			cls=self.__class__.__name__,
			id=self.id,
			name=self.name,
			default_team_id=self.default_team_id,
			fanclub_id=self.fanclub_id
		)


#fanclub_memberships = sqlalchemy.Table(
#	'fanclub_memberships',
#	Base.metadata,
#	sqlalchemy.Column(
#		'user_id',
#		sqlalchemy.Integer,
#		sqlalchemy.ForeignKey('users.id')
#	),
#	sqlalchemy.Column(
#		'fanclub_id',
#		sqlalchemy.Integer,
#		sqlalchemy.ForeignKey('fanclubs.id')
#	)
#)


class Faceoff(Base):
	__tablename__ = 'faceoffs'

	id = sqlalchemy.Column(
		sqlalchemy.Integer,
		primary_key=True,
		nullable=False
	)

	match_id = sqlalchemy.Column(
		sqlalchemy.Integer,
		sqlalchemy.ForeignKey('matches.id')
	)

	fanclub1_id = sqlalchemy.Column(
		sqlalchemy.Integer,
		sqlalchemy.ForeignKey('fanclubs.id')
	)

	fanclub2_id = sqlalchemy.Column(
		sqlalchemy.Integer,
		sqlalchemy.ForeignKey('fanclubs.id')
	)

	def __init__(self):
		pass

	def __repr__(self):
		return '{cls}({id}, {match})'.format(
			cls=self.__class__.__name__,
			id=self.id,
			match=self.match
		)


Base.metadata.create_all(connection.engine)
