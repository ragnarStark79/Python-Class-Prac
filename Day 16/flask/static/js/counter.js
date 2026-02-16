// Counter functionality
let counter = 0;

function updateCounter() {
  document.getElementById('counterValue').textContent = counter;
}

function increment() {
  counter++;
  updateCounter();
}

function decrement() {
  counter--;
  updateCounter();
}

function reset() {
  counter = 0;
  updateCounter();
}

// Initialize counter on page load
document.addEventListener('DOMContentLoaded', function() {
  updateCounter();
});
