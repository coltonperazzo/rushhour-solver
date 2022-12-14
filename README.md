# Rush Hour Solver
Implements the A* algorithm to solve the popular rush hour puzzle.

rushhour(heuristicState, initalState)\n
heuristicState = 0 => blocking heuristic.\n
Returns how many vehicles, other than the main vehicle X is blocking it's path to the exit.

heuristicState = 1 => distance blocked heuristic.

#### Usage:
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
