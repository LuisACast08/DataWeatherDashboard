//Se conecta con las ruta /tableData por dafault
fetch("http://localhost:8000/tableData")
    .then(response => response.text())
    .then(html => {
        document.getElementById("tableD").innerHTML = html;
    })
    .catch(error => {
        console.error("Error, no se ha conectado con el servidor", error)
    })

//fetch dinámico
function getData(endpoint){
    fetch("http://localhost:8000" + endpoint)
    .then(response => response.text())
    .then(html => {
        document.getElementById("tableD").innerHTML = html;
    })
    .catch(error => {
        console.error("Error, no se ha conectado con el servidor", error)
    })
}