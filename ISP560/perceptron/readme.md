Calculate perceptron using python. This can calculate multiple number of variables.
I was thought by 2 lecturers and both of them has different methods. So, this is method 1.

p.s. I'm still confuse. lol

# How To Run

## In Code Edit

1. Go to `perceptron_cal.py`.
2. Navigate to the bottom of the code until you find `__name__ == "__main__"` part.
3. Change the variable value.
4. Open cmd / terminal.
5. Run `python perceptron_cal.py`.

## Using Console Input

1. Open cmd / terminal.
2. Run `python main.py`.
3. Enter the value.

# Case Example

## Variables

-   Inputs (ixs)

| x1  | x2  |
| --- | --- |
| 0   | 0   |
| 0   | 1   |
| 1   | 0   |
| 1   | 1   |

-   Desired Output (yd) = 0, 0, 0, 1
-   Weights (ws)
    -   w1 = 0.3
    -   w2 = -0.1
-   α = 0.1
-   θ = 0.2
-   Activation Function = step

## Inside Code

`ixs` is a variable that holds corresponds inputs of the perceptron. It is 2D list where each list inside it contains the value for each row of the inputs.

-   row1: x1 = 0, x2 = 0
-   row2: x1 = 0, x2 = 1

Therefore `ixs` is `ixs = [[0, 0], [0, 1]]`

When calling `full_solve` funtion, you can specify the maximum number of `epoch` using `epoch` parameter. You also can specify the activation funtion by giving a function to `fn` parameter.

```python
import activation_function as act_fn

full_solve(ixs, ws, yd, alpha, theta, epoch=5, fn=act_fn.step)
```

Above, we import `activation_function` module that contains different kind of activation function. Then when calling `full_solve` funtion, we give the paramater `fn` a `step` activation function. Note that there is no parantheses after the `act_fn.step` since we want to pass the function reference and not to call them.

You can define your own activation function by creating your own function or just use lambda.
`activation_function` is optional but don't forget to remove the import statement and also the parameter that required this module.
