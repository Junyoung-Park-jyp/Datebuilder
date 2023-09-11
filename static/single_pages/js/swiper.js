// 스와이퍼 JavaScript
const swiper = new Swiper(".swiper", {
  direction: "horizontal",
  loop: true,
  spaceBetween: 30, // 슬라이드 사이 여백
  slidesPerView: 4, // 한 슬라이드에 보여줄 갯수
  centeredSlides: true, //센터모드
  // If we need pagination
  autoplay: {
    delay: 2500, // 시간 설정
    disableOnInteraction: false, // false-스와이프 후 자동 재생
  },
  pagination: {
    // 호출(pager) 여부
    el: ".swiper-pagination", //버튼을 담을 태그 설정
    clickable: true, // 버튼 클릭 여부
  },
  // Navigation arrows
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});
