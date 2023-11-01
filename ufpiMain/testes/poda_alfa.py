def minimax_with_alpha_beta(board, depth, turn):


  # Se o jogo acabou, retorne o valor da função de avaliação.

  if is_game_over(board):
    return evaluate_board(board)

  # Se o limite de profundidade foi alcançado, retorne o valor da função de avaliação.

  if depth == 0:
    return evaluate_board(board)

  # Inicialize os valores alfa e beta.

  alpha = float("-inf")
  beta = float("inf")

  # Para cada possível movimento, avalie o valor do estado resultante.

  for move in get_possible_moves(board, turn):
    # Atualize os valores alfa e beta com o valor do melhor movimento possível do oponente.
    next_board = make_move(board, move, turn)
    value = minimax_with_alpha_beta(next_board, depth - 1, turn ^ 1)
    alpha = max(alpha, value)

    # Se o valor do movimento atual for melhor do que o valor do melhor movimento possível do oponente, retorne o valor do movimento atual.
    if alpha > beta:
      return alpha

  # Retorne o valor do melhor movimento possível.

  return alpha

