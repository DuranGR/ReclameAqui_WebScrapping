ReadMe

Requirements
    libraries
	- Pandas
	- Time
	- Selenium
    Installs
	- Selenium Chrome Webdriver
Manual of Instructions
	1. Find The Company you need the data from ReclameAqui
	2. Go to the URL where you can get the links from. The URL will be built like the following
	https://www.reclameaqui.com.br/empresa/"Company-Name"/lista-reclamacoes/?pagina=1
	3. Set the variable 'driver_path' with your path to the driver
	4. Change the for loop range in line 71 to your preference, the higher the range the higher is the number of complains
	5. Run the Code and wait for the process to finish, the code can take up to 3 hours depending on the number of complains
Bugs/Problems
	The program needs to be run non-stop, in the case of your internet stopping there code will most likely shut down

	The Maximun number of complains accessible is 1010, after the 101st page the website will keep repeating the complains from page 101

I hope this code may be of use to you :D



























