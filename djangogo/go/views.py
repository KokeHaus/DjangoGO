from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Go_Game, Board

@csrf_exempt
def playMove(req):
    import pdb
    pdb.set_trace()
    
    data = json.loads(req.body)
    gameID= data['gameid']
    boardstate = data['boardstate']
    return JsonResponse({
         'newBoardState': 'boardstate',
         'blackcaptures': "activeGame.capturedbyblack",
         'whitecaptures':'activeGame.capturedbywhite'
    })

@csrf_exempt
def getBoardState(req):
    return JsonResponse({
        'newBoardState': 'activeGame.getState()',
    })

def UpdateGame(req):
    data =json.loads(req.body)
    gameID=data['gameid']