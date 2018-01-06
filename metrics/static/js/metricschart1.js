Chart.defaults.global.legend.display = false;

var ctx = document.getElementById("metricschart").getContext('2d');

var metricChart = new Chart(ctx, {
	type: 'line',
	data: {
		labels: labelData,
		datasets: [{
			borderWidth: 2,
			data: chartData,
			backgroundColor: rgba(100, 100, 100, 1),
			borderColor: rgba(100,100,100),
		}]
	},
	options: {
		responsive: true,
		maintainAspectRatio: false,
		elements: {
			point: {
				radius: 0,
			}
		},
		scales: {
			xAxes: [{
				ticks: {
					autoSkip: true,
					maxTicksLimit: 7,
				}
			}],
			yAxes: [{
				ticks: {
					autoSkip: true,
					maxTicksLimit: 5,
				}
			}],
		}
	}
});