function params(set){
    var imdb = {ya: "Rating",xa: "Rating Count",grouplabel:function(d,i){i+=1;return "Cluster " + ' '+ i;},r:2 ,sumCX:function(d){return d*450/100},sumCY:function(d){return 450-d*4.5}};
    var actor = {ya: "Average Rating",xa: "Number of Movies",grouplabel:function(d,i){i+=1;return "Cluster " + ' '+ i;}, r:2 ,sumCX:function(d){return d*450/100}, sumCY:function(d){return 450-d*4.5}};
    var iris = {ya: "Sepal Length", xa: "Sepal Width", grouplabel:"Species ", r:2,sumCX:function(d){return d*450/10}, sumCY:function(d){return 450-d*45}};
    var blob = {ya: "Y", xa: "X", grouplabel:function(d,i){i+=1;return "Cluster " + ' '+ i;}, r:2,sumCX:function(d){return d*450/10}, sumCY:function(d){return d*10+450}};
    var ring = {ya: "Y", xa: "X", grouplabel:"Group ", r:2,sumCX:function(d){return d*450/1.2*1}, sumCY:function(d){return d*100+450/2}};

    console.log("from parmas");
    console.log(set);
    if (set==="ratings"){
      axes=imdb;
    }else if(set==="actors"){
      axes=actor;
    }else if(set==="iris"){
      axes=iris;
    }else if(set==="blobs"){
      axes=blob;
    }else if(set==="rings"){
      axes=ring;
    }else if(set==="crescents"){
      axes=ring;
    }
    console.log(axes);
    return axes;
};

