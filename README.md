# TRC20
My first module. Use the TRC20 function(deposit, withdrawl, create wallet...)

VERSION = 0.1BETA


**[Methods](#Methods)**

***
# How to use?

1. save the folder "TRC20" to your project
2. import module
  ```import TRC20```
3. initialize the user
   ```user1 = USER_WALLET(address="YOUR TRC20 ADDRESS")```
4. use the function. Example:
   ```user1.last_transactions()```
***
# <a id="Methods">Methods</a>
+ last_transactions()
+ deposit()
+ get_address()
+ version()
+ errors()

#### last_transactions()
   parameter  |    default   |   type  |          description       |
:-------------|:------------:|:-------:|----------------------------:
limit | 1 | int | how many recent transactions will be shown
only_from | False | bool | if it is True, only transactions that were sent from the address
only_to | False | bool | if it is True, only transactions that were sent to the address
