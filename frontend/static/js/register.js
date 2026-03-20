document.getElementById("registerForm").addEventListener("submit", function(e) {

    e.preventDefault();

    const data = {
        primernombre: document.getElementById("primernombre").value,
        segundonombre: document.getElementById("segundonombre").value,
        primerapellido: document.getElementById("primerapellido").value,
        segundoapellido: document.getElementById("segundoapellido").value,
        correo: document.getElementById("correo").value,
        password: document.getElementById("password").value,
        estado: document.getElementById("estado").value,
        rol_id_rol: document.getElementById("rol").value
    };

    fetch("http://127.0.0.1:5000/register", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("mensaje").innerText = data.message;
    });

});