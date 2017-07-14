/**
 * Created by Jeremiah on 7/10/2017.
 */
function search(){
    $('#results').html('');
    $('#buttons').html('');

    q = $('#query').val();

    $.get(
        "https://www.googleapis.com/youtube/v3/search",{
            part: 'snippet, id',
            q: q,
            type:'video',
            key: 'AIzaSyBakU9BMsO_6CQsiJ9Lv1p3HkBOyUBJJa4'},
            function(data){
                var nextPageToken = data.nextPageToken;
                var prevPageToken = data.prevPageToken;

                console.log(data);

                $.each(data.items, function(i, item) {
                    var output = getOutput(item);

                  $('#results').append(output);
                })

        }
    );
return output;
}

function getOutput(item){
    var videoId = item.id.videoId;
    var title = item.snippet.title;
    var description = item.snippet.description;
    var thumb = item.snippet.thumbnails.high.url;
    var channelTitle = item.snippet.channelTitle;
    var videoDate = item.snippet.publishedAt;

    var output = '<li>'; +
        '<div class="list-left">'+
        '<img src="'+thumb+'">'+
        '</div>'+
        '</div class="list-right">' +
        '<h3>'+title+'</h3>'
        '<small>By<span class ="ctitle">'+channelTitle+'</span>on '+videoDate+'</small>' +
        '<p>'+description+'</p>'+
        '</div>'+
        '</li>'+
        '<div class = "clearfix"></div>'+
        '';

    return output;
}