### Spending Tracker

A customer has asked to build an app that allows them to track their spending.

The app must be built using only:

- HTML/CSS
- Python
- Flask
- PostgreSQL and psycopg2

It must not use:

- Any Object Relational Mapper (e.g. ActiveRecord)
- JavaScript
- Any pre-built CSS libraries, such as Bootstrap
- Authentication

### Setup + Installation

 - in Terminal, navigate to the project folder
 - dropdb spending_tracker
 - createdb spending_tracker
 - psql -d spending_tracker -f project_folder/db/spending_tracker.sql
 - psql -d spending_tracker
 - flask run

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

![home](https://github.com/OleksiiK93/spending_tracker_project/assets/110308047/e6820a04-9b19-4e84-83b4-ad35b697a52c)
![merchants](https://github.com/OleksiiK93/spending_tracker_project/assets/110308047/2b3a4654-35cc-4190-ba27-f99df109bb72)
![transactions](https://github.com/OleksiiK93/spending_tracker_project/assets/110308047/1f448122-118a-4ca5-99be-c7a850bcdc26)

