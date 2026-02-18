# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 15:46:50 2026

@author: divya
"""
#task1
# STEP 1 — Import library
import random

# STEP 2 — Initialize variables
trials = 1000
count_sum_7 = 0

# STEP 3 — Simulate dice rolls
for i in range(trials):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    
    if dice1 + dice2 == 7:
        count_sum_7 += 1

# STEP 4 — Calculate Experimental Probability
experimental_probability = count_sum_7 / trials

print("Number of times sum = 7:", count_sum_7)
print("Experimental Probability:", experimental_probability)

#task2
# STEP 1 — Import libraries
import random
# ---------------------------------------------
# STEP 2 — Independent Event
# Coin (Heads) AND Die (6)
# ---------------------------------------------

print("----- Independent Event -----")

# Define probabilities
P_heads = 1/2
P_six = 1/6

# Apply formula P(A ∩ B) = P(A) * P(B)
P_independent = P_heads * P_six

print("P(Heads):", P_heads)
print("P(Roll 6):", P_six)
print("P(Heads AND 6):", P_independent)
# ---------------------------------------------
# STEP 3 — Dependent Event
# Two Red marbles without replacement
# ---------------------------------------------

print("\n----- Dependent Event -----")

total_marbles = 10
red_marbles = 5

# First pick
P_first_red = red_marbles / total_marbles

# Second pick (without replacement)
P_second_red = (red_marbles - 1) / (total_marbles - 1)

# Combined probability
P_dependent = P_first_red * P_second_red

print("P(First Red):", P_first_red)
print("P(Second Red | First Red):", P_second_red)
print("P(Two Reds):", P_dependent)


# ---------------------------------------------
# STEP 4 — Reflection
# ---------------------------------------------

print("\nReflection:")
print("The denominator changed because one marble was removed.")
print("This makes the second event dependent on the first.")

#task3
# STEP 1 — Define Probabilities
P_spam = 0.1
P_ham = 0.9

P_free_given_spam = 0.9
P_free_given_ham = 0.05

# STEP 2 — Calculate Total Probability of "Free"
P_free = (P_free_given_spam * P_spam) + \
         (P_free_given_ham * P_ham)

print("P(Free):", P_free)

# STEP 3 — Apply Bayes Theorem
P_spam_given_free = (P_free_given_spam * P_spam) / P_free

print("P(Spam | Free):", P_spam_given_free)