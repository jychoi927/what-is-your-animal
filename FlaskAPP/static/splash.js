var tabBarElement = document.getElementById("custom-overlay");
var splash = true;

    
function ViewLoad() {
    tabBarElement.style.display = 'flex';
    setTimeout(() => {
      splash = false;
      tabBarElement.style.display = 'none';
    }, 2000);
  }  

ViewLoad();