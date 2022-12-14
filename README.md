# Rush Hour Solver
Implements the A* algorithm to solve the popular rush hour puzzle.
![](https://m.media-amazon.com/images/I/71DO6coFVEL.jpg)

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
