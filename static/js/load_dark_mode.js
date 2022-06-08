// Load Dark Mode
function loadDarkMode() {
  var mode = localStorage.getItem("theme");
  if (mode) {
    document.documentElement.setAttribute("theme", mode);
  } else {
    localStorage.setItem("theme", "dark");
  }
}

loadDarkMode();
