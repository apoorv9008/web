$(document).ready(function() {
  $(document).on('click', '#tabs a', function(e) {
    e.preventDefault();
    let target = $(this).data('href');

    $('.hackathons-list').addClass('hidden');
    $('.nav-link').removeClass('active');
    $('.nav-link').css('font-weight', '');
    $(this).addClass('active');
    $(this).css('font-weight', '700');


    $('.hackathon-list').addClass('hidden');
    $('.hackathon-list.' + target).removeClass('hidden');

    $('html,body').animate({
      scrollTop: '+=1px'
    });
  });
});
