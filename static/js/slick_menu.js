$(".content_list").slick({
  dots: true,
  speed: 300,
  slidesToShow: 4,
  slidesToScroll: 4,
  variableWidth: true,
  adaptativeHeight: true,
  arrows: false,
  responsive: [
    {
      breakpoint: 993,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 3,
        dots: true,
      },
    },
    {
      breakpoint: 768,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2,
      },
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1,
      },
    },
  ],
});
