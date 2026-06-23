const scoreinput = document.getElementById("scoreinput");
const calc = document.getElementById("calcBtn");
const result = document.getElementById("results");

calc.addEventListener("click", function(){
    let score = Number(scoreinput.value);
    if (scoreinput.value === "" || isNaN(score) || score < 0 || score > 100) {
        result.innerHTML = "<p style='color:red'>Error : Please enter a valid number between 0 and 100 </p>";
        return;
    }

    let grade ="";
    let color ="";
    let description ="";

    if (score >= 70){
        grade = "A";
        color = "green";
        description = "EXCELLENT";
    }
    else if (score >= 60){
        grade = "B";
        color = "blue";
        description = "VERY GOOD";
    }
    else if (score >= 50){
        grade = "C";
        color = "orange";
        description = "GOOD";
    }
     else if (score >= 40){
        grade = "D";
        color = "brown";
        description = "PASS";
    }
    else{
        grade = "F";
        color = "red";
        description = "FAIL";
    }
    result.innerHTML = `<h3 style="color:${color};">RESULT</h3>
  <p>Score: ${score}</p>
  <p>Grade: ${grade}</p>
  <p>Description: ${description}</p>`;

  scoreinput.value ="";
  scoreinput.focus();
});