ALL CODE WAS TESTED USING WSL Terminal. The core functionality of the program is ran through driver.py; Namely, driver.py takes two arguments which need to be specified: --file_path, --mode.
    --file_path:
        This argument expects the path of a text file to be passed to it. I only tested its capabilities with relative addressing, but I assume absolute paths should work as well.

    --mode:
        HC: pass HC as a value for --mode to run Hill Climb
            - HC randomly initializes to a set of vertices and then finds the optimal neighbor at each state. It stops looking for neighbors when it can no longer improve. This process is repeated 10 times, and the best set from these 10 choices are selected
        ID: pass ID as a value for --mode to run Iterative Deepening
            - ID will find all solutions on the same level as the first solution found

    examples: All the examples from the class website have been saved in this directory under testcase_.txt
        Running Iterative Deepening on the testcase2.txt file:
            python3 driver.py --file_path testcase2.txt --mode ID

List of imported python libraries:
    - argparse
    - random

