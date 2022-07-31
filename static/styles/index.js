var i = 0;
var txt = "SUDOKU SOLVER";
var speed = 80;

window.onload = function typeWriter() {
    if (i < txt.length) {
        document.getElementById("title").textContent += txt.charAt(i);
        i++;
        setTimeout(typeWriter, speed);
    }
}

document.getElementById("mainButton").onclick = function () {
    location.href = "sudoku.html";
};