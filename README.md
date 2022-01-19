# Summer 2022 Shopify Data Science Intern Challenge

Kindly find my solutions in this directory as `question1.md` (or `question1.pdf`) for Question 1 and `question2.md` (or `question2.pdf`) for Question 2, or just follow them below:

---

## Question 1

First install the required packages by typing
```zsh
pip install -r requirements.txt
```

in the directory, then to run the script simply type
```zsh
python aov.py
```

## a. What went wrong with the calculation:

Intuitively, the problem could be that the total sum of the order amount was divided by a smaller number, like the total number of orders made (as compared to sum of the number of items). I confirmed this by selecting the values in the `order_amount` column on the google sheet provided and voila (bottom right), the default average over all the orders was equal to the wrongly calculated value that was given!

![1a](./images/1%20a.png)

## b. What metric would you report for this dataset

To calculate the average order value we must divide the total revenue by the number of items bought.

So in this case the following formula would:

```
Average order value (AOV) = sum(order_amount)/sum(total_items)
```

First, I created a copy of the given data to get an approximate target in google sheets itself:

![1b](./images/1%20b.png)

The value I predict the AOV should be is `$357.92`, which is the average order amount for every sneaker sold.

## c. What is its value:

Then, I downloaded the original data set as a csv file and wrote a python script to sanitize the data and calculate the AOV for _each_ sneaker.

Here is the output when I run the program:

![1c](./images/1%20c.png)

The value calculated is printed out to be `$357.92`, just as I predicted and the program greets the user a good day! :^)

`Final value: $357.92`

(PS: The instructions to run the script is on top of this page)

---

## Question 2

Enter the queries given into the following link and click on `Run SQL`
To run them:
<https://www.w3schools.com/SQL/TRYSQL.ASP?FILENAME=TRYSQL_SELECT_ALL>

## a. SQL Query:

```sql
SELECT COUNT(*) AS 'Total Orders Shipped by Speedy Express'
  FROM (Orders
 INNER JOIN Shippers
    ON Orders.ShipperID = Shippers.ShipperID)
 WHERE Shippers.ShipperName = 'Speedy Express';
```

## Output:

| 'Total Orders Shipped by Speedy Express' |
| ---------------------------------------- |
| 54                                       |

## b. SQL Query:

```sql
SELECT LastName AS 'Last Name of the Employee with the Most Orders'
  FROM (
SELECT TOP 1 COUNT(*) AS order_nums,
       LastName
  FROM (Orders
 INNER JOIN Employees
    ON Orders.EmployeeID = Employees.EmployeeID)
 GROUP BY LastName
 ORDER BY 1 DESC);
```

## Output:

| 'Last Name of the Employee with the Most Orders' |
| ------------------------------------------------ |
| Peacock                                          |

## c. SQL Query:

```sql
SELECT ProductName AS 'Most Ordered by Customers in Germany'
  FROM Products
 WHERE Products.ProductID = (
SELECT Products.ProductID
  FROM (
SELECT TOP 1 COUNT(*),
       Products.ProductID
  FROM Orders,
       OrderDetails,
       Customers,
       Products
 WHERE Orders.OrderID         = OrderDetails.OrderID
   AND Orders.CustomerID      = Customers.CustomerID
   AND OrderDetails.ProductID = Products.ProductID
   AND Customers.Country      = 'Germany'
 GROUP BY Products.ProductID
 ORDER BY 1 DESC));
```

## Output:

| 'Most Ordered by Customers in Germany' |
| -------------------------------------- |
| Gorgonzola Telino                      |

---

## Directory Structure:

```
|-- Shopify
    |-- aov.py
    |-- challenge.pdf
    |-- data.csv
    |-- question1.md
    |-- question1.pdf
    |-- question2.md
    |-- question2.pdf
    |-- images
        |-- 1 a.png
        |-- 1 b.png
        |-- 1 c.png
```

## License

All material in this repository is released in the public domain, except
for the challenge description and the csv data files which retains its original license.
