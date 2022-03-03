from re import X
from django.db import models
from uuid import UUID, uuid4
import numpy

class Go_Game(models.Model):
    _game_uuid = models.UUIDField(default=uuid4, unique=True)
    current_color = models.IntegerField(default = 0, unique = False, choices=[('black', 0),('white',1)])
    size = models.IntegerField(default = 19, unique = False, choices = [('small', 9),('medium',13),('large',19)])
    last_move_pass = models.BooleanField(default = False, unique = False)
    attempted_suicide = models.BooleanField(default = False, unique = False)
    is_ko = models.BooleanField(default = False, unique = False)
    scoringMode = models.BooleanField(default = False)

    @property
    def game_uuid(self,value):
        return str(self._game_uuid)

largestate = [[0 for i in range(19)] for j in range(19)]


class Board(models.Model):
    game = models.ForeignKey(Go_Game, models.CASCADE, related_name = 'boardstate')
    state = models.CharField(default = str(largestate), max_length=100000)

# print(str(largestate))