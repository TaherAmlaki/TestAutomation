import sys
import os 
from flask import Flask, render_template
import json 
from robot import run
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Visualizer.VisualizerListener import VisualizerListener
from Visualizer.ProcessTree import FlattenGraph


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", 
                            tree=tree_data, 
                            extra_inks=extra_links,
                            leaf_nodes = leaf_nodes,
                            show_labels = labels)


if __name__ == "__main__":
    if "-s" in sys.argv:
        ind = sys.argv.index("-s") + 1
        try:
            suite_path = sys.argv[ind]
        except IndexError:
            raise IndexError("suite_path value is not found") from None
    
    labels = False
    if "-labels" in sys.argv:
        try:
            ind = sys.argv.index("-labels") + 1
            labels = sys.argv[ind]
            labels = True if labels.lower() == "true" else False
        except IndexError:
            pass 

    print("==========> labels: ", labels)
    listener = VisualizerListener()
    options = {"log": None, "output": None, "report": None, 
               "listener": listener, "dryrun": "yes"}
    run(suite_path, **options)

    trees = listener.trees
    fltten = FlattenGraph(trees[0])
    tree_data, extra_links, leaf_nodes = fltten.links, fltten.extra_links, fltten.leaf_nodes

    app.run(debug=True)
