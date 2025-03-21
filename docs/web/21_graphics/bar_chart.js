const BAR_COLOR = '#3498db';
      
function createBarChart(home, data, width, height, margin) {
    // Create SVG drawing
    const draw = SVG().addTo(home).size(width, height);

    // Calculate chart dimensions
    const chartWidth = width - 2 * margin;
    const chartHeight = height - 2 * margin;

    // Get keys and values from the data
    const keys = Object.keys(data);
    const values = Object.values(data);

    // Calculate the maximum value for scaling
    const maxValue = Math.max(...values);

    // Calculate bar width and spacing
    const barWidth = chartWidth / keys.length * 0.8;
    const barSpacing = chartWidth / keys.length * 0.2;

    // Draw bars and labels
    keys.forEach((key, index) => {
	const barHeight = chartHeight * data[key] / maxValue;
	const x = margin + index * (barWidth + barSpacing);
	const y = height - margin - barHeight;

	// Draw bar
	draw.rect(barWidth, barHeight)
	    .move(x, y)
	    .fill(BAR_COLOR);

	// Draw label above bar
	draw.text(data[key].toFixed())
	    .move(x + barWidth / 2, y - 20)
	    .font({ size: 12, anchor: 'middle' });

	// Draw axis label
	draw.text(key)
	    .move(x + barWidth / 2, height - margin)
	    .font({ size: 12, anchor: 'start' })
	    .transform({ rotate: 45, origin: 'top left' });
    });
}
