def minimax(depth, node_index, is_maximizing_player, values, alpha, beta):
    if depth == 0:
        return values[node_index]

    if is_maximizing_player:
        best_value = float('-inf')
        for i in range(2):  # Two children (0 and 1)
            value = minimax(depth - 1, node_index * 2 + i, False, values, alpha, beta)
            best_value = max(best_value, value)
            alpha = max(alpha, best_value)
            if beta <= alpha:
                break  # Beta cut-off
        return best_value
    else:
        best_value = float('inf')
        for i in range(2):  # Two children (0 and 1)
            value = minimax(depth - 1, node_index * 2 + i, True, values, alpha, beta)
            best_value = min(best_value, value)
            beta = min(beta, best_value)
            if beta <= alpha:
                break  # Alpha cut-off
        return best_value

# Example usage
values = [3, 5, 2, 9, 0, 1, 8, 6]  # Leaf node values
depth = 3  # Depth of the game tree
result = minimax(depth, 0, True, values, float('-inf'), float('inf'))
print("The optimal value is:", result)
