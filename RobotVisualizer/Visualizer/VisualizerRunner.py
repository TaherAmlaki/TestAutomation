import sys
import os 
from robot import run
import json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Visualizer.VisualizerListener import VisualizerListener


if __name__ == "__main__":
    if "-s" in sys.argv:
        ind = sys.argv.index("-s") + 1
        try:
            suite_path = sys.argv[ind]
        except IndexError:
            raise IndexError("suite_path value is not found") from None
    
    tests = None
    if "-t" in sys.argv:
        ind = sys.argv.index("-t") + 1
        try:
            tests = sys.argv[ind:]
        except IndexError:
            pass

    listener = VisualizerListener()
    options = {"log": None, "output": None, "report": None, 
               "listener": listener, "dryrun": "yes"}
    if tests is None:
        tests = []
    run(suite_path, *tests, **options)
    trees = listener.trees
    trees[0].print_tree()
    """
    => GetPeople
        |-- Get Person 3 From SwApi
                |-- RequestsLibrary.Create Session
                |-- RequestsLibrary.Get Request
        |-- Get Person 5 From SwApi
                |-- RequestsLibrary.Create Session
                |-- RequestsLibrary.Get Request   
    """
    d = trees[0].convert_for_d3()
    print(json.dumps(d, indent=2))