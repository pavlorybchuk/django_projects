"use strict";

document.addEventListener("DOMContentLoaded", function () {
  const showNamesBtn = document.getElementById("show-names");
  const namesDiv = document.querySelector(".names");

  showNamesBtn.addEventListener("click", () => {
    namesDiv.classList.toggle("hidden");
    if (namesDiv.classList.contains("hidden")) {
      showNamesBtn.textContent = "Show names";
    } else {
      showNamesBtn.textContent = "Hide names";
    }
  });
  const counts = [
    parseInt(diagram.dataset.count_1),
    parseInt(diagram.dataset.count_2),
    parseInt(diagram.dataset.count_3),
    parseInt(diagram.dataset.count_4),
    parseInt(diagram.dataset.count_5),
  ];

  const ctx = document.querySelector("#diagram").getContext("2d");

  const myChart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: ["1", "2", "3", "4", "5"],
      datasets: [
        {
          data: counts,
          backgroundColor: [
            "rgba(255, 99, 132, 0.2)",
            "rgba(54, 162, 235, 0.2)",
            "rgba(255, 206, 86, 0.2)",
            "rgba(75, 192, 192, 0.2)",
            "rgba(153, 102, 255, 0.2)",
            "rgba(255, 159, 64, 0.2)",
          ],
          borderColor: [
            "rgba(255, 99, 132, 1)",
            "rgba(54, 162, 235, 1)",
            "rgba(255, 206, 86, 1)",
            "rgba(75, 192, 192, 1)",
            "rgba(153, 102, 255, 1)",
            "rgba(255, 159, 64, 1)",
          ],
          borderWidth: 1,
        },
      ],
    },
    options: {
      plugins: {
        legend: {
          display: false,
        },
        tooltip: {
          enabled: true,
        },
      },
      scales: {
        y: {
          beginAtZero: true,
          ticks: { stepSize: 1 },
          title: {
            display: true,
            text: "Count",
            font: { size: 14, weight: "bold" },
          },
        },
        x: {
          title: {
            display: true,
            text: "Rate", // 🔹 підпис осі X
            font: { size: 14, weight: "bold" },
          },
          ticks: { font: { size: 14 } },
        },
      },
    },
  });
});
