$(document).ready(function() {
    var translationsTableBody = $('#translationsTableBody');

    function addTranslationRow(country, translation) {
        var row = '<tr><td>' + country + '</td><td>' + translation + '</td></tr>';
        translationsTableBody.append(row);
    }

    for (var country in traducoesPaises) {
        if (traducoesPaises.hasOwnProperty(country)) {
            addTranslationRow(country, traducoesPaises[country]);
        }
    }

    $('#searchTranslationBtn').click(function() {
        var translationInput = $('#translationInput').val().trim().toLowerCase();
        var found = false;
        for (var country in traducoesPaises) {
            if (traducoesPaises.hasOwnProperty(country) && traducoesPaises[country].toLowerCase() === translationInput) {
                alert('Tradução encontrada: ' + country);
                found = true;
                break;
            }
        }
        if (!found) {
            alert('Nenhuma tradução encontrada para: ' + translationInput);
        }
    });
});
