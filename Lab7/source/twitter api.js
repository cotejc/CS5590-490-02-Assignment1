$('submit').click(function(){

    var search_term = {
        q:'bowery'
    };
    search(search_term);

});

function search(search_term){
    console.log('searching for ');
    console.dir(search_term);

    $.ajax({
        url : 'http//search.twitter.com/search.json?' + $.param(search_term),
        dataType: 'jsonp',
        success: function(data) {
            console.dir(data);

        }
    });
}