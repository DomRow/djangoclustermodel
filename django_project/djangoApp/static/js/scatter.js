function scatter_d3(data,set){
  
  //Margin properties to buffer d3 visualisation   
  var margin = {top: 20, right: 90, bottom: 30, left: 40},
  width = 960 - margin.left - margin.right,
  height = 500 - margin.top - margin.bottom;

  //x,y is a discrete linear range from x to width/height
  console.log(d3.max(data));
  var x = d3.scale.linear()
  .domain([1,d3.max(data)])
  .range([0, width]);
  var y = d3.scale.linear()
  .domain([1,10])
  .range([height, 0]);

  var color = d3.scale.category20();

  var xAxis = d3.svg.axis()
  .scale(x)
  .orient("bottom");

  var yAxis = d3.svg.axis()
  .scale(y)
  .orient("left");

  var imdb = {ya: "Rating",xa: "Rating Count",grouplabel:"Cluster ", sumCX:function(d){return d*width/100}, sumCY:function(d){return height-d*45}};
  var iris = {ya: "Sepal Length", xa: "Sepal Width", grouplabel:"Species ",sumCX:function(d){return d*width/10}, sumCY:function(d){return height-d*45}};

  if (set==="ratings"){
    console.log("rate");
    axes=imdb;
  }else if(set=="iris"){
    console.log("flowders");
    axes=iris;
  };

  var tooltip = d3.select("body").append("div")
  .attr("class", "tooltip")
  .style("opacity",0);

  var svg = d3.select("body").append("svg")
  .attr("width", width + margin.left + margin.right)
  .attr("height", height + margin.top + margin.bottom)
  .append("g")
  .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  
  //x
 //y.domain(d3.extent(data, function(d,i) {return d;}));
  

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
  .text(axes.xa);

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
  .text(axes.ya);



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
        return axes.sumCX(d[0]);
      })
      .attr("cy", function(d,i){
        return axes.sumCY(d[1]);
      })
      .style("fill", color(d) )
      .on("mouseover", function(d,k){
        console.log("MouseOver " +k);
        tooltip.transition()
        .duration(200)
        .style("opacity",1);
        tooltip.html("Title: </br>Director: </br>" +d  )
        .style("left", (d3.event.pageX + 12) + "px")
        .style("top", (d3.event.pageY - 28) + "px")
        .attr("transform", function(d, i) { return "translate(0," + i * 20 + ")"; });
      })
      .on("mouseout", function(d) {
        tooltip.transition()
        .duration(500)
        .style("opacity", 0);
      })//.on("mousedown", mousedown);    
    }); // cluster for each

  }); // data forEach

  var legend = svg.selectAll(".legend")
  .data(data, function(d,i){return i;})
  .enter().append("g")
  .attr("class", "legend")
  .attr("transform", function(d, i) { return "translate(40," + i * 20 + ")"; });

  legend.append("rect")
  .data(data,function(d){return d;})
  .attr("x", width - 18)
  .attr("width", 18)
  .attr("height", 18)
  .style("fill", function(d,i){
    return color(i);
  });

  legend.append("text")
  .attr("x", width+25)
  .attr("y", 9)
  .attr("dy", ".35em")
  .style("text-anchor", "middle")
  .text(axes.grouplabel,function(d,i) {
       return i; 
  });

  // function mousedown(){
  //   test=document.getElementById("tooltipside");
  //   test.innerHTML = ("tooltip");
  // };


};