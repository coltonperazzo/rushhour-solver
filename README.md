# Rush Hour Solver
Implements the A* algorithm to solve the popular rush hour puzzle.

# Usage:
```python
rushhour(heuristicState, initalState)
```

```heuristicState``` = integer (0 or 1) <br />
```initalState``` = array of strings <br />

```X``` denotes location of vehicle. <br />
```A-Z``` denotes other locations that are not the vehicle we are trying to get off the board.

# Example:
```python
rushhour(0, ["--B---","--B---","XXB---","--AA--","------","------"])
```

```
   --B---   
   --B---   
   XXB---   
   --AA--   
   ------   
   ------    
 
   --B---   
   --B---   
   XXB---   
   ---AA-   
   ------   
   ------    
 
   ------   
   --B---   
   XXB---   
   --BAA-   
   ------   
   ------    
 
   ------   
   ------   
   XXB---   
   --BAA-   
   --B---   
   ------    
 
   ------   
   ------   
   XX----   
   --BAA-   
   --B---   
   --B---    
 
   ------   
   ------   
   -XX---   
   --BAA-   
   --B---   
   --B---    
 
   ------   
   ------   
   --XX--   
   --BAA-   
   --B---   
   --B---    
 
   ------   
   ------   
   ---XX-   
   --BAA-   
   --B---   
   --B---    
 
   ------   
   ------   
   ----XX   
   --BAA-   
   --B---   
   --B--- 
 
Total moves: 8 
Total states explored: 37
```
