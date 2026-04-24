
// 1. Hacemos la petición al backend en el puerto 5000
fetch('http://localhost:5000/api/team')
  .then(response => {
    // 2. Cambiamos el indicador visual dependiendo de si el backend responde
    if (response.ok) {
      document.getElementById("status").innerText = "Backend Online 🟢";
      return response.json(); // Convertimos la respuesta a JSON
    } else {
      throw new Error('El backend respondió con error');
    }
  })
  .then(data => {
    // 3. Acá entra TU lógica, iterando sobre la "data" real que llegó de la base de datos
    const tabla = document.getElementById("tabla");
    
    data.forEach(miembro => {
      const fila = `
        <tr>
          <td>${miembro.nombre}</td>
          <td>${miembro.legajo}</td>
          <td>${miembro.feature}</td>
          <td>${miembro.servicio}</td>
          <td>${miembro.estado}</td>
        </tr>
      `;
      tabla.innerHTML += fila;
    });
  })
  .catch(error => {
    // 4. Si el backend está caído, lo atrapamos y cambiamos el estado
    document.getElementById("status").innerText = "Backend Offline 🔴";
    console.error("Error al obtener los datos:", error);
  });