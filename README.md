# Sudoku Solver using Backtracking

## Description
This is a small sudoku solving program I made for my flipped course project of second semester.  
I kept everything in one Python file to keep it simple and easy to read. 
This project solves Sudoku puzzles in a terminal using a backtracking approach. Instead of manually trying different combinations, the program automatically fills the grid while making sure all Sudoku rules are satisfied.

The solver can handle both standard 9x9 puzzles and smaller sizes like 4x4 by adjusting constraints dynamically.

## Problem Statement
Solving Sudoku manually can be time-consuming and requires repeated trial and error. This project demonstrates how such problems can be solved efficiently using AI-based search techniques.

## Approach
The Sudoku is treated as a Constraint Satisfaction Problem (CSP), where:
- Each cell is a variable
- Possible values range from 1 to N
- Constraints ensure no repetition in rows, columns, and subgrids

A backtracking (depth-first search) approach is used:
- Try placing a number in an empty cell
- Check if it satisfies all constraints
- Continue recursively
- If a conflict occurs, backtrack and try another value

## Features
- Solves Sudoku puzzles automatically
- Supports both default and user input puzzles
- Works with different grid sizes (like 4x4 and 9x9)
- Displays the board in a readable format

## How to Run
1. Make sure Python 3 is installed
2. Run the file: python main.py
3. Choose:
- Option 1 → Use default puzzle
- Option 2 → Enter your own puzzle

## Input Format
- Enter numbers row by row
- Use `0` for empty cells
- Separate values with space

Example: 
5 3 0 0 7 0 0 0 0


## Output
- Displays the original puzzle
- Displays the solved puzzle if a solution exists

## AI Concepts Used
- Backtracking Search (Depth First Search)
- Constraint Satisfaction Problem (CSP)
- Knowledge Representation using rules

## Challenges Faced
- Handling different grid sizes dynamically
- Ensuring constraints are checked efficiently
- Managing recursion and backtracking correctly

## What I Learned
- How search algorithms can be applied to real problems
- How constraint satisfaction works in practice
- Importance of breaking a problem into smaller steps
