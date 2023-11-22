$(document).ready(function () {
    // Inicialize o campo "veiculo" como um Select2 com pesquisa remota.
    $('#id_veiculo').select2({
        placeholder: 'Selecione um veículo',
        ajax: {
            url: 'busca_veiculos',
            dataType: 'json',
            delay: 250,
            data: function (params) {
                return {
                    q: params.term, // O termo de pesquisa do usuário
                };
            },
            processResults: function (data) {
                return {
                    results: data,
                };
            },
        },
    });
});