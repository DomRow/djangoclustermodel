function scatter_d3(data){
  var margin = {top: 20, right: 20, bottom: 30, left: 40},
  width = 960 - margin.left - margin.right,
  height = 500 - margin.top - margin.bottom;

  //x is a discret domain from x to width
  var x = d3.scale.linear()
  .range([0, width]);

var y = d3.scale.linear()
.range([height, 0]);

var color = d3.scale.category10();

var xAxis = d3.svg.axis()
.scale(x)
.orient("bottom");

var yAxis = d3.svg.axis()
.scale(y)
.orient("left");

var svg = d3.select("body").append("svg")
.attr("width", width + margin.left + margin.right)
.attr("height", height + margin.top + margin.bottom)
.append("g")
.attr("transform", "translate(" + margin.left + "," + margin.top + ")");



data.forEach(function(d) { 
    //d.rating = +d.rating;
    //d.rating_count = +d.rating_count;
    //d.cl = +d.cl;
  });
console.log('here');
x.domain(d3.extent(data, function(d) { return d[0]; })).nice();
y.domain(d3.extent(data, function(d) { return d[1]; })).nice();

svg.append("g")
.attr("class", "x axis")
.attr("transform", "translate(0," + height + ")")
.call(xAxis)
.style("fill",function(d){return color(d)})
.append("text")
.attr("class", "label")
.attr("x", width)
.attr("y", -6)
.style("text-anchor", "end")
.text("Rating Count");

svg.append("g")
.attr("class", "y axis")
.call(yAxis)
.style("fill",function(d){return color(d)})
.append("text")
.attr("class", "label")
.attr("transform", "rotate(-90)")
.attr("y", 6)
.attr("dy", ".71em")
.style("text-anchor", "end")
.text("Rating")

svg.selectAll(".dot")
.data(data)
.enter().append("circle")
.attr("class", "dot")
.attr("r", 10)
//CX is centre x
.attr("cx", function(d) {console.log(d[0][0]);return d[0][0]; })
.attr("cy", function(d) { return d[0][0]; })
.style("fill", function(d,i) {
  var colors;
  if (i==1){colors="purple";
  } else if (i==2){colors="yellow";
  } else if (i==3){colors="cyan";}
  return colors;
});
      //Will append cluster integer here
      //.style("fill", function(d) { return color(d.title); });

      var legend = svg.selectAll(".legend")
      .data(color.domain())
      .enter().append("g")
      .attr("class", "legend")
      .attr("transform", function(d, i) { return "translate(0," + i * 20 + ")"; });

      legend.append("rect")
      .attr("x", width - 18)
      .attr("width", 18)
      .attr("height", 18)
      .style("fill", color);

      legend.append("text")
      .attr("x", width - 24)
      .attr("y", 9)
      .attr("dy", ".35em")
      .style("text-anchor", "end")
      .text(function(d) { return d; });


      console.log("End of scatterfile");
    };