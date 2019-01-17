# Practical Assignments
Computer Science Practicals Repository

AMITY INTERNATIONAL SCHOOL
PRACTICAL LIST 2018-19
CLASS XI, COMPUTER SCIENCE (PYTHON)

1.	WAP to calculate the area and circumference of a circle if radius is given.

2.	WAP to find the simple interest if principal, rate and time are given

3.	Write a program to find the sum of first three multiples of a given number n

4.	Write a program to read your name, age and class and display message as - 
Welcome <name>
I am <age> years old and studying in class <class>
Last year I was <n> years old.

5.	WAP to find the denomination of currency in Re 1,2,5,10,50,100,500 and 1000 in a given amount entered by user.

6.	WAP to make a simple calculator that reads two numbers and an operator. On selection of an operator, perform operation and print the result as shown below-
Enter first number: 5
Enter second number: 7
Enter operator: *
Result: 5 * 7 = 35
7.	A farm has chickens and rabbits. Farm owner counts number of heads and legs and wishes to find out number of chickens and rabbits? Write a program to solve this classic ancient Chinese puzzle. If farm owner counts 35 heads and 94 legs. Calculate and print how many rabbits and chickens he has? 

8.	You are driving a little too fast and the police officer stops you and issues a ticket. Write code to compute the result, encoded as an integer value: 0=no ticket, 1=small ticket, 2=big ticket. 
If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday, on that day, your speed can be 5 higher in all cases.WAP to model above scenario.

9.	An electricity board charges according to the following rules:
a.	For the first 100 units – 40 p per unit (p = Paise)
b.	For the next 200 units - 50 p per unit
c.	Beyond 300 units - 60 p per unit
d.	All users have to pay meter charge also, which is Rs 50.
e.	Write a program to read the number of units consumed and print out the charges.

Sample output
Input units: 150
Charges Rs. 115        [calculated as (100*.4 + 50*.50 +50)]
10.	WAP that reads n digit number. After reading the number, compute and display the sum of the odd positioned digits, multiply all even positioned digits and add these two numbers. 

11.	Write a program which will find all such numbers which are divisible by 7 but are not multiple of 5, between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

12.	Develop a program to classify students amongst various categories as per their age entered. Read age of N students and count no of students falling in each category as described below  print a report as follows –
Group A: 12 yrs and above but less than 15 yrs	 - XX
Group B: 15 yrs and above but less than 17 yrs     - XX
Group C: 17 yrs and above but less than 19 yrs  	- XX 
Group D: Lesser than 12 yrs 			- XX
13.	Every book published by an international publisher should carry an International standard book Number(ISBN).It is 10 character 4 part number as shown below:-
0-07-041183-2
The first part denotes the region, the second represents the publisher, the third identifies the book and fourth is the digit. The check digit is computed as follows:-
Sum=(1*first digit)+(2*second digit)+(3*third digit)+……(9*ninth digit)
Check digit is the remainder when sum is divided by 11. Write a program that reads a given ISBN number and checks whether it represents a valid ISBN.
14.	Write a program to find if a number entered is a palindrome or not.

15.	A very famous numerical algorithm exists to find out the highest common factor (also called the greatest common divisor) of two numbers. The algorithm was invented by Euclid; it is therefore called the Euclid’s algorithm.
Here is how the algorithm works. Say you wish to find out the HCF of two numbers A and B. Simply repeat the following steps until both numbers become equal:
If A is greater than B, change A to A-B and do not modify B
If B is greater than A, change B to B-A and do not modify A

The value of A (and B) when both become equal will be the Highest Common Factor!
Let’s try this out with two numbers, A=18 and B=42.
B is greater than A, so B becomes 24 and A remains as 18. So, we have:
A = 18, B = 24 
If we repeat this process, we get:
A = 18, B = 6 A = 12, B = 6 A = 6, B = 6
Finally, both A and B become equal (both have value 6). The HCF of 18 and 42 is 6.

16.	According to a study, the approximate level of Intelligence of a person can be calculated using the following formula:
i=2(y+0.5x)
Write program, which will produce a table of values of  i,y and x where y varies from 1 to 6 and for each value of y , x varies from 5.5 to 12.5 in steps of 0.5.

17.	Write a program to play the "Guess the number"-game, where the number to be guessed is randomly chosen between 1 and 20. This is how program should work when executed 
(Only three chances allowed)
Hello! What is your name? 
Tanuj
Well, Tanuj, I have chosen of a number between 1 and 20. 
Take a guess. 
10 
Your guess is too low.
Take a guess.
15 
Your guess is too low. 
Take a guess. 
18 
Good job, Tanuj! You guessed my number in 3 guesses!

18.	WAP to print the sum of n terms of  the  following series -
   A) x+ x2/2 + x3/3 + x4/4 +....+ xn/n
B) 1/ (sqrt(2) + 2 / sqrt(3) + 3/ sqrt(4) +.......n/sqrt(n+1)
19.	Read today's date as DD,MM,YYYY format and print it as DD- MMM - YY
Eg Input date-
Enter day 25
Enter month 04
Enter year 2014
Result:  25-APR -14
20.	WAP to print a Pascaline triangle of n lines. 

21.	Read two strings and check if string1 is prefix, postfix or nothing from the string2. 
(Use re module)
For Eg-
string1: ever
string2: evergreen
Output:  prefix
22.	Write a program to read a string and print 
i)Frequency of all characters         ii) Word of highest length 
iii) The string in title case              iv) Read full name as a string and print only the initials.

Eg- 
Enter name: Mohan Das Karam Chand Gandhi
Output string M D K C Gandhi.
23.	Data can be represented in memory in different ways Binary, Decimal, Octal, and Hexadecimal. Input number in decimal and desired type (Specify B for Binary O for Octal, H for Hexadecimal) for output.   

Write a program to perform the conversions-
SAMPLE INPUT      12 
DESIRED TYPE      B	
Result:  1100
SAMPLE INPUT        25
DESIRED TYPE        O	
Result: 	41

24.	In Cryptography, a Caesar cipher is a very simple encryption techniques in which each letter in the plain text is replaced by a letter some fixed number of positions down the alphabet list in a cyclic manner. For example, with a shift of 3, A would be replaced by D, B would become E, and so on. The method is named after Julius Caesar, who used it to communicate with his generals. ROT-13 ("rotate by 13 places"). 
Create menu driven program to encrypt and decrypt which takes in a string and rotation (rotate by n places) and encrypts the string then decrypts the string. The program should be menu driven. Also if rotation is not specified then the encryption should take place by 13.

25.	Write a program that takes a list of numbers prints a histogram to the screen. 
****
*********
*******
Take a list of numbers and find frequency of each number and plots a histogram as shown above.

26.	Consider the following algorithm to generate a sequence of numbers and store them into a list. Start with an integer n. If n is even, divide by 2. If n is odd, multiply by 3 and add 1. Repeat this process with the new value of n, terminating when n = 1.

For example, the following sequence of numbers will be generated for n = 22:
22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
Now do the following on above created list-
a.	Print total number of elements in the list
b.	Print the sorted list by applying all the sorting techniques and find efficiency of each sorting tech ique
c.	Delete all occurrences of multiples of 10 and print it .

27.	Write a program to sort a given list of numbers using Bubble Sort algorithm and print the total number of operations taking place while sorting the given list.

28.	Write a program to sort the given list of numbers using Insertion sort algorithm and print the total number of operations taking place while sorting the given list.
29.	Write a program which takes 2 digits, X, Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

30.	Given below two dictionaries:
relatives ={"Lisa" : "daughter", "Bart" : "son", "Marge" : "mother", "Homer" : "father", "Santa" : "dog"} 
ages = {“Lisa” : 8, “Bart”:10,”Marge”:35,”Homer”:40,”Santa”:2}
Write a code that combines the two dictionaries to generate the following output:
The Simpsons: 
Homer is a father and is 40 years old 
Lisa is a daughter and is 8 years old 
Bart is a son and is 10 years old
Santa is a dog and is 2 years old 
Marge is a mother and is 35 years old 

31.	Write a program that takes a list of words and creates a dictionary with word as the key and number of occurrences of the word as the value. 
 For example if list is given as ['the','of','an','is','an','the']
Then the dictionary should be d={'the':2,'of':1,'an':2,'is':1}
32.	Write a program that takes a list of words and creates a dictionary with frequency (no of occurrences) of word as 	key and list of words for that frequency as value. 
For example if list is given as ['the','of','an','is','an','the']
Then dictionary should be {2:['the','an'],1:['of','is']}
33.Write a program to create a dictionary of names of flowers as keys and the colours in which they exist as values in tuples, for example  D={'rose':('red','black','pink'),'lily':('white','violet')} . Now write a code to print 
a) The flower which exists in maximum number of colors
b) The colour in which most of the flowers exist


34.There are 36 possible combinations, if we throw two dice. A simple pair of loops over range (6) +1 will enumerate all combinations. The sum of the two dice is more interesting than the actual combination. Create a dictionary of all combinations, using the sum of numbers on the two dice as the key. Each value of dictionary will be a tuple with all possible combination.

Section B- SQL  Questions

Q1. Create the table given with the structure given as
No(primary key), Qty as integer values, 
Title, author, subject and publisher as string values 
Price(not null) as decimal value. 
Now after inserting the records as shown in the table write the 	SQL query for  (i) to (vii)	
			     RELATION: BOOKHOUSE
No.	Title	Author	Subject	Publisher	Qty.	Price
1	Data Structure	Lipschute	DS	McGraw	4	217.00
2	DOS Guide	Nortron	OS	PHI	3	175.00
3	Turboc C++	Robort Lafore	Prog	Galgotia	5	270.00
4	Dbase Dummies	Palmer	DBMS	PustakM	7	130.00
5	Mastering Windows	Cowart	OS	BPB	1	225.00
6	Computer Studies 	French	FND	Galgotia	2	75.00
7	COBOL	Stern	Prog	John W	4	1000.00
8	Guide Network	Freed	NET	Zpress	3	200.00
9	Basic for Beginners	Norton	Prog	BPB	3	40.00
10	Advanced Pascal 	Schildt	Prog	McGraw	4	350.00

I)Display title of all books with price between 100 and 300
Ii)Display title and author of all the books having type “Prog” and published by BPB.
iii) Display number of books and average price for each type of publisher
Iv) Display title, price in descending order of price
V) Display all the books where title starts with “D” and qty is more than 3.
Vi)Display publisher wise total stock value (Qty * price) 
Vii)Display title of the book which is costliest.

Q2 Create the table  Order given with the structure given as
Orderno(primary key),Orders ,Payments as integer values, 
Cname(company name, distinct values),cloc(company location),as string values 
OrderDate(Not null ) as date type value
After inserting the records shown in the table write the SQL query for  (1) to (5)


Table : Order
Orderno	Orderdate	CName	Cloc	Orders(inRs)	Payments(inRs)

1	12/02/2008	Avlon	Delhi	100000	90000
2	21/11/2008	Parason	Jaipur	230000	230000
3	15/10/2008	Trident	Raipur	120000	100000
4	13/1/2008	Avlon	Jaipur	240000	240000
5	17/7/2008	Trident	Delhi	340000	310000
7	16/6/2008	Nalco	Chennai	140000	140000
1.	Add a new column Discount_percent to hold decimal values.
2.	Display all distinct companies listed in the table 
3.	Add values under Discount_percent column such that 10% discount is given to those companies who have made full payments.
4.	Find number of companies and average orders given to the company city wise.
5.	List all orders given between 1/1/2008 to 12/10/2008.

Q.3. Given below a table FAMILY. Write SQL queries for the following:
TABLE: FAMILY
Family_name	Female_Members	Male_Members	Income	Occupation

Mirsa	2	2	20000	Service
Tyagraja	1	2	28000	Business
Joshi	2	3	18000	Service
Khan	3	2	25000	Service
Gupta	2	1	10000	Farming
Rao	1	3	30000	Business
Yadav	1	2	20000	Farming
Chaddha	3	1	50000	Business
i)	Display occupation and average income as per their occupation.
ii)	Display family having lowest income.
iii)	List all those families where female members are less than 3, in ascending order of their income.
iv)	How many types of occupation are listed in table.
v)	Display a report showing total members and average per capita income of each family.
.
Q4. Create a table consignor with CnorId defined as primary key in Consignor table and defined as foreign key in consignee table. After inserting the shown records,	 write SQL query for  (i) to (v)				     
RELATION: CONSIGNOR
CnorID	CnorName	CnorAddress	City
ND01	R. Singhal 	24, ABC Enclave	New Delhi
ND02	Amit Kumar	123, Palm Avenue	New Delhi
MU15	R. Kohli	5/A, South Street	Mumbai
MU50	S. Kaur	27-K, Westend 	Mumbai

RELATION: CONSIGNEE
CneeID	CnorID	CneeName	CneeAddress	CneeCity
MU05	ND01	Rahul Kishore	5, Park Avenue	Mumbai
ND08	ND02	P. Dhingra	16/J, Moore Enclave	New Delhi
KO10	MU15	A P Roy	2A, Central Avenue 	Kolkata
MU32	ND02	S. Mittal	P 245, AB Colony	Mumbai
ND48	MU50	B P Jain	13, Block D, A Vihar	New Delhi 

i)	Display name of all the consignors from Mumbai
ii)	List the all the CnorName,Cneename and Cneecity 
iii)	List all the city and no of consignee belonging to that city
iv)	List all the CnorName and Cneename where consignor city is same as CneeCity
v)	Arrange the rows in ascending order of city from Consignee table

Q.5  Create the tables Doctor and Patient by choosing the appropriate data types for all attributes. Insert the shown records in these tables and write the required queries for 1-5	
 TABLE : DOCTOR
Doc_no	Name	Department	Cons_fee
D1	Dr. Garg	Cardiology	500
D3	Dr. Rakesh Jain	Pediatric	250
D4	Dr. Ajay Kumar	Physician	150
D6	Dr. Seema Patil	Cardiology	450
D9	Dr. Abha Verma	Pediatric	300

TABLE : PATIENT
pno	Name	Dt_birth	Doc_no
P2	Suraj	12-11-1969	D1
P4	Feroj	23-2-1980	D6
P5	Jai Prakash	3-10-1990	D4
P7	Anshul	1-6-2005	D3
P9	Zarina	4-9-2004	D9

1.	List department wise number of doctors in the department along with their average consultation fee.
2.	List the name of doctors who are taking consultation fee more than the average consultation fee.
3.	List Doctor Name along with the name of patient they are treating.
4.	Name the youngest patient.
5.	Display patient name and their age as on today.





Section C- Mongo DB
Consider the following structure of 'restaurants' collection:
{
  "address": {
     "building": "1007",
     "coord": [ -73.856077, 40.848447 ],
     "street": "Morris Park Ave",
     "zipcode": "10462"
  },
  "borough": "Bronx",
  "cuisine": "Bakery",
  
"grades": [
     { "date": { "$date": 1393804800000 }, "grade": "A", "score": 2 },
     { "date": { "$date": 1378857600000 }, "grade": "A", "score": 6 },
     { "date": { "$date": 1358985600000 }, "grade": "A", "score": 10 },
     { "date": { "$date": 1322006400000 }, "grade": "A", "score": 9 },
     { "date": { "$date": 1299715200000 }, "grade": "B", "score": 14 }
  ],
  "name": "Morris Park Bake Shop",
  "restaurant_id": "30075445"
}

1.Write a MongoDB query to display all the documents in the collection restaurants. 
2.Write a MongoDB query to display the fields restaurant_id, name, borough and cuisine for all the documents in the collection restaurant.
3.Write a MongoDB query to display the fields restaurant_id, name, borough and cuisine, but exclude the field _id for all the documents in the collection restaurant.
4.Write a MongoDB query to display the fields restaurant_id, name, borough and zip code, but exclude the field _id for all the documents in the collection restaurant
5.Write a MongoDB query to display all the restaurant which is in the borough Bronx.


6.Write a MongoDB query to display the first 5 restaurant which is in the borough Bronx
7.Write a MongoDB query to display the next 5 restaurants after skipping first 5 which are in the borough Bronx. 
8.Write a MongoDB query to find the restaurants who achieved a score more than 90. 
9.Write a MongoDB query to find the restaurants that achieved a score, more than 80 but less than 100. 
10.Write a MongoDB query to find the restaurants that do not prepare any cuisine of 'American' and their grade score more than 70 and latitude less than -65.754168
