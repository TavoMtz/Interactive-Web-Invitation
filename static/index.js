/* Usamos '/static/' para apuntar a tu carpeta */
particlesJS.load('particles-js', '/static/particles.json', function() {
  console.log('¡Partículas de Hyrule cargadas!');
});

function abrirModal(tipo) {
    document.getElementById('modal-container').style.display = 'flex';
    // Escondemos todos los contenidos
    document.getElementById('modal-mapa').style.display = 'none';
    document.getElementById('modal-rsvp').style.display = 'none';
    document.getElementById('modal-regalos').style.display = 'none';
    
    // Mostramos el que corresponde
    document.getElementById('modal-' + tipo).style.display = 'block';
}

function cerrarModal() {
    document.getElementById('modal-container').style.display = 'none';
}
function toggleMusica() {
    var audio = document.getElementById("musica-zelda");
    var boton = document.getElementById("btn-musica");
    
    if (audio.paused) {
        audio.play();
        boton.innerHTML = "⏸️ Pausar Música";
    } else {
        audio.pause();
        boton.innerHTML = "🎵 Reproducir Música";
    }
}
