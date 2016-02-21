function scatter_d3(data,titles){

  //console.log(titles);
  var loop = function(d){return d;};
     
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

  var tooltip = d3.select("body").append("div")
  .attr("class", "tooltip")
  .style("opacity",0);

  var svg = d3.select("body").append("svg")
  .attr("width", width + margin.left + margin.right)
  .attr("height", height + margin.top + margin.bottom)
  .append("g")
  .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  
  x.domain(d3.extent(data, function(d,i) {return d;}));
  y.domain(d3.extent(data, function(d,i) {return d;}));

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
  .text("Rating");



  //For each element in d, each group=cluster
  //clusers

  data.forEach(function(cluster, i){
    cluster.forEach(function(d,i){
      svg.selectAll(".dot")
      .data(cluster,function(d){
        return d;
      })
      .enter().append("circle")
      .attr("class", "dot")
      .attr("r", 4)
      .attr("cx",function(d,i){
        return d[0]*(width/100);//*(width/100);
      })
      .attr("cy", function(d,i){
        return height-d[1]*45;
      })
      .style("fill", color(d) )
      .on("mouseover", function(d,k){
        console.log("MouseOver " +k);
        tooltip.transition()
        .duration(200)
        .style("opacity",1);
        tooltip.html(titles[k]+"</br>" +d )
        .style("left", (d3.event.pageX + 5) + "px")
        .style("top", (d3.event.pageY - 28) + "px")
        .attr("transform", function(d, i) { return "translate(0," + i * 20 + ")"; });
      })
      .on("mouseout", function(d) {
        tooltip.transition()
        .duration(500)
        .style("opacity", 0);
      }).on("mousedown", mousedown);
      //-------------insert legend

      //-------legend end--------
    }); // cluster for each

  }); // data forEach

  var legend = svg.selectAll(".legend")
  .data(color.domain())
  .enter().append("g")
  .attr("class", "legend")
  .attr("transform", function(d, i) { return "translate(0," + i * 20 + ")"; });

  legend.append("rect")
  .data(color)
  .attr("x", width - 18)
  .attr("width", 18)
  .attr("height", 18)
  .style("fill", function(d,i){
    //console.log(cluster);
    return color(d);
  });

  legend.append("text")
  .attr("x", width - 24)
  .attr("y", 9)
  .attr("dy", ".35em")
  .style("text-anchor", "end")
  .text(function(d) { return d; });

  function mousedown(){
    test=document.getElementById("tooltipside");
    test.innerHTML = "tooltip";
  };


};