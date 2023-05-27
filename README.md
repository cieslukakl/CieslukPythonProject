<h1>Beautifull guide</h1> 
<h2>explaining how to run tests</h2>

<h3>Read following guid carefully and you will be rewarded with perfectly running tests</h3>

1. Tests are written in Python 3.10 with use of following packages (which should ne installed separatelly:
   1. pytest-bdd (pip install pytest-bdd)
   2. faker (pip install faker)
   3. pytest
   4. selenium
2. Installed plugins:
   1. Gherkin 221.5080.126

Tests are written in BDD (Behavior Driven Development). Given way of preparing tests was used to allow business users
easily understand and pariticpate in scenarios preparation.
BDD uses following keywords:
- GIVEN
- WHEN
- THEN

Files location:
- Files stored in tests_aradena/feature_files directory with .feature extension contain prepared tests (BDD)
which are later subject for automation. 
- Files stored in tests_aradena/pages directory contain classes for each page
- File stored in tests_aradena/step_definitions directory contain steps definitions for specific tests

To run all tests use:

- python -m pytest
