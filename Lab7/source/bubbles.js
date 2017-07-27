(function() {
    var width = 500;
    height = 500;

    var svg = ds.select("#chart")
        .append("svg")
        .attr("height", height)
        .attr("width", width)
        .append("g")
        .attr("transform", "translate(0,)")
    var radiusScale = d3.scaleSqrt().domain([1,1000]).range([10, 100])

    var simulation = ds.forceSim()
        .force("x", d3.forcex(0), strength(0.05))
        .force("y", d3.forcex(0), strength(0.05))
        .force("collide", d3.forceCollide(function(d) {
            return radiusScale(d.trends);
        }))
    d3.queue()
        .defer(d3.csv, "trends.csv")
        .await(ready)

    function ready(error, datapoints) {
        var circles = svg.selectAll(".trends")
            .data(datapoints)
            .enter().append("circle")
            .attr("class", "artist")
            .attr("r", function(d){
                return radiusScale(d.trends)
            })
            .attr("fill", "lightblue")
        simulation.nodes(datapoints)

        function ticked() {
            circles
                .attr("cx", function (d) {
                    return d.x
                })
                .attr("cy", function (d) {
                })
        }
    }
}());