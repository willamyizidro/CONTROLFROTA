function editarMotorista() {
    var select = document.getElementById("SelecionarMotorista");
    var selectedId = select.options[select.selectedIndex].value;
    if (selectedId) {
        window.location.href = `/editarMotorista/${selectedId}`;
    }
}

function editarVeiculo() {
    var select = document.getElementById("SelecionarPlaca");
    var selectedId = select.options[select.selectedIndex].value;
    if (selectedId) {
        window.location.href = `/editarVeiculo/${selectedId}`;
    }
}

function relatorioVeiculo() {
    var select = document.getElementById("SelecionarPlaca");
    var selectedId = select.options[select.selectedIndex].value;
    
    if (selectedId) {
        var xhr = new XMLHttpRequest();
        xhr.open('GET', `/relatorio_veiculo/${selectedId}`, true);
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                // Atualiza o conteúdo da div com o relatório
                document.getElementById("relatorioContainer").innerHTML = xhr.responseText;
            }
        };
        xhr.send();
    }
}

function abrirRelatorio() {
    var select = document.getElementById("SelecionarPlaca");
    var selectedId = select.options[select.selectedIndex].value;
    if (selectedId) {
        var url = `/relatorio_veiculo/${selectedId}`;
        
        // Abre a URL em uma nova aba
        window.open(url, '_blank');
    }
}

function abrirRelatorioGeral() {
    var select = document.getElementById("SelecionarPlaca");
    var selectedId = select.options[select.selectedIndex].value;
    if (selectedId) {
        var url = `/relatorio_geral_veiculo/${selectedId}`;
        
        // Abre a URL em uma nova aba
        window.open(url, '_blank');
    }
}



function editarManutencao() {
    var select = document.getElementById("SelecionarManutencao");
    var selectedId = select.options[select.selectedIndex].value;
    if (selectedId) {
        window.location.href = `/editarTipoManutencao/${selectedId}`;
    }
}