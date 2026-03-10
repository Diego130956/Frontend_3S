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



async function get_cachorro() {
    let resultado = await fetch("https://dog.ceo/api/breeds/image/random")

    if (resultado.ok) {
        let dados = await resultado.json()
        render_cachorro(dados)
    }

}

function render_cachorro(dados) {
        let urlImg = dados.message
        const ImgCachorro = document.getElementById("img-cachorro")
        const IconCachorro = document.getElementById("icon-cachorro")

        IconCachorro.style.display = "none"
        ImgCachorro.style.display = "block"
        ImgCachorro.src = urlImg
}

async function get_raposa() {
    let resultado = await fetch("https://randomfox.ca/floof")

    if (resultado.ok) {
        let dados = await resultado.json()
        render_raposa(dados)
    }

}

function render_raposa(dados) {
        let urlImg = dados.image
        const ImgRaposa = document.getElementById("img-raposa")
        const IconRaposa = document.getElementById("icon-raposa")

        IconRaposa.style.display = "none"
        ImgRaposa.style.display = "block"
        ImgRaposa.src = urlImg
}