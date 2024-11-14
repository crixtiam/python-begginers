

Test Costs for the heart-disease Data
-------------------------------------


Peter Turney
June 7, 1995



There are four files, in a C4.5-like format, that contain information
related to cost:

	1. heart-disease.cost
	2. heart-disease.delay
	3. heart-disease.expense
	4. heart-disease.group

For more information on the use and meaning of these files, see:

http://www.cs.washington.edu/research/jair/volume2/turney95a-html/title.html

The remainder of this file describes the format of the above four
files.


heart-disease.cost
------------------

Each row has the format "<test>: <cost>". The cost is in Canadian
dollars. The cost information is from the Ontario Health Insurance
Program's fee schedule. The costs in this file are for individual
tests, considered in isolation.  When tests are performed in groups,
there may be discounts, due to shared common costs. Groups of tests
with common costs are identified in the file "heart-disease.group". Costs
with discounts are in the file "heart-disease.expense".


heart-disease.delay
-------------------

Each row has the format "<test>: <immediate/delayed>". Tests with
immediate results are marked "immediate". Tests with delayed results
are marked "delayed". Delayed tests are typically blood tests, which
are usually shipped to a laboratory. The results are sent back to the
doctor the next day.


heart-disease.expense
---------------------

Each row has the format "<test>: <full cost>, <discount cost>".  The
full cost is charged when the given test is the first test of its group
that has been ordered for a given patient. The discount cost is charged
when the given test is the second or later test of its group that has
been ordered. Some of the tests involve, for example, making a patient
run on a tread mill while monitoring with an ECG. Several different
test results can be extracted from this one test (I am using the word
"test" in two different ways: a single feature or measurement on the
one hand, versus a single procedure -- which may be a group of
measurements or features -- on the other hand). Once you've decided to
pay for one of the tests in this group, the others are virtually free.
The major cost is the expertise required to interpret the ECG.


heart-disease.group
-------------------

The first row lists the groups. The remaining rows have the format
"<test>: <group>". The symbols used for groups are arbitrary. The
information in this file is meant to be used together with the
information in "heart-disease.expense".  The tests in a group share a
common cost.



