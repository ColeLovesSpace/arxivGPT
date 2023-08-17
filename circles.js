let circles = [];
const circleRadiusFactor = 0.5;
const referenceData = {};

function setup() {
  createCanvas(800, 600);
  noStroke();
  fill(100, 150, 200);

  const resultsDiv = document.getElementById("results");
  const references = extractReferences(resultsDiv.innerText);

  for (const [reference, count] of Object.entries(references)) {
    referenceData[reference] = { count, radius: sqrt(count) * circleRadiusFactor };
    circles.push(new Circle(reference, referenceData[reference].radius));
  }
}

function draw() {
  background(240);

  for (let i = 0; i < circles.length; i++) {
    circles[i].update();
    circles[i].display();

    for (let j = i + 1; j < circles.length; j++) {
      circles[i].collide(circles[j]);
    }
  }
}

class Circle {
  constructor(reference, radius) {
    this.x = random(width);
    this.y = random(height);
    this.vx = random(-1, 1);
    this.vy = random(-1, 1);
    this.radius = radius;
    this.reference = reference;
  }

  update() {
    this.x += this.vx;
    this.y += this.vy;

    if (this.x + this.radius > width || this.x - this.radius < 0) {
      this.vx *= -1;
    }

    if (this.y + this.radius > height || this.y - this.radius < 0) {
      this.vy *= -1;
    }
  }

  display() {
    ellipse(this.x, this.y, this.radius * 2);
    fill(0);
    text(this.reference, this.x - this.radius, this.y - this.radius - 10);
  }

  collide(other) {
    const dx = other.x - this.x;
    const dy = other.y - this.y;
    const distance = sqrt(dx * dx + dy * dy);
    const minDist = this.radius + other.radius;

    if (distance < minDist) {
      const angle = atan2(dy, dx);
      const targetX = this.x + cos(angle) * minDist;
      const targetY = this.y + sin(angle) * minDist;

      this.vx = (targetX - other.x) * 0.05;
      this.vy = (targetY - other.y) * 0.05;
      other.vx = (this.x - targetX) * 0.05;
      other.vy = (this.y - targetY) * 0.05;
    }
  }
}
