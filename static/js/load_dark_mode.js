// Load Dark Mode
function loadDarkMode() {
  var mode = localStorage.getItem("theme");
  if (mode) {
    document.documentElement.setAttribute("theme", mode);
  }

  console.log(mode);
}

loadDarkMode();
