const ctx = document.getElementById("grafica");

new Chart(ctx, {

type: "bar",

data: {

labels: ["Ingresos","Gastos"],

datasets: [{

label: "Finanzas",

data: [5000,3000],

borderWidth:1

}]

}

});