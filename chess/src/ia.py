from random import choice, randint
from chess.src.board import Board

def rand(chess_board,team="black"):
  '''
    Choses a random move from a random team piece.
  '''

  team_pieces = []
  for tile in chess_board.pieces:
    if chess_board.pieces[tile]["team"] == team:
      team_pieces.append(tile)


  moves = []
  while len(moves) == 0:
    if len(team_pieces) == 0:
      return None

    tile = choice(team_pieces)
    team_pieces.remove(tile)

    moves = chess_board.getLegalSequences(tile)
  
  return choice(moves)

def min_max(chess_board,team="black"):
  '''
    Choses a move with the best points diference.

  '''

  team_pieces = []
  for tile in chess_board.pieces:
    if chess_board.pieces[tile]["team"] == team:
      team_pieces.append(tile)

  final_move = []
  moves = []
  min_max = chess_board.points

  for piece in team_pieces:
    piece_moves = chess_board.getLegalSequences(piece)

    for move in piece_moves:
      moves.append(move)
      
  for move in moves:
    new_board = chess_board.deepcopy()
    new_board.execute(move)
    
    if(team == "black"):
      if new_board.points > min_max:
        min_max = new_board.points
        
        final_move = [move]
      elif new_board.points == min_max:
        final_move.append(move)
    else:
      if new_board.points < min_max:
        min_max = new_board.points
        
        final_move = [move]
      elif new_board.points == min_max:
        final_move.append(move)

  if len(final_move) <= 1:
    return final_move,min_max 

  i = randint(0,len(final_move)-1)
  return final_move[i],min_max

def in_min_max(chess_board,depth,alpha,beta,team="black"):
  '''
    Choses a move with the best points diference.

  '''
  if depth == 0:
    return chess_board.points

  team_pieces = []
  imp_moves = []
  norm_moves = []
  for tile in chess_board.pieces:
    if chess_board.pieces[tile]["team"] == team:
      team_pieces.append(tile)

  min_max = chess_board.points

  for piece in team_pieces:
    moves = chess_board.getLegalSequences(piece)

    for move in moves:
      if move[0].split()[2] in chess_board.pieces:
        imp_moves.append(move)
      else:
        norm_moves.append(move)

  # Important moves will be visited first
  imp_moves = imp_moves + norm_moves

  for move in imp_moves:
    new_board = chess_board.deepcopy()
    new_board.execute(move)
    
    if(team == "black"):
      child_points = in_min_max(new_board,depth - 1,alpha,beta,team="white") 

      min_max = max([child_points,min_max])
      alpha = max(min_max,alpha)
      if beta <= alpha:
        return min_max

    else:
      child_points = in_min_max(new_board,depth - 1,alpha,beta,team="black") 

      min_max = min([child_points,min_max])
      beta = min(min_max,beta)

      if beta <= alpha:
        return min_max
       
  return min_max


def alpha_beta(chess_board,team="black"):
  '''
    Implements a alpha-beta prunning.

  '''
  team_pieces = []
  for tile in chess_board.pieces:
    if chess_board.pieces[tile]["team"] == team:
      team_pieces.append(tile)


  final_move = []
  min_max_value = chess_board.points
  alpha = -99999
  beta = 99999


  for piece in team_pieces:
    moves = chess_board.getLegalSequences(piece)
    for move in moves:
      if(team == "black"):
        new_board = chess_board.deepcopy()
        new_board.execute(move)
        oponent_move_points = in_min_max(new_board,3,alpha,beta,team="white")
        alpha = max(oponent_move_points,alpha)
        
        if oponent_move_points > min_max_value or final_move == []:
          min_max_value = oponent_move_points
          final_move = [move]
        elif  oponent_move_points == min_max_value:
          final_move.append(move)

      else:
        new_board = chess_board.deepcopy()
        new_board.execute(move)
        oponent_move_points = in_min_max(new_board,3,alpha,beta,team="black")
        beta = min(oponent_move_points,beta)
        
        if oponent_move_points < min_max_value or final_move == []:
          min_max_value = oponent_move_points
          final_move = [move]
        elif  oponent_move_points == min_max_value:
          final_move.append(move)

  if len(final_move) <= 1:
    return final_move

  i = randint(0,len(final_move)-1)
  return final_move[i]
  