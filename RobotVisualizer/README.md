# Robot Framework Code Visualizer
## By Flask and D3.js tree visualization

![Visualized Code](https://www.taheramlaki.com/static/blog/images/robot_visualization_big_tree.png)
To understand code structure of my Robot Framework project I have created a visualization application 
using Robot Framework listener, python implementation for a tree structure, flask library, and d3.js for 
visualization on a browser. The result is a graph which shows hierarchy of the suite and links between keywords.


You can check out my article about this project [here](https://www.taheramlaki.com/blog/articles/robot-visualization-flask-d3/).


## Usage 
You can use this project by cloning **RobotVisualizer** and executing **FlaskApp** from your command line. 
The suite path should be passed by using **-s** or **--suite** options followed by the suite path, similar to below code snippet.
```
python .\RobotVisualizer\Visualizer\FlaskApp.py -s .\RobotVisualizer\Tests\GetPeople.robot
```

Mode options can be given to control depth of keywords links, ignoring or including BuiltIn keywords in the graph, and show or hide node labels.

```
-s or --suite, required, relative or absolute path to .robot file
-l or --labels, not required, Option to show node labels, default value is False, yes|true|t|y|1 => True
-ml or --maxlevel, not required, maximum keyword depth, default is infinite, integer values
-ib or --ignorebuiltin, not required, Option to ignore builtin keywords, default is True
```

The result is a horizontal graph starting from left to right, by suite node, and will be shown on browser at localhost:5000.

## Structure 
The project consist of implementation of a general tree or graph node class. 

A custom listener based on Robot Framework listener api version 2 is implemeneted to hook into test execution and 
create and update a graph object. This listener will contain root node of the code visualizer graph object.

To use the listener result for visualization by D3.js library, I reconfigure the graph data structure by flattening the data
and extracting the links which connecting a child to second (or higher) parent node.

And at last I server the data through a Flask web application and process the data using D3.js JavaScript library and visualize the graph.