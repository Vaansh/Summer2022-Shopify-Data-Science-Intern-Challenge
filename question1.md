## Question 1

To run the python program simply type

```zsh
python aov.py
```

### a.

#### What went wrong with the calculation:

Intuitively, the problem could be that the total sum of the order amount was divided by a smaller number, like the total number of orders made (as compared to sum of the number of items). I confirmed this by selecting the values in the `order_amount` column on the google sheet provided and voila (bottom right), the default average over all the orders was equal to the wrongly calculated value that was given!

![1a](./images/1%20a.png)

### b.

#### What metric would you report for this dataset

To calculate the average order value we must divide the total revenue by the number of items bought.

So in this case the following formula would:

```
Average order value (AOV) = sum(order_amount)/sum(total_items)
```

First, I created a copy of the given data to get an approximate target in google sheets itself:

![1b](./images/1%20b.png)

The value I predict the AOV should be is `$357.92`, which is the average order amount for every sneaker sold.

### c.

#### What is its value:

Then, I downloaded the original data set as a csv file and wrote a python script to sanitize the data and calculate the AOV for _each_ sneaker.

Here is the output when I run the program:
![1c](./images/1%20c.png)

The value calculated is printed out to be `$357.92`, just as I predicted and the program greets the user a good day! :^)

`Final value: $357.92`

(PS: The instructions to run the script is on top of this page)
