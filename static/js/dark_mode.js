// Dark Mode
const checkbox = document.querySelector("input[type=checkbox]");

if (localStorage.getItem("theme") === "dark") {
  checkbox.checked = true;
}

// Save Dark Mode
function saveDarkMode(mode) {
  localStorage.setItem("theme", mode);
}

checkbox.addEventListener("change", function () {
  if (this.checked) {
    saveDarkMode("dark");
  } else {
    saveDarkMode("ligth");
  }

  loadDarkMode();
});
