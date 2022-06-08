// Dark Mode
const checkbox = document.querySelector("input[type=checkbox]");

if (localStorage.getItem("theme") === "dark") {
  checkbox.checked = true;
}

// Save Dark Mode
const saveDarkMode = (mode) => {
  localStorage.setItem("theme", mode);
}

// Reset Dark Mode
const resetDarkMode = () => {
  localStorage.setItem("theme","dark");
}

checkbox.addEventListener("change", function () {
  if (this.checked) {
    saveDarkMode("dark");
  } else {
    saveDarkMode("light");
  }

  loadDarkMode();
});
