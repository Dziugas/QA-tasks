After shortly researching the best practices of Selenium testing I changed the following things.

Task 1:

- Used Pytest. I initially thought that it should be just a script, like in task 3 - my bad, didn't read the task well enough.
- Applied Page Object Pattern with classes for each page.
- Prioritized selecting elements by IDs and Name instead of XPATH & CSS.
- Used only the implicit wait. Though I remembered reading in https://www.obeythetestinggoat.com/
that implicit waits are "a little flakey". The author was recommmending more usage of raw time.sleep().
Would be interesting to hear what is the best practice here. 

Also, would be interesting to discuss the naming of locators. Would it be better if all would be uppercase or have a prefix like "_loc" etc. 

Task 3:

- Mostly reorganized the code into one class and some reusable methods.


chromedriver still not included ;)
