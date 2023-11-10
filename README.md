# my_data_process
Data processing exercise from Qwasar, Software Engeering program - Season 1 Arc 2.

## Specification
* Given a dataset of sales from My Online Coffee Shop, identify customers who are more likely to buy coffee online.
* Dataset is in csv format.
* Create a function with code logic. Solution is not hard coded. 
* Input for the function is a string array output from my_data_transform.
* The function will group the data and it will become a Hash of hash. It will return a json string:\
Example:\
"{'Gender': {'Male': 22, 'Female': 21}, 'Email': {'yahoo.com': 3, 'hotmail.com': 2}, ...}"
* Use STRINGS as keys.
* Discard the column FirstName, LastName, UserName and Coffee Quantity from our output.
* Prototype function: def my_data_process.
