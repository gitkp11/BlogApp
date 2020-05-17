$(document).ready(function(event){
  $('#delete').click(function(){
    return confirm("Are you sure to delete this post?");
  });


  $('.reply-btn').click(function() {
    $(this).parent().parent().next('.replied-comments').fadeToggle()
  });


  $(function(){
    setTimeout(function(){
      $('.alert').slideUp(2000);
    }, 5000);
  });


  $(document).on('click', '#like', function(event){
    event.preventDefault();
    var pk = $(this).attr('value');
    $.ajax({
      type: 'POST',
      url: '{% url "like_post" %}',
      data: {'id':pk, 'csrfmiddlewaretoken': '{{ csrf_token }}'},
      dataType: 'json',
      success: function(response){
        $('#like-section').html(response['form'])
        console.log($('#like-section').html(response['form']));
      },
      error: function(rs, e){
        console.log(rs.responseText);
      },
    });
  });


  $(document).on('submit', '.comment-form', function(event){
    event.preventDefault();
    console.log($(this).serialize());
    $.ajax({
      type: 'POST',
      url: $(this).attr('action'),
      data: $(this).serialize(),
      dataType: 'json',
      success: function(response) {
        $('.main-comment-section').html(response['form']);
        $('textarea').val('');
        $('.reply-btn').click(function() {
          $(this).parent().parent().next('.replied-comments').fadeToggle();
          $('textarea').val('');
        });
      },
      error: function(rs, e) {
        console.log(rs.responseText);
      },
    });
  });


  $(document).on('submit', '.reply-form', function(event){
    event.preventDefault();
    console.log($(this).serialize());
    $.ajax({
      type: 'POST',
      url: $(this).attr('action'),
      data: $(this).serialize(),
      dataType: 'json',
      success: function(response) {
        $('.main-comment-section').html(response['form']);
        $('textarea').val('');
        $('.reply-btn').click(function() {
          $(this).parent().parent().next('.replied-comments').fadeToggle();
          $('textarea').val('');
        });
      },
      error: function(rs, e) {
        console.log(rs.responseText);
      },
    });
  });
});