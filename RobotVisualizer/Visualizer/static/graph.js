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
                    .separation(function(a, b){
                        return (a.parent == b.parent ? 3 : 1) / a.depth;
                    })
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


////////////////////////////
const root = stratify(treeData);  //d3.hierarchy(treeData);
const links = tree(root).links();
let xCenters = {};
for(var [key, value] of Object.entries(root.descendants())){
    if (!xCenters[value.depth]){
        xCenters[value.depth] = [value.x]; 
    } else {
        xCenters[value.depth].push(value.x);
    }
}

for(const [key, val] of Object.entries(xCenters)){
    xCenters[key] = calculateAve(val);
}

x0 = xCenters[0];
for(const [key, val] of Object.entries(xCenters)){
    xCenters[key] = val - x0;
}

const nodeColors = [];
for (var i =0; i < Object.keys(xCenters).length; i++){
    nodeColors.push(getRandomColor());
}
/////////////////////////////
const linkPathGenerator = d3.linkHorizontal()
                            .x(d => d.y)
                            .y(d => d.x);

g.selectAll("path").data(links)
    .enter().append("path")
        .attr("d", linkPathGenerator)
    .each(function(d){
        let sel = d3.select(this);
        sel.attr("fill", "none")
            .attr("stroke-width", "1px")
            .attr("stroke", nodeColors[d.source.depth]);
    });


var extraLinksNodes = [];
extraLinks.forEach(function(link){
    let parentNode = root.descendants().filter(function(d) {return d.data.child === link.parent;})[0];
    let childNode = root.descendants().filter(function(d) {return d.data.child === link.child;})[0];
    extraLinksNodes.push({parent: parentNode, child: childNode});
});


extraLinksNodes.forEach(function(multiPair) {
        g.append("path")
            .attr("d", function() {
                var oTarget = {
                    x: multiPair.child.x,
                    y: multiPair.child.y
                };
                var oSource = {
                    x: multiPair.parent.x,
                    y: multiPair.parent.y
                };
                return linkPathGenerator({
                    source: oSource,
                    target: oTarget
                });
            })
            .attr("fill", "none")
            .attr("stroke-width", "1px")
            .attr("stroke", nodeColors[multiPair.parent.depth]);
    });	


var node = g.selectAll(".node")
    .data(root.descendants())
    .enter()
        .append("g")
            .attr("class", function(d) { return "node" + (d.children ? " node--internal" : " node--leaf"); })
            .attr("transform", function(d) { return "translate(" + d.y + "," + d.x + ")"; })
        .append("circle")
                .attr("r", 5)
            .each(function(d){
                let sel = d3.select(this);
                sel.style("fill", nodeColors[d.depth]);
            });


if(showLabels){
    g.selectAll("text").data(root.descendants())
    .enter().append("text")
        .attr("x", d => d.y)
        .attr("y", d => d.x)
        .attr("dy", d => leafNodes.includes(d.data.child) ? "0.5em" : "1.5em")
        .attr("dx", d => leafNodes.includes(d.data.child) ? "1em" : "0em")
        .attr("text-anchor", d => leafNodes.includes(d.data.child) ? "start" : "middle")
        .attr("font-size", d => 2 - 0.5 * d.depth + "em")
    .text(d => d.data.child.split(".").pop());
}


function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

function calculateAve(arr){
    var total = 0;
    for(var i = 0; i < arr.length; i++) {
        total += arr[i];
    }
    return total / arr.length;
}