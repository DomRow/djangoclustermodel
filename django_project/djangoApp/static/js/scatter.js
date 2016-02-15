function scatter_d3(data){
console.log(data);

  var margin = {top: 20, right: 20, bottom: 30, left: 40},
  width = 960 - margin.left - margin.right,
  height = 500 - margin.top - margin.bottom;

  //x is a discrete linear range from x to width
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

var xValue = function(d){ return d;}
//var newX,newY;
var yValue = function(d){ return d;}

var tooltip = d3.select("body").append("div")
  .attr("class", "tooltip")
  .style("opacity",0);

var svg = d3.select("body").append("svg")
.attr("width", width + margin.left + margin.right)
.attr("height", height + margin.top + margin.bottom)
.append("g")
.attr("transform", "translate(" + margin.left + "," + margin.top + ")");

x.domain(d3.extent(data, function(d,i) {console.log('dclusterta '+d);return d;}));
y.domain(d3.extent(data, function(d,i) {console.log('dclustertb '+d);return d;}));

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



//For each element in d, each group=cluster
//clusers
data.forEach(function(d,i){
  console.log(data.length);
  cluster=d;
  //console.log("hi " +d3.max(cluster));
  return cluster;
 }); 
  console.log('Data is: ' +data[0]);
  console.log('Cluster var is: ' +cluster);
  cluster.forEach(function(d){
    rating=d[0];
    rating_count=d[1];
    svg.selectAll(".dot")
    .data(cluster)
    .enter().append("circle")
    .attr("class", "dot")
    .attr("r", 5)
    //Scaling factor
    .attr("cx",function(d,i){
      console.log("D from cx " +d[0]+" and result "+(9*d[0])); //" and result "+(9*d[0]));
      //newX=d[0];
      return d[0]*(width/100);//*(width/100);
    })
    .attr("cy", function(d,i){
      console.log("D from cy " +d[1]+ " and result " +(45*d[1]));
      //newY=d[1];
      return height-d[1]*45;
    })
    .style("fill", color(d) )
    .on("mouseover", function(d){
      temp=d;
      console.log("HIYO " +xValue(d));
      tooltip.transition()
        .duration(200)
        .style("opacity",1);
        tooltip.html("Title" + "<br/> (" + xValue(d) +")")
                   .style("left", (d3.event.pageX + 5) + "px")
                   .style("top", (d3.event.pageY - 28) + "px");
    })
    .on("mouseout", function(d) {
              tooltip.transition()
                   .duration(500)
                   .style("opacity", 0);
          });
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
      .style("fill", function(d,i){
        //colors = cluster.length;
        return color(d);
      });

      legend.append("text")
      .attr("x", width - 24)
      .attr("y", 9)
      .attr("dy", ".35em")
      .style("text-anchor", "end")
      .text(function(d) { return d; });


      console.log("End of scatterfile");
    };