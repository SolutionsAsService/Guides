/* Compass & Trail: skills-check ticks (kept in this browser only) and the bearing calculator. */
(function () {
  "use strict";
  var KEY = "compass-trail-skills";

  function load() {
    try { return JSON.parse(localStorage.getItem(KEY)) || {}; } catch (err) { return {}; }
  }
  function save(state) {
    try { localStorage.setItem(KEY, JSON.stringify(state)); } catch (err) { /* private mode: ticks last for this visit */ }
  }
  var state = load();

  function count(chapter) {
    return Object.keys(state).filter(function (k) { return state[k] && k.indexOf(chapter + "-") === 0; }).length;
  }

  function paint() {
    document.querySelectorAll("[data-check]").forEach(function (box) { box.checked = !!state[box.dataset.check]; });
    document.querySelectorAll("[data-progress]").forEach(function (el) {
      var ch = el.dataset.progress;
      var total = (document.querySelector('[data-bar="' + ch + '"]') || document.querySelector('[data-chapter="' + ch + '"]') || {}).dataset;
      total = total ? +total.total : 0;
      var n = count(ch);
      if (el.closest(".tile")) el.textContent = n ? n + " of " + total + " skills" : total + " skills";
      else if (el.closest(".meta")) el.textContent = n + " of " + total + " ticked";
      else el.textContent = n + " of " + total + " skills";
    });
    document.querySelectorAll("[data-bar]").forEach(function (bar) {
      var n = count(bar.dataset.bar);
      bar.style.width = (100 * n / +bar.dataset.total) + "%";
      bar.parentNode.hidden = !n;
    });
  }

  document.addEventListener("change", function (ev) {
    var box = ev.target.closest("[data-check]");
    if (!box) return;
    if (box.checked) state[box.dataset.check] = 1; else delete state[box.dataset.check];
    save(state);
    paint();
  });
  document.addEventListener("click", function (ev) {
    var btn = ev.target.closest("[data-reset]");
    if (!btn) return;
    Object.keys(state).forEach(function (k) { if (k.indexOf(btn.dataset.reset + "-") === 0) delete state[k]; });
    save(state);
    paint();
  });
  paint();

  /* bearing calculator: east declination is added going from magnetic to true */
  var calc = document.getElementById("calc");
  if (calc) {
    var norm = function (b) { b = b % 360; return b < 0 ? b + 360 : b; };
    var fmt = function (b) { return (Math.round(norm(b) * 10) / 10) + "°"; };
    var run = function () {
      var b = parseFloat(document.getElementById("c-bearing").value);
      var d = parseFloat(document.getElementById("c-dec").value) || 0;
      var east = document.getElementById("c-dir").value === "E";
      var fromMag = document.getElementById("c-from").value === "m";
      var out = document.getElementById("c-out");
      if (isNaN(b) || b < 0 || b > 360) { out.textContent = "Enter a bearing between 0° and 360°."; return; }
      var signed = east ? d : -d;
      var mag = fromMag ? b : b - signed;
      var tru = fromMag ? b + signed : b;
      out.textContent = (fromMag ? "Magnetic " + fmt(mag) + " is true " + fmt(tru) : "True " + fmt(tru) + " is magnetic " + fmt(mag)) +
        ". The back bearing is " + fmt(tru + 180) + " true, " + fmt(mag + 180) + " magnetic.";
    };
    calc.addEventListener("input", run);
    calc.addEventListener("submit", function (ev) { ev.preventDefault(); });
    run();
  }
})();
