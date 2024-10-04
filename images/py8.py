# I'll now display the image in this environment directly.
import matplotlib.pyplot as plt
import numpy as np

# Define cumulative penalty function
def cumulative_penalty(amount, factor):
    return amount * factor

# Initial values
original_amount = 1000
splits = [1, 4, 10]  # 1 for no sybil, 4 for sybil with 4 accounts, 10 for sybil with 10 accounts
penalty_factor = 0.1  # penalty rate

# Plot cumulative penalties for different splits
plt.figure(figsize=(10, 6))

for split in splits:
    total_withdrawn = original_amount / split
    cumulative_penalties = [cumulative_penalty(total_withdrawn * i, penalty_factor) for i in range(1, split + 1)]
    plt.plot(range(1, split + 1), cumulative_penalties, label=f'Splits = {split}')

plt.xlabel('Number of Withdrawals (Accounts)', color='white')
plt.ylabel('Cumulative Penalty', color='white')
plt.title('Cumulative Penalty Impact with Sybil Attack Attempts', color='white')
plt.legend()
plt.grid(True)

# Set the plot background to black
plt.gca().set_facecolor('black')
plt.gcf().set_facecolor('black')

# Set the color of the labels and title
plt.gca().spines['bottom'].set_color('white')
plt.gca().spines['top'].set_color('white') 
plt.gca().spines['right'].set_color('white')
plt.gca().spines['left'].set_color('white')
plt.gca().tick_params(axis='x', colors='white')
plt.gca().tick_params(axis='y', colors='white')

plt.legend(facecolor='black', edgecolor='white')
plt.show()
