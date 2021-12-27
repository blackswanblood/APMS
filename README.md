# SQL Project - APMS

Hello all!

### Project description

This project concentrates on the domain of theme parks (amusement parks). The database of our project models the employment, logistics, and ticket services of the park. 

#### Staff

There will be staff with different roles: cashiers, technicians, and operators, each tending to their respective facilities. 

#### Ticket

Regarding tickets, tourists can choose from day passes or individual rides: ride tickets will be associated with individual rides, and day passes will provide access for all rides. Tickets are merely for rides. There are also tickets for children and adults based on the tourist’s age. 

#### Tourist

Tourists can play on arcade machines, where they can win points to exchange gifts. Each arcade offers different gifts as prizes. All the arcades in the park have some arcade machines, but it is possible that identical machines appear in different arcades. Consequently, machines cannot uniquely be identified by its name unless combined with the arcade it belongs to. 

### Normalization
It entails organizing the columns and tables of a database to ensure that their dependencies are properly enforced by database integrity constraints and reduce the redundancy and eliminates undesired characteristics. All relation schemas have been reduced to BCNF.

Inspired by a dating app and Disney land database management system.

## How to use it?
**APMS** is an amusement park management system built on the python-based framework Django and SQLite, as well as a Bootstrap 4 template developed by Colorlib (https://github.com/puikinsh/concept) for the system GUI. The database of the project models the ticket service, employment, and amusement facilities of the park. On the project website, all the tables in the database and entries for each query are listed in a navigating bar (dropdown menu), which makes it easy and intuitive to operate on it. Also, there are some basic statistics of the system, such as the total number of tourists and staff, the number of gifts that have been redeemed, and the number of rides in the park displayed at the beginning of the main page. For each query, the users are able to either decide the fields of the query specifically or complete an operation we have already initialized. The users are also able to see all the tables related to the query on a new page, and the result table after processing it. Moreover, from each query page, it is straightforward to go back to the home page by clicking the APMS (Amusement Park Management System) symbol.

- Install Django and `cd` to the workspace directory. Run the following commands.
``` python
python manage.py  runserver
```
- Visit http://127.0.0.1:8000/SystemSite/ with your favorite web browser.



# Acknowedgement
HTML template reference: https://github.com/puikinsh/concept.

Django docs: https://www.djangoproject.com/
