$(document).ready(function() {

    var deleteBtn = $('.delete-btn');
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');

    $(searchBtn).on('click', function() {
        searchForm.submit();
    });
});