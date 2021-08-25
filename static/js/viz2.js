class Viz2 {
    /**
     * Construct function
     * Initialize chart
     */
    constructor() {
        this.svg1 = d3.select("#svg1");
        this.w1 = this.svg1._groups[0][0].clientWidth;
        this.h1 = this.svg1._groups[0][0].clientHeight;
    }

    initRated() {
        d3.json("http://127.0.0.1:5000/get_top20_rated").then(data => {
            this.drawMostRatedChart(data, this.svg1, this.w1, this.h1);
        });
    }

    drawMostRatedChart(data, svg, width, height) {
        // Params
        let margin = {
            left: 60,
            right: 20,
            top: 5,
            bottom: 50
        }
        // Format the data
        data = data.map((d, i) => {
            let asin = d["asin"];
            let avgRating = d3.mean(d["rating"]);
            let times = d['rating'].length;
            let name = "No." + (i + 1);
            return {
                name,
                asin,
                avgRating,
                times
            }
        });
        // Create a scale for x coordinates
        let x = d3.scaleBand()
            .domain(data.map(d => d.name))
            .range([margin.left, width - margin.right])
            .padding(0.15);
        // Create a scale for y coordinates
        let y = d3.scaleLinear()
            .domain([0, d3.max(data, d => d.times)]).nice()
            .range([height - margin.bottom, margin.top]);
        // Create Axis
        let xAxis = g => g
            .attr("transform", `translate(0,${height - margin.bottom})`)
            .call(d3.axisBottom(x).tickSizeOuter(0));
        let yAxis = g => g
            .attr("transform", `translate(${margin.left},0)`)
            .call(d3.axisLeft(y))
            .call(g => g.selectAll(".domain").remove());
        const gx = svg.append("g")
            .call(xAxis);
        const gy = svg.append("g")
            .call(yAxis);
        // Create Text 
        svg.selectAll(".domain").remove();
        gx.selectAll("text")
            .style("font-size", "14px")
            .style("font-weight", "bold")
            .style("font-family", "Arial, Helvetica, sans-serif");
        gy.selectAll("text")
            .style("font-size", "12px")
            // .style("font-weight", "bold")
            .style("font-family", "Arial, Helvetica, sans-serif");
        svg.append("g")
            .attr("transform", `translate(${margin.left - 45}, ${height / 2.0})rotate(-90)`)
            .append("text")
            .text("Rated Times")
            .style("direction", "rtl")
            .style("text-anchor", "middle")
            .style("fill", "#000")
            .style("font-size", "12px")
            // .style("font-weight", "bold")
            .style("font-family", "Arial, Helvetica, sans-serif")
            ;
        // Create Line
        svg.append("g")
            .append("path")
            .datum(data)
            .attr("fill", "none")
            .attr("stroke", "#3ca4c4")
            .attr("stroke-width", 1.5)
            .attr("d", d3.line()
                .x(function (d, i) { return x(d.name) + x.bandwidth() / 2.0 })
                .y(function (d) { return y(d.times) })
            );
        svg.append("g")
            .selectAll("circle")
            .data(data)
            .join("circle")
            .attr("cx", d => x(d.name) + x.bandwidth() / 2.0)
            .attr("cy", d => y(d.times))
            .attr("r", 5)
            .attr("fill", "#ccc")
            .attr("stroke", "#3ca4c4")
            .attr("stroke-width", 1.5)
            .on("mousemove", (e, d) => {
                let offsetX = e.pageX;
                let offsetY = e.pageY;
                let html = `
                <div style="text-align:left">
                    <label>Asin:${d.asin}</label>
                    <br />
                    <label>Rated Times:${d.times}</label>
                </div>
                `
                this.showTooltip(offsetX + 10, offsetY + 10, html);
            })
            .on("mouseout", () => {
                this.closeTooltip();
            })
            ;
        ;

        // Create text for product ID
        svg.append("g")
            .selectAll(".asin-text")
            .data(data)
            .join("g")
            .attr('transform', d => `translate(${x(d.name) + x.bandwidth() / 2.0 + 4}, ${y(0) - 10})rotate(-90)`)
            .append("text")
            .text(d => d.asin)
            .style("direction", "rtl")
            .style("text-anchor", "end")
            .style("transform", "rotate(90)")
            .style("fill", "#000")
            .style("font-size", "10px")
            .style("font-weight", "bold")
            .style("font-family", "Arial, Helvetica, sans-serif");
        ;

    }

    showTooltip(x, y, html) {
        d3.select("#tooltip").html(html)
            .style("left", x + "px")
            .style("top", y + "px")
            .style("opacity", 0.95)
            .style("display", "")
            ;
    }

    /**
     * Close Tooltip
     */
    closeTooltip() {
        d3.select("#tooltip").style("display", "none");
    }
};


const viz2 = new Viz2();
viz2.initRated();