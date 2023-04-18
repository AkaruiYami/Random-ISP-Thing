# Introduction

The fact that I need to calculate the same thing over and over again make me wonder if I can just use python to help be do them. Much faster and simple! Imagine you are given 2 points and you need to find y base on x that lay in between those 2 points. Do it once is ok, but doing it 5 times with 5 different pair of points. No. So, this is my solution!

# How to use

from your command promt, type:

```python
python linear_graph_solver.py -r "FileName.txt"
```

This will read all your inputs from file `FileName.txt`. If your input file is in another directory, make sure to give the correct path to that file. Such as `data/example.txt`.

To read single input type:

```python
python linear_graph_solver.py -x X -p1 X1 Y1 -p2 X2 Y2
```

This will calculate y when x=X for x that lay in between p1 and p2.
