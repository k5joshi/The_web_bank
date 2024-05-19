# The_web_bank
this is an cli working model of a banking system.
 3149315891799 accno.




2. Authentication and Authorization:
After a user logs in, we need to authenticate their credentials and authorize their access to accounts by verifying that they own those accounts.

Modification in Bank_account.py:

Update Deposit and Withdrawal Methods: Add a parameter user_id to these methods to pass the ID of the logged-in user.

Authorization Check: Before performing any deposit or withdrawal operation, ensure that the logged-in user is the owner of the account being accessed.


3. Enhancing User Creation and Authentication:
Improve user creation by generating a unique user_id for each user and saving user data into the database.

Modification in Users.py:
Generate Unique User ID: Implement a method to generate a unique user_id for each user.
Update user_creation Method: Modify the user_creation method to generate a user_id for the new user and save user data into the database.
These modifications will help ensure that only the owner of an account can access and modify it, enhancing security and data integrity in the system.

Let me know if you need further explanation or assistance with any specific part!