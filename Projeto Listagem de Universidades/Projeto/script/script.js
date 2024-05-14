$(document).ready(function() {
    $('#searchBtn').click(function() {
        var countryInput = $('#countryInput').val().trim().toLowerCase();
        var url = 'http://universities.hipolabs.com/search?country=' + countryInput;

        $.ajax({
            url: url,
            type: 'GET',
            success: function(data) {
                if (data.length === 0) {
                    $('#universitiesList').html('<p>Nenhuma universidade encontrada para o país especificado.</p>');
                } else {
                    displayResults(data);
                    $('html, body').animate({ scrollTop: 0 }, 'slow');
                }
            },
            error: function(xhr, status, error) {
                console.error('Erro ao buscar universidades:', error);
            }
        });
    });

    function displayResults(universities) {
        var universitiesList = $('#universitiesList');
        universitiesList.empty();

        var table = '<table class="table"><thead><tr><th>Nome</th><th>Website</th></tr></thead><tbody>';
        universities.forEach(function(university) {
            var website = Array.isArray(university.web_pages) ? university.web_pages[0] : university.web_pages;
            table += '<tr><td>' + university.name + '</td><td><a href="' + website + '">' + website + '</a></td></tr>';
        });
        table += '</tbody></table>';
        universitiesList.append(table);
    }
});
