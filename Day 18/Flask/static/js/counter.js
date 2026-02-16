// Stopwatch functionality (HH:MM:SS.mmm)
let elapsedMs = 0;
let runningSince = null; // performance.now() timestamp when started
let rafId = null;

function pad2(n) {
  return String(n).padStart(2, '0');
}

function pad3(n) {
  return String(n).padStart(3, '0');
}

function formatTimeMs(totalMs) {
  const totalSeconds = Math.floor(totalMs / 1000);
  const ms = Math.floor(totalMs % 1000);

  const hours = Math.floor(totalSeconds / 3600);
  const minutes = Math.floor((totalSeconds % 3600) / 60);
  const seconds = totalSeconds % 60;

  return {
    hours,
    minutes,
    seconds,
    ms,
    text: `${pad2(hours)}:${pad2(minutes)}:${pad2(seconds)}.${pad3(ms)}`,
  };
}

function computeElapsedMs() {
  if (runningSince === null) return elapsedMs;
  return elapsedMs + (performance.now() - runningSince);
}

function render() {
  const el = document.getElementById('stopwatchValue');
  if (!el) return;

  el.textContent = formatTimeMs(computeElapsedMs()).text;

  const startBtn = document.getElementById('stopwatchStart');
  const pauseBtn = document.getElementById('stopwatchPause');

  const running = runningSince !== null;
  if (startBtn) startBtn.disabled = running;
  if (pauseBtn) pauseBtn.disabled = !running;
}

function tick() {
  render();
  if (runningSince !== null) {
    rafId = window.requestAnimationFrame(tick);
  }
}

function startStopwatch() {
  if (runningSince !== null) return;
  runningSince = performance.now();
  if (rafId === null) {
    rafId = window.requestAnimationFrame(tick);
  }
  render();
}

function pauseStopwatch() {
  if (runningSince === null) return;
  elapsedMs = computeElapsedMs();
  runningSince = null;
  if (rafId !== null) {
    window.cancelAnimationFrame(rafId);
    rafId = null;
  }
  render();
}

function resetStopwatch() {
  elapsedMs = 0;
  runningSince = null;
  if (rafId !== null) {
    window.cancelAnimationFrame(rafId);
    rafId = null;
  }
  render();
}

document.addEventListener('DOMContentLoaded', () => {
  const startBtn = document.getElementById('stopwatchStart');
  const pauseBtn = document.getElementById('stopwatchPause');
  const resetBtn = document.getElementById('stopwatchReset');

  if (startBtn) startBtn.addEventListener('click', startStopwatch);
  if (pauseBtn) pauseBtn.addEventListener('click', pauseStopwatch);
  if (resetBtn) resetBtn.addEventListener('click', resetStopwatch);

  render();
});
