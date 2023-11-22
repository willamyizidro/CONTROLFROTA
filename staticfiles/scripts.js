function cadastrar() {
    var nome = document.querySelector("input#nome");
    var usuario = document.querySelector("input#usuario");
    var email = document.querySelector("input#email");
    var senha = document.querySelector("input#senha");
    var confirmasenha = document.querySelector("input#confirmasenha");
    var mensagem = document.querySelector("div#res");

    var erros = [];

    if (nome.value === "") {
        erros.push("Nome é obrigatório.");
        nome.style.border = "3px solid red";
    } 
    else {
        nome.style.border = "1px solid #ccc";
    }

    if (usuario.value === "") {
        erros.push("Usuário é obrigatório.");
        usuario.style.border = "3px solid red";
    } 
    else {
        usuario.style.border = "1px solid #ccc";
    }

    if (email.value === "") {
        erros.push("Email é obrigatório.");
        email.style.border = "3px solid red";
    } 
    else {
        email.style.border = "1px solid #ccc";
    }

    if (senha.value.length < 8) {
        erros.push("A senha deve ter pelo menos 8 caracteres.");
        senha.style.border = "3px solid red";
    } 
    else {
        senha.style.border = "1px solid #ccc";
    }

    if (senha.value !== confirmasenha.value) {
        erros.push("As senhas não coincidem.");
        senha.style.border = "3px solid red";
        confirmasenha.style.border = "3px solid red";
    } 
    else {
        confirmasenha.style.border = "1px solid #ccc";
    }

    if (erros.length > 0) {
        mensagem.innerHTML = erros.join("<br>");
        mensagem.style.color = "red";
    } 
    else {
        mensagem.innerHTML = "Deu certo cara";
    }
}