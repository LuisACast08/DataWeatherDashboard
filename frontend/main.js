//Se conecta con las rutas del backend
fetch("http://localhost:8000/tableData")
    .then(response => response.text())
    .then(html => {
        document.getElementById("tableD").innerHTML = html;
    })
    .catch(error => {
        console.error("Error, no se ha conectado con el servidor", error)
    })