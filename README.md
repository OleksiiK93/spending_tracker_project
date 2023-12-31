### Spending Tracker

A customer has asked to build an app that allows them to track their spending.

#### MVP

* The app should allow the user to create and edit merchants, e.g. Tesco, Amazon, ScotRail
* The app should allow the user to create and edit tags for their spending, e.g. groceries, entertainment, transport
* The user should be able to assign tags and merchants to a transaction, as well as an amount spent on each transaction.
* The app should display all the transactions a user has made in a single view, with each transaction's amount, merchant and tag, and a total for all transactions.

#### Inspired by:

Monzo, MoneyDashboard, lots of mobile/online banking apps

#### Extensions

* The user should be able to mark Merchants and Tags as deactivated. Users will not be able to choose deactivated merchants/tags when creating a transaction. 
* Transactions should have a timestamp, and the user should be able to view transactions sorted by the time they took place.
* The user should be able to supply a budget, and the app should alert the user somehow when they are nearing this budget or have gone over it.

#### Advanced  Extensions

* The user should be able to filter their view of transactions, for example, to view all transactions in a given month, or view all spending on groceries.

#### Setup
Make sure that you have the following installed on your system:
* [PostgreSQL](https://www.postgresql.org/download/)
* [Flask](https://flask.palletsprojects.com/en/2.3.x/installation/)

1. Download the ZIP archive with the code.
2. Extract the archive.
3. Open the directory with the extracted files in Terminal.
4. Create the database by executing the following command `createdb spending_tracker`.   

#### Learnings
* Working with PostgreSQL (create databases, list databases)