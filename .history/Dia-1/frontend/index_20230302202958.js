const pedirAlumnos = async () => {
    fetch('https//localhost:5000/alumnos', {method: "GET",});

    const data =await respuesta.json();

    console.log(data);
};