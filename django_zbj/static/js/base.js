//var swiper = new Swiper('.swiper-container', {
//	loop : true,
//slidesPerView : 'auto',
//loopedSlides :8,
////	pagination: '.swiper-pagination',
////	paginationClickable: '.swiper-pagination',
////	nextButton: '.swiper-button-next',
////	prevButton: '.swiper-button-prev',
////	spaceBetween: 30,
////	effect: 'coverflow',
////	slidesPerView: 2,
////	centeredSlides: true,
//	autoplay: 3000,
//
//});



$('body').click(function() {
	$('.xxx').css('display', 'none')
})
$(function() {
	$('#txt01').keyup(function() {
		var sVar = $(this).val();
		$.ajax({
				type: "get",
				url: "https://sug.so.360.cn/suggest?",
				dataType: 'jsonp',
				data: {
					word: sVar
				}
			})
			.done(function(data) {
				console.log(data.s)
				var aData = data.s;
				$('.list').empty();
				$('.xxx').css('display', 'block')
				for(var i = 0; i < aData.length; i++) {
					var $li = $('<tr><td>' + aData[i] + '</td></tr>');
					$li.appendTo($('.list'));
				}
				$('td').css('font-size','28px')
				$('td').click(function() {
					var con = this.innerText
					console.log(con)
					$('#txt01').val(con)
					$('.xxx').css('display', 'none')
				})
				$('td').mouseover(function() {
					$(this).css("background-color", "gainsboro");
				}).mouseleave(function() {
					$(this).css("background-color", "#EEEEEE");
				})
			})
	})

})

