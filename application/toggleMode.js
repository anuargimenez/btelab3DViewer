function toggleMode() {
    var body = document.getElementsByTagName("body")[0];
    var button = document.getElementById("toggleModeButton");
    
    if (body.classList.contains("dark-mode")) {
      body.classList.remove("dark-mode");
      button.textContent = "Dark Mode";
    } else {
      body.classList.add("dark-mode");
      button.textContent = "Light Mode";
    }
  }
  