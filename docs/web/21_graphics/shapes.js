// Create an SVG drawing
const drawing = SVG().addTo('#drawing').size(300, 200);

// Create a square
drawing.rect(50, 50).move(10, 10).fill('#1e90ff');

// Create a circle
drawing.circle(50).move(100, 10).fill('#ff6347');

// Create a line
drawing.line(10, 100, 290, 100).stroke({ width: 2, color: '#2ecc71' });

// Add text
drawing.text('example').move(120, 150).font({ size: 24, family: 'Arial' });
