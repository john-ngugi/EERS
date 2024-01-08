const url1 = "/ResponseApp/getChartData/";
let chartData = []
fetch(url1)
    .then(response => response.json())
    .then(data => {
        console.log(data)

        chartData = [data.total_medical, data.total_crime, data.total_fire]
            // Get the HTML canvas element with the ID 'myChart'
        const ctx = document.getElementById('myChart');

        // Create a new Doughnut chart using Chart.js
        new Chart(ctx, {
            type: 'doughnut', // Specifies the chart type as 'doughnut'

            // Data configuration for the chart
            data: {
                labels: [
                    'medical',
                    'police',
                    'fire'
                ], // Labels for each segment of the chart
                datasets: [{
                    label: 'Total', // Dataset label
                    data: chartData, //Data values for each segment
                    backgroundColor: [
                        'rgb(255, 99, 132)', // Background color for the 'Red' segment
                        'rgb(54, 162, 235)', // Background color for the 'Blue' segment
                        'rgb(255, 205, 86)' // Background color for the 'Yellow' segment
                    ],
                    hoverOffset: 4 // Offset when hovering over chart segments
                }]
            },
            options: {
                maintainAspectRatio: true, // Maintain the aspect ratio of the chart
                cutout: 190, // Specify the cutout radius for the doughnut hole in the center
            }
        });


        const ctx1 = document.getElementById('ongoinglocation');

        // Create a new Doughnut chart using Chart.js
        new Chart(ctx1, {
            type: 'doughnut', // Specifies the chart type as 'doughnut'

            // Data configuration for the chart
            data: {
                labels: [
                    'Red',
                    'Blue',
                    'Yellow'
                ], // Labels for each segment of the chart
                datasets: [{
                    label: 'My First Dataset', // Dataset label
                    data: [300, 50, 100], //Data values for each segment
                    backgroundColor: [
                        'rgb(255, 99, 132)', // Background color for the 'Red' segment
                        'rgb(54, 162, 235)', // Background color for the 'Blue' segment
                        'rgb(255, 205, 86)' // Background color for the 'Yellow' segment
                    ],
                    hoverOffset: 4 // Offset when hovering over chart segments
                }]
            },
            options: {
                maintainAspectRatio: true, // Maintain the aspect ratio of the chart
                cutout: 190, // Specify the cutout radius for the doughnut hole in the center
            }
        });

    })