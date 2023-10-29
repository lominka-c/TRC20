# TRC20
My first module. Use the TRC20 function(deposit, withdrawl, create wallet...)

VERSION = 0.1BETA

[How to use](#HowToUse)
[Methods](#Methods)

***
# <a id="HowToUse">How to use?</a>

1. save the folder "TRC20" to your project
2. import module
 
import TRC20
3. initialize the user
  
user1 = USER_WALLET(address="YOUR TRC20 ADDRESS")
4. use the function. Example:
  
user1.last_transactions()
***
# <a id="Methods">Methods</a>
+ [last_transactions()](#lT)
+ [deposit()](#deposit)
+ [get_address()](#gA)
+ [version()](#version)
+ [errors()](#errors)

#### <a id="lT">last_transactions()</a>
parameter | default | type | description |
:-------------|:------------:|:-------:|:----------------------------
limit | 1 | int | how many recent transactions will be shown
only_from | False | bool | if it is True, only transactions that were sent from the address
only_to | False | bool | if it is True, only transactions that were sent to the address

#### <a id="deposit">deposit()</a>
parameter | default | type | description |
:-------------|:------------:|:-------:|:----------------------------
lT | 0 | list | the last transaction
time | 5 | int | how many minutes ago the transaction could have been made. If the transaction time is outside the limit, no action will be taken

#### <a id="gA">get_address()</a>
parameter | default | type | description |
:-------------|:------------:|:-------:|:----------------------------


#### <a id="version">version()</a>
parameter | default | type | description |
:-------------|:------------:|:-------:|:----------------------------

#### <a id="errors">errors()</a>
parameter | default | type | description |
:-------------|:------------:|:-------:|:----------------------------
code | 0 | int | gives information about exactly what the error is
