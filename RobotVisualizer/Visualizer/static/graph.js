/* 
I learned and inspired on how to visualize a tree from this youtube 
https://www.youtube.com/watch?v=jfpV7OBptYE&t=1s
from Curran Kelleher, and learned how to add new links to a tree 
from this article http://bl.ocks.org/robschmuecker/6afc2ecb05b191359862
by Rob Schmuecker
*/

const width = document.body.clientWidth;
const height = document.body.clientHeight;
const svg = d3.select('svg');

var stratify = d3.stratify()
                    .id(d => d.child)
                    .parentId(d => d.parent);


const margin = {top: 20, right: 150, bottom: 20, left: 150};
const innerWidth = width - margin.left - margin.right; 
const innerHeight = height - margin.top - margin.bottom;
const tree = d3.tree()
                    .size([innerHeight, innerWidth]);

const zoomG = svg 
    .attr("width", width)
    .attr("height", height)
        .append("g");

const g = zoomG.append("g")
            .attr("transform", "translate("+ margin.left + "," + margin.top + ")");

svg.call(d3.zoom().on('zoom', () => {
    zoomG.attr("transform", d3.event.transform);
}));

svg.attr("width", width)
    .attr("height", height);


const root = stratify(treeData);  //d3.hierarchy(treeData);
const links = tree(root).links();
const linkPathGenerator = d3.linkHorizontal()
                            .x(d => d.y)
                            .y(d => d.x);

g.selectAll("path").data(links)
    .enter().append("path")
    .attr("d", linkPathGenerator);


var node = g.selectAll(".node")
    .data(root.descendants())
    .enter().append("g")
        .attr("class", function(d) { return "node" + (d.children ? " node--internal" : " node--leaf"); })
        .attr("transform", function(d) { return "translate(" + d.y + "," + d.x + ")"; })


node.append("circle")
        .attr("r", 10)
        .each(function(){
            let sel = d3.select(this);
            sel.style("fill", getRandomColor());
        });

var extraLinksNodes = [];
extraLinks.forEach(function(link){
    let parentNode = root.descendants().filter(function(d) {return d.data.child === link.parent;})[0];
    let childNode = root.descendants().filter(function(d) {return d.data.child === link.child;})[0];
    extraLinksNodes.push({parent: parentNode, child: childNode});
});


extraLinksNodes.forEach(function(multiPair) {
        g.append("path")
            .attr("class", "additionalParentLink")
            .attr("d", function() {
                var oTarget = {
                    x: multiPair.parent.x,
                    y: multiPair.parent.y
                };
                var oSource = {
                    x: multiPair.child.x,
                    y: multiPair.child.y
                };
                /*if (multiPair.child.depth === multiPair.couplingParent1.depth) {
                    return "M" + oSource.y + " " + oSource.x + " L" + (oTarget.y + ((Math.abs((oTarget.x - oSource.x))) * 0.25)) + " " + oTarget.x + " " + oTarget.y + " " + oTarget.x;
                }*/
                return linkPathGenerator({
                    source: oSource,
                    target: oTarget
                });
            });
    });	


g.selectAll("text").data(root.descendants())
    .enter().append("text")
        .attr("x", d => d.y)
        .attr("y", d => d.x)
        .attr("dy", d => leafNodes.includes(d.data.child) ? "0.5em" : "1.5em")
        .attr("dx", d => leafNodes.includes(d.data.child) ? "1em" : "0em")
        .attr("text-anchor", d => leafNodes.includes(d.data.child) ? "start" : "middle")
        .attr("font-size", d => 2 - 0.5 * d.depth + "em")
    .text(d => d.data.child.split(".").pop());


    
function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    console.log("color is ", color);
    return color;
}