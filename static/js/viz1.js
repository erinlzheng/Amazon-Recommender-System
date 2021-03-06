class Viz1 {
    /**
     * Construct function
     * Initialize chart
     */
    constructor() {
        this.svg1 = d3.select("#svg1");
        this.w1 = this.svg1._groups[0][0].clientWidth;
        this.h1 = this.svg1._groups[0][0].clientHeight;
    }

    initAvgRating() {
        d3.json("http://127.0.0.1:5000/get_top20_avg_rating").then(data => {
            this.drawAvgRatingChart(data, this.svg1, this.w1, this.h1);
        });
    }


    /**
     * Parameter
     * @param {*} data 
     * @param {*} svg 
     * @param {*} width 
     * @param {*} height 
     */
    drawAvgRatingChart(data, svg, width, height) {
        // Parameter
        let margin = {
            left: 50,
            right: 20,
            top: 5,
            bottom: 30
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
        let yRating = d3.scaleLinear()
            .domain([0, d3.max(data, d => d.avgRating)]).nice()
            .range([height - margin.bottom, margin.top]);
        // Create Axis
        let xAxis = g => g
            .attr("transform", `translate(0,${height - margin.bottom})`)
            .call(d3.axisBottom(x).tickSizeOuter(0));
        let yAxis = g => g
            .attr("transform", `translate(${margin.left},0)`)
            .call(d3.axisLeft(yRating))
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
            .attr("transform", `translate(${margin.left - 35}, ${height / 2.0})rotate(-90)`)
            .append("text")
            .text("Avg Rating")
            .style("direction", "rtl")
            .style("text-anchor", "middle")
            .style("fill", "#000")
            .style("font-size", "12px")
            // .style("font-weight", "bold")
            .style("font-family", "Arial, Helvetica, sans-serif")
            ;
        // Create Rectangle
        const ratingBar = svg.append("g")
            .attr("fill", "#3ca4c4")
            .selectAll("rect")
            .data(data)
            .join("rect")
            .style("mix-blend-mode", "multiply")
            .attr("x", d => x(d.name))
            .attr("y", d => yRating(d.avgRating))
            .attr("rx", 10)
            .attr("ry", 10)
            .attr("height", d => yRating(0) - yRating(d.avgRating))
            .attr("width", x.bandwidth())
            .on("mousemove", (e, d) => {
                let offsetX = e.pageX;
                let offsetY = e.pageY;
                let html = `
                <div style="text-align:left">
                    <label>Asin:${d.asin}</label>
                    <br />
                    <label>Avg Rating:${d.avgRating}</label>
                </div>
                `
                this.showTooltip(offsetX + 10, offsetY + 10, html);
            })
            .on("mouseout", () => {
                this.closeTooltip();
            })
            ;;
        // Create text for product ID
        svg.append("g")
            .selectAll(".asin-text")
            .data(data)
            .join("g")
            .attr('transform', d => `translate(${x(d.name) + x.bandwidth() / 2.0 + 4}, ${yRating(0) - 10})rotate(-90)`)
            .append("text")
            .text(d => d.asin)
            .style("direction", "rtl")
            .style("text-anchor", "end")
            .style("transform", "rotate(90)")
            .style("fill", "#fff")
            .style("font-size", "14px")
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


const viz1 = new Viz1();
viz1.initAvgRating();