window.onLoad = init()

function init(){
    Highcharts.chart('containerChart', {
    data: {
        table: 'dtLibrosPorCarrera'
    },
    chart: {
        type: 'line'
    },
    title: {
        text: 'Cantidad de libros prestados por carrera'
    },
    yAxis: {
        allowDecimals: false,
        title: {
            text: 'Cantidad'
        }
    },
    tooltip: {
        formatter: function () {
            return '<b>' + this.series.name + '</b><br/>' +
                this.point.y + ' ' + this.point.name.toLowerCase();
            }
        }
    });

    Highcharts.chart('containerChartBooks', {
    data: {
        table: 'dtLibros'
    },
    chart: {
        type: 'column'
    },
    title: {
        text: '5 Libros con mayor demanda'
    },
    yAxis: {
        allowDecimals: false,
        title: {
            text: 'Cantidad de libros prestados'
        }
    },
    tooltip: {
        formatter: function () {
            return '<b>' + this.series.name + '</b><br/>' +
                this.point.y + ' ' + this.point.name.toLowerCase();
            }
        }
    });

    Highcharts.chart('containerChartAlumnos', {
    data: {
        table: 'dtAlumnos'
    },
    chart: {
        type: 'column'
    },
    title: {
        text: 'Alumnos que mas utilizan la plataforma'
    },
    yAxis: {
        allowDecimals: false,
        title: {
            text: 'Cantidad de libros prestados'
        }
    },
    tooltip: {
        formatter: function () {
            return '<b>' + this.series.name + '</b><br/>' +
                this.point.y + ' ' + this.point.name.toLowerCase();
            }
        }
    });
}
