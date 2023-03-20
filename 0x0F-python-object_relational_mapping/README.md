 # Python - Object-relational mapping

In this project, I learned about how object-relational mapping is used for
database scripting. I became familiar with using MySQLdb and SQLAlchemy to
query, create, edit, and delete tables in MySQL.

## Tests :heavy_check_mark:

* [tests](./tests): Folder of SQL and Python scripts for setting up test tables
		    for all files. Provided by Holberton School.

## Tasks :page_with_curl:

* **0. Get all states**
* [0-select_states.py](./0-select_states.py): Python script that uses MySQLdb
to list all states in the database `hbtn_0e_0_usa`.


* **1. Filter states**
* [1-filter_states.py](./1-filter_states.py): Python script that uses MySQLdb
to list all states with names starting with `N` in the database `hbtn_0e_0_usa`.																										    
* **2. Filter states by user input**
*  [2-my_filter_states.py](./2-my_filter_states.py): Python script that uses
MySQLdb to display all values matching a given name in the `states` table of
the database `hbtn_0e_0_usa`.
																																											     

																																											    * **3. SQL Injection...**
																																						      * [3-my_safe_filter_states.py](./3-my_safe_filter_states.py): Python script
																																																			      that uses MySQLdb to display all values matching a given name in the `states`
																																																										      table of the database `hbtn_0e_0_usa`.


																																																															    * **4. Cities by states**
																																																															      * [4-cities_by_state.py](./4-cities_by_state.py): Python script that uses
																																																																						  MySQLdb to list all cities from the database `hbtn_0e_4_usa`.
																																																																												  

																																																																												 * **5. All cities by state**
																																																																												   * [5-filter_cities.py](./5-filter_cities.py): Python script that uses MySQLdb
																																																																																		   to list all cities of a given state in the database `hbtn_0e_4_usa`.
																																																																																							    

																																																																																							   * **6. First state model**
																																																																																							     * [model_state.py](./model_state.py): Python module defining a class `State`
																																																																																												     that inherits from SQLAlchemy `Base` and links to the MySQL table `states`.

																																																																																																      * **7. All states via SQLAlchemy**
																																																																																																        * [7-model_state_fetch_all.py](./7-model_state_fetch_all.py): Python script
																																																																																																								        that uses SQLAlchemy to list all `State` objects from the database
																																																																																																															        `hbtn_0e_6_usa`.
																																																																																																																		  

																																																																																																																		* **8. First state**
																																																																																																																		  * [8-model_state_fetch_first.py](./8-model_state_fetch_first.py): Python script
																																																																																																																										      that uses SQLAlchemy to print the first `State` object from the database
																																																																																																																																	      `hbtn_0e_6_usa`, ordered by `states.id`.
																																																																																																																																						        

																																																																																																																																						      * **9. Contains `a`**
																																																																																																																																						        * [9-model_state_filter_a.py](./9-model_state_filter_a.py): Python script
																																																																																																																																														      that uses SQLAlchemy to list all `State` objects that contain the letter `a`
																																																																																																																																																					      in the database `hbtn_0e_6_usa`.
																																																																																																																																																									        

																																																																																																																																																									      * **10. Get a state**
																																																																																																																																																									        * [10-model_state_my_get.py](./10-model_state_my_get.py): Python script that
																																																																																																																																																																	    uses SQLAlchemy to print the `id` of the `State` object with name matching that
																																																																																																																																																																								    passed as argument in the database `hbtn_0e_6_usa`.


																																																																																																																																																																														   * **11. Add a new state**
																																																																																																																																																																														     * [11-model_state_insert.py](./11-model_state_insert.py): Python script that
																																																																																																																																																																																					         uses SQLAlchemy to add the `State` object "Louisiana" to the database
																																																																																																																																																																																												`hbtn_0e_6_usa`.


																																																																																																																																																																																														* **12. Update a state**
																																																																																																																																																																																														  * [12-model_state_update_id_2.py](./12-model_state_update_id_2.py): Python
																																																																																																																																																																																																						        script that uses SQLAlchemy to change the name of the `State` object with
																																																																																																																																																																																																													        `id = 2` in the database `hbtn_0e_6_usa` to "New Mexico".
																																																																																																																																																																																																																			         
																																																																																																																																																																																																																			       * **13. Delete states**
																																																																																																																																																																																																																			         * [13-model_state_delete_a.py](./13-model_state_delete_a.py): Python script
																																																																																																																																																																																																																											         that uses SQLAlchemy to delete all `State` objects with a name containing the
																																																																																																																																																																																																																																		         letter `a` from the database `hbtn_0e_6_usa`.

																																																																																																																																																																																																																																								      * **14. Cities in state**
																																																																																																																																																																																																																																								        * [model_city.py](./model_city.py): Python module defining a class `City`
																																																																																																																																																																																																																																													      that inherits from SQLAlchemy `Base` and links to the MySQL table `cities`.
																																																																																																																																																																																																																																																	          