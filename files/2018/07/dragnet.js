const REGEX = /\{(.+)\}/;
const LABEL_DATA_ATTRIBUTE = 'data-dragnet-label';
const DRAGGABLE_CLASS = 'dragnet__label';

let detectOverlap = (function () {
    function getPositions(elem) {
        let pos = elem.getBoundingClientRect();
        return [[pos.left, pos.right], [pos.top, pos.bottom]];
    }

    function comparePositions(p1, p2) {
        let r1, r2;
        r1 = p1[0] < p2[0] ? p1 : p2;
        r2 = p1[0] < p2[0] ? p2 : p1;
        return r1[1] > r2[0] || r1[0] === r2[0];
    }

    return function (a, b) {
        let pos1 = getPositions(a),
            pos2 = getPositions(b);
        return comparePositions(pos1[0], pos2[0]) && comparePositions(pos1[1], pos2[1]);
    };
})();

var Dragnet = class {
  constructor(svg) {
    this.svg = svg;
    this.labelDataAttribute = LABEL_DATA_ATTRIBUTE;
    this.draggableClass = DRAGGABLE_CLASS;
    this.regex = REGEX;
  }

  // Public Methods
  getX(index) {
    return 500;
  }

  getY(index) {
    return 25 * (index + 1);
  }

  onIncorrect() {
    alert('Some answers wrong');
  }

  onCorrect() {
    alert('All answers are correct.');
  }

  // Private Methods, you're unlikely to have to modify these
  parseLabels() {
    this.svg.querySelectorAll('text').forEach((text, i) => {
      let match = this.regex.exec(text.textContent);
      if (!match) { return; }
      let answer = match[1];
      text.textContent = "--";
      text.setAttribute(this.labelDataAttribute, answer);
      this.svg.insertAdjacentHTML('beforeend', `<text transform="matrix(1 0 0 1 0 0)"
        class="${this.draggableClass}" x="${this.getX(i)}" y="${this.getY(i)}">${answer}</text>`);
    });

    this.setupEventListeners()
  }

  setupEventListeners() {
    this.svg.addEventListener('mousedown', this.mouseDown.bind(this));
    this.svg.addEventListener('mousemove', this.mouseMove.bind(this));
    this.svg.addEventListener('mouseup', this.mouseUp.bind(this));
  }

  mouseDown(evt) {
    if (!evt.target.classList.contains(DRAGGABLE_CLASS)) {
      return;
    }

    this.selectedElement = evt.target;
    this.currentX = evt.clientX;
    this.currentY = evt.clientY;
    this.currentMatrix = this.selectedElement.getAttributeNS(null, "transform").slice(7,-1).split(' ');

    for(let i=0; i < this.currentMatrix.length; i++) {
      this.currentMatrix[i] = parseFloat(this.currentMatrix[i]);
    }
  }

  mouseMove(evt) {
    if (!this.selectedElement) { return; }

    let dx = evt.clientX - this.currentX;
    let dy = evt.clientY - this.currentY;
    this.currentMatrix[4] += dx;
    this.currentMatrix[5] += dy;
    let newMatrix = "matrix(" + this.currentMatrix.join(' ') + ")";

    this.selectedElement.setAttributeNS(null, "transform", newMatrix);
    this.currentX = evt.clientX;
    this.currentY = evt.clientY;
  }

  mouseUp(evt) {
    if (!this.selectedElement) { return; }

    if (!this.hovered()) {
      this.resetPosition(this.selectedElement);
    }

    if (this.allMatched()) {
      if (this.allCorrect()) {
        this.onCorrect();
      } else {
        this.onIncorrect();
      }
    }

    this.selectedElement = null;
  }

  hovered() {
    let placeholders = Array.prototype.slice.call(this.svg.querySelectorAll(`[${this.labelDataAttribute}]`));

    return placeholders.some(label => detectOverlap(label, this.selectedElement));
  }

  allMatched() {
    let placeholders = Array.prototype.slice.call(this.svg.querySelectorAll(`[${this.labelDataAttribute}]`));
    let labels = Array.prototype.slice.call(this.svg.querySelectorAll(`.${this.draggableClass}`));

    return labels.every(element => {
      return placeholders.some(label => detectOverlap(label, element));
    });
  }

  allCorrect() {
    let placeholders = Array.prototype.slice.call(this.svg.querySelectorAll(`[${this.labelDataAttribute}]`));
    let labels = Array.prototype.slice.call(this.svg.querySelectorAll(`.${this.draggableClass}`));

    return labels.every(element => {
      let hoveredElement = placeholders.find(label => detectOverlap(label, element));
      return hoveredElement && element.textContent === hoveredElement.getAttribute(this.labelDataAttribute);
    });
  }

  resetPosition(target) {
    target.setAttributeNS(null, 'transform', 'matrix(1 0 0 1 0 0)');
  }
};
