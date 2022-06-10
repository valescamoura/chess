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
  imp_moves = []
  norm_moves = []
  min_max = chess_board.points

  for piece in team_pieces:
    moves = chess_board.getLegalSequences(piece)

    for move in moves:
      if move[0].split()[2] in chess_board.pieces:
        imp_moves.append(move)
      else:
        norm_moves.append(move)

  if len(imp_moves) != 0:
    for move in imp_moves:
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
  
  elif min_max == chess_board.points:
    final_move = norm_moves

  i = randint(0,len(final_move)-1)
  return final_move[i]

  
def alpha_beta(chess_board,team="black"):
  '''
    Implements a alpha-beta prunning.

  '''

  team_pieces = []
  for tile in chess_board.pieces:
    if chess_board.pieces[tile]["team"] == team:
      team_pieces.append(tile)


  final_move = 0
  min_max_value = chess_board.points

  for piece in team_pieces:
    moves = chess_board.getLegalSequences(piece)
    for move in moves:
      if(team == "black"):
        new_board = chess_board.deepcopy()
        new_board.execute(move)
        white_move = min_max(chess_board,team="white")
        new_board.execute(white_move)

        if new_board.points > min_max_value or final_move == 0:
          min_max_value = new_board.points
          final_move = move
      else:
        new_board = chess_board.deepcopy()
        new_board.execute(move)
        white_move = min_max(chess_board,team="black")
        new_board.execute(white_move)
        
        if new_board.points < min_max_value or final_move == 0:
          min_max_value = new_board.points
          final_move = move

  return final_move
  