# pythons
Resources:
Python 3.7, IDLE (any platform - Win, Linux, Mac, Raspberry Pi)  Python 2.x will work, but the reference materials use Python 3, and using a consistent version of Python will make the tasks easier.
Automate the Boring Stuff with Python: Practical Programming for Total Beginners, Al Sweigart.  Available in Paper, e-book, or online at http://inventwithpython.com/#automate
(optional) Python Crash Course: A Hands-On, Project-Based Introduction to Programming, Eric Matthes. 
(recommended) Python Pocket Reference: Python In Your Pocket (Pocket Reference (O'Reilly)) - The O'Reilly pocket references are compact, reasonably complete, and a useful long term tool.
Python Documentation (online - generally very good documentation)
 
 
* Introduction to Software Development as a project
* Discussion of customer requirements
* Purpose of the project
* Inputs, outputs, general performance expectations

Deliverables
* Plan of the project
* Discussion of the data flow associated with the project
* Preliminary inventory of needed methods and attributes and how they relate to the data flows.
* (second project): Introduction to Classes and Objects
**  (second project - advanced): introduction to libraries
* Development plan - which methods in which order
* Preliminary test plan
* Test cases (what constitutes a successful project)

Project Development:
* Create the individual methods, For each method
* Identify & write down the purpose (to limit the scope)
* Identify the arguments and return value necessary
* If creation of a new class or Attribute makes sense, note that as well
* With the preliminary data flow, invoke the stubbed out methods
* Populating the individual methods. (also for each method)
* Create attributes as necessary
* Using the reference materials, identify the elements of Python not already known that will be used.  This creates a demand for various skills and knowledge, at the moment they are used.  Very reflective of how a project might go "in the real world."
(optional - for second set) create test cases and use the Python unit test framework
* When each method works, test the project as a whole (Integration & Integration testing)  This invites a useful discussion on what does it mean for something to "work"

Improvement
* Create an improved algorithm.  For example, if a sequential search is used, use a binary
* Revise the user interface
 
Project examples:
* Area Codes.  There are 3 digits dedicated to area codes, but there are rules so fewer than 800 are actually allowed.  There are a couple of interesting tasks here. 
Determination of what is and is not a valid Area Code

Given that a list of area codes and cities are downloaded from the internet, the program will have to
* Open the file (dialog or dialog box)
* Parse the file (line by line)
* Parse each line - the two parsing activities are substantially different.  This second one allows a basic regex introduction
* Given that the requested code may not actually exist in the list, the search algorithm will have to have a way to exit gracefully with a "null" result and present that information to the user.
Stage 2:
* Perform a search on an ordered list of known size. 
* Pass the results back - options are to concatenate AC and city into a string and return that, or …?
* Present the output to the user -
** Some mechanism to allow another lookup
* Would be nice to have some metric on the relative number of searches necessary to find the answer (or that no answer exists).

