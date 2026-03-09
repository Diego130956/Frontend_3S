// var nome = prompt("Como você chama?")
//
// if (nome == null) {
//     alert("Recaregue a pagína")
// } else {
//
//     let correto = confirm("Você se chama" + nome + "?")
//
//     if (correto) {
//         alert(nome + " Bem-vindo ao site recursos")
//
//     } else {
//         alert("Recarregue a pagína")
//     }
//
//
// }

function LimpaInputLogin() {
    const inputEmail = document.getElementById("input-email")
    const inputSenha = document.getElementById("input-senha")

    inputSenha.value = ''
    inputEmail.value = ''
}

function LimpaInputCadastro() {
    const inputNome = document.getElementById("input-nome")
    const inputData = document.getElementById("input-data")
    const inputCpf = document.getElementById("input-cpf")
    const inputEmail = document.getElementById("input-email1")
    const inputSenha = document.getElementById("input-senha2")
    const inputCargo = document.getElementById("input-cargo")
    const inputSalario = document.getElementById("input-salario")

    inputNome.value = ''
    inputData.value = ''
    inputCpf.value = ''
    inputEmail.value = ''
    inputSenha.value = ''
    inputCargo.value = ''
    inputSalario.value = ''


}

document.addEventListener("DOMContentLoaded", function () {
    const formLogin = document.getElementById("form-login")
    formLogin.addEventListener("submit", function (event) {

        const inputEmail = document.getElementById("form-email")
        const inputSenha = document.getElementById("form-senha")

        let temErro = false

        //     Verificar se os inputs estão vazios
        if (inputEmail.value === '') {
            inputEmail.classList.add('is-invalid')
            temErro = true
        } else {
            inputEmail.classList.remove('is-invalid')

        }
        if (inputSenha.value === '') {
            inputSenha.classList.add('is-invalid')
            temErro = true
        } else {
            inputSenha.classList.remove('is-invalid')

        }

        if (temErro) {
            event.preventDefault()
            alert("Preencher todos os campos")
        }
    })




    const formCadastro = document.getElementById("form-cadastro")
    formCadastro.addEventListener("submit", function (event) {
        const inputNome = document.getElementById("input-nome")
        const inputData = document.getElementById("input-data")
        const inputCpf = document.getElementById("input-cpf")
        const inputEmail = document.getElementById("input-email")
        const inputSenha = document.getElementById("input-senha")
        const inputCargo = document.getElementById("input-cargo")
        const inputSalario = document.getElementById("input-salario")
        let temErro = false
        //     Verificar se os inputs estão vazios
        if (inputNome.value === '') {
            inputNome.classList.add('is-invalid')
            temErro = true
        } else {
            inputNome.classList.remove('is-invalid')

        }
        if (inputData.value === '') {
            inputData.classList.add('is-invalid')
            temErro = true
        } else {
            inputData.classList.remove('is-invalid')

        }
        if (inputCpf.value === '') {
            inputCpf.classList.add('is-invalid')
            temErro = true
        } else {
            inputCpf.classList.remove('is-invalid')

        }
        if (inputEmail.value === '') {
            inputEmail.classList.add('is-invalid')
            temErro = true
        } else {
            inputEmail.classList.remove('is-invalid')

        }
        if (inputSenha.value === '') {
            inputSenha.classList.add('is-invalid')
            temErro = true
        } else {
            inputEmail.classList.remove('is-invalid')

        }
        if (inputCargo.value === '') {
            inputCargo.classList.add('is-invalid')
            temErro = true
        } else {
            inputCargo.classList.remove('is-invalid')

        }
        if (inputSalario.value === '') {
            inputSalario.classList.add('is-invalid')
            temErro = true
        } else {
            inputSalario.classList.remove('is-invalid')

        }
        if (temErro) {
            event.preventDefault()
            alert("Preencher todos os campos")
        }


    })
})
