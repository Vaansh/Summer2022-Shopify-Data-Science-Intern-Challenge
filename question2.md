## Question 2

Enter the queries given into the following link and click on `Run SQL` to run them:
<https://www.w3schools.com/SQL/TRYSQL.ASP?FILENAME=TRYSQL_SELECT_ALL>

### a.

#### SQL Query:

```sql
SELECT COUNT(*) AS 'Total Orders Shipped by Speedy Express'
  FROM (Orders
 INNER JOIN Shippers
    ON Orders.ShipperID = Shippers.ShipperID)
 WHERE Shippers.ShipperName = 'Speedy Express';
```

#### Output:

| 'Total Orders Shipped by Speedy Express' |
| ---------------------------------------- |
| 54                                       |

### b.

#### SQL Query:

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

#### Output:

| 'Last Name of the Employee with the Most Orders' |
| ------------------------------------------------ |
| Peacock                                          |

### c.

#### SQL Query:

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

#### Output:

| 'Most Ordered by Customers in Germany' |
| -------------------------------------- |
| Gorgonzola Telino                      |
