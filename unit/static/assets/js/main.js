$('.tabs .tab').on('click',function(){
    $('.pages .content').fadeOut();
    let sectionShow = $(this).data('class');
    let title = $(this).data('title');
    $(sectionShow).css("display", "flex").hide().fadeIn();
    $('.nav-title').text(title)
})

menuIcon.onclick = function(){
    if(sidebar.style.marginLeft == '0px')
        sidebar.style.marginLeft = '-80px'
    else
        sidebar.style.marginLeft = '0px'
}

window.onresize = function(){
    if(window.clienWidth <= 540)
        sidebar.style.marginLeft = '-80px'
}