async function get_gato() {
    let resultado = await fetch("https://api.thecatapi.com/v1/images/search")

    if (resultado.ok) {
        let dados = await resultado.json()
        render_gato(dados)
    }

}

function render_gato(dados) {
        let urlImg = dados[0].url
        const ImgGato = document.getElementById("img-gato")
        const IconGato = document.getElementById("icon-gato")

        IconGato.style.display = "none"
        ImgGato.style.display = "block"
        ImgGato.src = urlImg
}