# math-assignment
📑 Python script that solves a certain old math assignment.

<br><br><br>

## How it works?
The script works by brute forcing the answer. I didn't want to spend more time on the script than on deducing the answers (actually it took longer as always...), so I decided to use the permutations function to get all possible orders.

<br>

## Example of the assignment
The intention is to put all the numbers between 1–16 in the table below so that in each row and the sum of the numbers in the column produces the indicated number. Some of the numbers have already been put in the right position. Complete the rest.

|         |     |     |     |     | SUM |
| ------- | --- | --- | --- | --- | --- |
|         |     | 10  |     | 12  | 29  |
|         | 16  |     | 6   |     | 35  |
|         |     |     | 7   |     | 25  |
|         | 13  | 9   |     | 11  | 47  |
| **SUM** | 34  | 25  | 31  | 46  |     |


<br>


## Running the script
You can run the script by simply running 
```
python3 solve.py
```

## Results
Script will print out the answer in the terminal. For the example assignment, the answer would be:
```
3 10 4 12
16 5 6 8
2 1 7 15
13 9 14 11
```
